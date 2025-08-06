#!/usr/bin/env python3
"""
Selenium script to capture screenshots of migrated pages for manual review
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
from datetime import datetime

class ScreenshotCapture:
    def __init__(self):
        # Set up Chrome options
        self.options = Options()
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--force-device-scale-factor=1')
        self.options.add_argument('--high-dpi-support=1')
        
        # Create screenshots directory
        self.screenshot_dir = 'migration-screenshots'
        os.makedirs(self.screenshot_dir, exist_ok=True)
        
        # List of pages to capture
        self.pages_to_capture = [
            {
                'name': 'migration-showcase',
                'path': 'migration-showcase.html',
                'wait_for': '.comparison-card'
            },
            {
                'name': 'migration-report',
                'path': 'migration-report.html',
                'wait_for': '.stat-card'
            },
            {
                'name': 'services-overview',
                'path': 'services/index.html',
                'wait_for': '.service-card'
            },
            {
                'name': 'forensic-economics-service',
                'path': 'services/forensic-economics/index.html',
                'wait_for': '.hero-section'
            },
            {
                'name': 'business-valuation-service',
                'path': 'services/business-valuation/index.html',
                'wait_for': '.hero-section'
            },
            {
                'name': 'practice-areas-overview',
                'path': 'practice-areas/index.html',
                'wait_for': '.practice-area-card'
            },
            {
                'name': 'personal-injury-practice',
                'path': 'practice-areas/personal-injury/index.html',
                'wait_for': '.hero-section'
            },
            {
                'name': 'coventry-business-valuation-city',
                'path': 'locations/cities/coventry-ri-business-valuation-analyst.html',
                'wait_for': '.location-hero'
            },
            {
                'name': 'central-falls-vocational-city',
                'path': 'locations/cities/central-falls-ri-ri-vocational-expert.html',
                'wait_for': '.hero-section'
            },
            {
                'name': 'bristol-forensic-economist-city',
                'path': 'locations/cities/bristol-ri-forensic-economist.html',
                'wait_for': '.location-hero'
            }
        ]
    
    def capture_screenshots(self):
        """Capture screenshots of all pages"""
        # Initialize driver
        driver = webdriver.Chrome(options=self.options)
        
        try:
            print(f"Starting screenshot capture at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Screenshots will be saved to: {os.path.abspath(self.screenshot_dir)}\n")
            
            for page in self.pages_to_capture:
                self.capture_page(driver, page)
            
            # Also capture full page scrolling screenshots for key pages
            self.capture_full_page_screenshots(driver)
            
            print(f"\n✅ Screenshot capture complete!")
            print(f"📁 Screenshots saved in: {os.path.abspath(self.screenshot_dir)}")
            
        finally:
            driver.quit()
    
    def capture_page(self, driver, page_info):
        """Capture screenshot of a single page"""
        try:
            # Construct full path
            full_path = f"file://{os.path.abspath(page_info['path'])}"
            
            print(f"📸 Capturing: {page_info['name']}")
            print(f"   URL: {full_path}")
            
            # Navigate to page
            driver.get(full_path)
            
            # Wait for key element to load
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, page_info['wait_for'])))
            
            # Additional wait for animations to complete
            time.sleep(2)
            
            # Take viewport screenshot
            screenshot_path = os.path.join(self.screenshot_dir, f"{page_info['name']}-viewport.png")
            driver.save_screenshot(screenshot_path)
            print(f"   ✓ Saved viewport screenshot: {screenshot_path}")
            
            # Check for text readability issues
            self.check_text_readability(driver, page_info['name'])
            
        except Exception as e:
            print(f"   ❌ Error capturing {page_info['name']}: {str(e)}")
    
    def capture_full_page_screenshots(self, driver):
        """Capture full-page scrolling screenshots of key pages"""
        print("\n📸 Capturing full-page screenshots...")
        
        key_pages = [
            ('services/forensic-economics/index.html', 'forensic-economics-full'),
            ('locations/cities/coventry-ri-business-valuation-analyst.html', 'coventry-business-full')
        ]
        
        for path, name in key_pages:
            try:
                full_path = f"file://{os.path.abspath(path)}"
                driver.get(full_path)
                time.sleep(2)
                
                # Get full page dimensions
                total_height = driver.execute_script("return document.body.scrollHeight")
                viewport_height = driver.execute_script("return window.innerHeight")
                
                # Capture sections
                sections = []
                for i in range(0, total_height, viewport_height):
                    driver.execute_script(f"window.scrollTo(0, {i})")
                    time.sleep(0.5)
                    
                    section_path = os.path.join(self.screenshot_dir, f"{name}-section-{i//viewport_height}.png")
                    driver.save_screenshot(section_path)
                    sections.append(section_path)
                
                print(f"   ✓ Captured {len(sections)} sections for {name}")
                
            except Exception as e:
                print(f"   ❌ Error capturing full page {name}: {str(e)}")
    
    def check_text_readability(self, driver, page_name):
        """Check for text readability issues"""
        try:
            # Check for common text readability issues
            issues = []
            
            # Check text contrast
            low_contrast = driver.execute_script("""
                const elements = document.querySelectorAll('*');
                const lowContrast = [];
                
                elements.forEach(el => {
                    const style = window.getComputedStyle(el);
                    const color = style.color;
                    const bgColor = style.backgroundColor;
                    
                    // Simple check for white text on light background
                    if (color === 'rgb(255, 255, 255)' && 
                        (bgColor === 'rgba(0, 0, 0, 0)' || 
                         bgColor === 'rgb(255, 255, 255)' ||
                         bgColor.includes('248, 250, 252'))) {
                        lowContrast.push({
                            tag: el.tagName,
                            text: el.innerText?.substring(0, 50)
                        });
                    }
                });
                
                return lowContrast.slice(0, 5);
            """)
            
            if low_contrast:
                issues.append(f"Low contrast text found: {len(low_contrast)} elements")
            
            # Check for missing text
            empty_headings = driver.execute_script("""
                const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
                const empty = Array.from(headings).filter(h => !h.innerText.trim());
                return empty.length;
            """)
            
            if empty_headings > 0:
                issues.append(f"Empty headings found: {empty_headings}")
            
            # Check font sizes
            tiny_text = driver.execute_script("""
                const elements = document.querySelectorAll('p, span, div');
                const tiny = Array.from(elements).filter(el => {
                    const fontSize = window.getComputedStyle(el).fontSize;
                    return parseFloat(fontSize) < 12;
                });
                return tiny.length;
            """)
            
            if tiny_text > 0:
                issues.append(f"Very small text found: {tiny_text} elements")
            
            if issues:
                print(f"   ⚠️  Readability issues in {page_name}:")
                for issue in issues:
                    print(f"      - {issue}")
            else:
                print(f"   ✓ No major readability issues detected")
                
        except Exception as e:
            print(f"   ⚠️  Could not check readability: {str(e)}")
    
    def generate_review_html(self):
        """Generate HTML page for easy review of screenshots"""
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Migration Screenshots Review</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .screenshot-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .screenshot-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .screenshot-card h3 {
            margin: 0;
            padding: 15px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }
        .screenshot-card img {
            width: 100%;
            height: auto;
            display: block;
            cursor: pointer;
        }
        .screenshot-card img:hover {
            opacity: 0.9;
        }
        .issues {
            padding: 15px;
            background: #fff3cd;
            color: #856404;
            font-size: 14px;
        }
        .fullscreen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            display: none;
            z-index: 1000;
        }
        .fullscreen img {
            max-width: 90%;
            max-height: 90%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .fullscreen.active {
            display: block;
        }
        .close-btn {
            position: absolute;
            top: 20px;
            right: 40px;
            color: white;
            font-size: 40px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>UI Migration Screenshots Review</h1>
    <p style="text-align: center;">Click any screenshot to view full size</p>
    
    <div class="screenshot-grid">
"""
        
        # Add screenshot cards
        for filename in sorted(os.listdir(self.screenshot_dir)):
            if filename.endswith('.png'):
                name = filename.replace('-viewport.png', '').replace('-', ' ').title()
                html_content += f"""
        <div class="screenshot-card">
            <h3>{name}</h3>
            <img src="{self.screenshot_dir}/{filename}" onclick="showFullscreen(this)" alt="{name}">
        </div>
"""
        
        html_content += """
    </div>
    
    <div class="fullscreen" id="fullscreen" onclick="hideFullscreen()">
        <span class="close-btn">&times;</span>
        <img id="fullscreen-img" src="" alt="">
    </div>
    
    <script>
        function showFullscreen(img) {
            document.getElementById('fullscreen-img').src = img.src;
            document.getElementById('fullscreen').classList.add('active');
        }
        
        function hideFullscreen() {
            document.getElementById('fullscreen').classList.remove('active');
        }
    </script>
</body>
</html>
"""
        
        review_path = 'screenshot-review.html'
        with open(review_path, 'w') as f:
            f.write(html_content)
        
        print(f"\n📄 Review page created: {os.path.abspath(review_path)}")

def main():
    capture = ScreenshotCapture()
    capture.capture_screenshots()
    capture.generate_review_html()

if __name__ == '__main__':
    main()