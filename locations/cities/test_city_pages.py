#!/usr/bin/env python3
"""
Comprehensive performance testing for city pages
"""

import time
import json
from datetime import datetime

# Test configuration
BASE_URL = "http://localhost:8000"
TEST_PAGES = [
    # NYC
    ("New York, NY - Vocational Expert", "new-york-ny-ny-vocational-expert.html"),
    ("New York, NY - Life Care Planner", "new-york-ny-ny-life-care-planner.html"),
    # LA
    ("Los Angeles, CA - Vocational Expert", "los-angeles-ca-ca-vocational-expert.html"),
    ("Los Angeles, CA - Life Care Planner", "los-angeles-ca-ca-life-care-planner.html"),
    # Chicago
    ("Chicago, IL - Vocational Expert", "chicago-il-il-vocational-expert.html"),
    ("Chicago, IL - Life Care Planner", "chicago-il-il-life-care-planner.html"),
    # Houston
    ("Houston, TX - Vocational Expert", "houston-tx-tx-vocational-expert.html"),
    ("Houston, TX - Life Care Planner", "houston-tx-tx-life-care-planner.html"),
    # Boston
    ("Boston, MA - Vocational Expert", "boston-ma-ma-vocational-expert.html"),
    ("Boston, MA - Life Care Planner", "boston-ma-ma-life-care-planner.html"),
]

def test_page_load(url):
    """Test page loading and return metrics"""
    import requests
    from bs4 import BeautifulSoup
    
    start_time = time.time()
    
    try:
        response = requests.get(url, timeout=10)
        load_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Check for key elements
            title = soup.find('title')
            meta_desc = soup.find('meta', {'name': 'description'})
            nav = soup.find(['nav', 'header'])
            images = soup.find_all('img')
            links = soup.find_all('a', href=True)
            icons = soup.find_all(['i', 'svg'], class_=lambda x: x and 'fa' in x)
            
            # Count internal links
            internal_links = [link for link in links if link['href'].startswith(('/','#','./'))]
            
            return {
                "status": "success",
                "load_time": load_time,
                "status_code": response.status_code,
                "has_title": bool(title and title.text),
                "title": title.text if title else "Missing",
                "has_meta_description": bool(meta_desc and meta_desc.get('content')),
                "meta_description": meta_desc.get('content', '')[:100] + "..." if meta_desc else "Missing",
                "has_navigation": bool(nav),
                "image_count": len(images),
                "icon_count": len(icons),
                "internal_link_count": len(internal_links),
                "total_link_count": len(links),
                "page_size": len(response.content),
            }
        else:
            return {
                "status": "error",
                "load_time": load_time,
                "status_code": response.status_code,
                "error": f"HTTP {response.status_code}"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "load_time": (time.time() - start_time) * 1000,
            "error": str(e)
        }

def check_mobile_viewport(url):
    """Check if page has mobile viewport meta tag"""
    import requests
    from bs4 import BeautifulSoup
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            viewport = soup.find('meta', {'name': 'viewport'})
            return bool(viewport and viewport.get('content'))
    except:
        pass
    return False

def generate_performance_report(results):
    """Generate a detailed performance report"""
    report = []
    report.append("# City Pages Performance Test Report")
    report.append(f"**Test Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Test Environment:** Local server at {BASE_URL}")
    
    # Summary statistics
    successful_tests = [r for r in results if r['result']['status'] == 'success']
    avg_load_time = sum(r['result']['load_time'] for r in successful_tests) / len(successful_tests) if successful_tests else 0
    
    report.append("\n## Executive Summary")
    report.append(f"- **Total Pages Tested:** {len(results)}")
    report.append(f"- **Successful Tests:** {len(successful_tests)}")
    report.append(f"- **Failed Tests:** {len(results) - len(successful_tests)}")
    report.append(f"- **Average Load Time:** {avg_load_time:.0f}ms")
    
    # Performance benchmarks
    report.append("\n## Performance Benchmarks")
    excellent = sum(1 for r in successful_tests if r['result']['load_time'] < 1000)
    good = sum(1 for r in successful_tests if 1000 <= r['result']['load_time'] < 3000)
    needs_improvement = sum(1 for r in successful_tests if 3000 <= r['result']['load_time'] < 5000)
    poor = sum(1 for r in successful_tests if r['result']['load_time'] >= 5000)
    
    report.append(f"- **Excellent (< 1s):** {excellent} pages")
    report.append(f"- **Good (1-3s):** {good} pages")
    report.append(f"- **Needs Improvement (3-5s):** {needs_improvement} pages")
    report.append(f"- **Poor (> 5s):** {poor} pages")
    
    # Detailed results by city
    report.append("\n## Detailed Results by City")
    
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Boston"]
    for city in cities:
        city_results = [r for r in results if city in r['name']]
        if city_results:
            report.append(f"\n### {city}")
            for result in city_results:
                r = result['result']
                report.append(f"\n#### {result['name']}")
                if r['status'] == 'success':
                    report.append(f"- **Load Time:** {r['load_time']:.0f}ms")
                    report.append(f"- **Page Size:** {r['page_size'] / 1024:.1f}KB")
                    report.append(f"- **Title:** {'✓' if r['has_title'] else '✗'} {r.get('title', 'Missing')}")
                    report.append(f"- **Meta Description:** {'✓' if r['has_meta_description'] else '✗'}")
                    report.append(f"- **Navigation:** {'✓' if r['has_navigation'] else '✗'}")
                    report.append(f"- **Images:** {r['image_count']}")
                    report.append(f"- **Icons:** {r['icon_count']}")
                    report.append(f"- **Internal Links:** {r['internal_link_count']}")
                    report.append(f"- **Mobile Viewport:** {'✓' if result.get('has_mobile_viewport') else '✗'}")
                else:
                    report.append(f"- **Status:** Failed - {r.get('error', 'Unknown error')}")
    
    # Issues and recommendations
    report.append("\n## Issues Found")
    issues = []
    
    for result in results:
        if result['result']['status'] == 'success':
            r = result['result']
            if not r['has_title']:
                issues.append(f"- {result['name']}: Missing page title")
            if not r['has_meta_description']:
                issues.append(f"- {result['name']}: Missing meta description")
            if r['icon_count'] == 0:
                issues.append(f"- {result['name']}: No icons found (Font Awesome may not be loading)")
            if r['load_time'] > 3000:
                issues.append(f"- {result['name']}: Slow load time ({r['load_time']:.0f}ms)")
            if not result.get('has_mobile_viewport'):
                issues.append(f"- {result['name']}: Missing mobile viewport meta tag")
        else:
            issues.append(f"- {result['name']}: Failed to load - {result['result'].get('error', 'Unknown error')}")
    
    if issues:
        for issue in issues:
            report.append(issue)
    else:
        report.append("- No major issues found")
    
    report.append("\n## Recommendations")
    report.append("1. **Performance Optimization:**")
    report.append("   - Optimize images and use lazy loading")
    report.append("   - Minify CSS and JavaScript files")
    report.append("   - Enable browser caching")
    report.append("   - Consider using a CDN for static assets")
    
    report.append("\n2. **SEO Improvements:**")
    report.append("   - Ensure all pages have unique, descriptive titles")
    report.append("   - Add meta descriptions to pages missing them")
    report.append("   - Implement structured data for local business")
    
    report.append("\n3. **Mobile Optimization:**")
    report.append("   - Ensure all pages have viewport meta tags")
    report.append("   - Test responsive design on various devices")
    report.append("   - Optimize touch targets for mobile users")
    
    return "\n".join(report)

def main():
    """Main test execution"""
    print("Starting comprehensive performance tests...")
    results = []
    
    for name, page in TEST_PAGES:
        print(f"\nTesting: {name}")
        url = f"{BASE_URL}/{page}"
        
        # Test page load and gather metrics
        result = test_page_load(url)
        
        # Check mobile viewport
        has_mobile_viewport = check_mobile_viewport(url)
        
        results.append({
            "name": name,
            "page": page,
            "url": url,
            "result": result,
            "has_mobile_viewport": has_mobile_viewport
        })
        
        # Print immediate feedback
        if result['status'] == 'success':
            print(f"  ✓ Load time: {result['load_time']:.0f}ms")
            print(f"  ✓ Icons found: {result['icon_count']}")
            print(f"  ✓ Mobile viewport: {'Yes' if has_mobile_viewport else 'No'}")
        else:
            print(f"  ✗ Error: {result.get('error', 'Unknown error')}")
        
        time.sleep(0.5)  # Brief pause between tests
    
    # Generate report
    report = generate_performance_report(results)
    
    # Save report
    with open("performance_report.md", "w") as f:
        f.write(report)
    
    # Save raw results
    with open("performance_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n" + "="*60)
    print("\nTest complete! Report saved to performance_report.md")
    
    return report

if __name__ == "__main__":
    report = main()
    print("\n" + report)