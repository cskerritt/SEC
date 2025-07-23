#!/usr/bin/env python3
"""
Performance testing script for city pages
Tests loading speed, responsiveness, and functionality
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json

# Test configuration
BASE_URL = "http://localhost:8000"
CITIES = [
    {
        "name": "New York, NY",
        "pages": [
            "new-york-ny-ny-vocational-expert.html",
            "new-york-ny-ny-life-care-planner.html"
        ]
    },
    {
        "name": "Los Angeles, CA", 
        "pages": [
            "los-angeles-ca-ca-vocational-expert.html",
            "los-angeles-ca-ca-life-care-planner.html"
        ]
    },
    {
        "name": "Chicago, IL",
        "pages": [
            "chicago-il-il-vocational-expert.html",
            "chicago-il-il-life-care-planner.html"
        ]
    },
    {
        "name": "Houston, TX",
        "pages": [
            "houston-tx-tx-vocational-expert.html",
            "houston-tx-tx-life-care-planner.html"
        ]
    },
    {
        "name": "Boston, MA",
        "pages": [
            "boston-ma-ma-vocational-expert.html",
            "boston-ma-ma-life-care-planner.html"
        ]
    }
]

def setup_driver(mobile=False):
    """Setup Chrome driver with options"""
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    if mobile:
        # Mobile emulation
        mobile_emulation = {"deviceName": "iPhone 12 Pro"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    return webdriver.Chrome(options=chrome_options)

def measure_page_load_time(driver, url):
    """Measure page load time using Navigation Timing API"""
    start_time = time.time()
    driver.get(url)
    
    # Wait for page to load
    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    
    # Get performance timing
    navigation_start = driver.execute_script("return window.performance.timing.navigationStart")
    load_complete = driver.execute_script("return window.performance.timing.loadEventEnd")
    
    if load_complete > 0:
        load_time = (load_complete - navigation_start) / 1000.0
    else:
        load_time = time.time() - start_time
    
    return load_time

def test_page_elements(driver, page_name):
    """Test various page elements"""
    issues = []
    
    try:
        # Check for title
        title = driver.title
        if not title:
            issues.append("Missing page title")
        
        # Check for meta description
        try:
            meta_desc = driver.find_element(By.CSS_SELECTOR, 'meta[name="description"]')
            if not meta_desc.get_attribute("content"):
                issues.append("Empty meta description")
        except NoSuchElementException:
            issues.append("Missing meta description")
        
        # Check for hero section
        try:
            hero = driver.find_element(By.CSS_SELECTOR, '.hero, .jumbotron, header')
        except NoSuchElementException:
            issues.append("No hero/header section found")
        
        # Check for navigation
        try:
            nav = driver.find_element(By.CSS_SELECTOR, 'nav, .navigation, .navbar')
        except NoSuchElementException:
            issues.append("No navigation found")
        
        # Check for contact information
        contact_found = False
        for selector in ['.contact', 'a[href*="tel:"]', 'a[href*="mailto:"]']:
            try:
                driver.find_element(By.CSS_SELECTOR, selector)
                contact_found = True
                break
            except NoSuchElementException:
                pass
        
        if not contact_found:
            issues.append("No contact information found")
        
        # Check for images/icons
        images = driver.find_elements(By.TAG_NAME, 'img')
        broken_images = 0
        for img in images:
            if img.get_attribute('naturalWidth') == '0':
                broken_images += 1
        
        if broken_images > 0:
            issues.append(f"{broken_images} broken images found")
        
        # Check for Font Awesome icons
        icons = driver.find_elements(By.CSS_SELECTOR, 'i[class*="fa-"], svg[class*="fa-"]')
        if len(icons) == 0:
            issues.append("No Font Awesome icons found")
        
        # Check internal links
        internal_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/"], a[href^="./"], a[href^="../"]')
        broken_links = []
        
        for link in internal_links[:5]:  # Test first 5 internal links
            href = link.get_attribute('href')
            if href and not href.startswith('#'):
                try:
                    response = requests.head(href, timeout=2)
                    if response.status_code >= 400:
                        broken_links.append(href)
                except:
                    pass
        
        if broken_links:
            issues.append(f"{len(broken_links)} broken internal links")
            
    except Exception as e:
        issues.append(f"Error during element testing: {str(e)}")
    
    return issues

def test_mobile_responsiveness(driver, url):
    """Test mobile responsiveness"""
    issues = []
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Check viewport meta tag
        try:
            viewport = driver.find_element(By.CSS_SELECTOR, 'meta[name="viewport"]')
            if not viewport.get_attribute("content"):
                issues.append("Missing viewport meta tag content")
        except NoSuchElementException:
            issues.append("Missing viewport meta tag")
        
        # Check for horizontal scroll
        body_width = driver.execute_script("return document.body.scrollWidth")
        window_width = driver.execute_script("return window.innerWidth")
        
        if body_width > window_width:
            issues.append(f"Horizontal scroll detected (body: {body_width}px, window: {window_width}px)")
        
        # Check for responsive elements
        elements = driver.find_elements(By.CSS_SELECTOR, '*')
        overflow_elements = 0
        
        for element in elements[:50]:  # Check first 50 elements
            try:
                rect = element.rect
                if rect['x'] + rect['width'] > window_width:
                    overflow_elements += 1
            except:
                pass
        
        if overflow_elements > 0:
            issues.append(f"{overflow_elements} elements overflow viewport")
            
    except Exception as e:
        issues.append(f"Error during mobile testing: {str(e)}")
    
    return issues

def generate_report(results):
    """Generate performance report"""
    report = []
    report.append("# City Pages Performance Test Report")
    report.append(f"Test Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("\n## Summary")
    
    total_pages = sum(len(city["results"]) for city in results)
    total_issues = sum(len(page["desktop_issues"]) + len(page["mobile_issues"]) for city in results for page in city["results"])
    avg_load_time = sum(page["desktop_load_time"] for city in results for page in city["results"]) / total_pages
    
    report.append(f"- Total pages tested: {total_pages}")
    report.append(f"- Total issues found: {total_issues}")
    report.append(f"- Average load time: {avg_load_time:.2f} seconds")
    
    report.append("\n## Detailed Results")
    
    for city in results:
        report.append(f"\n### {city['name']}")
        
        for page in city["results"]:
            report.append(f"\n#### {page['page']}")
            report.append(f"- **Desktop Load Time**: {page['desktop_load_time']:.2f} seconds")
            report.append(f"- **Mobile Load Time**: {page['mobile_load_time']:.2f} seconds")
            
            if page["desktop_issues"]:
                report.append("- **Desktop Issues**:")
                for issue in page["desktop_issues"]:
                    report.append(f"  - {issue}")
            else:
                report.append("- **Desktop Issues**: None")
            
            if page["mobile_issues"]:
                report.append("- **Mobile Issues**:")
                for issue in page["mobile_issues"]:
                    report.append(f"  - {issue}")
            else:
                report.append("- **Mobile Issues**: None")
    
    report.append("\n## Performance Benchmarks")
    report.append("- **Excellent**: < 1 second")
    report.append("- **Good**: 1-3 seconds")
    report.append("- **Needs Improvement**: 3-5 seconds")
    report.append("- **Poor**: > 5 seconds")
    
    return "\n".join(report)

def main():
    """Main test execution"""
    print("Starting performance tests...")
    results = []
    
    for city in CITIES:
        city_results = {
            "name": city["name"],
            "results": []
        }
        
        for page in city["pages"]:
            print(f"\nTesting {city['name']} - {page}")
            url = f"{BASE_URL}/{page}"
            
            # Desktop testing
            desktop_driver = setup_driver(mobile=False)
            try:
                desktop_load_time = measure_page_load_time(desktop_driver, url)
                desktop_issues = test_page_elements(desktop_driver, page)
                print(f"  Desktop load time: {desktop_load_time:.2f}s")
            except Exception as e:
                desktop_load_time = -1
                desktop_issues = [f"Failed to load page: {str(e)}"]
                print(f"  Desktop test failed: {str(e)}")
            finally:
                desktop_driver.quit()
            
            # Mobile testing
            mobile_driver = setup_driver(mobile=True)
            try:
                mobile_load_time = measure_page_load_time(mobile_driver, url)
                mobile_issues = test_mobile_responsiveness(mobile_driver, url)
                print(f"  Mobile load time: {mobile_load_time:.2f}s")
            except Exception as e:
                mobile_load_time = -1
                mobile_issues = [f"Failed to load page: {str(e)}"]
                print(f"  Mobile test failed: {str(e)}")
            finally:
                mobile_driver.quit()
            
            city_results["results"].append({
                "page": page,
                "desktop_load_time": desktop_load_time,
                "desktop_issues": desktop_issues,
                "mobile_load_time": mobile_load_time,
                "mobile_issues": mobile_issues
            })
            
            time.sleep(1)  # Brief pause between tests
        
        results.append(city_results)
    
    # Generate and save report
    report = generate_report(results)
    
    with open("performance_test_report.md", "w") as f:
        f.write(report)
    
    # Also save raw results as JSON
    with open("performance_test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n\nTest complete! Report saved to performance_test_report.md")
    print("\n" + "="*50)
    print(report)

if __name__ == "__main__":
    main()