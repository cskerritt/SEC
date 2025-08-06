#!/usr/bin/env python3
"""
Capture screenshots after contrast fix
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def capture_fixed_pages():
    """Capture screenshots of fixed pages"""
    # Set up Chrome options
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--force-device-scale-factor=1')
    
    # Create directory
    os.makedirs('fixed-screenshots', exist_ok=True)
    
    # Initialize driver
    driver = webdriver.Chrome(options=options)
    
    try:
        # List of fixed pages to capture
        pages = [
            ('coventry-business-valuation', 'locations/cities/coventry-ri-business-valuation-analyst.html'),
            ('central-falls-vocational', 'locations/cities/central-falls-ri-ri-vocational-expert.html'),
            ('bristol-forensic-economist', 'locations/cities/bristol-ri-forensic-economist.html')
        ]
        
        for name, path in pages:
            try:
                url = f"file://{os.path.abspath(path)}"
                print(f"📸 Capturing {name} (fixed version)...")
                
                driver.get(url)
                time.sleep(3)  # Wait for everything to load
                
                # Capture screenshot
                screenshot_path = f"fixed-screenshots/{name}-fixed.png"
                driver.save_screenshot(screenshot_path)
                print(f"   ✓ Saved: {screenshot_path}")
                
                # Check text visibility
                check_visibility(driver, name)
                
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
        
    finally:
        driver.quit()
    
    print("\n✅ Fixed screenshots captured!")
    print("📁 Check the 'fixed-screenshots' directory")

def check_visibility(driver, page_name):
    """Check text visibility improvements"""
    try:
        # Check hero text
        hero_text = driver.execute_script("""
            const hero = document.querySelector('.hero-section, .hero, .location-hero');
            if (hero) {
                const style = window.getComputedStyle(hero);
                const h1 = hero.querySelector('h1');
                if (h1) {
                    const h1Style = window.getComputedStyle(h1);
                    return {
                        background: style.background,
                        heroColor: style.color,
                        h1Color: h1Style.color
                    };
                }
            }
            return null;
        """)
        
        if hero_text:
            print(f"   ✓ Hero section styles applied")
            print(f"     - H1 color: {hero_text['h1Color']}")
        
    except Exception as e:
        print(f"   ⚠️  Could not check visibility: {str(e)}")

if __name__ == '__main__':
    capture_fixed_pages()