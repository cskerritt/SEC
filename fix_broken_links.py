#!/usr/bin/env python3
"""
Script to fix broken links in state location pages.
Converts state-specific service links to directory-based links.
"""

import os
import re
import glob

def fix_broken_links():
    """Fix broken links in location pages."""
    
    # Define the main states directory
    locations_dir = "/Users/chrisskerritt/SEC/locations"
    
    # Get all HTML files in the main locations directory (not subdirectories)
    html_files = glob.glob(os.path.join(locations_dir, "*.html"))
    
    # Define replacement patterns
    patterns = [
        # Forensic economist patterns
        (r'([a-z-]+)-forensic-economist\.html', r'forensic-economics/'),
        # Business valuation patterns  
        (r'([a-z-]+)-business-valuation-analyst\.html', r'business-valuation/'),
        # Vocational expert patterns
        (r'([a-z-]+)-vocational-expert\.html', r'vocational-expert/'),
        # Life care planner patterns
        (r'([a-z-]+)-life-care-planner\.html', r'life-care-planning/'),
    ]
    
    fixed_files = []
    
    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply all replacement patterns
            for pattern, replacement in patterns:
                content = re.sub(pattern, replacement, content)
            
            # Only write if content changed
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(os.path.basename(file_path))
                print(f"Fixed links in: {os.path.basename(file_path)}")
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\nFixed {len(fixed_files)} files:")
    for file in sorted(fixed_files):
        print(f"  - {file}")

if __name__ == "__main__":
    fix_broken_links()