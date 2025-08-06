#!/usr/bin/env python3
"""
Verify the test batch migration results
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def verify_test_batch():
    """Verify the test batch migration"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    
    # Test one of the newly migrated pages
    test_page = 'locations/cities/aberdeen-sd-business-valuation-analyst.html'
    
    try:
        url = f"file://{os.path.abspath(test_page)}"
        print(f"🔍 Verifying: {test_page}")
        
        driver.get(url)
        time.sleep(2)
        
        # Check for Bootstrap
        bootstrap_check = driver.execute_script("""
            return {
                hasBootstrap: document.querySelector('link[href*="bootstrap@5.3.2"]') !== null,
                hasContrastFix: document.querySelector('link[href*="text-contrast-fix-v2.css"]') !== null,
                hasUILibrary: document.querySelector('link[href*="ui-library-bootstrap.css"]') !== null
            };
        """)
        
        print("\n📦 Libraries loaded:")
        print(f"  ✓ Bootstrap 5.3.2: {bootstrap_check['hasBootstrap']}")
        print(f"  ✓ Text Contrast Fix v2: {bootstrap_check['hasContrastFix']}")
        print(f"  ✓ UI Library CSS: {bootstrap_check['hasUILibrary']}")
        
        # Check hero section styles
        hero_check = driver.execute_script("""
            const hero = document.querySelector('.location-hero, .hero, .hero-section');
            if (hero) {
                const styles = window.getComputedStyle(hero);
                const h1 = hero.querySelector('h1');
                const p = hero.querySelector('p');
                
                return {
                    hasHero: true,
                    background: styles.background || styles.backgroundColor,
                    h1Color: h1 ? window.getComputedStyle(h1).color : 'not found',
                    pColor: p ? window.getComputedStyle(p).color : 'not found',
                    hasGradient: styles.backgroundImage.includes('gradient')
                };
            }
            return { hasHero: false };
        """)
        
        if hero_check['hasHero']:
            print("\n🎨 Hero section styles:")
            print(f"  ✓ Blue gradient applied: {hero_check['hasGradient']}")
            print(f"  ✓ H1 color: {hero_check['h1Color']}")
            print(f"  ✓ P color: {hero_check['pColor']}")
            
            if 'rgb(255, 255, 255)' in hero_check['h1Color']:
                print("\n✅ Text contrast verified - white text on blue gradient!")
            else:
                print("\n⚠️  Text may need contrast adjustment")
        
        # Take a screenshot
        os.makedirs('test-batch-screenshots', exist_ok=True)
        screenshot_path = f"test-batch-screenshots/{os.path.basename(test_page).replace('.html', '.png')}"
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot saved: {screenshot_path}")
        
    finally:
        driver.quit()
    
    print("\n✅ Test batch verification complete!")
    print("If everything looks good, you can proceed with the full migration.")

if __name__ == '__main__':
    verify_test_batch()