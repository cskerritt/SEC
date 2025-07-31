#!/usr/bin/env python3
"""
Script to add city-pages.css to all forensic economist city pages that are missing it
"""

import os
import glob

def fix_forensic_economist_css():
    # Find all forensic economist city pages
    forensic_pages = glob.glob("locations/cities/*-forensic-economist.html")
    
    print(f"Found {len(forensic_pages)} forensic economist pages to check")
    
    fixed_count = 0
    already_has_count = 0
    
    for page_path in forensic_pages:
        try:
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if city-pages.css is already included
            if 'city-pages.css' in content:
                already_has_count += 1
                continue
            
            # Add city-pages.css after locations.css
            if '<link href="../../css/locations.css" rel="stylesheet"/>' in content:
                new_content = content.replace(
                    '<link href="../../css/locations.css" rel="stylesheet"/>',
                    '<link href="../../css/locations.css" rel="stylesheet"/>\n    <link href="../../css/city-pages.css" rel="stylesheet"/>'
                )
                
                # Write the updated content
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                fixed_count += 1
                print(f"Fixed: {page_path}")
            else:
                print(f"Warning: Could not find locations.css link in {page_path}")
            
        except Exception as e:
            print(f"Error processing {page_path}: {e}")
    
    print(f"\nSummary:")
    print(f"- Total forensic economist pages: {len(forensic_pages)}")
    print(f"- Pages that already had city-pages.css: {already_has_count}")
    print(f"- Pages fixed: {fixed_count}")

if __name__ == "__main__":
    fix_forensic_economist_css()