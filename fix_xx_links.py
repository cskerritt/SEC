#!/usr/bin/env python3
"""
Fix remaining xx in related service links
"""

import os
import re
from pathlib import Path

def fix_xx_in_links(filepath):
    """Fix xx in href links"""
    filename = os.path.basename(filepath)
    
    # Extract state from filename (e.g., auburn-wa-wa-life-care-planner.html -> wa)
    match = re.match(r'(.+?)-([a-z]{2})-', filename)
    if not match:
        return False
    
    state_abbr = match.group(2)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix all xx in href links with the state abbreviation
    content = re.sub(r'href="([^"]*?)-xx-', f'href="\\1-{state_abbr}-', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Main function"""
    cities_path = Path('/Users/chrisskerritt/SEC/locations/cities')
    
    print("Fixing xx in related service links...")
    print("=" * 60)
    
    files_fixed = 0
    files_checked = 0
    
    # Get all HTML files
    for filepath in sorted(cities_path.glob('*.html')):
        files_checked += 1
        if fix_xx_in_links(filepath):
            files_fixed += 1
            print(f"Fixed: {filepath.name}")
    
    print("\n" + "=" * 60)
    print(f"Files checked: {files_checked}")
    print(f"Files fixed: {files_fixed}")

if __name__ == '__main__':
    main()