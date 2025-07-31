#!/usr/bin/env python3
"""
Fix heading structure issues in state location pages.
Adds visually-hidden h3 elements where service-links-section lacks proper hierarchy.
"""

import os
import re
import glob

def fix_heading_structure(file_path):
    """Fix heading structure in a single HTML file."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file already has the visually-hidden h3 - skip if already fixed
    if 'visually-hidden' in content and 'Service Links' in content:
        print(f"  ✓ Already fixed: {os.path.basename(file_path)}")
        return False
    
    # Pattern to find service-links-section without visually-hidden h3
    pattern = r'(<section class="service-links-section">\s*<div class="container">\s*)(</div>|<div class="service-links-grid">)'
    
    # Replacement with visually-hidden h3
    def replacement(match):
        state_name = extract_state_name(file_path)
        return f'{match.group(1)}<h3 class="visually-hidden">{state_name} Service Links</h3>\n            {match.group(2)}'
    
    new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)
    
    # Only write if content changed
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Fixed: {os.path.basename(file_path)}")
        return True
    else:
        print(f"  ⚠️  No changes needed: {os.path.basename(file_path)}")
        return False

def extract_state_name(file_path):
    """Extract state name from file path and format it properly."""
    
    # Get base filename without extension
    filename = os.path.basename(file_path).replace('.html', '')
    
    # Handle special cases
    special_cases = {
        'washington-dc': 'Washington DC',
        'new-york': 'New York',
        'new-jersey': 'New Jersey',
        'new-hampshire': 'New Hampshire',
        'new-mexico': 'New Mexico',
        'north-carolina': 'North Carolina',
        'north-dakota': 'North Dakota',
        'south-carolina': 'South Carolina',
        'south-dakota': 'South Dakota',
        'west-virginia': 'West Virginia',
        'rhode-island': 'Rhode Island'
    }
    
    if filename in special_cases:
        return special_cases[filename]
    
    # Convert kebab-case to Title Case
    return filename.replace('-', ' ').title()

def main():
    """Main function to fix heading structure across all state pages."""
    
    # Get all state HTML files (excluding index.html and subdirectories)
    locations_dir = '/Users/chrisskerritt/SEC/locations'
    state_files = glob.glob(os.path.join(locations_dir, '*.html'))
    state_files = [f for f in state_files if not f.endswith('/index.html')]
    
    print(f"Found {len(state_files)} state files to process...")
    print()
    
    fixed_count = 0
    
    for file_path in sorted(state_files):
        if fix_heading_structure(file_path):
            fixed_count += 1
    
    print()
    print(f"✅ Heading structure fixes completed!")
    print(f"   Fixed: {fixed_count} files")
    print(f"   Total: {len(state_files)} files processed")

if __name__ == '__main__':
    main()