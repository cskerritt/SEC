const { chromium } = require('playwright');

async function testNavigation() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  const page = await context.newPage();
  
  const pages = [
    'http://localhost:4000/',
    'http://localhost:4000/services/',
    'http://localhost:4000/practice-areas/',
    'http://localhost:4000/about/',
    'http://localhost:4000/case-studies/',
    'http://localhost:4000/blog/'
  ];
  
  console.log('Testing navigation on all pages...\n');
  
  for (const url of pages) {
    console.log(`\nTesting: ${url}`);
    console.log('='.repeat(50));
    
    await page.goto(url, { waitUntil: 'networkidle' });
    
    // Test Services dropdown
    const servicesDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Services") .dropdown');
    const practiceDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Practice Areas") .dropdown');
    
    // Hover over Services
    await page.hover('.nav-menu .has-dropdown:has-text("Services")');
    await page.waitForTimeout(500);
    
    // Check if dropdown is visible
    const servicesVisible = await servicesDropdown.isVisible();
    console.log(`  Services dropdown visible: ${servicesVisible}`);
    
    if (servicesVisible) {
      // Try to click on a service link
      try {
        const forensicLink = await page.locator('.dropdown a:has-text("Forensic Economics")').first();
        const isClickable = await forensicLink.isVisible();
        console.log(`  Forensic Economics link clickable: ${isClickable}`);
      } catch (e) {
        console.log('  ERROR: Could not find Forensic Economics link');
      }
    }
    
    // Test Practice Areas dropdown
    await page.hover('.nav-menu .has-dropdown:has-text("Practice Areas")');
    await page.waitForTimeout(500);
    
    const practiceVisible = await practiceDropdown.isVisible();
    console.log(`  Practice Areas dropdown visible: ${practiceVisible}`);
    
    // Check Contact button
    const contactBtn = await page.locator('.nav-cta').first();
    if (await contactBtn.count() > 0) {
      const bgColor = await contactBtn.evaluate(el => 
        window.getComputedStyle(el).backgroundColor
      );
      console.log(`  Contact button color: ${bgColor}`);
    } else {
      console.log('  Contact button: NOT FOUND');
    }
  }
  
  // Test mobile navigation
  console.log('\n\nTesting Mobile Navigation');
  console.log('='.repeat(50));
  
  // Set mobile viewport
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:4000/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  
  // Check if mobile menu toggle is visible
  const mobileToggle = await page.locator('.mobile-menu-toggle');
  const toggleVisible = await mobileToggle.isVisible();
  console.log(`Mobile menu toggle visible: ${toggleVisible}`);
  
  if (toggleVisible) {
    // Click toggle to open menu
    await mobileToggle.click();
    await page.waitForTimeout(500);
    
    // Check if menu is open
    const mobileMenu = await page.locator('.nav-menu');
    const menuVisible = await mobileMenu.isVisible();
    console.log(`Mobile menu opens: ${menuVisible}`);
    
    // Check if Services dropdown works on mobile
    const mobileServices = await page.locator('.nav-menu .has-dropdown:has-text("Services")');
    if (await mobileServices.count() > 0) {
      await mobileServices.click();
      await page.waitForTimeout(500);
      
      const mobileDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Services") .dropdown');
      const dropdownVisible = await mobileDropdown.isVisible();
      console.log(`Mobile Services dropdown works: ${dropdownVisible}`);
    }
  }
  
  await browser.close();
}

testNavigation().catch(console.error);
