const { chromium } = require('playwright');

async function testNavigation() {
  const browser = await chromium.launch({ 
    headless: false,  // Set to false to see what's happening
    slowMo: 500      // Slow down actions to see them
  });
  
  const page = await browser.newPage();
  
  console.log('📍 Testing Navigation on Homepage...\n');
  
  // Go to the homepage
  await page.goto('http://localhost:4000/');
  await page.waitForLoadState('networkidle');
  
  // Test 1: Check if Contact button exists and is blue
  console.log('🔍 Test 1: Contact Button');
  const contactButton = await page.locator('.nav-cta');
  const contactExists = await contactButton.count() > 0;
  
  if (contactExists) {
    const bgColor = await contactButton.evaluate(el => 
      window.getComputedStyle(el).backgroundColor
    );
    console.log(`  ✓ Contact button found`);
    console.log(`  → Background color: ${bgColor}`);
    
    // Check if it's blue (rgb(30, 58, 138) = #1e3a8a)
    if (bgColor.includes('30') && bgColor.includes('58') && bgColor.includes('138')) {
      console.log('  ✅ Contact button is BLUE!\n');
    } else {
      console.log('  ❌ Contact button is NOT blue\n');
    }
  } else {
    console.log('  ❌ Contact button NOT found\n');
  }
  
  // Test 2: Check Services dropdown
  console.log('🔍 Test 2: Services Dropdown');
  const servicesLink = await page.locator('.has-dropdown:has-text("Services") > a').first();
  
  if (await servicesLink.count() > 0) {
    console.log('  ✓ Services link found');
    
    // Hover over Services to open dropdown
    await servicesLink.hover();
    await page.waitForTimeout(1000);
    
    // Check if dropdown is visible
    const dropdown = await page.locator('.has-dropdown:has-text("Services") .dropdown').first();
    const isVisible = await dropdown.isVisible();
    
    console.log(`  → Dropdown visible after hover: ${isVisible}`);
    
    if (isVisible) {
      // Try to get computed styles of dropdown
      const dropdownStyles = await dropdown.evaluate(el => {
        const styles = window.getComputedStyle(el);
        return {
          display: styles.display,
          visibility: styles.visibility,
          opacity: styles.opacity,
          pointerEvents: styles.pointerEvents,
          zIndex: styles.zIndex,
          position: styles.position
        };
      });
      
      console.log('  → Dropdown styles:');
      console.log(`    - display: ${dropdownStyles.display}`);
      console.log(`    - visibility: ${dropdownStyles.visibility}`);
      console.log(`    - opacity: ${dropdownStyles.opacity}`);
      console.log(`    - pointer-events: ${dropdownStyles.pointerEvents}`);
      console.log(`    - z-index: ${dropdownStyles.zIndex}`);
      console.log(`    - position: ${dropdownStyles.position}`);
      
      // Count service items
      const serviceItems = await page.locator('.has-dropdown:has-text("Services") .dropdown a');
      const itemCount = await serviceItems.count();
      console.log(`  → Service items found: ${itemCount}`);
      
      // List all services
      for (let i = 0; i < itemCount; i++) {
        const text = await serviceItems.nth(i).textContent();
        console.log(`    ${i + 1}. ${text.trim()}`);
      }
      
      // Test 3: Try to click a dropdown item
      console.log('\n🔍 Test 3: Clicking Dropdown Item');
      try {
        const forensicLink = await page.locator('.has-dropdown:has-text("Services") .dropdown a:has-text("Forensic Economics")').first();
        
        // Check if it's clickable
        const isClickable = await forensicLink.evaluate(el => {
          const rect = el.getBoundingClientRect();
          const elementAtPoint = document.elementFromPoint(rect.left + rect.width/2, rect.top + rect.height/2);
          return elementAtPoint === el || el.contains(elementAtPoint);
        });
        
        console.log(`  → Is "Forensic Economics" link clickable: ${isClickable}`);
        
        if (!isClickable) {
          // Find what element is blocking it
          const blockingElement = await forensicLink.evaluate(el => {
            const rect = el.getBoundingClientRect();
            const elementAtPoint = document.elementFromPoint(rect.left + rect.width/2, rect.top + rect.height/2);
            if (elementAtPoint && elementAtPoint !== el) {
              return {
                tagName: elementAtPoint.tagName,
                className: elementAtPoint.className,
                id: elementAtPoint.id,
                zIndex: window.getComputedStyle(elementAtPoint).zIndex
              };
            }
            return null;
          });
          
          if (blockingElement) {
            console.log('  ❌ Element is being blocked by:');
            console.log(`    - Tag: ${blockingElement.tagName}`);
            console.log(`    - Class: ${blockingElement.className}`);
            console.log(`    - ID: ${blockingElement.id}`);
            console.log(`    - z-index: ${blockingElement.zIndex}`);
          }
        }
        
        // Try to click it anyway
        await forensicLink.click({ force: true });
        await page.waitForTimeout(2000);
        
        // Check if navigation happened
        const currentUrl = page.url();
        if (currentUrl.includes('forensic-economics')) {
          console.log('  ✅ Successfully navigated to Forensic Economics page!');
        } else {
          console.log(`  ❌ Click didn't navigate. Still on: ${currentUrl}`);
        }
        
      } catch (error) {
        console.log(`  ❌ Error clicking dropdown: ${error.message}`);
      }
      
    } else {
      console.log('  ❌ Dropdown is NOT visible after hover\n');
    }
  } else {
    console.log('  ❌ Services link NOT found\n');
  }
  
  // Test 4: Check what CSS files are loaded
  console.log('\n🔍 Test 4: Loaded CSS Files');
  const cssFiles = await page.evaluate(() => {
    const links = Array.from(document.querySelectorAll('link[rel="stylesheet"]'));
    return links.map(link => link.href.replace(window.location.origin, ''));
  });
  
  console.log('  CSS files loaded:');
  cssFiles.forEach(file => {
    console.log(`    - ${file}`);
    if (file.includes('navigation-fix-override')) {
      console.log('      ✅ Override CSS is loaded!');
    }
  });
  
  await browser.close();
}

// Run the test
testNavigation().catch(console.error);