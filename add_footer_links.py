#!/usr/bin/env python3
"""
Add footer links to major city pages across all HTML files
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Major cities to include in footer
MAJOR_CITIES = [
    {"name": "New York", "slug": "new-york-ny"},
    {"name": "Los Angeles", "slug": "los-angeles-ca"},
    {"name": "Chicago", "slug": "chicago-il"},
    {"name": "Houston", "slug": "houston-tx"},
    {"name": "Phoenix", "slug": "phoenix-az"},
    {"name": "Philadelphia", "slug": "philadelphia-pa"},
    {"name": "San Antonio", "slug": "san-antonio-tx"},
    {"name": "San Diego", "slug": "san-diego-ca"},
    {"name": "Dallas", "slug": "dallas-tx"},
    {"name": "San Jose", "slug": "san-jose-ca"},
    {"name": "Austin", "slug": "austin-tx"},
    {"name": "Jacksonville", "slug": "jacksonville-fl"},
    {"name": "Fort Worth", "slug": "fort-worth-tx"},
    {"name": "Columbus", "slug": "columbus-oh"},
    {"name": "Charlotte", "slug": "charlotte-nc"},
    {"name": "San Francisco", "slug": "san-francisco-ca"},
    {"name": "Indianapolis", "slug": "indianapolis-in"},
    {"name": "Seattle", "slug": "seattle-wa"},
    {"name": "Denver", "slug": "denver-co"},
    {"name": "Boston", "slug": "boston-ma"},
    {"name": "Atlanta", "slug": "atlanta-ga"},
    {"name": "Miami", "slug": "miami-fl"},
    {"name": "Las Vegas", "slug": "las-vegas-nv"},
    {"name": "Portland", "slug": "portland-or"},
    {"name": "Detroit", "slug": "detroit-mi"}
]

def add_city_links_to_footer(file_path):
    """Add major city links to footer if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find the main footer
        footer = soup.find('footer', class_='main-footer')
        if not footer:
            return False
        
        # Check if city links already exist
        if footer.find('h4', string='Major Cities'):
            return False
        
        # Find the footer grid
        footer_grid = footer.find('div', class_='footer-grid')
        if not footer_grid:
            return False
        
        # Create new city links column
        city_col = soup.new_tag('div', attrs={'class': 'footer-col'})
        
        # Add heading
        heading = soup.new_tag('h4')
        heading.string = 'Major Cities'
        city_col.append(heading)
        
        # Add city list
        city_list = soup.new_tag('ul')
        
        # Add first 5 major cities
        for city in MAJOR_CITIES[:5]:
            li = soup.new_tag('li')
            link = soup.new_tag('a', href=f'/locations/cities/{city["slug"]}-forensic-economist.html')
            link.string = f'{city["name"]} Forensic Economist'
            li.append(link)
            city_list.append(li)
        
        # Add link to all locations
        li = soup.new_tag('li')
        link = soup.new_tag('a', href='/sitemap.html')
        link.string = 'View All Locations'
        li.append(link)
        city_list.append(li)
        
        city_col.append(city_list)
        
        # Insert after the last column
        last_col = footer_grid.find_all('div', class_='footer-col')[-1]
        last_col.insert_after(city_col)
        
        # Save the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        return True
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def should_add_footer_links(file_path):
    """Determine if file should have footer links added"""
    # Only add to main pages, not city pages themselves
    if '/locations/cities/' in file_path:
        return False
    
    # Skip test and review files
    if any(skip in file_path for skip in ['test-', 'review-', 'manual-', 'navigator']):
        return False
    
    # Only HTML files
    if not file_path.endswith('.html'):
        return False
    
    return True

def update_all_footers():
    """Update footers on all appropriate pages"""
    base_dir = Path(__file__).resolve().parent
    updated_count = 0
    
    # Key pages to update
    key_pages = [
        'index.html',
        'about/index.html',
        'contact/index.html',
        'services/index.html',
        'services/forensic-economics/index.html',
        'services/business-valuation/index.html',
        'practice-areas/index.html',
        'practice-areas/personal-injury/index.html',
        'practice-areas/medical-malpractice/index.html',
        'practice-areas/employment/index.html',
        'practice-areas/commercial-disputes/index.html',
        'case-studies/index.html',
        'resources/index.html'
    ]
    
    for page in key_pages:
        file_path = os.path.join(base_dir, page)
        if os.path.exists(file_path):
            if add_city_links_to_footer(file_path):
                updated_count += 1
                print(f"Updated footer: {page}")
    
    print(f"\nTotal footers updated: {updated_count}")

if __name__ == "__main__":
    update_all_footers()