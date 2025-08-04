const { chromium } = require('playwright');

async function testNavigation() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ viewport: { width: 1920, height: 1080 } });
  const page = await context.newPage();
  
  console.log('============================================================');
  console.log('DESKTOP NAVIGATION TEST');
  console.log('============================================================');
  
  // Test homepage
  await page.goto('http://localhost:4000/', { waitUntil: 'networkidle' });
  
  // Test Services dropdown
  await page.hover('.nav-menu .has-dropdown:has-text("Services")');
  await page.waitForTimeout(500);
  
  const servicesDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Services") .dropdown');
  const servicesVisible = await servicesDropdown.isVisible();
  console.log('Services dropdown visible: ' + servicesVisible);
  
  // Check all 5 services
  const services = ['Forensic Economics', 'Business Valuation', 'Life Care Planning', 'Vocational Expert', 'Business Consulting'];
  for (const service of services) {
    const link = await page.locator('.dropdown a:has-text("' + service + '")').first();
    const serviceExists = await link.count() > 0;
    console.log('  - ' + service + ': ' + (serviceExists ? 'YES' : 'NO'));
  }
  
  // Test Practice Areas dropdown
  await page.hover('.nav-menu .has-dropdown:has-text("Practice Areas")');
  await page.waitForTimeout(500);
  
  const practiceDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Practice Areas") .dropdown');
  const practiceVisible = await practiceDropdown.isVisible();
  console.log('Practice Areas dropdown visible: ' + practiceVisible);
  
  // Check new practice areas
  const practiceAreas = ['Product Liability', 'Family Law & Divorce'];
  for (const area of practiceAreas) {
    const link = await page.locator('.dropdown a:has-text("' + area + '")').first();
    const areaExists = await link.count() > 0;
    console.log('  - ' + area + ': ' + (areaExists ? 'YES' : 'NO'));
  }
  
  // Check Contact button color
  const contactBtn = await page.locator('.nav-cta').first();
  const bgColor = await contactBtn.evaluate(el => window.getComputedStyle(el).backgroundColor);
  const isBlue = bgColor === 'rgb(30, 58, 138)';
  console.log('Contact button is blue: ' + isBlue + ' (' + bgColor + ')');
  
  // Test other pages
  console.log('\nTesting consistency across pages:');
  const pages = ['/services/', '/practice-areas/', '/about/', '/case-studies/', '/blog/'];
  
  for (const path of pages) {
    await page.goto('http://localhost:4000' + path, { waitUntil: 'networkidle' });
    await page.hover('.nav-menu .has-dropdown:has-text("Services")');
    await page.waitForTimeout(300);
    const dropdown = await page.locator('.nav-menu .has-dropdown:has-text("Services") .dropdown');
    const visible = await dropdown.isVisible();
    console.log('  ' + path + ': Dropdown works: ' + (visible ? 'YES' : 'NO'));
  }
  
  console.log('\n============================================================');
  console.log('MOBILE NAVIGATION TEST');
  console.log('============================================================');
  
  // Set mobile viewport
  await page.setViewportSize({ width: 375, height: 667 });
  await page.goto('http://localhost:4000/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);
  
  // Check mobile toggle
  const mobileToggle = await page.locator('.mobile-menu-toggle');
  const toggleVisible = await mobileToggle.isVisible();
  console.log('Mobile menu toggle visible: ' + toggleVisible);
  
  if (toggleVisible) {
    // Open menu
    await mobileToggle.click();
    await page.waitForTimeout(500);
    
    const mobileMenu = await page.locator('.nav-menu');
    const menuOpen = await mobileMenu.isVisible();
    console.log('Mobile menu opens: ' + menuOpen);
    
    // Test mobile dropdown
    const mobileServices = await page.locator('.nav-menu .has-dropdown:has-text("Services")');
    if (await mobileServices.count() > 0) {
      await mobileServices.click();
      await page.waitForTimeout(500);
      
      const mobileDropdown = await page.locator('.nav-menu .has-dropdown:has-text("Services") .dropdown');
      const dropdownOpen = await mobileDropdown.isVisible();
      console.log('Mobile Services dropdown opens: ' + dropdownOpen);
      
      // Check if links are clickable
      if (dropdownOpen) {
        const forensicLink = await page.locator('.dropdown a:has-text("Forensic Economics")').first();
        const clickable = await forensicLink.isVisible();
        console.log('Mobile dropdown links clickable: ' + clickable);
      }
    }
    
    // Check mobile Contact button
    const mobileContact = await page.locator('.nav-menu .nav-cta');
    if (await mobileContact.count() > 0) {
      const mobileBg = await mobileContact.evaluate(el => window.getComputedStyle(el).backgroundColor);
      const mobileBlue = mobileBg === 'rgb(30, 58, 138)';
      console.log('Mobile Contact button is blue: ' + mobileBlue);
    }
  }
  
  console.log('\n============================================================');
  console.log('TEST COMPLETE');
  console.log('============================================================');
  
  await browser.close();
}

testNavigation().catch(console.error);
