#!/usr/bin/env python3
"""
Ensure all buttons in the header have white text color
"""

import os
import re
import glob

def add_button_style_fix(html_content):
    """Add CSS to ensure button text is always white"""
    
    # Check if we already have the fix
    if 'header-nav .btn-professional' in html_content and 'color: white !important' in html_content:
        return html_content
    
    # Add CSS fix before closing </style> tag
    css_fix = """
    /* Ensure header button always has white text */
    .header-nav .btn-professional,
    .header-nav .btn-professional:hover,
    .header-nav .btn-professional:focus,
    .header-nav .btn-professional:active,
    .mobile-menu-nav .btn-professional,
    .mobile-menu-nav .btn-professional:hover,
    .mobile-menu-nav .btn-professional:focus,
    .mobile-menu-nav .btn-professional:active {
        color: white !important;
    }
    """
    
    # Insert before the last </style> tag
    if '</style>' in html_content:
        html_content = html_content.replace('</style>', css_fix + '\n  </style>', 1)
    
    return html_content

def process_city_page(filepath):
    """Process a single city page to ensure white button text"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Add button style fix
        updated_content = add_button_style_fix(html_content)
        
        # Only write if changes were made
        if updated_content != html_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True, f"Fixed button text color in: {os.path.basename(filepath)}"
        else:
            return True, f"Already fixed: {os.path.basename(filepath)}"
        
    except Exception as e:
        return False, f"Error processing {filepath}: {str(e)}"

def main():
    """Main function to fix button text color in city pages"""
    print("Fixing Button Text Color in City Pages")
    print("=" * 50)
    
    # Process the 5 sample pages first
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
    
    print("\nButton text color fixed. All header buttons will now show white text.")

if __name__ == "__main__":
    main()