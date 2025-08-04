const { chromium } = require('playwright');

async function testLayouts() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  const page = await context.newPage();
  
  const pages = [
    { url: 'http://localhost:4000/', name: 'Homepage' },
    { url: 'http://localhost:4000/services/', name: 'Services' },
    { url: 'http://localhost:4000/practice-areas/', name: 'Practice Areas' },
    { url: 'http://localhost:4000/about/', name: 'About' },
    { url: 'http://localhost:4000/case-studies/', name: 'Case Studies' }
  ];
  
  for (const pageInfo of pages) {
    console.log('Checking layout of: ' + pageInfo.name);
    await page.goto(pageInfo.url, { waitUntil: 'networkidle' });
    
    // Check for main sections
    const hasHero = await page.locator('.hero, .page-header, .about-hero').count() > 0;
    const hasContainer = await page.locator('.container').count() > 0;
    const hasContent = await page.locator('main, section').count() > 0;
    
    console.log('  Has hero/header: ' + hasHero);
    console.log('  Has container: ' + hasContainer);
    console.log('  Has content sections: ' + hasContent);
    
    // Check spacing
    const firstSection = await page.locator('section').first();
    if (await firstSection.count() > 0) {
      const padding = await firstSection.evaluate(el => {
        const styles = window.getComputedStyle(el);
        return {
          top: styles.paddingTop,
          bottom: styles.paddingBottom
        };
      });
      console.log('  Section padding: ' + padding.top + ' / ' + padding.bottom);
    }
    
    console.log('');
  }
  
  await browser.close();
}

testLayouts().catch(console.error);
