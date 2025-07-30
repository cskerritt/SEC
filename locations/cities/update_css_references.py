#!/usr/bin/env python3

import os
import re

def update_css_in_file(filepath):
    """Update CSS reference in a single file"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Replace service-pages.css with city-service-pages.css
        updated_content = content.replace(
            '<link rel="stylesheet" href="../../css/service-pages.css">',
            '<link rel="stylesheet" href="../../css/city-service-pages.css">'
        )
        
        # Only write if changes were made
        if content != updated_content:
            with open(filepath, 'w') as f:
                f.write(updated_content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

# Get all HTML files in the current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview-system.html']

updated_count = 0
for filename in html_files:
    if update_css_in_file(filename):
        updated_count += 1
        print(f"Updated: {filename}")

print(f"\nTotal files updated: {updated_count}")