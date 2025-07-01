#!/usr/bin/env python3
"""
Generate a comprehensive sitemap.xml for skerritteconomics.com
Fixes Google indexing issues by including all pages with proper priorities and structure
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
import re

# Base configuration
BASE_DIR = "/Users/chrisskerritt/SEC"
BASE_URL = "https://skerritteconomics.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Priority mapping
PRIORITY_MAP = {
    "index.html": 1.0,  # Homepage
    "services": 0.9,    # Services pages
    "practice-areas": 0.9,  # Practice areas pages
    "contact": 0.8,     # Contact page
    "about": 0.7,       # About page
    "case-studies": 0.7,  # Case studies
    "resources": 0.7,   # Resources
    "locations/cities": 0.6,  # City pages
    "locations": 0.7,   # State/region pages
    "faq": 0.6,         # FAQ
    "default": 0.5      # Default for other pages
}

def get_priority(path):
    """Determine priority based on path"""
    if path == "/" or path == "/index.html":
        return 1.0
    elif "/services/" in path or path == "/services/":
        return 0.9
    elif "/practice-areas/" in path or path == "/practice-areas/":
        return 0.9
    elif "/contact" in path:
        return 0.8
    elif "/about" in path:
        return 0.7
    elif "/case-studies" in path:
        return 0.7
    elif "/resources" in path:
        return 0.7
    elif "/locations/cities/" in path:
        return 0.6
    elif "/locations/" in path:
        return 0.7
    elif "/faq" in path:
        return 0.6
    else:
        return 0.5

def should_include_file(file_path):
    """Determine if a file should be included in sitemap"""
    # Exclude patterns
    exclude_patterns = [
        r'\.backup$',
        r'test-',
        r'review-',
        r'navigator',
        r'manual-',
        r'serve-',
        r'open-',
        r'generate-',
        r'fix-',
        r'update-',
        r'template',
        r'_includes',
        r'_layouts',
        r'\.py$',
        r'\.js$',
        r'\.css$',
        r'\.md$',
        r'\.json$',
        r'\.txt$',
        r'\.sh$',
        r'\.yml$',
        r'\.xml$',
        r'\.log$',
        r'Gemfile',
        r'CNAME',
        r'favicon',
        r'\.jpg$',
        r'\.png$',
        r'\.ico$',
        r'googledb051dc4bdb1fec0\.html'  # Google verification file
    ]
    
    for pattern in exclude_patterns:
        if re.search(pattern, file_path, re.IGNORECASE):
            return False
    
    return True

def normalize_url(path):
    """Normalize URL path to avoid duplicates"""
    # Remove index.html from paths
    if path.endswith('/index.html'):
        path = path[:-10]  # Remove index.html but keep trailing slash
    
    # Ensure trailing slash for directories
    if not path.endswith('.html') and not path.endswith('/'):
        path += '/'
    
    return path

def collect_urls():
    """Collect all URLs to include in sitemap"""
    urls = []
    seen_urls = set()
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip hidden directories and special directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]
        
        for file in files:
            if file.endswith('.html') and should_include_file(file):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, BASE_DIR)
                
                # Convert to URL path
                url_path = '/' + relative_path.replace('\\', '/')
                url_path = normalize_url(url_path)
                
                # Skip if we've already seen this URL
                full_url = BASE_URL + url_path
                if full_url in seen_urls:
                    continue
                
                seen_urls.add(full_url)
                
                # Get modification time
                mtime = os.path.getmtime(full_path)
                lastmod = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
                
                # Get priority
                priority = get_priority(url_path)
                
                urls.append({
                    'loc': full_url,
                    'lastmod': lastmod,
                    'priority': priority
                })
    
    # Sort URLs by priority (highest first) then alphabetically
    urls.sort(key=lambda x: (-x['priority'], x['loc']))
    
    return urls

def generate_sitemap():
    """Generate the sitemap.xml file"""
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Collect all URLs
    urls = collect_urls()
    
    # Add each URL to sitemap
    for url_data in urls:
        url_elem = ET.SubElement(urlset, 'url')
        
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = url_data['loc']
        
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = url_data['lastmod']
        
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = str(url_data['priority'])
    
    # Create tree and write to file
    tree = ET.ElementTree(urlset)
    
    # Pretty print the XML
    import xml.dom.minidom as minidom
    xml_str = ET.tostring(urlset, encoding='unicode')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent='  ', encoding='UTF-8')
    
    # Remove extra blank lines
    lines = pretty_xml.decode('utf-8').split('\n')
    lines = [line for line in lines if line.strip()]
    pretty_xml = '\n'.join(lines)
    
    # Write to file
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"Sitemap generated successfully!")
    print(f"Total URLs: {len(urls)}")
    print(f"Saved to: {sitemap_path}")
    
    # Print summary by category
    categories = {
        'Homepage': 0,
        'Services': 0,
        'Practice Areas': 0,
        'City Pages': 0,
        'Location Pages': 0,
        'Other': 0
    }
    
    for url_data in urls:
        url = url_data['loc']
        if url.endswith('skerritteconomics.com/'):
            categories['Homepage'] += 1
        elif '/services/' in url:
            categories['Services'] += 1
        elif '/practice-areas/' in url:
            categories['Practice Areas'] += 1
        elif '/locations/cities/' in url:
            categories['City Pages'] += 1
        elif '/locations/' in url:
            categories['Location Pages'] += 1
        else:
            categories['Other'] += 1
    
    print("\nURL Summary by Category:")
    for category, count in categories.items():
        print(f"  {category}: {count}")

if __name__ == "__main__":
    generate_sitemap()