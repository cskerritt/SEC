#!/usr/bin/env python3
"""
Verify the contrast fix is working properly
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def verify_contrast_fix():
    """Take screenshots to verify contrast fix"""
    # Set up Chrome options
    options = Options()
    options.add_argument('--window-size=1920,1080')
    
    # Create directory
    os.makedirs('contrast-verification', exist_ok=True)
    
    # Initialize driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Test page
        url = f"file://{os.path.abspath('locations/cities/coventry-ri-business-valuation-analyst.html')}"
        print(f"🔍 Verifying contrast fix on: coventry-ri-business-valuation-analyst.html")
        
        driver.get(url)
        time.sleep(3)
        
        # Take full page screenshot
        driver.save_screenshot('contrast-verification/full-page-with-fix.png')
        print("   ✓ Full page screenshot saved")
        
        # Scroll to hero section and take focused screenshot
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        driver.save_screenshot('contrast-verification/hero-section-with-fix.png')
        print("   ✓ Hero section screenshot saved")
        
        # Check computed styles
        hero_styles = driver.execute_script("""
            const hero = document.querySelector('.location-hero');
            if (hero) {
                const styles = window.getComputedStyle(hero);
                const h1 = hero.querySelector('h1');
                const p = hero.querySelector('p');
                
                return {
                    background: styles.background,
                    backgroundColor: styles.backgroundColor,
                    color: styles.color,
                    h1Color: h1 ? window.getComputedStyle(h1).color : 'not found',
                    pColor: p ? window.getComputedStyle(p).color : 'not found'
                };
            }
            return null;
        """)
        
        if hero_styles:
            print("\n📊 Computed Styles:")
            print(f"   Background: {hero_styles['background'][:100]}...")
            print(f"   Background Color: {hero_styles['backgroundColor']}")
            print(f"   Text Color: {hero_styles['color']}")
            print(f"   H1 Color: {hero_styles['h1Color']}")
            print(f"   P Color: {hero_styles['pColor']}")
            
            # Check if fix is working
            if 'rgb(255, 255, 255)' in hero_styles['h1Color']:
                print("\n✅ SUCCESS: Text is white!")
            else:
                print("\n❌ ISSUE: Text is not white")
                
            if 'gradient' in hero_styles['background'] or 'rgb(' in hero_styles['backgroundColor']:
                print("✅ SUCCESS: Background has gradient/color!")
            else:
                print("❌ ISSUE: Background is missing")
        
        # Scroll through page sections
        sections = [
            ('Services Section', 400),
            ('Industry Expertise', 800),
            ('Contact CTA', 1200)
        ]
        
        for section_name, scroll_pos in sections:
            driver.execute_script(f"window.scrollTo(0, {scroll_pos})")
            time.sleep(1)
            filename = f"contrast-verification/{section_name.lower().replace(' ', '-')}.png"
            driver.save_screenshot(filename)
            print(f"   ✓ {section_name} screenshot saved")
        
    finally:
        driver.quit()
    
    print("\n✅ Verification complete! Check the 'contrast-verification' directory")
    print("📁 Screenshots saved to: contrast-verification/")

if __name__ == '__main__':
    verify_contrast_fix()