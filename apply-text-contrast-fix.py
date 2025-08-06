#!/usr/bin/env python3
"""
Apply text contrast fix to all migrated pages
"""

import os
import re

def apply_contrast_fix(file_path):
    """Apply text contrast fix CSS to a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has the fix
        if 'text-contrast-fix.css' in content:
            print(f"✓ Already fixed: {file_path}")
            return False
        
        # Check if it's a migrated file (has Bootstrap)
        if 'bootstrap@5.3.2' not in content and 'bootstrap.min.css' not in content:
            print(f"⏭ Skipping non-migrated: {file_path}")
            return False
        
        # Add the contrast fix CSS after the UI library CSS
        if '/css/ui-library-bootstrap.css' in content:
            content = content.replace(
                '<link rel="stylesheet" href="/css/ui-library-bootstrap.css">',
                '<link rel="stylesheet" href="/css/ui-library-bootstrap.css">\n<link rel="stylesheet" href="/css/text-contrast-fix.css">'
            )
        elif '../../css/ui-library-bootstrap.css' in content:
            content = content.replace(
                '<link rel="stylesheet" href="../../css/ui-library-bootstrap.css">',
                '<link rel="stylesheet" href="../../css/ui-library-bootstrap.css">\n<link rel="stylesheet" href="../../css/text-contrast-fix.css">'
            )
        else:
            # Add after Bootstrap CSS
            content = re.sub(
                r'(<link[^>]*bootstrap[^>]*>)',
                r'\1\n<link rel="stylesheet" href="/css/text-contrast-fix.css">',
                content,
                count=1
            )
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Fixed contrast: {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {str(e)}")
        return False

def fix_all_pages():
    """Apply contrast fix to all migrated pages"""
    fixed_count = 0
    
    # Fix service pages
    service_pages = [
        'services/index.html',
        'services/forensic-economics/index.html',
        'services/business-valuation/index.html',
        'services/vocational-expert/index.html',
        'services/life-care-planning/index.html'
    ]
    
    print("Fixing service pages...")
    for page in service_pages:
        if os.path.exists(page) and apply_contrast_fix(page):
            fixed_count += 1
    
    # Fix practice area pages
    practice_pages = [
        'practice-areas/index.html',
        'practice-areas/personal-injury/index.html',
        'practice-areas/medical-malpractice/index.html',
        'practice-areas/employment/index.html',
        'practice-areas/commercial-disputes/index.html',
        'practice-areas/family-law/index.html',
        'practice-areas/product-liability/index.html'
    ]
    
    print("\nFixing practice area pages...")
    for page in practice_pages:
        if os.path.exists(page) and apply_contrast_fix(page):
            fixed_count += 1
    
    # Fix city pages
    print("\nFixing city pages...")
    city_dir = 'locations/cities'
    if os.path.exists(city_dir):
        for filename in os.listdir(city_dir):
            if filename.endswith('.html') and not filename.endswith('.pre-ui-backup'):
                file_path = os.path.join(city_dir, filename)
                if apply_contrast_fix(file_path):
                    fixed_count += 1
    
    print(f"\n✅ Fixed {fixed_count} pages with contrast improvements")

if __name__ == '__main__':
    fix_all_pages()