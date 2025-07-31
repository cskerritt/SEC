#!/usr/bin/env python3
"""
Add all city pages to sitemap.xml
"""

import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# Parse the existing sitemap
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Namespace for sitemap
namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Check which URLs are already in the sitemap
existing_urls = set()
for url in root.findall('sitemap:url', namespace):
    loc = url.find('sitemap:loc', namespace)
    if loc is not None:
        existing_urls.add(loc.text)

# Count added entries
added_count = 0

# Get all city pages
cities_dir = "/Users/chrisskerritt/SEC/locations/cities"
if os.path.exists(cities_dir):
    city_files = [f for f in os.listdir(cities_dir) if f.endswith('.html') and f != 'preview-system.html']
    
    # Sort by type for better organization
    city_hubs = []
    service_pages = []
    
    for file in city_files:
        if any(service in file for service in ['-forensic-economist.html', '-business-valuation-analyst.html', 
                                               '-vocational-expert.html', '-life-care-planner.html']):
            service_pages.append(file)
        else:
            city_hubs.append(file)
    
    # Find insert position after state pages
    insert_position = None
    for i, url in enumerate(root):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None and '/locations/wyoming.html' in loc.text:
            insert_position = i + 1
            break
    
    if insert_position is None:
        # If we can't find wyoming, insert after locations index
        for i, url in enumerate(root):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc is not None and loc.text == 'https://skerritteconomics.com/locations/':
                insert_position = i + 1
                break
    
    if insert_position is None:
        insert_position = 20  # Default position
    
    # Add city hub pages (higher priority)
    for file in sorted(city_hubs):
        city_url = f"https://skerritteconomics.com/locations/cities/{file}"
        
        if city_url not in existing_urls:
            # Create new URL element
            url_elem = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            
            loc_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            loc_elem.text = city_url
            
            lastmod_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
            lastmod_elem.text = today
            
            priority_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
            priority_elem.text = '0.6'
            
            # Insert at the appropriate position
            root.insert(insert_position + added_count, url_elem)
            added_count += 1
    
    # Add service-specific pages (lower priority)
    for file in sorted(service_pages):
        service_url = f"https://skerritteconomics.com/locations/cities/{file}"
        
        if service_url not in existing_urls:
            # Create new URL element
            url_elem = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            
            loc_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            loc_elem.text = service_url
            
            lastmod_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
            lastmod_elem.text = today
            
            priority_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
            priority_elem.text = '0.5'
            
            # Insert at the appropriate position
            root.insert(insert_position + added_count, url_elem)
            added_count += 1

# Format the XML properly
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Apply formatting
indent(root)

# Write the updated sitemap
tree.write('sitemap.xml', encoding='UTF-8', xml_declaration=True)

print(f"Added {added_count} city page entries to sitemap.xml")
print("Sitemap successfully updated with all city pages!")