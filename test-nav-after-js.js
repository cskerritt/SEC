const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  console.log('Testing navigation after JavaScript execution...\n');
  
  await page.goto('http://localhost:4000/');
  
  // Wait for JavaScript to execute
  await page.waitForTimeout(1000);
  
  const result = await page.evaluate(() => {
    const nav = document.querySelector('.main-nav');
    if (!nav) return { found: false };
    
    const computedStyles = window.getComputedStyle(nav);
    const inlineStyles = nav.style;
    
    return {
      found: true,
      computedPosition: computedStyles.position,
      inlinePosition: inlineStyles.position,
      computedTop: computedStyles.top,
      inlineTop: inlineStyles.top,
      computedZIndex: computedStyles.zIndex,
      inlineZIndex: inlineStyles.zIndex,
      bodyPaddingTop: window.getComputedStyle(document.body).paddingTop,
      jsScriptLoaded: !!document.querySelector('script[src*="force-navigation-fixed"]')
    };
  });
  
  console.log('Navigation Analysis:');
  if (result.found) {
    console.log('  Computed position:', result.computedPosition);
    console.log('  Inline position:', result.inlinePosition || '(none)');
    console.log('  Computed top:', result.computedTop);
    console.log('  Inline top:', result.inlineTop || '(none)');
    console.log('  Computed z-index:', result.computedZIndex);
    console.log('  Inline z-index:', result.inlineZIndex || '(none)');
    console.log('  Body padding-top:', result.bodyPaddingTop);
    console.log('  Force-nav JS loaded:', result.jsScriptLoaded ? '✓' : '✗');
  } else {
    console.log('  Navigation not found!');
  }
  
  await browser.close();
})();