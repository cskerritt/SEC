#!/usr/bin/env node

/**
 * Automated QA Checks for Jekyll Site
 * Runs various checks on pages including SEO, broken links, performance, etc.
 */

const { chromium } = require('playwright');
const fs = require('fs').promises;
const path = require('path');

const CONFIG = {
    baseUrl: 'http://localhost:4001',
    timeout: 30000,
    checksToRun: {
        seo: true,
        links: true,
        images: true,
        performance: true,
        accessibility: true,
        console: true,
        responsive: true
    }
};

class QAChecker {
    constructor() {
        this.results = {};
        this.browser = null;
    }

    async init() {
        this.browser = await chromium.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
    }

    async close() {
        if (this.browser) {
            await this.browser.close();
        }
    }

    async checkPage(pagePath) {
        const page = await this.browser.newPage();
        const url = `${CONFIG.baseUrl}/${pagePath}`;
        const pageResults = {
            url: url,
            path: pagePath,
            timestamp: new Date().toISOString(),
            checks: {},
            issues: [],
            score: 0
        };

        try {
            // Navigate to page
            await page.goto(url, { 
                waitUntil: 'networkidle',
                timeout: CONFIG.timeout 
            });

            // Run all checks
            if (CONFIG.checksToRun.seo) {
                pageResults.checks.seo = await this.checkSEO(page, pageResults);
            }

            if (CONFIG.checksToRun.links) {
                pageResults.checks.links = await this.checkLinks(page, pageResults);
            }

            if (CONFIG.checksToRun.images) {
                pageResults.checks.images = await this.checkImages(page, pageResults);
            }

            if (CONFIG.checksToRun.performance) {
                pageResults.checks.performance = await this.checkPerformance(page, pageResults);
            }

            if (CONFIG.checksToRun.accessibility) {
                pageResults.checks.accessibility = await this.checkAccessibility(page, pageResults);
            }

            if (CONFIG.checksToRun.console) {
                pageResults.checks.console = await this.checkConsoleErrors(page, pageResults);
            }

            if (CONFIG.checksToRun.responsive) {
                pageResults.checks.responsive = await this.checkResponsive(page, pageResults);
            }

            // Calculate score
            const totalChecks = Object.keys(pageResults.checks).length;
            const passedChecks = Object.values(pageResults.checks).filter(check => check.passed).length;
            pageResults.score = Math.round((passedChecks / totalChecks) * 100);

        } catch (error) {
            pageResults.error = error.message;
            pageResults.issues.push({
                type: 'error',
                category: 'page-load',
                message: `Failed to load page: ${error.message}`
            });
        } finally {
            await page.close();
        }

        return pageResults;
    }

    async checkSEO(page, results) {
        const seoCheck = {
            passed: true,
            details: {}
        };

        try {
            // Check title
            const title = await page.title();
            seoCheck.details.title = title;
            if (!title || title.length < 10) {
                seoCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'seo',
                    message: 'Page title is missing or too short'
                });
            } else if (title.length > 60) {
                results.issues.push({
                    type: 'warning',
                    category: 'seo',
                    message: `Page title is too long (${title.length} chars, recommended < 60)`
                });
            }

            // Check meta description
            const metaDescription = await page.$eval('meta[name="description"]', el => el.content).catch(() => null);
            seoCheck.details.metaDescription = metaDescription;
            if (!metaDescription) {
                seoCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'seo',
                    message: 'Meta description is missing'
                });
            } else if (metaDescription.length > 160) {
                results.issues.push({
                    type: 'warning',
                    category: 'seo',
                    message: `Meta description is too long (${metaDescription.length} chars, recommended < 160)`
                });
            }

            // Check H1
            const h1Count = await page.$$eval('h1', elements => elements.length);
            seoCheck.details.h1Count = h1Count;
            if (h1Count === 0) {
                seoCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'seo',
                    message: 'Page is missing H1 tag'
                });
            } else if (h1Count > 1) {
                results.issues.push({
                    type: 'warning',
                    category: 'seo',
                    message: `Page has multiple H1 tags (${h1Count})`
                });
            }

            // Check heading hierarchy
            const headings = await page.$$eval('h1, h2, h3, h4, h5, h6', elements => 
                elements.map(el => ({
                    level: parseInt(el.tagName[1]),
                    text: el.textContent.trim()
                }))
            );
            seoCheck.details.headingCount = headings.length;

            // Check for canonical URL
            const canonical = await page.$eval('link[rel="canonical"]', el => el.href).catch(() => null);
            seoCheck.details.canonical = canonical;
            if (!canonical) {
                results.issues.push({
                    type: 'warning',
                    category: 'seo',
                    message: 'Canonical URL is missing'
                });
            }

        } catch (error) {
            seoCheck.passed = false;
            seoCheck.error = error.message;
        }

        return seoCheck;
    }

    async checkLinks(page, results) {
        const linksCheck = {
            passed: true,
            details: {
                total: 0,
                internal: 0,
                external: 0,
                broken: []
            }
        };

        try {
            const links = await page.$$eval('a[href]', elements => 
                elements.map(el => ({
                    href: el.href,
                    text: el.textContent.trim(),
                    isExternal: !el.href.includes(window.location.hostname)
                }))
            );

            linksCheck.details.total = links.length;
            linksCheck.details.internal = links.filter(l => !l.isExternal).length;
            linksCheck.details.external = links.filter(l => l.isExternal).length;

            // Check for broken internal links (simplified check)
            for (const link of links.filter(l => !l.isExternal)) {
                try {
                    const response = await page.evaluate(async (url) => {
                        try {
                            const res = await fetch(url, { method: 'HEAD' });
                            return res.status;
                        } catch {
                            return 0;
                        }
                    }, link.href);

                    if (response >= 400 || response === 0) {
                        linksCheck.details.broken.push(link);
                        linksCheck.passed = false;
                        results.issues.push({
                            type: 'error',
                            category: 'links',
                            message: `Broken link: ${link.href} (${link.text || 'no text'})`
                        });
                    }
                } catch (error) {
                    // Skip link check errors
                }
            }

        } catch (error) {
            linksCheck.error = error.message;
        }

        return linksCheck;
    }

    async checkImages(page, results) {
        const imagesCheck = {
            passed: true,
            details: {
                total: 0,
                withAlt: 0,
                withoutAlt: 0,
                broken: []
            }
        };

        try {
            const images = await page.$$eval('img', elements => 
                elements.map(el => ({
                    src: el.src,
                    alt: el.alt,
                    naturalWidth: el.naturalWidth,
                    naturalHeight: el.naturalHeight,
                    loading: el.loading
                }))
            );

            imagesCheck.details.total = images.length;

            images.forEach(img => {
                // Check alt text
                if (!img.alt) {
                    imagesCheck.details.withoutAlt++;
                    results.issues.push({
                        type: 'warning',
                        category: 'accessibility',
                        message: `Image missing alt text: ${img.src}`
                    });
                } else {
                    imagesCheck.details.withAlt++;
                }

                // Check if image loaded
                if (img.naturalWidth === 0 || img.naturalHeight === 0) {
                    imagesCheck.details.broken.push(img.src);
                    imagesCheck.passed = false;
                    results.issues.push({
                        type: 'error',
                        category: 'images',
                        message: `Broken image: ${img.src}`
                    });
                }
            });

        } catch (error) {
            imagesCheck.error = error.message;
        }

        return imagesCheck;
    }

    async checkPerformance(page, results) {
        const performanceCheck = {
            passed: true,
            details: {}
        };

        try {
            const metrics = await page.evaluate(() => {
                const navigation = performance.getEntriesByType('navigation')[0];
                const paint = performance.getEntriesByType('paint');
                
                return {
                    domContentLoaded: navigation ? navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart : 0,
                    loadComplete: navigation ? navigation.loadEventEnd - navigation.loadEventStart : 0,
                    firstPaint: paint.find(p => p.name === 'first-paint')?.startTime || 0,
                    firstContentfulPaint: paint.find(p => p.name === 'first-contentful-paint')?.startTime || 0
                };
            });

            performanceCheck.details = metrics;

            // Check performance thresholds
            if (metrics.firstContentfulPaint > 3000) {
                performanceCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'performance',
                    message: `Slow First Contentful Paint: ${metrics.firstContentfulPaint.toFixed(0)}ms (target < 3000ms)`
                });
            } else if (metrics.firstContentfulPaint > 2000) {
                results.issues.push({
                    type: 'warning',
                    category: 'performance',
                    message: `First Contentful Paint could be faster: ${metrics.firstContentfulPaint.toFixed(0)}ms`
                });
            }

            // Check page size
            const resources = await page.evaluate(() => 
                performance.getEntriesByType('resource').map(r => ({
                    name: r.name,
                    size: r.transferSize,
                    duration: r.duration
                }))
            );

            const totalSize = resources.reduce((sum, r) => sum + (r.size || 0), 0);
            performanceCheck.details.totalSize = totalSize;
            performanceCheck.details.resourceCount = resources.length;

            if (totalSize > 5000000) { // 5MB
                performanceCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'performance',
                    message: `Page size too large: ${(totalSize / 1024 / 1024).toFixed(2)}MB`
                });
            }

        } catch (error) {
            performanceCheck.error = error.message;
        }

        return performanceCheck;
    }

    async checkAccessibility(page, results) {
        const accessibilityCheck = {
            passed: true,
            details: {}
        };

        try {
            // Check for ARIA landmarks
            const landmarks = await page.$$eval('[role]', elements => elements.length);
            accessibilityCheck.details.ariaLandmarks = landmarks;

            // Check form labels
            const inputs = await page.$$eval('input, select, textarea', elements => 
                elements.map(el => ({
                    type: el.type || el.tagName.toLowerCase(),
                    id: el.id,
                    name: el.name,
                    hasLabel: !!el.labels?.length || !!el.getAttribute('aria-label') || !!el.getAttribute('aria-labelledby')
                }))
            );

            const unlabeledInputs = inputs.filter(i => !i.hasLabel && i.type !== 'hidden' && i.type !== 'submit');
            accessibilityCheck.details.unlabeledInputs = unlabeledInputs.length;

            if (unlabeledInputs.length > 0) {
                accessibilityCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'accessibility',
                    message: `${unlabeledInputs.length} form inputs without labels`
                });
            }

            // Check color contrast (simplified)
            const hasLowContrastText = await page.evaluate(() => {
                const elements = document.querySelectorAll('*');
                let lowContrastCount = 0;
                
                elements.forEach(el => {
                    const style = window.getComputedStyle(el);
                    const color = style.color;
                    const bgColor = style.backgroundColor;
                    
                    // Very basic check - real contrast checking requires more complex calculations
                    if (color && bgColor && color !== 'rgb(0, 0, 0)' && bgColor !== 'rgba(0, 0, 0, 0)') {
                        // This is a placeholder - real implementation would calculate actual contrast ratio
                        // For now, we'll skip this check
                    }
                });
                
                return lowContrastCount;
            });

            // Check for skip navigation link
            const skipNav = await page.$('[href="#main"], [href="#content"], .skip-nav');
            if (!skipNav) {
                results.issues.push({
                    type: 'warning',
                    category: 'accessibility',
                    message: 'No skip navigation link found'
                });
            }

        } catch (error) {
            accessibilityCheck.error = error.message;
        }

        return accessibilityCheck;
    }

    async checkConsoleErrors(page, results) {
        const consoleCheck = {
            passed: true,
            details: {
                errors: [],
                warnings: []
            }
        };

        // Set up console message listener before navigation
        const consoleMessages = [];
        page.on('console', msg => {
            if (msg.type() === 'error' || msg.type() === 'warning') {
                consoleMessages.push({
                    type: msg.type(),
                    text: msg.text()
                });
            }
        });

        // Wait a bit for any console messages
        await page.waitForTimeout(1000);

        consoleMessages.forEach(msg => {
            if (msg.type === 'error') {
                consoleCheck.details.errors.push(msg.text);
                consoleCheck.passed = false;
                results.issues.push({
                    type: 'error',
                    category: 'console',
                    message: `Console error: ${msg.text}`
                });
            } else if (msg.type === 'warning') {
                consoleCheck.details.warnings.push(msg.text);
                results.issues.push({
                    type: 'warning',
                    category: 'console',
                    message: `Console warning: ${msg.text}`
                });
            }
        });

        return consoleCheck;
    }

    async checkResponsive(page, results) {
        const responsiveCheck = {
            passed: true,
            details: {
                mobile: {},
                tablet: {},
                desktop: {}
            }
        };

        const viewports = [
            { name: 'mobile', width: 375, height: 667 },
            { name: 'tablet', width: 768, height: 1024 },
            { name: 'desktop', width: 1920, height: 1080 }
        ];

        try {
            for (const viewport of viewports) {
                await page.setViewportSize({ width: viewport.width, height: viewport.height });
                await page.waitForTimeout(500);

                // Check for horizontal scroll
                const hasHorizontalScroll = await page.evaluate(() => {
                    return document.documentElement.scrollWidth > document.documentElement.clientWidth;
                });

                responsiveCheck.details[viewport.name].hasHorizontalScroll = hasHorizontalScroll;

                if (hasHorizontalScroll) {
                    responsiveCheck.passed = false;
                    results.issues.push({
                        type: 'error',
                        category: 'responsive',
                        message: `Horizontal scroll detected at ${viewport.name} viewport (${viewport.width}px)`
                    });
                }

                // Check if navigation is accessible
                const navVisible = await page.isVisible('nav, .nav, .navigation, .main-nav').catch(() => false);
                responsiveCheck.details[viewport.name].navigationVisible = navVisible;

                if (!navVisible && viewport.name !== 'desktop') {
                    // Check for mobile menu button
                    const mobileMenuVisible = await page.isVisible('.mobile-menu, .menu-toggle, .hamburger').catch(() => false);
                    if (!mobileMenuVisible) {
                        results.issues.push({
                            type: 'warning',
                            category: 'responsive',
                            message: `Navigation might not be accessible on ${viewport.name}`
                        });
                    }
                }
            }
        } catch (error) {
            responsiveCheck.error = error.message;
        }

        return responsiveCheck;
    }

    async runChecks(pages) {
        console.log(`🔍 Running automated QA checks on ${pages.length} pages...\n`);
        
        const results = {
            metadata: {
                startTime: new Date().toISOString(),
                baseUrl: CONFIG.baseUrl,
                totalPages: pages.length,
                checksEnabled: CONFIG.checksToRun
            },
            pages: {},
            summary: {
                passed: 0,
                failed: 0,
                warnings: 0,
                errors: 0
            }
        };

        for (let i = 0; i < pages.length; i++) {
            const page = pages[i];
            process.stdout.write(`\r[${i + 1}/${pages.length}] Checking: ${page.padEnd(60)}`);
            
            const pageResults = await this.checkPage(page);
            results.pages[page] = pageResults;
            
            // Update summary
            if (pageResults.score === 100) {
                results.summary.passed++;
            } else {
                results.summary.failed++;
            }
            
            results.summary.errors += pageResults.issues.filter(i => i.type === 'error').length;
            results.summary.warnings += pageResults.issues.filter(i => i.type === 'warning').length;
        }

        results.metadata.endTime = new Date().toISOString();
        console.log('\n\n✅ Checks completed!\n');
        
        return results;
    }
}

async function main() {
    // Load page list
    let pages;
    try {
        const content = await fs.readFile('all-pages.txt', 'utf-8');
        pages = content.trim().split('\n').map(line => line.replace('_site/', ''));
    } catch (error) {
        console.error('Error loading page list:', error);
        console.log('Using sample pages for testing...');
        pages = [
            'index.html',
            'about/index.html',
            'services/forensic-economics/index.html'
        ];
    }

    // Create QA checker
    const checker = new QAChecker();
    
    try {
        await checker.init();
        const results = await checker.runChecks(pages.slice(0, 10)); // Limit to first 10 pages for testing
        
        // Save results
        const outputPath = `qa-automated-results-${new Date().toISOString().split('T')[0]}.json`;
        await fs.writeFile(outputPath, JSON.stringify(results, null, 2));
        
        // Print summary
        console.log('📊 Summary:');
        console.log(`   Total pages checked: ${results.summary.passed + results.summary.failed}`);
        console.log(`   ✅ Passed: ${results.summary.passed}`);
        console.log(`   ❌ Failed: ${results.summary.failed}`);
        console.log(`   ⚠️  Warnings: ${results.summary.warnings}`);
        console.log(`   🚨 Errors: ${results.summary.errors}`);
        console.log(`\n📁 Full results saved to: ${outputPath}`);
        
        // Show top issues
        const allIssues = [];
        Object.entries(results.pages).forEach(([path, pageData]) => {
            pageData.issues.forEach(issue => {
                allIssues.push({ ...issue, path });
            });
        });
        
        const topErrors = allIssues.filter(i => i.type === 'error').slice(0, 5);
        if (topErrors.length > 0) {
            console.log('\n🚨 Top Errors:');
            topErrors.forEach(issue => {
                console.log(`   - ${issue.path}: ${issue.message}`);
            });
        }
        
    } catch (error) {
        console.error('Error running checks:', error);
    } finally {
        await checker.close();
    }
}

// Run if called directly
if (require.main === module) {
    main().catch(console.error);
}

module.exports = { QAChecker, CONFIG };