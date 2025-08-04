const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('http://localhost:4000/about/', { waitUntil: 'networkidle' });
  
  const textColors = await page.evaluate(() => {
    const hero = document.querySelector('.about-hero');
    const h1 = hero.querySelector('h1');
    const title = hero.querySelector('.title');
    const lead = hero.querySelector('.lead');
    
    return {
      heroBackground: window.getComputedStyle(hero).background,
      h1Color: window.getComputedStyle(h1).color,
      titleColor: window.getComputedStyle(title).color,
      leadColor: window.getComputedStyle(lead).color
    };
  });
  
  console.log('About Hero Colors:');
  console.log('  H1 color:', textColors.h1Color);
  console.log('  Title color:', textColors.titleColor);
  console.log('  Lead color:', textColors.leadColor);
  console.log('  Background includes gradient:', textColors.heroBackground.includes('gradient'));
  
  await browser.close();
})();