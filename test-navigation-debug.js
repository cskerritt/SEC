const { chromium } = require('playwright');

async function debugNavigation() {
  const browser = await chromium.launch({ 
    headless: false,
    slowMo: 100
  });
  
  const page = await browser.newPage();
  
  console.log('🔍 Deep debugging navigation issues...\n');
  
  await page.goto('http://localhost:4000/');
  await page.waitForLoadState('networkidle');
  
  // Check all styles applied to dropdown
  console.log('📋 Checking dropdown styles BEFORE hover:');
  const dropdownStylesBefore = await page.evaluate(() => {
    const dropdown = document.querySelector('.has-dropdown .dropdown');
    if (!dropdown) return null;
    
    const computed = window.getComputedStyle(dropdown);
    const rect = dropdown.getBoundingClientRect();
    
    // Get all CSS rules that apply to this element
    const matchingRules = [];
    for (let sheet of document.styleSheets) {
      try {
        for (let rule of sheet.cssRules) {
          if (rule.selectorText && dropdown.matches(rule.selectorText)) {
            matchingRules.push({
              selector: rule.selectorText,
              styles: rule.style.cssText,
              source: sheet.href || 'inline'
            });
          }
        }
      } catch (e) {
        // Some stylesheets might not be accessible
      }
    }
    
    return {
      computed: {
        display: computed.display,
        visibility: computed.visibility,
        opacity: computed.opacity,
        pointerEvents: computed.pointerEvents,
        zIndex: computed.zIndex,
        position: computed.position,
        top: computed.top,
        left: computed.left
      },
      rect: {
        top: rect.top,
        left: rect.left,
        width: rect.width,
        height: rect.height
      },
      matchingRules: matchingRules
    };
  });
  
  console.log('Computed styles:', dropdownStylesBefore?.computed);
  console.log('\nMatching CSS rules:');
  dropdownStylesBefore?.matchingRules?.forEach(rule => {
    console.log(`  From ${rule.source}:`);
    console.log(`    ${rule.selector} { ${rule.styles} }`);
  });
  
  // Hover and check again
  console.log('\n📋 Hovering over Services link...');
  await page.hover('.has-dropdown:has-text("Services") > a');
  await page.waitForTimeout(1000);
  
  console.log('\n📋 Checking dropdown styles AFTER hover:');
  const dropdownStylesAfter = await page.evaluate(() => {
    const dropdown = document.querySelector('.has-dropdown:hover .dropdown');
    if (!dropdown) {
      // Try alternative selectors
      const alt1 = document.querySelector('.has-dropdown .dropdown');
      const parent = document.querySelector('.has-dropdown');
      
      return {
        dropdownFound: !!alt1,
        parentHovered: parent ? parent.matches(':hover') : false,
        computed: alt1 ? window.getComputedStyle(alt1) : null
      };
    }
    
    const computed = window.getComputedStyle(dropdown);
    return {
      dropdownFound: true,
      computed: {
        display: computed.display,
        visibility: computed.visibility,
        opacity: computed.opacity,
        pointerEvents: computed.pointerEvents,
        zIndex: computed.zIndex
      }
    };
  });
  
  console.log('Result:', dropdownStylesAfter);
  
  // Check if JavaScript is interfering
  console.log('\n📋 Checking for JavaScript interference:');
  const jsInfo = await page.evaluate(() => {
    const dropdown = document.querySelector('.has-dropdown .dropdown');
    const parent = document.querySelector('.has-dropdown');
    
    // Check event listeners
    const events = [];
    if (parent) {
      // Modern browsers
      const listeners = getEventListeners ? getEventListeners(parent) : {};
      for (let event in listeners) {
        events.push(`${event}: ${listeners[event].length} listeners`);
      }
    }
    
    // Check if any JS is setting inline styles
    return {
      dropdownInlineStyle: dropdown?.getAttribute('style'),
      parentInlineStyle: parent?.getAttribute('style'),
      events: events,
      jQueryLoaded: typeof jQuery !== 'undefined',
      otherLibraries: {
        bootstrap: typeof bootstrap !== 'undefined',
        foundation: typeof Foundation !== 'undefined'
      }
    };
  });
  
  console.log('JavaScript info:', jsInfo);
  
  // Try to force the dropdown to show
  console.log('\n📋 Forcing dropdown to show with JavaScript:');
  await page.evaluate(() => {
    const dropdown = document.querySelector('.has-dropdown .dropdown');
    if (dropdown) {
      dropdown.style.cssText = `
        display: block !important;
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: auto !important;
        z-index: 999999 !important;
      `;
      console.log('Forced styles applied');
    }
  });
  
  // Now try to click
  const isClickable = await page.evaluate(() => {
    const link = document.querySelector('.has-dropdown .dropdown a');
    if (!link) return { found: false };
    
    const rect = link.getBoundingClientRect();
    const elementAtPoint = document.elementFromPoint(
      rect.left + rect.width/2, 
      rect.top + rect.height/2
    );
    
    return {
      found: true,
      clickable: elementAtPoint === link || link.contains(elementAtPoint),
      blocking: elementAtPoint ? {
        tag: elementAtPoint.tagName,
        class: elementAtPoint.className,
        id: elementAtPoint.id
      } : null
    };
  });
  
  console.log('\nClickability after forcing visible:', isClickable);
  
  if (isClickable.found && isClickable.clickable) {
    console.log('✅ Dropdown IS clickable when forced visible!');
    console.log('This means the issue is with the hover CSS not applying properly.');
  } else if (isClickable.blocking) {
    console.log('❌ Even when visible, dropdown is blocked by:', isClickable.blocking);
  }
  
  await browser.close();
}

debugNavigation().catch(console.error);