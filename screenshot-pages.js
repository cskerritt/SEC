#!/usr/bin/env node

/**
 * Screenshot tool for Jekyll pages
 * Takes screenshots of all pages and saves them with metadata
 */

const { chromium } = require('playwright');
const fs = require('fs').promises;
const path = require('path');
const readline = require('readline');

// Configuration
const CONFIG = {
    baseUrl: 'http://localhost:4001',
    screenshotDir: 'page-screenshots',
    viewport: { width: 1920, height: 1080 },
    fullPage: true,
    timeout: 30000,
    waitForLoadState: 'networkidle'
};

// Create readline interface for progress updates
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Progress tracking
let processedCount = 0;
let failedPages = [];
let screenshotData = {};

async function ensureDirectoryExists(dir) {
    try {
        await fs.mkdir(dir, { recursive: true });
    } catch (error) {
        console.error(`Error creating directory ${dir}:`, error);
    }
}

async function loadPageList() {
    try {
        const content = await fs.readFile('all-pages.txt', 'utf-8');
        return content.trim().split('\n').map(line => line.replace('_site/', ''));
    } catch (error) {
        console.error('Error loading page list:', error);
        return [];
    }
}

async function takeScreenshot(browser, pagePath, index, total) {
    const page = await browser.newPage();
    const url = `${CONFIG.baseUrl}/${pagePath}`;
    const screenshotFileName = pagePath.replace(/\//g, '-').replace('.html', '') + '.png';
    const screenshotPath = path.join(CONFIG.screenshotDir, screenshotFileName);
    
    try {
        // Update progress
        process.stdout.write(`\r[${index + 1}/${total}] Processing: ${pagePath.padEnd(60)}`);
        
        // Set viewport
        await page.setViewportSize(CONFIG.viewport);
        
        // Navigate to page
        await page.goto(url, { 
            waitUntil: CONFIG.waitForLoadState,
            timeout: CONFIG.timeout 
        });
        
        // Wait a bit for any animations to complete
        await page.waitForTimeout(1000);
        
        // Take screenshot
        await page.screenshot({
            path: screenshotPath,
            fullPage: CONFIG.fullPage
        });
        
        // Get page title and metadata
        const title = await page.title();
        const description = await page.$eval('meta[name="description"]', el => el.content).catch(() => '');
        
        // Store screenshot data
        screenshotData[pagePath] = {
            screenshot: screenshotFileName,
            url: url,
            title: title,
            description: description,
            timestamp: new Date().toISOString(),
            success: true
        };
        
        processedCount++;
        
    } catch (error) {
        failedPages.push({ path: pagePath, error: error.message });
        screenshotData[pagePath] = {
            screenshot: null,
            url: url,
            error: error.message,
            timestamp: new Date().toISOString(),
            success: false
        };
    } finally {
        await page.close();
    }
}

async function processInBatches(pages, batchSize = 5) {
    const browser = await chromium.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    try {
        for (let i = 0; i < pages.length; i += batchSize) {
            const batch = pages.slice(i, i + batchSize);
            const promises = batch.map((page, idx) => 
                takeScreenshot(browser, page, i + idx, pages.length)
            );
            await Promise.all(promises);
        }
    } finally {
        await browser.close();
    }
}

async function generateReport() {
    const reportPath = path.join(CONFIG.screenshotDir, 'screenshot-report.json');
    const report = {
        metadata: {
            totalPages: Object.keys(screenshotData).length,
            successfulScreenshots: processedCount,
            failedScreenshots: failedPages.length,
            timestamp: new Date().toISOString(),
            config: CONFIG
        },
        pages: screenshotData,
        failures: failedPages
    };
    
    await fs.writeFile(reportPath, JSON.stringify(report, null, 2));
    return report;
}

async function generateHTMLGallery() {
    const galleryPath = path.join(CONFIG.screenshotDir, 'gallery.html');
    const successfulPages = Object.entries(screenshotData)
        .filter(([_, data]) => data.success)
        .sort((a, b) => a[0].localeCompare(b[0]));
    
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Screenshot Gallery - ${new Date().toLocaleDateString()}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }
        h1 { 
            text-align: center; 
            color: #333; 
            margin-bottom: 30px;
        }
        .stats {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
            gap: 20px;
        }
        .screenshot-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .screenshot-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .screenshot-image {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-bottom: 1px solid #eee;
            cursor: pointer;
        }
        .screenshot-info {
            padding: 15px;
        }
        .screenshot-title {
            font-weight: 600;
            color: #333;
            margin-bottom: 5px;
        }
        .screenshot-path {
            font-size: 0.85rem;
            color: #666;
            font-family: monospace;
            word-break: break-all;
        }
        .filters {
            margin-bottom: 20px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .filter-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            z-index: 1000;
            padding: 20px;
        }
        .modal.active {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .modal-content {
            max-width: 90%;
            max-height: 90%;
        }
        .modal-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
        }
        .close-modal {
            position: absolute;
            top: 20px;
            right: 40px;
            color: white;
            font-size: 40px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Page Screenshot Gallery</h1>
    
    <div class="stats">
        <p>Total Screenshots: ${successfulPages.length} | Failed: ${failedPages.length} | Generated: ${new Date().toLocaleString()}</p>
    </div>
    
    <div class="filters">
        <input type="text" class="filter-input" placeholder="Filter screenshots by path..." id="filterInput">
    </div>
    
    <div class="gallery" id="gallery">
        ${successfulPages.map(([pagePath, data]) => `
            <div class="screenshot-card" data-path="${pagePath}">
                <img class="screenshot-image" 
                     src="${data.screenshot}" 
                     alt="${data.title || pagePath}"
                     onclick="openModal('${data.screenshot}')"
                     loading="lazy">
                <div class="screenshot-info">
                    <div class="screenshot-title">${data.title || 'Untitled'}</div>
                    <div class="screenshot-path">${pagePath}</div>
                </div>
            </div>
        `).join('')}
    </div>
    
    <div class="modal" id="modal" onclick="closeModal()">
        <span class="close-modal">&times;</span>
        <img class="modal-image" id="modalImage" src="">
    </div>
    
    <script>
        // Filter functionality
        document.getElementById('filterInput').addEventListener('input', (e) => {
            const filter = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.screenshot-card');
            
            cards.forEach(card => {
                const path = card.dataset.path.toLowerCase();
                card.style.display = path.includes(filter) ? 'block' : 'none';
            });
        });
        
        // Modal functionality
        function openModal(src) {
            document.getElementById('modalImage').src = src;
            document.getElementById('modal').classList.add('active');
        }
        
        function closeModal() {
            document.getElementById('modal').classList.remove('active');
        }
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    </script>
</body>
</html>`;
    
    await fs.writeFile(galleryPath, html);
    return galleryPath;
}

async function main() {
    console.log('🚀 Starting Jekyll Page Screenshot Tool\n');
    
    // Ensure screenshot directory exists
    await ensureDirectoryExists(CONFIG.screenshotDir);
    
    // Load page list
    console.log('📄 Loading page list...');
    const pages = await loadPageList();
    console.log(`Found ${pages.length} pages to screenshot\n`);
    
    if (pages.length === 0) {
        console.log('❌ No pages found. Make sure all-pages.txt exists.');
        process.exit(1);
    }
    
    // Check if Jekyll server is running
    console.log(`🔍 Checking if Jekyll server is running at ${CONFIG.baseUrl}...`);
    try {
        const testBrowser = await chromium.launch({ headless: true });
        const testPage = await testBrowser.newPage();
        await testPage.goto(CONFIG.baseUrl, { timeout: 5000 });
        await testPage.close();
        await testBrowser.close();
        console.log('✅ Jekyll server is accessible\n');
    } catch (error) {
        console.log(`❌ Cannot access Jekyll server at ${CONFIG.baseUrl}`);
        console.log('Please start Jekyll server with: bundle exec jekyll serve --port 4001\n');
        process.exit(1);
    }
    
    // Process pages in batches
    console.log('📸 Taking screenshots...\n');
    const startTime = Date.now();
    
    await processInBatches(pages);
    
    const duration = ((Date.now() - startTime) / 1000).toFixed(2);
    console.log(`\n\n✅ Completed in ${duration} seconds`);
    console.log(`📊 Successful: ${processedCount} | Failed: ${failedPages.length}\n`);
    
    // Generate report
    console.log('📝 Generating report...');
    const report = await generateReport();
    console.log(`Report saved to: ${path.join(CONFIG.screenshotDir, 'screenshot-report.json')}`);
    
    // Generate HTML gallery
    console.log('🎨 Generating HTML gallery...');
    const galleryPath = await generateHTMLGallery();
    console.log(`Gallery saved to: ${galleryPath}`);
    
    // Show failed pages if any
    if (failedPages.length > 0) {
        console.log('\n⚠️  Failed pages:');
        failedPages.forEach(({ path, error }) => {
            console.log(`  - ${path}: ${error}`);
        });
    }
    
    console.log('\n✨ Done! Open the gallery.html file to view all screenshots.');
    rl.close();
}

// Handle errors
process.on('unhandledRejection', (error) => {
    console.error('\n❌ Unhandled error:', error);
    process.exit(1);
});

// Run the script
main();