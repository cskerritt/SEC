#!/usr/bin/env python3
"""
Fix CSS paths in city pages to use correct relative paths
"""

import os
import re

def fix_css_paths(file_path):
    """Fix CSS paths in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix the paths
        content = content.replace(
            '<link rel="stylesheet" href="/css/ui-library-bootstrap.css">',
            '<link rel="stylesheet" href="../../css/ui-library-bootstrap.css">'
        )
        content = content.replace(
            '<link rel="stylesheet" href="/css/text-contrast-fix.css">',
            '<link rel="stylesheet" href="../../css/text-contrast-fix.css">'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Fixed paths in: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {str(e)}")
        return False

def main():
    """Fix paths in all migrated city pages"""
    city_pages = [
        'locations/cities/bristol-ri-business-valuation-analyst.html',
        'locations/cities/bristol-ri-forensic-economist.html',
        'locations/cities/bristol-ri-ri-life-care-planner.html',
        'locations/cities/bristol-ri-ri-vocational-expert.html',
        'locations/cities/central-falls-ri-business-valuation-analyst.html',
        'locations/cities/central-falls-ri-forensic-economist.html',
        'locations/cities/central-falls-ri-ri-life-care-planner.html',
        'locations/cities/central-falls-ri-ri-vocational-expert.html',
        'locations/cities/coventry-ri-business-valuation-analyst.html',
        'locations/cities/coventry-ri-forensic-economist.html'
    ]
    
    fixed = 0
    for page in city_pages:
        if os.path.exists(page) and fix_css_paths(page):
            fixed += 1
    
    print(f"\n✅ Fixed CSS paths in {fixed} pages")

if __name__ == '__main__':
    main()