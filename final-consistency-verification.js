const { chromium } = require('playwright');
const fs = require('fs');
const { execSync } = require('child_process');

async function getRandomCityPages(count) {
  // Get random city pages
  const allCityPages = execSync('find _site/locations/cities -name "*.html" | sort -R | head -' + count)
    .toString()
    .trim()
    .split('\n')
    .filter(f => f);
  
  return allCityPages.map(file => ({
    url: `http://localhost:4000/${file.replace('_site/', '')}`,
    name: file.split('/').pop(),
    type: 'city'
  }));
}

async function testPageConsistency(page, pageInfo) {
  await page.goto(pageInfo.url, { waitUntil: 'domcontentloaded', timeout: 10000 });
  await page.waitForTimeout(800);
  
  const consistency = await page.evaluate(() => {
    const nav = document.querySelector('.main-nav');
    const footer = document.querySelector('footer, .main-footer');
    const container = document.querySelector('.container');
    const body = document.body;
    
    // Get computed styles
    const navStyles = nav ? window.getComputedStyle(nav) : null;
    const footerStyles = footer ? window.getComputedStyle(footer) : null;
    const bodyStyles = window.getComputedStyle(body);
    
    return {
      header: {
        exists: !!nav,
        isFixed: navStyles ? navStyles.position === 'fixed' : false,
        height: nav ? nav.offsetHeight : 0,
        background: navStyles ? navStyles.backgroundColor : 'none'
      },
      footer: {
        exists: !!footer,
        background: footerStyles ? footerStyles.backgroundColor : 'none',
        hasContact: footer ? footer.textContent.includes('@skerritteconomics.com') : false
      },
      layout: {
        hasContainer: !!container,
        bodyPaddingTop: bodyStyles.paddingTop,
        fontFamily: bodyStyles.fontFamily.split(',')[0].replace(/['"]/g, '')
      },
      navigation: {
        dropdownsExist: !!document.querySelector('.has-dropdown'),
        contactBtnExists: !!document.querySelector('.nav-cta')
      }
    };
  });
  
  return {
    ...pageInfo,
    ...consistency,
    passes: consistency.header.isFixed && 
            consistency.footer.exists && 
            consistency.layout.hasContainer
  };
}

async function runFinalVerification() {
  console.log('FINAL UI/UX CONSISTENCY VERIFICATION');
  console.log('=' .repeat(80));
  console.log('Testing random sample of pages across all categories...\n');
  
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  // Get test pages
  const mainPages = [
    { url: 'http://localhost:4000/', name: 'Homepage', type: 'main' },
    { url: 'http://localhost:4000/about/', name: 'About', type: 'main' },
    { url: 'http://localhost:4000/services/', name: 'Services', type: 'service' },
    { url: 'http://localhost:4000/practice-areas/', name: 'Practice Areas', type: 'practice' },
    { url: 'http://localhost:4000/locations/', name: 'Locations', type: 'location' }
  ];
  
  // Get 50 random city pages
  const cityPages = await getRandomCityPages(50);
  
  const allPages = [...mainPages, ...cityPages];
  
  console.log(`Testing ${allPages.length} pages (${mainPages.length} main + ${cityPages.length} city pages)\n`);
  
  const results = [];
  let passCount = 0;
  let failCount = 0;
  
  for (let i = 0; i < allPages.length; i++) {
    const pageInfo = allPages[i];
    process.stdout.write(`\r[${i + 1}/${allPages.length}] Testing ${pageInfo.type} pages...`);
    
    try {
      const result = await testPageConsistency(page, pageInfo);
      results.push(result);
      
      if (result.passes) {
        passCount++;
      } else {
        failCount++;
      }
    } catch (error) {
      results.push({
        ...pageInfo,
        error: error.message,
        passes: false
      });
      failCount++;
    }
  }
  
  await browser.close();
  
  // Analyze results
  console.log('\n\n' + '=' .repeat(80));
  console.log('VERIFICATION RESULTS');
  console.log('=' .repeat(80));
  
  const stats = {
    totalTested: allPages.length,
    passed: passCount,
    failed: failCount,
    successRate: ((passCount / allPages.length) * 100).toFixed(1)
  };
  
  console.log(`\n📊 OVERALL STATISTICS:`);
  console.log(`  Total pages tested: ${stats.totalTested}`);
  console.log(`  Passed: ${stats.passed} (${stats.successRate}%)`);
  console.log(`  Failed: ${stats.failed}`);
  
  // Check specific consistency metrics
  const fixedNavCount = results.filter(r => r.header && r.header.isFixed).length;
  const hasFooterCount = results.filter(r => r.footer && r.footer.exists).length;
  const hasContainerCount = results.filter(r => r.layout && r.layout.hasContainer).length;
  
  console.log(`\n✅ CONSISTENCY METRICS:`);
  console.log(`  Fixed navigation: ${fixedNavCount}/${allPages.length} (${(fixedNavCount/allPages.length*100).toFixed(1)}%)`);
  console.log(`  Has footer: ${hasFooterCount}/${allPages.length} (${(hasFooterCount/allPages.length*100).toFixed(1)}%)`);
  console.log(`  Has container: ${hasContainerCount}/${allPages.length} (${(hasContainerCount/allPages.length*100).toFixed(1)}%)`);
  
  // List failures
  const failures = results.filter(r => !r.passes);
  if (failures.length > 0) {
    console.log(`\n❌ FAILED PAGES (${failures.length}):`);
    failures.slice(0, 10).forEach(f => {
      const issues = [];
      if (f.header && !f.header.isFixed) issues.push('nav not fixed');
      if (f.footer && !f.footer.exists) issues.push('no footer');
      if (f.layout && !f.layout.hasContainer) issues.push('no container');
      if (f.error) issues.push(`error: ${f.error}`);
      
      console.log(`  - ${f.name}: ${issues.join(', ')}`);
    });
    
    if (failures.length > 10) {
      console.log(`  ... and ${failures.length - 10} more`);
    }
  }
  
  // Final verdict
  console.log('\n' + '=' .repeat(80));
  if (stats.successRate >= 95) {
    console.log('✅ EXCELLENT: UI/UX consistency is above 95%!');
  } else if (stats.successRate >= 90) {
    console.log('⚠️  GOOD: UI/UX consistency is above 90% but needs minor improvements');
  } else {
    console.log('❌ NEEDS WORK: UI/UX consistency is below 90%');
  }
  
  // Save detailed report
  const report = {
    timestamp: new Date().toISOString(),
    statistics: stats,
    metrics: {
      fixedNav: `${fixedNavCount}/${allPages.length}`,
      hasFooter: `${hasFooterCount}/${allPages.length}`,
      hasContainer: `${hasContainerCount}/${allPages.length}`
    },
    failures: failures.map(f => ({
      name: f.name,
      type: f.type,
      issues: {
        navFixed: f.header ? f.header.isFixed : false,
        hasFooter: f.footer ? f.footer.exists : false,
        hasContainer: f.layout ? f.layout.hasContainer : false
      }
    }))
  };
  
  fs.writeFileSync('final-consistency-report.json', JSON.stringify(report, null, 2));
  console.log('\n📄 Detailed report saved to final-consistency-report.json');
}

runFinalVerification().catch(console.error);