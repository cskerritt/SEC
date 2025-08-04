const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Testing navigation position on key pages...\n');
  
  const pages = [
    { url: 'http://localhost:4000/', name: 'Homepage' },
    { url: 'http://localhost:4000/services/', name: 'Services' },
    { url: 'http://localhost:4000/practice-areas/', name: 'Practice Areas' },
    { url: 'http://localhost:4000/about/', name: 'About' }
  ];
  
  for (const testPage of pages) {
    await page.goto(testPage.url);
    await page.waitForLoadState('networkidle');
    
    const result = await page.evaluate(() => {
      const nav = document.querySelector('.main-nav');
      if (!nav) return { found: false };
      
      const styles = window.getComputedStyle(nav);
      const cssFiles = Array.from(document.querySelectorAll('link[rel="stylesheet"]'))
        .map(link => link.href.split('/').pop().split('?')[0]);
      
      return {
        found: true,
        position: styles.position,
        top: styles.top,
        zIndex: styles.zIndex,
        ultimateCssLoaded: cssFiles.includes('ultimate-consistency-fix.css'),
        overrideCssLoaded: cssFiles.includes('navigation-fix-override.css'),
        bodyPaddingTop: window.getComputedStyle(document.body).paddingTop
      };
    });
    
    console.log(`${testPage.name}:`);
    if (result.found) {
      console.log(`  Position: ${result.position}`);
      console.log(`  Top: ${result.top}`);
      console.log(`  Z-Index: ${result.zIndex}`);
      console.log(`  Body Padding: ${result.bodyPaddingTop}`);
      console.log(`  Ultimate CSS: ${result.ultimateCssLoaded ? '✓' : '✗'}`);
      console.log(`  Override CSS: ${result.overrideCssLoaded ? '✓' : '✗'}`);
    } else {
      console.log('  Navigation not found!');
    }
    console.log();
  }
  
  await browser.close();
})();