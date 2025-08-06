#!/usr/bin/env python3
"""
Final verification of contrast fix with proper blue background
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def final_verification():
    """Final screenshot verification"""
    options = Options()
    options.add_argument('--window-size=1920,1080')
    
    os.makedirs('final-screenshots', exist_ok=True)
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Test Coventry page
        url = f"file://{os.path.abspath('locations/cities/coventry-ri-business-valuation-analyst.html')}"
        print("🔍 Final verification of contrast fix...")
        
        driver.get(url)
        time.sleep(3)
        
        # Take hero screenshot
        driver.save_screenshot('final-screenshots/hero-with-blue-gradient.png')
        print("   ✓ Hero section screenshot saved")
        
        # Check final styles
        hero_check = driver.execute_script("""
            const hero = document.querySelector('.location-hero');
            if (hero) {
                const styles = window.getComputedStyle(hero);
                const h1 = hero.querySelector('h1');
                const p = hero.querySelector('p');
                
                // Check for gradient
                const hasGradient = styles.backgroundImage.includes('gradient') || 
                                   styles.background.includes('gradient');
                
                return {
                    hasGradient: hasGradient,
                    backgroundImage: styles.backgroundImage,
                    backgroundColor: styles.backgroundColor,
                    h1Color: h1 ? window.getComputedStyle(h1).color : 'not found',
                    pColor: p ? window.getComputedStyle(p).color : 'not found'
                };
            }
            return null;
        """)
        
        if hero_check:
            print("\n✅ FINAL VERIFICATION:")
            print(f"   Blue Gradient Applied: {hero_check['hasGradient']}")
            print(f"   H1 Text Color: {hero_check['h1Color']}")
            print(f"   P Text Color: {hero_check['pColor']}")
            
            if hero_check['hasGradient'] and 'rgb(255, 255, 255)' in hero_check['h1Color']:
                print("\n🎉 SUCCESS: Blue gradient background with white text!")
            else:
                print("\n⚠️  Still needs adjustment")
                print(f"   Background Image: {hero_check['backgroundImage']}")
                print(f"   Background Color: {hero_check['backgroundColor']}")
        
        # Take additional screenshots
        sections = [
            ('Full Page', 0),
            ('Services', 600),
            ('Footer', 'document.body.scrollHeight - window.innerHeight')
        ]
        
        for name, scroll in sections:
            if isinstance(scroll, str):
                driver.execute_script(f"window.scrollTo(0, {scroll})")
            else:
                driver.execute_script(f"window.scrollTo(0, {scroll})")
            time.sleep(1)
            driver.save_screenshot(f'final-screenshots/{name.lower().replace(" ", "-")}.png')
            print(f"   ✓ {name} screenshot saved")
        
    finally:
        driver.quit()
    
    print("\n📁 Final screenshots saved to: final-screenshots/")
    print("✅ Verification complete!")

if __name__ == '__main__':
    final_verification()