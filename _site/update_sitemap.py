#!/usr/bin/env python3
"""
Update sitemap.xml to include all state pages
"""

import xml.etree.ElementTree as ET
from datetime import datetime

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# State pages to add
states = [
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",
    "maine", "maryland", "massachusetts", "michigan", "minnesota",
    "mississippi", "missouri", "montana", "nebraska", "nevada",
    "new-hampshire", "new-jersey", "new-mexico", "new-york",
    "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon",
    "pennsylvania", "rhode-island", "south-carolina", "south-dakota",
    "tennessee", "texas", "utah", "vermont", "virginia", "washington",
    "washington-dc", "west-virginia", "wisconsin", "wyoming"
]

# Parse the existing sitemap
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Namespace for sitemap
namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Check which state pages are already in the sitemap
existing_urls = set()
for url in root.findall('sitemap:url', namespace):
    loc = url.find('sitemap:loc', namespace)
    if loc is not None:
        existing_urls.add(loc.text)

# Count added entries
added_count = 0

# Find the position after the main locations page
insert_position = None
for i, url in enumerate(root):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if loc is not None and loc.text == 'https://skerritteconomics.com/locations/':
        insert_position = i + 1
        break

if insert_position is None:
    # If we can't find the locations page, insert at the beginning
    insert_position = 10

# Add state pages if they don't exist
for state in states:
    state_url = f"https://skerritteconomics.com/locations/{state}.html"
    
    if state_url not in existing_urls:
        # Create new URL element
        url_elem = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
        
        loc_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        loc_elem.text = state_url
        
        lastmod_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
        lastmod_elem.text = today
        
        priority_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
        priority_elem.text = '0.7'
        
        # Insert at the appropriate position
        root.insert(insert_position + added_count, url_elem)
        added_count += 1

# Also check for the blog/topics page
blog_topics_url = "https://skerritteconomics.com/blog/topics/"
if blog_topics_url not in existing_urls:
    url_elem = ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
    
    loc_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    loc_elem.text = blog_topics_url
    
    lastmod_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')
    lastmod_elem.text = today
    
    priority_elem = ET.SubElement(url_elem, '{http://www.sitemaps.org/schemas/sitemap/0.9}priority')
    priority_elem.text = '0.8'
    
    # Find blog position and insert after it
    for i, url in enumerate(root):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None and '/blog/' in loc.text and '/blog/topics/' not in loc.text:
            root.insert(i + 1, url_elem)
            added_count += 1
            break

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

print(f"Added {added_count} new entries to sitemap.xml")
print("Sitemap successfully updated!")