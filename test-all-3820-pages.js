const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function findAllHtmlFiles(dir) {
  const files = [];
  
  function walk(currentDir) {
    const items = fs.readdirSync(currentDir);
    
    for (const item of items) {
      const fullPath = path.join(currentDir, item);
      const stat = fs.statSync(fullPath);
      
      if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
        walk(fullPath);
      } else if (item.endsWith('.html')) {
        files.push(fullPath);
      }
    }
  }
  
  walk(dir);
  return files;
}

(async () => {
  console.log('Starting comprehensive test of ALL pages...\n');
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Find all HTML files
  const htmlFiles = findAllHtmlFiles('_site');
  console.log(`Found ${htmlFiles.length} HTML pages to test\n`);
  
  const issues = [];
  let tested = 0;
  let fixed = 0;
  let notFixed = 0;
  let noNav = 0;
  let errors = 0;
  
  // Test in batches to show progress
  const batchSize = 100;
  
  for (let i = 0; i < htmlFiles.length; i++) {
    const file = htmlFiles[i];
    const relativePath = file.replace('_site/', '').replace('_site\\', '');
    const url = `http://localhost:4000/${relativePath}`;
    
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 5000 });
      
      // Wait for JS to execute
      await page.waitForTimeout(600);
      
      const result = await page.evaluate(() => {
        const nav = document.querySelector('.main-nav');
        if (!nav) return { hasNav: false };
        
        const computedStyles = window.getComputedStyle(nav);
        const inlineStyles = nav.style;
        
        // Check final position
        const finalPosition = inlineStyles.position || computedStyles.position;
        
        return {
          hasNav: true,
          isFixed: finalPosition === 'fixed',
          position: finalPosition
        };
      });
      
      tested++;
      
      if (!result.hasNav) {
        noNav++;
        issues.push({ path: relativePath, issue: 'No navigation found' });
      } else if (result.isFixed) {
        fixed++;
      } else {
        notFixed++;
        issues.push({ path: relativePath, issue: `Navigation is ${result.position}` });
      }
      
    } catch (error) {
      tested++;
      errors++;
      if (!relativePath.includes('404') && !relativePath.includes('error')) {
        issues.push({ path: relativePath, issue: `Error: ${error.message}` });
      }
    }
    
    // Show progress every batch
    if ((i + 1) % batchSize === 0 || i === htmlFiles.length - 1) {
      process.stdout.write(`\rProgress: ${i + 1}/${htmlFiles.length} pages tested...`);
    }
  }
  
  console.log('\n\n' + '=' .repeat(80));
  console.log('COMPREHENSIVE TEST RESULTS');
  console.log('=' .repeat(80));
  console.log(`Total HTML files found: ${htmlFiles.length}`);
  console.log(`Successfully tested: ${tested}`);
  console.log(`Pages with FIXED navigation: ${fixed}`);
  console.log(`Pages with NON-FIXED navigation: ${notFixed}`);
  console.log(`Pages with NO navigation: ${noNav}`);
  console.log(`Pages with errors: ${errors}`);
  
  const successRate = ((fixed / tested) * 100).toFixed(1);
  console.log(`\nSuccess rate: ${successRate}%`);
  
  if (notFixed > 0) {
    console.log('\n' + '=' .repeat(80));
    console.log('PAGES WITH NON-FIXED NAVIGATION (first 50):');
    console.log('=' .repeat(80));
    
    const nonFixedIssues = issues.filter(i => i.issue.includes('Navigation is'));
    nonFixedIssues.slice(0, 50).forEach(issue => {
      console.log(`  ${issue.path} - ${issue.issue}`);
    });
    
    if (nonFixedIssues.length > 50) {
      console.log(`  ... and ${nonFixedIssues.length - 50} more`);
    }
  }
  
  if (noNav > 0) {
    console.log('\n' + '=' .repeat(80));
    console.log('PAGES WITH NO NAVIGATION (first 20):');
    console.log('=' .repeat(80));
    
    const noNavIssues = issues.filter(i => i.issue === 'No navigation found');
    noNavIssues.slice(0, 20).forEach(issue => {
      console.log(`  ${issue.path}`);
    });
    
    if (noNavIssues.length > 20) {
      console.log(`  ... and ${noNavIssues.length - 20} more`);
    }
  }
  
  // Save detailed report
  const report = {
    timestamp: new Date().toISOString(),
    totalPages: htmlFiles.length,
    tested: tested,
    fixed: fixed,
    notFixed: notFixed,
    noNav: noNav,
    errors: errors,
    successRate: successRate,
    issues: issues
  };
  
  fs.writeFileSync('navigation-test-report.json', JSON.stringify(report, null, 2));
  console.log('\nDetailed report saved to navigation-test-report.json');
  
  if (notFixed === 0 && noNav === 0) {
    console.log('\n✅ SUCCESS: All pages have fixed navigation!');
  } else {
    console.log(`\n❌ ISSUES FOUND: ${notFixed + noNav} pages need fixes`);
  }
  
  await browser.close();
})();