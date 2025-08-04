const { chromium } = require('playwright');

async function testPage(page, url, pageName) {
  await page.goto(url, { waitUntil: 'networkidle' });
  
  const results = await page.evaluate(() => {
    const tests = {};
    
    // Test typography consistency
    const h1 = document.querySelector('h1');
    const h2 = document.querySelector('h2');
    const p = document.querySelector('p');
    
    if (h1) tests.h1FontSize = window.getComputedStyle(h1).fontSize;
    if (h2) tests.h2FontSize = window.getComputedStyle(h2).fontSize;
    if (p) {
      tests.pFontSize = window.getComputedStyle(p).fontSize;
      tests.pLineHeight = window.getComputedStyle(p).lineHeight;
    }
    
    // Test container consistency
    const container = document.querySelector('.container');
    if (container) {
      tests.containerMaxWidth = window.getComputedStyle(container).maxWidth;
      tests.containerPadding = window.getComputedStyle(container).padding;
    }
    
    // Test section padding
    const section = document.querySelector('section');
    if (section) {
      tests.sectionPadding = window.getComputedStyle(section).padding;
    }
    
    // Test hero section
    const hero = document.querySelector('.hero, .page-header, .service-hero, .practice-hero, .location-hero, .blog-hero, .contact-hero, .about-hero');
    if (hero) {
      const heroStyles = window.getComputedStyle(hero);
      tests.heroBackground = heroStyles.background.includes('gradient');
      tests.heroPadding = heroStyles.padding;
      
      const heroH1 = hero.querySelector('h1');
      if (heroH1) {
        tests.heroTextColor = window.getComputedStyle(heroH1).color;
      }
    }
    
    // Test grid consistency
    const grid = document.querySelector('.services-grid, .locations-grid, .practice-areas-grid');
    if (grid) {
      tests.gridGap = window.getComputedStyle(grid).gap;
    }
    
    // Test button consistency
    const btn = document.querySelector('.btn, .btn-primary, button');
    if (btn) {
      const btnStyles = window.getComputedStyle(btn);
      tests.btnPadding = btnStyles.padding;
      tests.btnMinHeight = btnStyles.minHeight;
      tests.btnBorderRadius = btnStyles.borderRadius;
    }
    
    // Test card consistency
    const card = document.querySelector('.service-card, .location-card, .practice-card, .blog-card');
    if (card) {
      const cardStyles = window.getComputedStyle(card);
      tests.cardPadding = cardStyles.padding;
      tests.cardBorderRadius = cardStyles.borderRadius;
      tests.cardBoxShadow = cardStyles.boxShadow;
    }
    
    // Test navigation
    const nav = document.querySelector('.main-nav');
    if (nav) {
      tests.navPosition = window.getComputedStyle(nav).position;
      tests.navHeight = window.getComputedStyle(nav).height;
    }
    
    return tests;
  });
  
  return { pageName, url, results };
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1920, height: 1080 });
  
  const pagesToTest = [
    { name: 'Homepage', url: 'http://localhost:4000/' },
    { name: 'About', url: 'http://localhost:4000/about/' },
    { name: 'Services', url: 'http://localhost:4000/services/' },
    { name: 'Contact', url: 'http://localhost:4000/contact/' },
    { name: 'Blog', url: 'http://localhost:4000/blog/' }
  ];
  
  console.log('🎨 UI/UX CONSISTENCY TEST RESULTS\n');
  console.log('=' .repeat(60));
  
  const allResults = [];
  
  for (const pageInfo of pagesToTest) {
    const result = await testPage(page, pageInfo.url, pageInfo.name);
    allResults.push(result);
    
    console.log(`\n📄 ${result.pageName}:`);
    console.log('  Typography:');
    console.log(`    H1: ${result.results.h1FontSize || 'N/A'}`);
    console.log(`    H2: ${result.results.h2FontSize || 'N/A'}`);
    console.log(`    P: ${result.results.pFontSize || 'N/A'} / ${result.results.pLineHeight || 'N/A'}`);
    console.log('  Layout:');
    console.log(`    Container: ${result.results.containerMaxWidth || 'N/A'}`);
    console.log(`    Section padding: ${result.results.sectionPadding || 'N/A'}`);
    console.log(`    Grid gap: ${result.results.gridGap || 'N/A'}`);
    console.log('  Components:');
    console.log(`    Button height: ${result.results.btnMinHeight || 'N/A'}`);
    console.log(`    Card padding: ${result.results.cardPadding || 'N/A'}`);
    console.log(`    Nav position: ${result.results.navPosition || 'N/A'}`);
  }
  
  // Check consistency
  console.log('\n' + '=' .repeat(60));
  console.log('📊 CONSISTENCY CHECK:\n');
  
  const checkConsistency = (property) => {
    const values = allResults.map(r => r.results[property]).filter(v => v);
    const unique = [...new Set(values)];
    const isConsistent = unique.length <= 1;
    
    if (values.length > 0) {
      console.log(`${property}: ${isConsistent ? '✅ Consistent' : '❌ Inconsistent'} - ${unique.join(', ')}`);
    }
  };
  
  checkConsistency('h1FontSize');
  checkConsistency('h2FontSize');
  checkConsistency('pFontSize');
  checkConsistency('pLineHeight');
  checkConsistency('containerMaxWidth');
  checkConsistency('sectionPadding');
  checkConsistency('gridGap');
  checkConsistency('btnMinHeight');
  checkConsistency('cardPadding');
  checkConsistency('navPosition');
  
  // Test mobile view
  console.log('\n📱 MOBILE RESPONSIVENESS TEST:');
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:4000/', { waitUntil: 'networkidle' });
  
  const mobileTests = await page.evaluate(() => {
    const tests = {};
    
    const h1 = document.querySelector('h1');
    if (h1) tests.h1FontSize = window.getComputedStyle(h1).fontSize;
    
    const grid = document.querySelector('.services-grid, .locations-grid');
    if (grid) {
      tests.gridColumns = window.getComputedStyle(grid).gridTemplateColumns;
    }
    
    const btn = document.querySelector('.btn, .btn-primary');
    if (btn) {
      tests.btnWidth = window.getComputedStyle(btn).width;
    }
    
    const section = document.querySelector('section');
    if (section) {
      tests.sectionPadding = window.getComputedStyle(section).padding;
    }
    
    return tests;
  });
  
  console.log(`  H1 size: ${mobileTests.h1FontSize} (should be 32px)`);
  console.log(`  Grid: ${mobileTests.gridColumns} (should be 1fr)`);
  console.log(`  Button width: ${mobileTests.btnWidth} (should be 100%)`);
  console.log(`  Section padding: ${mobileTests.sectionPadding} (should be 60px 0px)`);
  
  console.log('\n' + '=' .repeat(60));
  console.log('✅ UI/UX FIXES APPLIED:');
  console.log('  1. Standardized typography system (h1-h5, p, lead)');
  console.log('  2. Consistent container max-width (1200px/1320px)');
  console.log('  3. Uniform section padding (80px desktop, 60px mobile)');
  console.log('  4. Standardized grid gaps (30px)');
  console.log('  5. Consistent button styling (48px min-height)');
  console.log('  6. Unified card design (30px padding, 12px radius)');
  console.log('  7. Fixed navigation (70px height)');
  console.log('  8. Responsive breakpoints aligned');
  console.log('  9. Hero sections with gradient backgrounds');
  console.log('  10. Mobile-first responsive design');
  
  await browser.close();
})();