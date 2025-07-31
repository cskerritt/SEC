#!/usr/bin/env python3
"""
Interactive Sitemap Review System
Allows reviewing all pages in sitemap, adding notes, and exporting to markdown
"""

import xml.etree.ElementTree as ET
import os
import json
import re
from datetime import datetime
from pathlib import Path
import webbrowser
from urllib.parse import urlparse

class SitemapReviewer:
    def __init__(self, sitemap_path, notes_file='sitemap_review_notes.json'):
        self.sitemap_path = sitemap_path
        self.notes_file = notes_file
        self.pages = []
        self.notes = {}
        self.current_index = 0
        self.page_size = 10
        
        # Load existing notes if available
        self.load_notes()
        
        # Parse sitemap
        self.parse_sitemap()
    
    def parse_sitemap(self):
        """Parse the sitemap XML file"""
        try:
            tree = ET.parse(self.sitemap_path)
            root = tree.getroot()
            
            # Handle namespace
            ns = {'ns0': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            
            # Extract all URLs
            for url_elem in root.findall('.//ns0:url', ns):
                loc = url_elem.find('ns0:loc', ns)
                lastmod = url_elem.find('ns0:lastmod', ns)
                priority = url_elem.find('ns0:priority', ns)
                
                if loc is not None:
                    url = loc.text
                    page_info = {
                        'url': url,
                        'lastmod': lastmod.text if lastmod is not None else 'N/A',
                        'priority': priority.text if priority is not None else 'N/A',
                        'path': self.extract_path(url),
                        'type': self.categorize_page(url)
                    }
                    self.pages.append(page_info)
            
            print(f"Loaded {len(self.pages)} pages from sitemap")
            
        except Exception as e:
            print(f"Error parsing sitemap: {e}")
    
    def extract_path(self, url):
        """Extract the path from URL"""
        parsed = urlparse(url)
        return parsed.path
    
    def categorize_page(self, url):
        """Categorize page type based on URL"""
        path = url.lower()
        
        if '/locations/cities/' in path:
            return 'city'
        elif '/locations/' in path:
            return 'state'
        elif '/services/' in path:
            return 'service'
        elif '/practice-areas/' in path:
            return 'practice-area'
        elif '/blog/' in path:
            return 'blog'
        elif '/case-studies/' in path:
            return 'case-study'
        elif '/about' in path:
            return 'about'
        elif '/contact' in path:
            return 'contact'
        elif path.endswith('/'):
            return 'index'
        else:
            return 'other'
    
    def load_notes(self):
        """Load existing notes from JSON file"""
        if os.path.exists(self.notes_file):
            try:
                with open(self.notes_file, 'r') as f:
                    self.notes = json.load(f)
                print(f"Loaded existing notes for {len(self.notes)} pages")
            except:
                self.notes = {}
    
    def save_notes(self):
        """Save notes to JSON file"""
        with open(self.notes_file, 'w') as f:
            json.dump(self.notes, f, indent=2)
        print(f"Notes saved to {self.notes_file}")
    
    def display_page(self, page):
        """Display a single page's information"""
        print("\n" + "="*80)
        print(f"Page {self.pages.index(page) + 1} of {len(self.pages)}")
        print("="*80)
        print(f"URL: {page['url']}")
        print(f"Path: {page['path']}")
        print(f"Type: {page['type']}")
        print(f"Last Modified: {page['lastmod']}")
        print(f"Priority: {page['priority']}")
        
        # Show existing note if any
        if page['url'] in self.notes:
            print(f"\nExisting Note: {self.notes[page['url']]}")
        else:
            print("\nNo notes for this page yet.")
    
    def display_page_batch(self, start_idx):
        """Display a batch of pages"""
        end_idx = min(start_idx + self.page_size, len(self.pages))
        
        print("\n" + "="*100)
        print(f"Pages {start_idx + 1} to {end_idx} of {len(self.pages)}")
        print("="*100)
        print(f"{'#':<4} {'Type':<15} {'Path':<50} {'Note':<30}")
        print("-"*100)
        
        for i in range(start_idx, end_idx):
            page = self.pages[i]
            note = self.notes.get(page['url'], '')
            if len(note) > 27:
                note = note[:27] + '...'
            
            print(f"{i+1:<4} {page['type']:<15} {page['path']:<50} {note:<30}")
    
    def add_note(self, page_index, note):
        """Add or update note for a page"""
        if 0 <= page_index < len(self.pages):
            page = self.pages[page_index]
            self.notes[page['url']] = note
            print(f"Note added for: {page['path']}")
    
    def export_to_markdown(self, output_file='sitemap_review.md'):
        """Export all notes to a markdown file"""
        with open(output_file, 'w') as f:
            f.write("# Sitemap Review Notes\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total Pages: {len(self.pages)}\n")
            f.write(f"Pages with Notes: {len(self.notes)}\n\n")
            
            # Group pages by type
            pages_by_type = {}
            for page in self.pages:
                page_type = page['type']
                if page_type not in pages_by_type:
                    pages_by_type[page_type] = []
                pages_by_type[page_type].append(page)
            
            # Write sections by type
            for page_type, pages in sorted(pages_by_type.items()):
                f.write(f"## {page_type.title().replace('-', ' ')} Pages\n\n")
                
                # Count pages with notes
                with_notes = sum(1 for p in pages if p['url'] in self.notes)
                f.write(f"Total: {len(pages)} | With Notes: {with_notes}\n\n")
                
                # List pages with notes
                for page in pages:
                    if page['url'] in self.notes:
                        f.write(f"### {page['path']}\n")
                        f.write(f"- **URL**: {page['url']}\n")
                        f.write(f"- **Last Modified**: {page['lastmod']}\n")
                        f.write(f"- **Note**: {self.notes[page['url']]}\n\n")
                
                # Summary of pages without notes
                without_notes = [p for p in pages if p['url'] not in self.notes]
                if without_notes:
                    f.write(f"\n**Pages without notes ({len(without_notes)}):**\n")
                    for page in without_notes[:10]:  # Show first 10
                        f.write(f"- {page['path']}\n")
                    if len(without_notes) > 10:
                        f.write(f"- ... and {len(without_notes) - 10} more\n")
                
                f.write("\n")
        
        print(f"Review exported to {output_file}")
    
    def search_pages(self, query):
        """Search for pages by URL or path"""
        results = []
        query_lower = query.lower()
        
        for i, page in enumerate(self.pages):
            if query_lower in page['url'].lower() or query_lower in page['path'].lower():
                results.append((i, page))
        
        return results
    
    def run_interactive(self):
        """Run the interactive review interface"""
        print("\nSitemap Review System")
        print("====================")
        print(f"Total pages: {len(self.pages)}")
        print(f"Pages with notes: {len(self.notes)}")
        
        while True:
            print("\n" + "-"*50)
            print("Commands:")
            print("  l    - List current page batch")
            print("  n    - Next page batch")
            print("  p    - Previous page batch")
            print("  g #  - Go to page number")
            print("  a # 'note' - Add note to page number")
            print("  s 'query' - Search pages")
            print("  e    - Export to markdown")
            print("  save - Save notes")
            print("  q    - Quit")
            print("-"*50)
            
            cmd = input("\nCommand: ").strip()
            
            if cmd == 'q':
                self.save_notes()
                break
            
            elif cmd == 'l':
                self.display_page_batch(self.current_index)
            
            elif cmd == 'n':
                if self.current_index + self.page_size < len(self.pages):
                    self.current_index += self.page_size
                    self.display_page_batch(self.current_index)
                else:
                    print("Already at the last page batch")
            
            elif cmd == 'p':
                if self.current_index - self.page_size >= 0:
                    self.current_index -= self.page_size
                    self.display_page_batch(self.current_index)
                else:
                    print("Already at the first page batch")
            
            elif cmd.startswith('g '):
                try:
                    page_num = int(cmd[2:]) - 1
                    if 0 <= page_num < len(self.pages):
                        self.current_index = (page_num // self.page_size) * self.page_size
                        self.display_page_batch(self.current_index)
                        self.display_page(self.pages[page_num])
                    else:
                        print(f"Invalid page number. Must be between 1 and {len(self.pages)}")
                except ValueError:
                    print("Invalid page number")
            
            elif cmd.startswith('a '):
                parts = cmd[2:].split(' ', 1)
                if len(parts) == 2:
                    try:
                        page_num = int(parts[0]) - 1
                        note = parts[1].strip('"\'')
                        self.add_note(page_num, note)
                    except ValueError:
                        print("Invalid page number")
                else:
                    print("Usage: a # 'note text'")
            
            elif cmd.startswith('s '):
                query = cmd[2:].strip('"\'')
                results = self.search_pages(query)
                if results:
                    print(f"\nFound {len(results)} matching pages:")
                    for i, (idx, page) in enumerate(results[:20]):
                        note = self.notes.get(page['url'], '')
                        if note:
                            note = f" - {note[:40]}..."
                        print(f"{idx+1}: {page['path']}{note}")
                    if len(results) > 20:
                        print(f"... and {len(results) - 20} more")
                else:
                    print("No matching pages found")
            
            elif cmd == 'e':
                self.export_to_markdown()
            
            elif cmd == 'save':
                self.save_notes()
            
            else:
                print("Unknown command. Type 'q' to quit.")

def main():
    # Initialize the reviewer
    reviewer = SitemapReviewer('sitemap.xml')
    
    # Run interactive mode
    reviewer.run_interactive()

if __name__ == '__main__':
    main()