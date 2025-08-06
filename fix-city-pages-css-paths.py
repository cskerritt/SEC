#!/usr/bin/env python3
"""
Fix CSS paths in city pages to use correct relative paths for modern UI
"""

import os
import re
import glob

def fix_css_paths(html_content):
    """Fix CSS paths to use correct relative paths"""
    
    # Remove all old CSS files
    css_patterns = [
        r'<link[^>]*href="[^"]*(?:styles\.css|city-pages\.css|override\.css|locations\.css|city-pages-enhanced\.css|city-footer-sections\.css|mobile-optimized\.css)[^"]*"[^>]*>\s*',
        r'<link[^>]*href="[^"]*icons\.css[^"]*"[^>]*>\s*'
    ]
    
    for pattern in css_patterns:
        html_content = re.sub(pattern, '', html_content)
    
    # Add modern UI CSS with correct relative path
    modern_css = '''  <!-- Modern UI CSS -->
  <link rel="stylesheet" href="../../css/modern-ui.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'''
    
    # Insert before the fonts preconnect or before </head> if no fonts
    if '<link href="https://fonts.googleapis.com" rel="preconnect"/>' in html_content:
        html_content = html_content.replace(
            '<link href="https://fonts.googleapis.com" rel="preconnect"/>',
            modern_css + '\n  <link href="https://fonts.googleapis.com" rel="preconnect"/>'
        )
    else:
        # Insert before closing head tag
        html_content = re.sub(r'(\s*)(</head>)', r'\1' + modern_css + r'\n\1\2', html_content, count=1)
    
    return html_content

def process_city_page(filepath):
    """Process a single city page to fix CSS paths"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Fix CSS paths
        html_content = fix_css_paths(html_content)
        
        # Save updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return True, f"Fixed CSS paths in: {os.path.basename(filepath)}"
        
    except Exception as e:
        return False, f"Error processing {filepath}: {str(e)}"

def main():
    """Main function to fix CSS paths in city pages"""
    print("Fixing CSS Paths in City Pages")
    print("=" * 50)
    
    # Process the 5 sample pages that were already migrated
    sample_pages = [
        '/Users/chrisskerritt/SEC/locations/cities/phenix-city-al-al-life-care-planner.html',
        '/Users/chrisskerritt/SEC/locations/cities/north-kingstown-ri-ri-vocational-expert.html',
        '/Users/chrisskerritt/SEC/locations/cities/cary-nc-nc-vocational-expert.html',
        '/Users/chrisskerritt/SEC/locations/cities/blue-springs-mo-business-valuation-analyst.html',
        '/Users/chrisskerritt/SEC/locations/cities/sunland-park-nm-nm-vocational-expert.html'
    ]
    
    for page in sample_pages:
        if os.path.exists(page):
            success, message = process_city_page(page)
            print(f"{'✓' if success else '✗'} {message}")
        else:
            print(f"✗ File not found: {os.path.basename(page)}")
    
    print("\nCSS paths fixed in sample pages.")
    print("Now open the pages in a browser to see the modern UI properly styled.")

if __name__ == "__main__":
    main()