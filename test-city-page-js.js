const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Enable console logging
  page.on('console', msg => console.log('Browser console:', msg.text()));
  page.on('pageerror', err => console.log('Page error:', err));
  
  const url = 'http://localhost:4000/locations/cities/providence-ri-forensic-economist.html';
  
  console.log('Loading:', url);
  await page.goto(url, { waitUntil: 'networkidle' });
  
  // Check what scripts are loaded
  const scripts = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('script[src]')).map(s => s.src);
  });
  
  console.log('\nScripts loaded:');
  scripts.forEach(s => console.log('  -', s));
  
  // Check what CSS is loaded
  const styles = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('link[rel="stylesheet"]')).map(l => l.href);
  });
  
  console.log('\nCSS loaded:');
  styles.forEach(s => console.log('  -', s));
  
  // Wait for JS to execute
  await page.waitForTimeout(1000);
  
  // Check navigation position
  const navInfo = await page.evaluate(() => {
    const nav = document.querySelector('.main-nav');
    if (!nav) return { found: false };
    
    const computed = window.getComputedStyle(nav);
    const inline = nav.style;
    
    return {
      found: true,
      computedPosition: computed.position,
      inlinePosition: inline.position || 'none',
      bodyPadding: window.getComputedStyle(document.body).paddingTop,
      navClasses: nav.className,
      jsExecuted: window.navigationFixed || false
    };
  });
  
  console.log('\nNavigation status:');
  console.log('  Found:', navInfo.found);
  if (navInfo.found) {
    console.log('  Computed position:', navInfo.computedPosition);
    console.log('  Inline position:', navInfo.inlinePosition);
    console.log('  Body padding:', navInfo.bodyPadding);
    console.log('  Nav classes:', navInfo.navClasses);
  }
  
  await browser.close();
})();