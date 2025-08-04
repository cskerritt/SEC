const { chromium } = require('playwright');

async function auditPage(page, url, pageName) {
  await page.goto(url, { waitUntil: 'networkidle' });
  
  const issues = await page.evaluate(() => {
    const problems = [];
    
    // Check hero/header sections
    const hero = document.querySelector('.hero, .page-header, .service-hero, .practice-hero, .location-hero, .blog-hero, .contact-hero, .about-hero, .case-studies-header');
    if (hero) {
      const heroStyles = window.getComputedStyle(hero);
      const heroText = hero.querySelector('h1, h2');
      
      if (heroText) {
        const textColor = window.getComputedStyle(heroText).color;
        if (!textColor.includes('255')) {
          problems.push('Hero text not white');
        }
      }
      
      if (!heroStyles.background.includes('gradient')) {
        problems.push('Hero missing gradient background');
      }
      
      const container = hero.querySelector('.container');
      if (container) {
        const containerStyles = window.getComputedStyle(container);
        const maxWidth = containerStyles.maxWidth;
        if (maxWidth !== '1200px' && maxWidth !== '1280px') {
          problems.push(`Container max-width inconsistent: ${maxWidth}`);
        }
      }
    }
    
    // Check navigation
    const nav = document.querySelector('.main-nav');
    if (nav) {
      const navStyles = window.getComputedStyle(nav);
      if (navStyles.position !== 'fixed') {
        problems.push('Navigation not fixed position');
      }
    }
    
    // Check content sections
    const sections = document.querySelectorAll('section');
    const paddings = new Set();
    sections.forEach(section => {
      const padding = window.getComputedStyle(section).padding;
      paddings.add(padding);
    });
    
    if (paddings.size > 3) {
      problems.push(`Inconsistent section padding: ${paddings.size} different values`);
    }
    
    // Check typography
    const paragraphs = document.querySelectorAll('p');
    const lineHeights = new Set();
    const fontSizes = new Set();
    
    paragraphs.forEach(p => {
      const styles = window.getComputedStyle(p);
      lineHeights.add(styles.lineHeight);
      fontSizes.add(styles.fontSize);
    });
    
    if (lineHeights.size > 4) {
      problems.push(`Too many line-height variations: ${lineHeights.size}`);
    }
    
    if (fontSizes.size > 5) {
      problems.push(`Too many font-size variations: ${fontSizes.size}`);
    }
    
    // Check buttons
    const buttons = document.querySelectorAll('.btn, button, a.btn-primary, a.btn-secondary');
    const buttonHeights = new Set();
    
    buttons.forEach(btn => {
      const height = window.getComputedStyle(btn).height;
      buttonHeights.add(height);
    });
    
    if (buttonHeights.size > 3) {
      problems.push(`Inconsistent button heights: ${buttonHeights.size} different values`);
    }
    
    // Check cards
    const cards = document.querySelectorAll('.service-card, .location-card, .practice-card, .blog-card, .case-study-card');
    const cardShadows = new Set();
    
    cards.forEach(card => {
      const shadow = window.getComputedStyle(card).boxShadow;
      cardShadows.add(shadow);
    });
    
    if (cardShadows.size > 2) {
      problems.push(`Inconsistent card shadows: ${cardShadows.size} different values`);
    }
    
    // Check grids
    const grids = document.querySelectorAll('.services-grid, .locations-grid, .practice-areas-grid');
    grids.forEach(grid => {
      const gap = window.getComputedStyle(grid).gap;
      if (!gap.includes('30px') && !gap.includes('2rem') && !gap.includes('24px')) {
        problems.push(`Non-standard grid gap: ${gap}`);
      }
    });
    
    return problems;
  });
  
  return { pageName, url, issues };
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1920, height: 1080 });
  
  const pagesToAudit = [
    { name: 'Homepage', url: 'http://localhost:4000/' },
    { name: 'About', url: 'http://localhost:4000/about/' },
    { name: 'Services Main', url: 'http://localhost:4000/services/' },
    { name: 'Forensic Economics Service', url: 'http://localhost:4000/services/forensic-economics/' },
    { name: 'Life Care Planning Service', url: 'http://localhost:4000/services/life-care-planning/' },
    { name: 'Vocational Expert Service', url: 'http://localhost:4000/services/vocational-expert/' },
    { name: 'Business Valuation Service', url: 'http://localhost:4000/services/business-valuation/' },
    { name: 'Personal Injury Practice', url: 'http://localhost:4000/practice-areas/personal-injury/' },
    { name: 'Medical Malpractice Practice', url: 'http://localhost:4000/practice-areas/medical-malpractice/' },
    { name: 'Employment Practice', url: 'http://localhost:4000/practice-areas/employment/' },
    { name: 'Blog', url: 'http://localhost:4000/blog/' },
    { name: 'Case Studies', url: 'http://localhost:4000/case-studies/' },
    { name: 'Contact', url: 'http://localhost:4000/contact/' },
    { name: 'Rhode Island Location', url: 'http://localhost:4000/locations/rhode-island/' },
    { name: 'Massachusetts Location', url: 'http://localhost:4000/locations/massachusetts/' }
  ];
  
  console.log('🔍 UI/UX AUDIT REPORT\n');
  console.log('=' .repeat(60));
  
  const allIssues = [];
  
  for (const pageInfo of pagesToAudit) {
    const result = await auditPage(page, pageInfo.url, pageInfo.name);
    allIssues.push(result);
    
    if (result.issues.length > 0) {
      console.log(`\n❌ ${result.pageName}:`);
      result.issues.forEach(issue => {
        console.log(`   - ${issue}`);
      });
    } else {
      console.log(`\n✅ ${result.pageName}: No issues found`);
    }
  }
  
  // Summary
  console.log('\n' + '=' .repeat(60));
  console.log('📊 SUMMARY\n');
  
  const commonIssues = {};
  allIssues.forEach(page => {
    page.issues.forEach(issue => {
      if (!commonIssues[issue]) {
        commonIssues[issue] = [];
      }
      commonIssues[issue].push(page.pageName);
    });
  });
  
  console.log('Most common issues:');
  Object.entries(commonIssues)
    .sort((a, b) => b[1].length - a[1].length)
    .forEach(([issue, pages]) => {
      if (pages.length > 1) {
        console.log(`\n"${issue}" affects ${pages.length} pages:`);
        console.log(`  ${pages.join(', ')}`);
      }
    });
  
  await browser.close();
})();