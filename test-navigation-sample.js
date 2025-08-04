const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Test representative pages from each section
  const testPages = [
    // Main pages
    { url: 'http://localhost:4000/', name: 'Homepage' },
    { url: 'http://localhost:4000/about/', name: 'About' },
    { url: 'http://localhost:4000/contact/', name: 'Contact' },
    { url: 'http://localhost:4000/blog/', name: 'Blog' },
    { url: 'http://localhost:4000/case-studies/', name: 'Case Studies' },
    
    // Service pages
    { url: 'http://localhost:4000/services/', name: 'Services Main' },
    { url: 'http://localhost:4000/services/forensic-economics/', name: 'Forensic Economics' },
    { url: 'http://localhost:4000/services/business-valuation/', name: 'Business Valuation' },
    { url: 'http://localhost:4000/services/life-care-planning/', name: 'Life Care Planning' },
    { url: 'http://localhost:4000/services/vocational-expert/', name: 'Vocational Expert' },
    { url: 'http://localhost:4000/services/business-consulting/', name: 'Business Consulting' },
    
    // Practice areas
    { url: 'http://localhost:4000/practice-areas/', name: 'Practice Areas Main' },
    { url: 'http://localhost:4000/practice-areas/personal-injury/', name: 'Personal Injury' },
    { url: 'http://localhost:4000/practice-areas/medical-malpractice/', name: 'Medical Malpractice' },
    { url: 'http://localhost:4000/practice-areas/employment/', name: 'Employment' },
    { url: 'http://localhost:4000/practice-areas/commercial-disputes/', name: 'Commercial Disputes' },
    { url: 'http://localhost:4000/practice-areas/family-law/', name: 'Family Law' },
    { url: 'http://localhost:4000/practice-areas/product-liability/', name: 'Product Liability' },
    
    // Location pages
    { url: 'http://localhost:4000/locations/', name: 'Locations Main' },
    { url: 'http://localhost:4000/locations/rhode-island/', name: 'Rhode Island' },
    { url: 'http://localhost:4000/locations/massachusetts/', name: 'Massachusetts' },
    { url: 'http://localhost:4000/locations/connecticut/', name: 'Connecticut' },
    
    // Sample city pages
    { url: 'http://localhost:4000/locations/cities/providence-ri-forensic-economist.html', name: 'Providence' },
    { url: 'http://localhost:4000/locations/cities/boston-ma-forensic-economist.html', name: 'Boston' },
    { url: 'http://localhost:4000/locations/cities/hartford-ct-forensic-economist.html', name: 'Hartford' },
    
    // Tool pages
    { url: 'http://localhost:4000/tools/present-value-calculator/', name: 'PV Calculator' },
    { url: 'http://localhost:4000/tools/wage-loss-calculator/', name: 'Wage Loss Calculator' }
  ];
  
  console.log('Testing navigation on sample of key pages...\n');
  console.log('=' .repeat(80));
  
  let totalIssues = 0;
  const issues = [];
  
  for (const testPage of testPages) {
    try {
      await page.goto(testPage.url, { waitUntil: 'networkidle' });
      
      // Wait for JavaScript to execute
      await page.waitForTimeout(700);
      
      const result = await page.evaluate(() => {
        const nav = document.querySelector('.main-nav');
        if (!nav) return { hasNav: false };
        
        const computedStyles = window.getComputedStyle(nav);
        const inlineStyles = nav.style;
        
        // Final position after all CSS and JS
        const finalPosition = inlineStyles.position || computedStyles.position;
        
        return {
          hasNav: true,
          computedPosition: computedStyles.position,
          inlinePosition: inlineStyles.position || 'none',
          finalPosition: finalPosition,
          isFixed: finalPosition === 'fixed',
          bodyPadding: window.getComputedStyle(document.body).paddingTop
        };
      });
      
      const status = result.isFixed ? '✓' : '❌';
      const position = result.isFixed ? 'FIXED' : result.finalPosition.toUpperCase();
      
      console.log(`${status} ${testPage.name.padEnd(25)} - Position: ${position}, Body padding: ${result.bodyPadding}`);
      
      if (!result.isFixed) {
        issues.push(testPage.name);
        totalIssues++;
      }
      
    } catch (error) {
      console.log(`⚠️  ${testPage.name.padEnd(25)} - Error: ${error.message}`);
      issues.push(`${testPage.name} (error)`);
      totalIssues++;
    }
  }
  
  console.log('\n' + '=' .repeat(80));
  console.log('SUMMARY');
  console.log('=' .repeat(80));
  console.log(`Pages tested: ${testPages.length}`);
  console.log(`Pages with fixed navigation: ${testPages.length - totalIssues}`);
  console.log(`Pages with issues: ${totalIssues}`);
  
  if (totalIssues > 0) {
    console.log('\nPages without fixed navigation:');
    issues.forEach(issue => console.log(`  - ${issue}`));
  } else {
    console.log('\n✅ All tested pages have fixed navigation!');
  }
  
  await browser.close();
})();