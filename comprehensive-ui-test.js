const { chromium } = require('playwright');
const fs = require('fs');

// Define test pages from each section
const testPages = [
  // Main pages
  { url: 'http://localhost:4000/', name: 'Homepage', type: 'main' },
  { url: 'http://localhost:4000/about/', name: 'About', type: 'main' },
  { url: 'http://localhost:4000/contact/', name: 'Contact', type: 'main' },
  { url: 'http://localhost:4000/blog/', name: 'Blog', type: 'main' },
  { url: 'http://localhost:4000/case-studies/', name: 'Case Studies', type: 'main' },
  
  // Service pages
  { url: 'http://localhost:4000/services/', name: 'Services Main', type: 'service' },
  { url: 'http://localhost:4000/services/forensic-economics/', name: 'Forensic Economics', type: 'service' },
  { url: 'http://localhost:4000/services/business-valuation/', name: 'Business Valuation', type: 'service' },
  { url: 'http://localhost:4000/services/life-care-planning/', name: 'Life Care Planning', type: 'service' },
  { url: 'http://localhost:4000/services/vocational-expert/', name: 'Vocational Expert', type: 'service' },
  
  // Practice areas
  { url: 'http://localhost:4000/practice-areas/', name: 'Practice Areas Main', type: 'practice' },
  { url: 'http://localhost:4000/practice-areas/personal-injury/', name: 'Personal Injury', type: 'practice' },
  { url: 'http://localhost:4000/practice-areas/medical-malpractice/', name: 'Medical Malpractice', type: 'practice' },
  { url: 'http://localhost:4000/practice-areas/employment/', name: 'Employment', type: 'practice' },
  { url: 'http://localhost:4000/practice-areas/family-law/', name: 'Family Law', type: 'practice' },
  { url: 'http://localhost:4000/practice-areas/product-liability/', name: 'Product Liability', type: 'practice' },
  
  // Locations
  { url: 'http://localhost:4000/locations/', name: 'Locations Main', type: 'location' },
  { url: 'http://localhost:4000/locations/rhode-island/', name: 'Rhode Island', type: 'location' },
  { url: 'http://localhost:4000/locations/massachusetts/', name: 'Massachusetts', type: 'location' },
  { url: 'http://localhost:4000/locations/connecticut/', name: 'Connecticut', type: 'location' },
  
  // Sample city pages
  { url: 'http://localhost:4000/locations/cities/providence-ri-forensic-economist.html', name: 'Providence City', type: 'city' },
  { url: 'http://localhost:4000/locations/cities/boston-ma-forensic-economist.html', name: 'Boston City', type: 'city' },
  { url: 'http://localhost:4000/locations/cities/hartford-ct-forensic-economist.html', name: 'Hartford City', type: 'city' },
  
  // Tools
  { url: 'http://localhost:4000/tools/', name: 'Tools Main', type: 'tool' },
  { url: 'http://localhost:4000/tools/present-value-calculator/', name: 'PV Calculator', type: 'tool' }
];

async function testPage(page, pageInfo) {
  const results = {
    name: pageInfo.name,
    type: pageInfo.type,
    url: pageInfo.url,
    header: {},
    footer: {},
    layout: {},
    typography: {},
    colors: {},
    buttons: {},
    responsive: {},
    navigation: {},
    issues: []
  };
  
  try {
    await page.goto(pageInfo.url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000); // Wait for JS to execute
    
    // Test Header
    const headerTests = await page.evaluate(() => {
      const nav = document.querySelector('.main-nav');
      const logo = document.querySelector('.logo');
      const contactBtn = document.querySelector('.nav-cta');
      const dropdown = document.querySelector('.has-dropdown');
      
      const results = {
        hasNav: !!nav,
        isFixed: nav ? window.getComputedStyle(nav).position === 'fixed' : false,
        navHeight: nav ? nav.offsetHeight : 0,
        hasLogo: !!logo,
        hasContactBtn: !!contactBtn,
        contactBtnColor: contactBtn ? window.getComputedStyle(contactBtn).backgroundColor : 'none',
        hasDropdown: !!dropdown,
        navBg: nav ? window.getComputedStyle(nav).backgroundColor : 'none',
        navShadow: nav ? window.getComputedStyle(nav).boxShadow : 'none'
      };
      
      // Test dropdown functionality
      if (dropdown) {
        dropdown.dispatchEvent(new MouseEvent('mouseenter'));
        const dropdownMenu = dropdown.querySelector('.dropdown');
        results.dropdownWorks = dropdownMenu ? 
          window.getComputedStyle(dropdownMenu).visibility === 'visible' : false;
      }
      
      return results;
    });
    results.header = headerTests;
    
    // Test Footer
    const footerTests = await page.evaluate(() => {
      const footer = document.querySelector('footer, .main-footer, .site-footer');
      
      if (!footer) return { hasFooter: false };
      
      const styles = window.getComputedStyle(footer);
      return {
        hasFooter: true,
        bgColor: styles.backgroundColor,
        textColor: styles.color,
        padding: styles.padding,
        hasCopyright: footer.textContent.includes('©') || footer.textContent.includes('Copyright'),
        hasContactInfo: footer.textContent.includes('chris@skerritteconomics.com'),
        columns: footer.querySelectorAll('.footer-col').length
      };
    });
    results.footer = footerTests;
    
    // Test Layout
    const layoutTests = await page.evaluate(() => {
      const container = document.querySelector('.container');
      const body = document.body;
      const sections = document.querySelectorAll('section');
      const hero = document.querySelector('.hero, .page-header, .service-hero, .practice-hero');
      
      return {
        hasContainer: !!container,
        containerWidth: container ? window.getComputedStyle(container).maxWidth : 'none',
        bodyPaddingTop: window.getComputedStyle(body).paddingTop,
        sectionCount: sections.length,
        hasHero: !!hero,
        heroHasGradient: hero ? 
          window.getComputedStyle(hero).background.includes('gradient') : false
      };
    });
    results.layout = layoutTests;
    
    // Test Typography
    const typographyTests = await page.evaluate(() => {
      const h1 = document.querySelector('h1');
      const h2 = document.querySelector('h2');
      const h3 = document.querySelector('h3');
      const p = document.querySelector('p');
      const body = document.body;
      
      return {
        fontFamily: window.getComputedStyle(body).fontFamily,
        h1Size: h1 ? window.getComputedStyle(h1).fontSize : 'none',
        h1Color: h1 ? window.getComputedStyle(h1).color : 'none',
        h2Size: h2 ? window.getComputedStyle(h2).fontSize : 'none',
        h2Color: h2 ? window.getComputedStyle(h2).color : 'none',
        h3Size: h3 ? window.getComputedStyle(h3).fontSize : 'none',
        bodyTextColor: p ? window.getComputedStyle(p).color : 'none',
        lineHeight: p ? window.getComputedStyle(p).lineHeight : 'none'
      };
    });
    results.typography = typographyTests;
    
    // Test Colors
    const colorTests = await page.evaluate(() => {
      const links = document.querySelectorAll('a');
      const buttons = document.querySelectorAll('.btn');
      const primaryBtn = document.querySelector('.btn-primary');
      const secondaryBtn = document.querySelector('.btn-secondary');
      
      return {
        linkColor: links.length > 0 ? window.getComputedStyle(links[0]).color : 'none',
        primaryBtnBg: primaryBtn ? window.getComputedStyle(primaryBtn).backgroundColor : 'none',
        primaryBtnColor: primaryBtn ? window.getComputedStyle(primaryBtn).color : 'none',
        secondaryBtnBorder: secondaryBtn ? window.getComputedStyle(secondaryBtn).borderColor : 'none'
      };
    });
    results.colors = colorTests;
    
    // Test Buttons
    const buttonTests = await page.evaluate(() => {
      const btn = document.querySelector('.btn');
      
      if (!btn) return { hasButtons: false };
      
      const styles = window.getComputedStyle(btn);
      return {
        hasButtons: true,
        padding: styles.padding,
        borderRadius: styles.borderRadius,
        fontWeight: styles.fontWeight,
        transition: styles.transition
      };
    });
    results.buttons = buttonTests;
    
    // Test Navigation Functionality
    const navTests = await page.evaluate(() => {
      const menuItems = document.querySelectorAll('.nav-menu a');
      const dropdowns = document.querySelectorAll('.has-dropdown');
      
      return {
        menuItemCount: menuItems.length,
        dropdownCount: dropdowns.length,
        allLinksClickable: Array.from(menuItems).every(link => 
          window.getComputedStyle(link).pointerEvents !== 'none'
        )
      };
    });
    results.navigation = navTests;
    
    // Check for issues
    if (!results.header.isFixed) results.issues.push('Navigation not fixed');
    if (!results.header.hasLogo) results.issues.push('Logo missing');
    if (!results.header.hasContactBtn) results.issues.push('Contact button missing');
    if (!results.footer.hasFooter) results.issues.push('Footer missing');
    if (!results.layout.hasContainer) results.issues.push('Container missing');
    if (results.header.navHeight !== 70 && results.header.navHeight !== 60) {
      results.issues.push(`Incorrect nav height: ${results.header.navHeight}px`);
    }
    
  } catch (error) {
    results.error = error.message;
    results.issues.push(`Error loading page: ${error.message}`);
  }
  
  return results;
}

async function runComprehensiveTest() {
  console.log('Starting Comprehensive UI/UX Consistency Test');
  console.log('=' .repeat(80));
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Also test mobile viewport
  const mobilePage = await browser.newPage();
  await mobilePage.setViewportSize({ width: 375, height: 667 });
  
  const results = [];
  const mobileResults = [];
  
  // Test each page
  for (const pageInfo of testPages) {
    process.stdout.write(`Testing ${pageInfo.name}...`);
    
    // Desktop test
    const desktopResult = await testPage(page, pageInfo);
    results.push(desktopResult);
    
    // Mobile test
    const mobileResult = await testPage(mobilePage, { ...pageInfo, name: `${pageInfo.name} (Mobile)` });
    mobileResults.push(mobileResult);
    
    if (desktopResult.issues.length === 0) {
      console.log(' ✓');
    } else {
      console.log(` ✗ (${desktopResult.issues.length} issues)`);
    }
  }
  
  await browser.close();
  
  // Analyze consistency
  console.log('\n' + '=' .repeat(80));
  console.log('CONSISTENCY ANALYSIS');
  console.log('=' .repeat(80));
  
  // Check header consistency
  const navHeights = [...new Set(results.map(r => r.header.navHeight))];
  const navPositions = [...new Set(results.map(r => r.header.isFixed))];
  const contactColors = [...new Set(results.map(r => r.header.contactBtnColor))];
  
  console.log('\n📍 HEADER CONSISTENCY:');
  console.log(`  Navigation positions: ${navPositions.length === 1 && navPositions[0] === true ? '✓ All fixed' : '✗ Inconsistent'}`);
  console.log(`  Navigation heights: ${navHeights.length <= 2 ? '✓ Consistent' : '✗ Varies'} (${navHeights.join(', ')}px)`);
  console.log(`  Contact button colors: ${contactColors.length === 1 ? '✓ Consistent' : '✗ Varies'}`);
  
  // Check footer consistency
  const footerBgs = [...new Set(results.map(r => r.footer.bgColor))];
  const footerColumns = [...new Set(results.map(r => r.footer.columns))];
  
  console.log('\n📍 FOOTER CONSISTENCY:');
  console.log(`  Footer backgrounds: ${footerBgs.length <= 2 ? '✓ Consistent' : '✗ Varies'}`);
  console.log(`  Footer columns: ${footerColumns.length === 1 ? '✓ Consistent' : '✗ Varies'} (${footerColumns.join(', ')} columns)`);
  
  // Check layout consistency
  const containerWidths = [...new Set(results.map(r => r.layout.containerWidth))];
  const bodyPaddings = [...new Set(results.map(r => r.layout.bodyPaddingTop))];
  
  console.log('\n📍 LAYOUT CONSISTENCY:');
  console.log(`  Container widths: ${containerWidths.length <= 2 ? '✓ Consistent' : '✗ Varies'}`);
  console.log(`  Body padding-top: ${bodyPaddings.length <= 2 ? '✓ Consistent' : '✗ Varies'} (${bodyPaddings.join(', ')})`);
  
  // Check typography consistency
  const fonts = [...new Set(results.map(r => r.typography.fontFamily))];
  const h1Sizes = [...new Set(results.map(r => r.typography.h1Size))];
  
  console.log('\n📍 TYPOGRAPHY CONSISTENCY:');
  console.log(`  Font families: ${fonts.length === 1 ? '✓ Consistent' : '✗ Varies'}`);
  console.log(`  H1 sizes: ${h1Sizes.length <= 3 ? '✓ Consistent' : '✗ Varies'}`);
  
  // List pages with issues
  const pagesWithIssues = results.filter(r => r.issues.length > 0);
  if (pagesWithIssues.length > 0) {
    console.log('\n⚠️  PAGES WITH ISSUES:');
    pagesWithIssues.forEach(page => {
      console.log(`  ${page.name}:`);
      page.issues.forEach(issue => console.log(`    - ${issue}`));
    });
  } else {
    console.log('\n✅ All pages passed consistency checks!');
  }
  
  // Mobile specific issues
  const mobileIssues = mobileResults.filter(r => r.issues.length > 0);
  if (mobileIssues.length > 0) {
    console.log('\n📱 MOBILE ISSUES:');
    console.log(`  ${mobileIssues.length} pages have mobile-specific issues`);
  }
  
  // Save detailed report
  const report = {
    timestamp: new Date().toISOString(),
    summary: {
      totalPages: testPages.length,
      pagesWithIssues: pagesWithIssues.length,
      desktopResults: results,
      mobileResults: mobileResults,
      consistency: {
        navHeights,
        navPositions,
        contactColors,
        footerBgs,
        containerWidths,
        fonts
      }
    }
  };
  
  fs.writeFileSync('ui-consistency-report.json', JSON.stringify(report, null, 2));
  console.log('\n📄 Detailed report saved to ui-consistency-report.json');
  
  return report;
}

// Run the test
runComprehensiveTest().catch(console.error);