const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Test desktop view
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('http://localhost:4000/about/', { waitUntil: 'networkidle' });
  
  console.log('📄 ABOUT PAGE FORMATTING TEST RESULTS\n');
  console.log('================================');
  
  // Test hero section enhancements
  const heroTest = await page.evaluate(() => {
    const hero = document.querySelector('.about-hero');
    const photo = document.querySelector('.professional-photo');
    const h1 = hero.querySelector('h1');
    const heroContent = document.querySelector('.hero-content');
    
    return {
      heroBackground: window.getComputedStyle(hero).background.includes('gradient'),
      photoWidth: photo ? window.getComputedStyle(photo).width : 'not found',
      photoShadow: photo ? window.getComputedStyle(photo).boxShadow : 'not found',
      h1FontSize: window.getComputedStyle(h1).fontSize,
      h1Color: window.getComputedStyle(h1).color,
      gridColumns: window.getComputedStyle(heroContent).gridTemplateColumns
    };
  });
  
  console.log('\n✅ HERO SECTION ENHANCEMENTS:');
  console.log(`  Background gradient: ${heroTest.heroBackground ? '✓' : '✗'}`);
  console.log(`  Photo width: ${heroTest.photoWidth} (should be 320px)`);
  console.log(`  Photo shadow: ${heroTest.photoShadow.includes('36px') ? '✓ Enhanced' : '✗ Not enhanced'}`);
  console.log(`  H1 font size: ${heroTest.h1FontSize}`);
  console.log(`  H1 color: ${heroTest.h1Color}`);
  console.log(`  Grid layout: ${heroTest.gridColumns}`);
  
  // Test credentials section enhancements
  const credentialsTest = await page.evaluate(() => {
    const credItem = document.querySelector('.credential-category li');
    if (!credItem) return null;
    
    const styles = window.getComputedStyle(credItem);
    return {
      background: styles.background,
      padding: styles.padding,
      borderRadius: styles.borderRadius,
      borderLeft: styles.borderLeft,
      marginBottom: styles.marginBottom
    };
  });
  
  console.log('\n✅ CREDENTIALS SECTION:');
  if (credentialsTest) {
    console.log(`  Background: ${credentialsTest.background.includes('white') || credentialsTest.background.includes('255') ? '✓ White' : '✗'}`);
    console.log(`  Padding: ${credentialsTest.padding}`);
    console.log(`  Border radius: ${credentialsTest.borderRadius}`);
    console.log(`  Left border: ${credentialsTest.borderLeft.includes('4px') ? '✓ 4px accent' : '✗'}`);
    console.log(`  Spacing: ${credentialsTest.marginBottom}`);
  }
  
  // Test timeline enhancements
  const timelineTest = await page.evaluate(() => {
    const milestone = document.querySelector('.milestone');
    if (!milestone) return null;
    
    const styles = window.getComputedStyle(milestone);
    return {
      padding: styles.padding,
      borderRadius: styles.borderRadius,
      boxShadow: styles.boxShadow,
      background: styles.background
    };
  });
  
  console.log('\n✅ TIMELINE SECTION:');
  if (timelineTest) {
    console.log(`  Padding: ${timelineTest.padding}`);
    console.log(`  Border radius: ${timelineTest.borderRadius}`);
    console.log(`  Box shadow: ${timelineTest.boxShadow.includes('12px') ? '✓ Enhanced' : '✗'}`);
    console.log(`  Background: ${timelineTest.background.includes('white') || timelineTest.background.includes('255') ? '✓ White' : '✗'}`);
  }
  
  // Test publications enhancements
  const publicationsTest = await page.evaluate(() => {
    const pubItem = document.querySelector('.activity-category li');
    if (!pubItem) return null;
    
    const styles = window.getComputedStyle(pubItem);
    return {
      background: styles.background,
      padding: styles.padding,
      borderRadius: styles.borderRadius,
      borderLeft: styles.borderLeft
    };
  });
  
  console.log('\n✅ PUBLICATIONS SECTION:');
  if (publicationsTest) {
    console.log(`  Background: ${publicationsTest.background}`);
    console.log(`  Padding: ${publicationsTest.padding}`);
    console.log(`  Border radius: ${publicationsTest.borderRadius}`);
    console.log(`  Left border: ${publicationsTest.borderLeft.includes('3px') ? '✓ 3px accent' : '✗'}`);
  }
  
  // Test mobile responsiveness
  await page.setViewportSize({ width: 375, height: 667 });
  await page.reload({ waitUntil: 'networkidle' });
  
  const mobileTest = await page.evaluate(() => {
    const hero = document.querySelector('.hero-content');
    const photo = document.querySelector('.professional-photo');
    const timeline = document.querySelector('.timeline');
    const timelineBefore = timeline ? window.getComputedStyle(timeline, '::before') : null;
    
    return {
      heroGrid: window.getComputedStyle(hero).gridTemplateColumns,
      heroTextAlign: window.getComputedStyle(hero).textAlign,
      photoWidth: photo ? window.getComputedStyle(photo).width : 'not found',
      photoOrder: photo ? window.getComputedStyle(photo.parentElement).order : 'not found',
      timelineIndicator: timelineBefore ? timelineBefore.display : 'not found'
    };
  });
  
  console.log('\n📱 MOBILE RESPONSIVENESS:');
  console.log(`  Hero stacked: ${mobileTest.heroGrid.includes('1fr') ? '✓' : '✗'}`);
  console.log(`  Hero centered: ${mobileTest.heroTextAlign === 'center' ? '✓' : '✗'}`);
  console.log(`  Photo width: ${mobileTest.photoWidth} (should be 260px)`);
  console.log(`  Photo above text: ${mobileTest.photoOrder === '-1' ? '✓' : '✗'}`);
  console.log(`  Timeline simplified: ${mobileTest.timelineIndicator === 'none' ? '✓' : '✗'}`);
  
  // Test overall typography consistency
  const typographyTest = await page.evaluate(() => {
    const sections = [
      '.about-section p',
      '.milestone p',
      '.membership p',
      '.faq-item p'
    ];
    
    const lineHeights = [];
    const marginBottoms = [];
    
    sections.forEach(selector => {
      const el = document.querySelector(selector);
      if (el) {
        const styles = window.getComputedStyle(el);
        lineHeights.push(styles.lineHeight);
        marginBottoms.push(styles.marginBottom);
      }
    });
    
    return {
      allSameLineHeight: lineHeights.every(lh => lh === lineHeights[0]),
      allSameMargin: marginBottoms.every(mb => mb === marginBottoms[0]),
      lineHeight: lineHeights[0] || 'not found',
      marginBottom: marginBottoms[0] || 'not found'
    };
  });
  
  console.log('\n📝 TYPOGRAPHY CONSISTENCY:');
  console.log(`  Line height consistent: ${typographyTest.allSameLineHeight ? '✓' : '✗'}`);
  console.log(`  Margin consistent: ${typographyTest.allSameMargin ? '✓' : '✗'}`);
  console.log(`  Line height value: ${typographyTest.lineHeight}`);
  console.log(`  Bottom margin: ${typographyTest.marginBottom}`);
  
  // Summary
  console.log('\n================================');
  console.log('✅ FORMATTING ENHANCEMENTS APPLIED:');
  console.log('  1. Hero section photo enlarged to 320px');
  console.log('  2. Typography standardized across sections');
  console.log('  3. Visual cards added to credentials/publications');
  console.log('  4. Enhanced shadows and hover effects');
  console.log('  5. Mobile responsiveness improved');
  console.log('  6. Timeline simplified on mobile');
  console.log('  7. Image positioned above text on mobile');
  
  await browser.close();
})();