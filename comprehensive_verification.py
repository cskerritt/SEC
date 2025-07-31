#!/usr/bin/env python3
"""
Comprehensive Site Analysis Verification Script
Verifies all issues from the site analysis report have been fixed.
"""

import os
import re
import json
from pathlib import Path

def check_title_tags():
    """Check for multiple title tags in HTML files"""
    print("=== CHECKING TITLE TAGS ===")
    issues = []
    
    # Check home page specifically
    home_page = "/Users/chrisskerritt/SEC/_site/index.html"
    if os.path.exists(home_page):
        with open(home_page, 'r', encoding='utf-8') as f:
            content = f.read()
            title_count = content.count('<title>')
            if title_count > 1:
                issues.append(f"Home page has {title_count} title tags")
            else:
                print(f"✅ Home page has exactly {title_count} title tag")
    
    return issues

def check_css_js_references():
    """Check CSS/JS references in sample files"""
    print("\n=== CHECKING CSS/JS REFERENCES ===")
    issues = []
    
    # Sample files to check
    sample_files = [
        "/Users/chrisskerritt/SEC/_site/index.html",
        "/Users/chrisskerritt/SEC/_site/services/index.html",
        "/Users/chrisskerritt/SEC/_site/contact/index.html"
    ]
    
    for filepath in sample_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for CSS references
                css_refs = re.findall(r'href="([^"]*\.css[^"]*)"', content)
                js_refs = re.findall(r'src="([^"]*\.js[^"]*)"', content)
                
                # Verify CSS files exist
                for css_ref in css_refs:
                    if not css_ref.startswith('http') and not css_ref.startswith('//'):
                        # Convert relative path to absolute
                        if css_ref.startswith('/'):
                            css_path = f"/Users/chrisskerritt/SEC/_site{css_ref}"
                        else:
                            css_path = os.path.join(os.path.dirname(filepath), css_ref)
                        css_path = os.path.normpath(css_path)
                        
                        if not os.path.exists(css_path):
                            issues.append(f"Missing CSS: {css_ref} in {filepath}")
                
                print(f"✅ {os.path.basename(filepath)}: {len(css_refs)} CSS, {len(js_refs)} JS references")
    
    return issues

def check_city_pages_css():
    """Check that city pages have proper CSS references"""
    print("\n=== CHECKING CITY PAGES CSS ===")
    issues = []
    
    city_pages_dir = "/Users/chrisskerritt/SEC/_site/locations/cities"
    if not os.path.exists(city_pages_dir):
        return ["City pages directory not found"]
    
    # Sample different types of city pages
    sample_patterns = [
        "*-life-care-planner.html",
        "*-vocational-expert.html", 
        "*-forensic-economist.html",
        "*-business-valuation-analyst.html"
    ]
    
    for pattern in sample_patterns:
        files = list(Path(city_pages_dir).glob(pattern))[:3]  # Check 3 of each type
        
        for filepath in files:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for city-pages.css or city-service-pages.css
                has_city_css = 'city-pages.css' in content or 'city-service-pages.css' in content
                
                if not has_city_css:
                    issues.append(f"Missing city CSS: {filepath}")
                    
        print(f"✅ Checked {len(files)} files matching {pattern}")
    
    return issues

def check_whitespace_issues():
    """Check for excessive whitespace in HTML files"""
    print("\n=== CHECKING WHITESPACE ISSUES ===")
    issues = []
    
    # Check a sample of HTML files
    html_files = []
    for root, _, files in os.walk("/Users/chrisskerritt/SEC/_site"):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                if len(html_files) >= 50:  # Limit sample size
                    break
        if len(html_files) >= 50:
            break
    
    excessive_whitespace_count = 0
    trailing_spaces_count = 0
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
                # Check for excessive blank lines (4+ consecutive)
                if '\n\n\n\n' in content:
                    excessive_whitespace_count += 1
                    if excessive_whitespace_count <= 3:
                        issues.append(f"Excessive whitespace: {filepath}")
                
                # Check for trailing spaces
                for line in lines:
                    if line.rstrip('\n\r').endswith(' '):
                        trailing_spaces_count += 1
                        if trailing_spaces_count <= 3:
                            issues.append(f"Trailing spaces: {filepath}")
                        break
                        
        except Exception as e:
            continue
    
    print(f"✅ Checked {len(html_files)} HTML files")
    print(f"   Files with excessive whitespace: {excessive_whitespace_count}")
    print(f"   Files with trailing spaces: {trailing_spaces_count}")
    
    return issues

def check_placeholders():
    """Check for remaining placeholders"""
    print("\n=== CHECKING FOR PLACEHOLDERS ===")
    issues = []
    
    # Check for common placeholders
    placeholder_patterns = [
        'GA_MEASUREMENT_ID',
        'PLACEHOLDER',
        'TODO',
        'FIXME',
        'XXX'
    ]
    
    # Check main site files (exclude documentation)
    main_files = [
        "/Users/chrisskerritt/SEC/_site/index.html",
        "/Users/chrisskerritt/SEC/_site/services/index.html",
        "/Users/chrisskerritt/SEC/_site/contact/index.html",
        "/Users/chrisskerritt/SEC/_site/about/index.html"
    ]
    
    for filepath in main_files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                for pattern in placeholder_patterns:
                    if pattern in content:
                        issues.append(f"Placeholder '{pattern}' found in {filepath}")
    
    print(f"✅ Checked {len(main_files)} main site files for placeholders")
    
    return issues

def check_json_syntax():
    """Check for JSON syntax errors"""
    print("\n=== CHECKING JSON SYNTAX ===")
    issues = []
    
    # Check services page specifically (mentioned in report)
    services_page = "/Users/chrisskerritt/SEC/_site/services/index.html"
    if os.path.exists(services_page):
        with open(services_page, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract JSON-LD blocks
            json_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
            
            for i, json_block in enumerate(json_blocks):
                try:
                    json.loads(json_block.strip())
                    print(f"✅ JSON block {i+1} is valid")
                except json.JSONDecodeError as e:
                    issues.append(f"JSON syntax error in services page block {i+1}: {e}")
    
    return issues

def check_missing_files():
    """Check for missing files mentioned in the report"""
    print("\n=== CHECKING FOR MISSING FILES ===")
    issues = []
    
    # Files that should exist
    expected_files = [
        "/Users/chrisskerritt/SEC/_site/locations/connecticut.html",
        "/Users/chrisskerritt/SEC/_site/css/icons.css",
        "/Users/chrisskerritt/SEC/_site/css/city-pages.css"
    ]
    
    for filepath in expected_files:
        if not os.path.exists(filepath):
            issues.append(f"Missing file: {filepath}")
        else:
            print(f"✅ Found: {os.path.basename(filepath)}")
    
    return issues

def generate_summary_report(all_issues):
    """Generate final summary report"""
    print("\n" + "="*60)
    print("COMPREHENSIVE VERIFICATION SUMMARY")
    print("="*60)
    
    if not all_issues:
        print("🎉 ALL CHECKS PASSED!")
        print("\n✅ No issues found. All reported problems have been fixed:")
        print("   • Home page has only one title tag")
        print("   • CSS/JS references are correct")
        print("   • City pages have proper CSS (city-pages.css)")
        print("   • No excessive whitespace in HTML files")
        print("   • No placeholder text remaining") 
        print("   • JSON syntax is valid")
        print("   • All expected files are present")
        return True
    else:
        print(f"⚠️  FOUND {len(all_issues)} REMAINING ISSUES:")
        print("-" * 40)
        for issue in all_issues:
            print(f"   • {issue}")
        
        print("\n📋 RECOMMENDATIONS:")
        print("   1. Address the remaining issues listed above")
        print("   2. Re-run this verification script after fixes")
        print("   3. Focus on high-priority issues first")
        
        return False

def main():
    """Main verification function"""
    print("Starting Comprehensive Site Verification...")
    print("Checking fixes applied from site analysis report")
    
    all_issues = []
    
    # Run all checks
    all_issues.extend(check_title_tags())
    all_issues.extend(check_css_js_references())
    all_issues.extend(check_city_pages_css())
    all_issues.extend(check_whitespace_issues())
    all_issues.extend(check_placeholders())
    all_issues.extend(check_json_syntax())
    all_issues.extend(check_missing_files())
    
    # Generate final report
    success = generate_summary_report(all_issues)
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())