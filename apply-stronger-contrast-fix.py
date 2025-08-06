#!/usr/bin/env python3
"""
Apply stronger contrast fix to migrated pages
"""

import os

def apply_stronger_fix(file_path):
    """Replace text-contrast-fix.css with text-contrast-fix-v2.css"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the CSS reference
        content = content.replace(
            'href="../../css/text-contrast-fix.css"',
            'href="../../css/text-contrast-fix-v2.css"'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {file_path} - {str(e)}")
        return False

def main():
    """Apply fix to all migrated city pages"""
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
    
    print("Applying stronger contrast fix...")
    
    updated = 0
    for page in city_pages:
        if os.path.exists(page) and apply_stronger_fix(page):
            updated += 1
    
    print(f"\n✅ Updated {updated} pages with stronger contrast fix")

if __name__ == '__main__':
    main()