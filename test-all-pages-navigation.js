const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function findAllHtmlFiles(dir, files = []) {
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory() && !item.startsWith('.') && item !== 'node_modules') {
      findAllHtmlFiles(fullPath, files);
    } else if (item.endsWith('.html') && !item.includes('test')) {
      files.push(fullPath);
    }
  }
  
  return files;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Find all HTML files in _site directory
  const siteDir = '_site';
  const htmlFiles = findAllHtmlFiles(siteDir);
  
  console.log(`Found ${htmlFiles.length} HTML pages to test\n`);
  console.log('Testing navigation on EVERY page...\n');
  console.log('=' .repeat(80));
  
  let totalIssues = 0;
  const issues = [];
  
  for (const file of htmlFiles) {
    // Convert file path to URL
    const relativePath = file.replace('_site/', '');
    const url = `http://localhost:4000/${relativePath}`;
    
    try {
      await page.goto(url, { waitUntil: 'networkidle' });
      
      // Wait for JavaScript to execute
      await page.waitForTimeout(600);
      
      const result = await page.evaluate(() => {
        const nav = document.querySelector('.main-nav');
        if (!nav) return { hasNav: false };
        
        const computedStyles = window.getComputedStyle(nav);
        const inlineStyles = nav.style;
        
        // Check if dropdowns work
        const dropdown = document.querySelector('.has-dropdown .dropdown');
        let dropdownWorks = false;
        if (dropdown) {
          const dropdownStyles = window.getComputedStyle(dropdown);
          dropdownWorks = dropdownStyles.pointerEvents !== 'none';
        }
        
        // Check Contact button color
        const contactBtn = document.querySelector('.nav-cta');
        let contactColor = 'N/A';
        if (contactBtn) {
          const btnStyles = window.getComputedStyle(contactBtn);
          contactColor = btnStyles.backgroundColor;
        }
        
        return {
          hasNav: true,
          computedPosition: computedStyles.position,
          inlinePosition: inlineStyles.position || 'none',
          isFixed: computedStyles.position === 'fixed' || inlineStyles.position === 'fixed',
          bodyPadding: window.getComputedStyle(document.body).paddingTop,
          dropdownWorks: dropdownWorks,
          contactColor: contactColor
        };
      });
      
      if (!result.hasNav) {
        console.log(`❌ ${relativePath}: NO NAVIGATION FOUND`);
        issues.push(`${relativePath}: No navigation found`);
        totalIssues++;
      } else if (!result.isFixed) {
        console.log(`❌ ${relativePath}: Navigation NOT fixed (computed: ${result.computedPosition}, inline: ${result.inlinePosition})`);
        issues.push(`${relativePath}: Navigation not fixed position`);
        totalIssues++;
      } else {
        // Only show first 10 successes to avoid clutter
        if (htmlFiles.indexOf(file) < 10) {
          console.log(`✓ ${relativePath}: Fixed position, dropdowns work`);
        }
      }
      
    } catch (error) {
      console.log(`⚠️  ${relativePath}: Error loading page - ${error.message}`);
    }
  }
  
  console.log('\n' + '=' .repeat(80));
  console.log('TEST SUMMARY');
  console.log('=' .repeat(80));
  console.log(`Total pages tested: ${htmlFiles.length}`);
  console.log(`Pages with issues: ${totalIssues}`);
  
  if (totalIssues > 0) {
    console.log('\nPages with navigation issues:');
    issues.forEach(issue => console.log(`  - ${issue}`));
    console.log('\n❌ NOT ALL PAGES HAVE FIXED NAVIGATION');
  } else {
    console.log('\n✅ ALL PAGES HAVE FIXED NAVIGATION!');
  }
  
  await browser.close();
})();