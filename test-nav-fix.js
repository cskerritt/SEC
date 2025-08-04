const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('http://localhost:4000/');
  await page.waitForLoadState('networkidle');
  
  // Check if navigation is fixed
  const navPosition = await page.evaluate(() => {
    const nav = document.querySelector('.main-nav');
    if (\!nav) return 'No navigation found';
    const styles = window.getComputedStyle(nav);
    return styles.position;
  });
  
  console.log('Navigation position:', navPosition);
  
  // Check if ultimate-consistency-fix.css is loaded
  const cssLoaded = await page.evaluate(() => {
    const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'));
    return links.some(link => link.href.includes('ultimate-consistency-fix.css'));
  });
  
  console.log('Ultimate consistency CSS loaded:', cssLoaded);
  
  // Check if navigation fix override is loaded
  const overrideLoaded = await page.evaluate(() => {
    const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'));
    return links.some(link => link.href.includes('navigation-fix-override.css'));
  });
  
  console.log('Navigation override CSS loaded:', overrideLoaded);
  
  // Check body padding
  const bodyPadding = await page.evaluate(() => {
    const styles = window.getComputedStyle(document.body);
    return styles.paddingTop;
  });
  
  console.log('Body padding-top:', bodyPadding);
  
  await browser.close();
})();
