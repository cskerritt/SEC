#!/usr/bin/env python3
"""
Fix the class_ attributes that should be class attributes
"""

import os
import re
from pathlib import Path

def fix_class_attributes(content):
    """Fix class_ attributes to be class attributes"""
    # Replace all instances of class_=" with class="
    content = content.replace('class_="', 'class="')
    return content

def main():
    """Main function to fix class attributes in all city pages"""
    cities_dir = Path('locations/cities')
    
    # Get all city pages
    all_pages = list(cities_dir.glob('*-forensic-economist.html'))
    all_pages.extend(list(cities_dir.glob('*-business-valuation-analyst.html')))
    
    fixed_count = 0
    
    for page in all_pages:
        try:
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has the issue
            if 'class_="' in content:
                # Fix the content
                fixed_content = fix_class_attributes(content)
                
                # Write back the file
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                
                fixed_count += 1
                print(f"Fixed {page.name}")
        
        except Exception as e:
            print(f"Error processing {page}: {str(e)}")
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()