#!/usr/bin/env python3
"""
Generate RSS feed for blog posts
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from html.parser import HTMLParser
import re

class PostParser(HTMLParser):
    """Parse blog post HTML to extract metadata"""
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.in_p = False
        self.title = ""
        self.heading = ""
        self.description = ""
        self.paragraphs = []
        
    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "p" and len(self.paragraphs) < 3:
            self.in_p = True
            
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
        elif tag == "p":
            self.in_p = False
            
    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1 and not self.heading:
            self.heading += data
        elif self.in_p:
            self.paragraphs.append(data.strip())

def clean_text(text):
    """Clean text for XML"""
    # Remove multiple spaces and newlines
    text = re.sub(r'\s+', ' ', text)
    # Remove HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    return text.strip()

def get_post_date(filepath):
    """Extract date from file path"""
    # Path format: blog/2025/01/post-name.html
    parts = filepath.split('/')
    if len(parts) >= 4:
        try:
            year = int(parts[-3])
            month = int(parts[-2])
            # Assign a day based on filename to spread posts
            filename = parts[-1].replace('.html', '')
            day = (hash(filename) % 28) + 1  # Days 1-28
            return datetime(year, month, day)
        except:
            pass
    return datetime.now()

def parse_blog_post(filepath):
    """Parse a blog post HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = PostParser()
    parser.feed(content)
    
    # Extract clean title
    title = parser.heading or parser.title
    title = title.replace(' | Skerritt Economics', '')
    title = clean_text(title)
    
    # Get description from first meaningful paragraph
    description = ""
    for p in parser.paragraphs:
        cleaned = clean_text(p)
        if len(cleaned) > 50 and not cleaned.startswith('Posted on'):
            description = cleaned
            if len(description) > 300:
                description = description[:297] + "..."
            break
    
    return {
        'title': title,
        'description': description,
        'date': get_post_date(filepath)
    }

# Create RSS root
rss = ET.Element('rss', version='2.0')
rss.set('xmlns:atom', 'http://www.w3.org/2005/Atom')

# Create channel
channel = ET.SubElement(rss, 'channel')

# Channel metadata
title = ET.SubElement(channel, 'title')
title.text = 'Skerritt Economics Blog'

link = ET.SubElement(channel, 'link')
link.text = 'https://skerritteconomics.com/blog/'

description = ET.SubElement(channel, 'description')
description.text = 'Expert insights on forensic economics, business valuation, vocational assessment, and life care planning from Skerritt Economics & Consulting.'

language = ET.SubElement(channel, 'language')
language.text = 'en-us'

# Self link
atom_link = ET.SubElement(channel, 'atom:link')
atom_link.set('href', 'https://skerritteconomics.com/blog/rss.xml')
atom_link.set('rel', 'self')
atom_link.set('type', 'application/rss+xml')

# Last build date
lastBuildDate = ET.SubElement(channel, 'lastBuildDate')
lastBuildDate.text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')

# Find all blog posts
blog_posts = []
blog_dir = '/Users/chrisskerritt/SEC/blog'

for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file.endswith('.html') and file != 'index.html':
            filepath = os.path.join(root, file)
            if '/2025/' in filepath:  # Only process dated posts
                blog_posts.append(filepath)

# Sort by date (newest first)
blog_posts.sort(reverse=True)

# Process each post
for post_path in blog_posts:
    try:
        post_data = parse_blog_post(post_path)
        
        # Create item
        item = ET.SubElement(channel, 'item')
        
        # Title
        item_title = ET.SubElement(item, 'title')
        item_title.text = post_data['title']
        
        # Link
        item_link = ET.SubElement(item, 'link')
        relative_path = post_path.replace('/Users/chrisskerritt/SEC/', '')
        item_link.text = f'https://skerritteconomics.com/{relative_path}'
        
        # Description
        item_desc = ET.SubElement(item, 'description')
        item_desc.text = post_data['description']
        
        # Pub date
        pubDate = ET.SubElement(item, 'pubDate')
        pubDate.text = post_data['date'].strftime('%a, %d %b %Y %H:%M:%S GMT')
        
        # GUID
        guid = ET.SubElement(item, 'guid')
        guid.text = item_link.text
        guid.set('isPermaLink', 'true')
        
    except Exception as e:
        print(f"Error processing {post_path}: {e}")

# Format the XML
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

indent(rss)

# Write RSS feed
tree = ET.ElementTree(rss)
output_path = '/Users/chrisskerritt/SEC/blog/rss.xml'
tree.write(output_path, encoding='UTF-8', xml_declaration=True)

print(f"RSS feed generated with {len(blog_posts)} posts")
print(f"Saved to: {output_path}")