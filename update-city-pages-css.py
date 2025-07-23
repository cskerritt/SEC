#!/usr/bin/env python3
"""
Script to update all city pages to include the new city-pages.css stylesheet
"""

import os
import glob

def update_city_pages():
    # Find all city pages
    vocational_pages = glob.glob("locations/cities/*-vocational-expert.html")
    life_care_pages = glob.glob("locations/cities/*-life-care-planner.html")
    
    all_pages = vocational_pages + life_care_pages
    
    print(f"Found {len(all_pages)} city pages to update")
    
    updated_count = 0
    
    for page_path in all_pages:
        try:
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if city-pages.css is already included
            if 'city-pages.css' in content:
                print(f"Skipping {page_path} - already has city-pages.css")
                continue
            
            # Add city-pages.css after locations.css
            if '<link href="../../css/locations.css" rel="stylesheet"/>' in content:
                new_content = content.replace(
                    '<link href="../../css/locations.css" rel="stylesheet"/>',
                    '<link href="../../css/locations.css" rel="stylesheet"/>\n    <link href="../../css/city-pages.css" rel="stylesheet"/>'
                )
            else:
                print(f"Warning: Could not find locations.css link in {page_path}")
                continue
            
            # Write the updated content
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            updated_count += 1
            
        except Exception as e:
            print(f"Error updating {page_path}: {e}")
    
    print(f"\nSuccessfully updated {updated_count} pages with city-pages.css")

if __name__ == "__main__":
    update_city_pages()