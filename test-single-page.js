const { chromium } = require('playwright');

(async () => {
  const url = process.argv[2];
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 5000 });
    await page.waitForTimeout(600);
    
    const result = await page.evaluate(() => {
      const nav = document.querySelector('.main-nav');
      if (!nav) return 'NO_NAV';
      
      const computedStyles = window.getComputedStyle(nav);
      const inlineStyles = nav.style;
      const finalPosition = inlineStyles.position || computedStyles.position;
      
      return finalPosition === 'fixed' ? 'FIXED' : finalPosition.toUpperCase();
    });
    
    console.log(result);
  } catch (error) {
    console.log('ERROR');
  }
  
  await browser.close();
})();
