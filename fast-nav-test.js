const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

async function findHtmlFiles() {
  const { stdout } = await execPromise('find _site -name "*.html" -type f 2>/dev/null');
  return stdout.trim().split('\n').filter(f => f);
}

async function testBatch(browser, files, batchNum) {
  const page = await browser.newPage();
  const results = [];
  
  for (const file of files) {
    const relativePath = file.replace('_site/', '');
    const url = `http://localhost:4000/${relativePath}`;
    
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 3000 });
      await page.waitForTimeout(500);
      
      const navStatus = await page.evaluate(() => {
        const nav = document.querySelector('.main-nav');
        if (!nav) return 'NO_NAV';
        
        const styles = window.getComputedStyle(nav);
        const inline = nav.style;
        const pos = inline.position || styles.position;
        
        return pos === 'fixed' ? 'FIXED' : pos.toUpperCase();
      });
      
      results.push({ file: relativePath, status: navStatus });
    } catch (error) {
      results.push({ file: relativePath, status: 'ERROR' });
    }
  }
  
  await page.close();
  return results;
}

(async () => {
  console.log('Finding all HTML files...');
  const files = await findHtmlFiles();
  console.log(`Found ${files.length} HTML files\n`);
  
  const browser = await chromium.launch({ headless: true });
  
  // Process in parallel batches
  const batchSize = 50;
  const batches = [];
  
  for (let i = 0; i < files.length; i += batchSize) {
    batches.push(files.slice(i, i + batchSize));
  }
  
  console.log(`Testing in ${batches.length} batches of ${batchSize} pages...\n`);
  
  const allResults = [];
  let batchNum = 0;
  
  // Process batches sequentially to avoid overload
  for (const batch of batches) {
    batchNum++;
    process.stdout.write(`\rProcessing batch ${batchNum}/${batches.length}...`);
    
    const results = await testBatch(browser, batch, batchNum);
    allResults.push(...results);
  }
  
  await browser.close();
  
  // Analyze results
  const fixed = allResults.filter(r => r.status === 'FIXED').length;
  const notFixed = allResults.filter(r => r.status !== 'FIXED' && r.status !== 'NO_NAV' && r.status !== 'ERROR').length;
  const noNav = allResults.filter(r => r.status === 'NO_NAV').length;
  const errors = allResults.filter(r => r.status === 'ERROR').length;
  
  console.log('\n\n' + '='.repeat(80));
  console.log('COMPREHENSIVE TEST RESULTS');
  console.log('='.repeat(80));
  console.log(`Total pages tested: ${files.length}`);
  console.log(`Pages with FIXED navigation: ${fixed}`);
  console.log(`Pages with NON-FIXED navigation: ${notFixed}`);
  console.log(`Pages with NO navigation: ${noNav}`);
  console.log(`Pages with errors: ${errors}`);
  
  const successRate = ((fixed / files.length) * 100).toFixed(1);
  console.log(`\nSuccess rate: ${successRate}%`);
  
  // Show problem pages
  if (notFixed > 0) {
    console.log('\n' + '='.repeat(80));
    console.log('PAGES WITH NON-FIXED NAVIGATION (first 30):');
    console.log('='.repeat(80));
    
    const problemPages = allResults.filter(r => r.status !== 'FIXED' && r.status !== 'NO_NAV' && r.status !== 'ERROR');
    problemPages.slice(0, 30).forEach(p => {
      console.log(`  ${p.file} - Position: ${p.status}`);
    });
    
    if (problemPages.length > 30) {
      console.log(`  ... and ${problemPages.length - 30} more`);
    }
  }
  
  // Save full report
  fs.writeFileSync('full-navigation-report.json', JSON.stringify({
    timestamp: new Date().toISOString(),
    total: files.length,
    fixed,
    notFixed,
    noNav,
    errors,
    successRate,
    problemPages: allResults.filter(r => r.status !== 'FIXED')
  }, null, 2));
  
  console.log('\nFull report saved to full-navigation-report.json');
  
  if (notFixed === 0 && noNav === 0) {
    console.log('\n✅ ALL PAGES HAVE FIXED NAVIGATION!');
  } else {
    console.log(`\n❌ ${notFixed + noNav} PAGES NEED FIXES`);
  }
})();