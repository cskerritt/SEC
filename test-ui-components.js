#!/usr/bin/env node

/**
 * UI Component Testing Framework
 * Tests Bootstrap 5 implementation across Skerritt Economics pages
 */

const fs = require('fs');
const path = require('path');

class UIComponentTester {
    constructor() {
        this.results = {
            passed: 0,
            failed: 0,
            warnings: 0,
            errors: []
        };
        this.requiredClasses = {
            bootstrap: ['btn', 'card', 'container', 'row', 'col'],
            responsive: ['col-md-', 'col-lg-', 'col-sm-'],
            custom: ['hover-lift', 'bg-gradient-hero', 'text-accent']
        };
    }

    /**
     * Test a single HTML file
     */
    testFile(filepath) {
        console.log(`Testing: ${filepath}`);
        
        try {
            const content = fs.readFileSync(filepath, 'utf8');
            
            // Test 1: Check for Bootstrap CSS
            if (!this.hasBootstrapCSS(content)) {
                this.addError(filepath, 'Missing Bootstrap CSS link');
            }
            
            // Test 2: Check for responsive meta tag
            if (!this.hasResponsiveMeta(content)) {
                this.addError(filepath, 'Missing responsive viewport meta tag');
            }
            
            // Test 3: Check for Bootstrap classes
            const bootstrapScore = this.checkBootstrapClasses(content);
            if (bootstrapScore < 0.5) {
                this.addWarning(filepath, `Low Bootstrap usage: ${Math.round(bootstrapScore * 100)}%`);
            }
            
            // Test 4: Check for accessibility
            this.checkAccessibility(content, filepath);
            
            // Test 5: Check for proper button styling
            this.checkButtons(content, filepath);
            
            // Test 6: Check for responsive images
            this.checkImages(content, filepath);
            
            this.results.passed++;
            
        } catch (error) {
            this.addError(filepath, `Failed to test: ${error.message}`);
        }
    }

    /**
     * Check if Bootstrap CSS is included
     */
    hasBootstrapCSS(content) {
        return content.includes('bootstrap@5.3.2') || 
               content.includes('bootstrap.min.css') ||
               content.includes('ui-library-setup.html');
    }

    /**
     * Check for responsive viewport meta tag
     */
    hasResponsiveMeta(content) {
        return content.includes('viewport') && 
               content.includes('width=device-width');
    }

    /**
     * Calculate Bootstrap class usage score
     */
    checkBootstrapClasses(content) {
        let foundClasses = 0;
        let totalClasses = 0;
        
        // Check for Bootstrap classes
        this.requiredClasses.bootstrap.forEach(className => {
            totalClasses++;
            if (content.includes(`class="${className}`) || 
                content.includes(`class='${className}`) ||
                content.includes(` ${className} `) ||
                content.includes(` ${className}"`)) {
                foundClasses++;
            }
        });
        
        // Check for responsive classes
        this.requiredClasses.responsive.forEach(className => {
            totalClasses++;
            if (content.includes(className)) {
                foundClasses++;
            }
        });
        
        return foundClasses / totalClasses;
    }

    /**
     * Check accessibility features
     */
    checkAccessibility(content, filepath) {
        // Check for alt text on images
        const imgMatches = content.match(/<img[^>]*>/g) || [];
        imgMatches.forEach(img => {
            if (!img.includes('alt=')) {
                this.addWarning(filepath, 'Image missing alt text');
            }
        });
        
        // Check for ARIA labels on interactive elements
        const buttonMatches = content.match(/<button[^>]*>/g) || [];
        buttonMatches.forEach(button => {
            if (!button.includes('aria-') && !button.includes('title=')) {
                this.addWarning(filepath, 'Button missing ARIA label');
            }
        });
        
        // Check for proper heading hierarchy
        const headings = content.match(/<h[1-6][^>]*>/g) || [];
        this.checkHeadingHierarchy(headings, filepath);
    }

    /**
     * Check heading hierarchy
     */
    checkHeadingHierarchy(headings, filepath) {
        let lastLevel = 0;
        headings.forEach(heading => {
            const level = parseInt(heading.match(/<h([1-6])/)[1]);
            if (level - lastLevel > 1 && lastLevel !== 0) {
                this.addWarning(filepath, `Skipped heading level: h${lastLevel} to h${level}`);
            }
            lastLevel = level;
        });
    }

    /**
     * Check button styling
     */
    checkButtons(content, filepath) {
        const oldButtonClasses = ['class="button"', "class='button'"];
        oldButtonClasses.forEach(oldClass => {
            if (content.includes(oldClass)) {
                this.addError(filepath, 'Found old button class - needs migration');
            }
        });
    }

    /**
     * Check responsive images
     */
    checkImages(content, filepath) {
        const imgMatches = content.match(/<img[^>]*>/g) || [];
        imgMatches.forEach(img => {
            if (!img.includes('img-fluid') && !img.includes('responsive')) {
                this.addWarning(filepath, 'Image may not be responsive');
            }
        });
    }

    /**
     * Add error to results
     */
    addError(filepath, message) {
        this.results.failed++;
        this.results.errors.push({
            type: 'error',
            file: filepath,
            message: message
        });
    }

    /**
     * Add warning to results
     */
    addWarning(filepath, message) {
        this.results.warnings++;
        this.results.errors.push({
            type: 'warning',
            file: filepath,
            message: message
        });
    }

    /**
     * Test all files in a directory
     */
    testDirectory(dirPath, pattern = '*.html') {
        const files = this.getFiles(dirPath, pattern);
        
        console.log(`\nTesting ${files.length} files...\n`);
        
        files.forEach(file => {
            this.testFile(file);
        });
        
        this.printResults();
    }

    /**
     * Get all matching files recursively
     */
    getFiles(dirPath, pattern) {
        const files = [];
        
        function walkDir(currentPath) {
            const entries = fs.readdirSync(currentPath);
            
            entries.forEach(entry => {
                const fullPath = path.join(currentPath, entry);
                const stat = fs.statSync(fullPath);
                
                if (stat.isDirectory() && !entry.startsWith('.') && entry !== '_site') {
                    walkDir(fullPath);
                } else if (stat.isFile() && entry.endsWith('.html')) {
                    files.push(fullPath);
                }
            });
        }
        
        walkDir(dirPath);
        return files;
    }

    /**
     * Print test results
     */
    printResults() {
        console.log('\n' + '='.repeat(60));
        console.log('UI Component Test Results');
        console.log('='.repeat(60));
        
        console.log(`\nTotal Files Tested: ${this.results.passed + this.results.failed}`);
        console.log(`✅ Passed: ${this.results.passed}`);
        console.log(`❌ Failed: ${this.results.failed}`);
        console.log(`⚠️  Warnings: ${this.results.warnings}`);
        
        if (this.results.errors.length > 0) {
            console.log('\nIssues Found:');
            console.log('-'.repeat(60));
            
            // Group by file
            const fileIssues = {};
            this.results.errors.forEach(error => {
                if (!fileIssues[error.file]) {
                    fileIssues[error.file] = [];
                }
                fileIssues[error.file].push(error);
            });
            
            Object.keys(fileIssues).forEach(file => {
                console.log(`\n${file}:`);
                fileIssues[file].forEach(issue => {
                    const icon = issue.type === 'error' ? '❌' : '⚠️';
                    console.log(`  ${icon} ${issue.message}`);
                });
            });
        }
        
        // Generate report file
        const report = {
            timestamp: new Date().toISOString(),
            summary: this.results,
            issues: this.results.errors
        };
        
        fs.writeFileSync('ui-test-report.json', JSON.stringify(report, null, 2));
        console.log('\n📄 Detailed report saved to: ui-test-report.json');
    }
}

// Run tests if called directly
if (require.main === module) {
    const tester = new UIComponentTester();
    
    // Get command line arguments
    const args = process.argv.slice(2);
    const targetPath = args[0] || '.';
    
    console.log('🧪 UI Component Testing Framework');
    console.log('Testing Bootstrap 5 implementation...\n');
    
    if (fs.statSync(targetPath).isDirectory()) {
        tester.testDirectory(targetPath);
    } else {
        tester.testFile(targetPath);
        tester.printResults();
    }
}

module.exports = UIComponentTester;