#!/usr/bin/env python3
"""
Generate an HTML-based sitemap review interface
No external dependencies required
"""

import xml.etree.ElementTree as ET
import json
import os
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import webbrowser

class HTMLSitemapReviewer:
    def __init__(self, sitemap_path='sitemap.xml'):
        self.sitemap_path = sitemap_path
        self.notes_file = 'sitemap_review_notes.json'
        self.pages = []
        self.notes = {}
        
        # Load data
        self.parse_sitemap()
        self.load_notes()
    
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
                        'path': urlparse(url).path,
                        'type': self.categorize_page(url)
                    }
                    self.pages.append(page_info)
            
            print(f"Loaded {len(self.pages)} pages from sitemap")
            
        except Exception as e:
            print(f"Error parsing sitemap: {e}")
    
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
        """Load existing notes"""
        if os.path.exists(self.notes_file):
            try:
                with open(self.notes_file, 'r') as f:
                    self.notes = json.load(f)
            except:
                self.notes = {}
    
    def generate_html(self):
        """Generate the HTML review interface"""
        html = '''<!DOCTYPE html>
<html>
<head>
    <title>Sitemap Review System</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #1e3a8a;
            margin-bottom: 20px;
        }
        .stats {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
            padding: 15px;
            background: #f9fafb;
            border-radius: 6px;
        }
        .stat {
            flex: 1;
        }
        .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #1e3a8a;
        }
        .stat-label {
            color: #6b7280;
            font-size: 14px;
        }
        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            align-items: center;
        }
        .search-box {
            flex: 1;
            min-width: 300px;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #e5e7eb;
            border-radius: 6px;
            font-size: 14px;
        }
        button {
            padding: 8px 16px;
            background: #1e3a8a;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: background 0.2s;
        }
        button:hover {
            background: #1e40af;
        }
        .filter-buttons {
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }
        .filter-btn {
            padding: 6px 12px;
            background: #e5e7eb;
            color: #374151;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }
        .filter-btn:hover {
            background: #d1d5db;
        }
        .filter-btn.active {
            background: #1e3a8a;
            color: white;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th {
            background: #f9fafb;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            color: #374151;
            border-bottom: 2px solid #e5e7eb;
            position: sticky;
            top: 0;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #e5e7eb;
        }
        tr:hover {
            background: #f9fafb;
        }
        .page-type {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 500;
        }
        .type-city { background: #dbeafe; color: #1e40af; }
        .type-state { background: #e0e7ff; color: #3730a3; }
        .type-service { background: #fce7f3; color: #be185d; }
        .type-practice-area { background: #f3e8ff; color: #7c3aed; }
        .type-blog { background: #fed7aa; color: #c2410c; }
        .type-index { background: #d1fae5; color: #065f46; }
        .type-other { background: #e5e7eb; color: #374151; }
        .note-input {
            width: 100%;
            min-width: 200px;
            padding: 6px 10px;
            border: 1px solid #e5e7eb;
            border-radius: 4px;
            font-size: 13px;
        }
        .pagination {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            margin-top: 20px;
            padding: 20px 0;
        }
        .page-info {
            color: #6b7280;
            font-size: 14px;
        }
        .preview-link {
            color: #1e3a8a;
            text-decoration: none;
            font-size: 12px;
        }
        .preview-link:hover {
            text-decoration: underline;
        }
        .save-notice {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #059669;
            color: white;
            padding: 12px 20px;
            border-radius: 6px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sitemap Review System</h1>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-value">''' + str(len(self.pages)) + '''</div>
                <div class="stat-label">Total Pages</div>
            </div>
            <div class="stat">
                <div class="stat-value">''' + str(len(self.notes)) + '''</div>
                <div class="stat-label">Pages with Notes</div>
            </div>
            <div class="stat">
                <div class="stat-value" id="currentFilter">all</div>
                <div class="stat-label">Current Filter</div>
            </div>
        </div>
        
        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Search by URL or path..." onkeyup="searchPages()" />
            </div>
            <button onclick="saveNotes()">Save All Notes</button>
            <button onclick="exportMarkdown()">Export to Markdown</button>
        </div>
        
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterPages('all', this)">All</button>
            <button class="filter-btn" onclick="filterPages('city', this)">Cities</button>
            <button class="filter-btn" onclick="filterPages('state', this)">States</button>
            <button class="filter-btn" onclick="filterPages('service', this)">Services</button>
            <button class="filter-btn" onclick="filterPages('practice-area', this)">Practice Areas</button>
            <button class="filter-btn" onclick="filterPages('blog', this)">Blog</button>
            <button class="filter-btn" onclick="filterPages('other', this)">Other</button>
            <button class="filter-btn" onclick="filterPages('with-notes', this)">With Notes</button>
            <button class="filter-btn" onclick="filterPages('without-notes', this)">Without Notes</button>
        </div>
        
        <table id="pagesTable">
            <thead>
                <tr>
                    <th width="5%">#</th>
                    <th width="10%">Type</th>
                    <th width="35%">Path</th>
                    <th width="40%">Notes</th>
                    <th width="10%">Actions</th>
                </tr>
            </thead>
            <tbody id="pagesBody">
            </tbody>
        </table>
        
        <div class="pagination">
            <button onclick="changePage(-1)" id="prevBtn">← Previous</button>
            <span class="page-info" id="pageInfo">Page 1 of 1</span>
            <button onclick="changePage(1)" id="nextBtn">Next →</button>
        </div>
    </div>
    
    <div class="save-notice" id="saveNotice">Notes saved!</div>
    
    <script>
        // Page data
        const allPages = ''' + json.dumps(self.pages) + ''';
        let notes = ''' + json.dumps(self.notes) + ''';
        let filteredPages = [...allPages];
        let currentPage = 1;
        const pageSize = 20;
        let currentFilter = 'all';
        
        function filterPages(filter, btn) {
            currentFilter = filter;
            currentPage = 1;
            
            // Update active button
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById('currentFilter').textContent = filter;
            
            // Apply filter
            if (filter === 'all') {
                filteredPages = [...allPages];
            } else if (filter === 'with-notes') {
                filteredPages = allPages.filter(p => notes[p.url]);
            } else if (filter === 'without-notes') {
                filteredPages = allPages.filter(p => !notes[p.url]);
            } else {
                filteredPages = allPages.filter(p => p.type === filter);
            }
            
            // Apply search
            searchPages();
        }
        
        function searchPages() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            
            if (searchTerm) {
                filteredPages = filteredPages.filter(p => 
                    p.url.toLowerCase().includes(searchTerm) || 
                    p.path.toLowerCase().includes(searchTerm)
                );
            } else {
                // Re-apply current filter
                filterPages(currentFilter, document.querySelector('.filter-btn.active'));
                return;
            }
            
            currentPage = 1;
            displayPages();
        }
        
        function displayPages() {
            const tbody = document.getElementById('pagesBody');
            tbody.innerHTML = '';
            
            const start = (currentPage - 1) * pageSize;
            const end = Math.min(start + pageSize, filteredPages.length);
            
            for (let i = start; i < end; i++) {
                const page = filteredPages[i];
                const globalIndex = allPages.indexOf(page);
                const note = notes[page.url] || '';
                
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${globalIndex + 1}</td>
                    <td><span class="page-type type-${page.type}">${page.type}</span></td>
                    <td>
                        ${page.path}
                        <br>
                        <a href="${page.url}" target="_blank" class="preview-link">Preview ↗</a>
                    </td>
                    <td>
                        <input type="text" 
                               class="note-input" 
                               id="note-${globalIndex}" 
                               value="${note}"
                               placeholder="Add note..." 
                               onchange="updateNote(${globalIndex}, this.value)"
                        />
                    </td>
                    <td>
                        <a href="${page.url}" target="_blank">View</a>
                    </td>
                `;
                tbody.appendChild(row);
            }
            
            // Update pagination
            const totalPages = Math.ceil(filteredPages.length / pageSize);
            document.getElementById('pageInfo').textContent = 
                `Page ${currentPage} of ${totalPages} (${filteredPages.length} items)`;
            document.getElementById('prevBtn').disabled = currentPage === 1;
            document.getElementById('nextBtn').disabled = currentPage === totalPages;
        }
        
        function changePage(delta) {
            const totalPages = Math.ceil(filteredPages.length / pageSize);
            currentPage = Math.max(1, Math.min(currentPage + delta, totalPages));
            displayPages();
            window.scrollTo(0, 0);
        }
        
        function updateNote(index, value) {
            const page = allPages[index];
            if (value) {
                notes[page.url] = value;
            } else {
                delete notes[page.url];
            }
            
            // Update stats
            document.querySelector('.stats .stat:nth-child(2) .stat-value').textContent = 
                Object.keys(notes).length;
        }
        
        function saveNotes() {
            // Create a download link for the notes JSON
            const dataStr = JSON.stringify(notes, null, 2);
            const dataBlob = new Blob([dataStr], {type: 'application/json'});
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'sitemap_review_notes.json';
            link.click();
            
            // Show save notice
            const notice = document.getElementById('saveNotice');
            notice.style.display = 'block';
            setTimeout(() => { notice.style.display = 'none'; }, 2000);
        }
        
        function exportMarkdown() {
            let markdown = '# Sitemap Review Notes\\n\\n';
            markdown += `Generated: ${new Date().toISOString()}\\n\\n`;
            markdown += `Total Pages: ${allPages.length}\\n`;
            markdown += `Pages with Notes: ${Object.keys(notes).length}\\n\\n`;
            
            // Group by type
            const pagesByType = {};
            allPages.forEach(page => {
                if (!pagesByType[page.type]) pagesByType[page.type] = [];
                pagesByType[page.type].push(page);
            });
            
            // Write sections
            Object.entries(pagesByType).sort().forEach(([type, pages]) => {
                markdown += `## ${type.charAt(0).toUpperCase() + type.slice(1).replace('-', ' ')} Pages\\n\\n`;
                
                const withNotes = pages.filter(p => notes[p.url]);
                markdown += `Total: ${pages.length} | With Notes: ${withNotes.length}\\n\\n`;
                
                withNotes.forEach(page => {
                    markdown += `### ${page.path}\\n`;
                    markdown += `- **URL**: ${page.url}\\n`;
                    markdown += `- **Note**: ${notes[page.url]}\\n\\n`;
                });
                
                markdown += '\\n';
            });
            
            // Download markdown
            const blob = new Blob([markdown], {type: 'text/markdown'});
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `sitemap_review_${new Date().toISOString().split('T')[0]}.md`;
            link.click();
        }
        
        // Initialize
        displayPages();
    </script>
</body>
</html>'''
        
        return html
    
    def generate_review_interface(self):
        """Generate and open the HTML review interface"""
        html = self.generate_html()
        
        # Save to file
        output_file = 'sitemap_review.html'
        with open(output_file, 'w') as f:
            f.write(html)
        
        print(f"Generated review interface: {output_file}")
        
        # Open in browser
        webbrowser.open(f'file://{os.path.abspath(output_file)}')
        
        return output_file

def main():
    # Create reviewer
    reviewer = HTMLSitemapReviewer()
    
    # Generate and open interface
    reviewer.generate_review_interface()
    
    print("\nReview interface opened in your browser!")
    print("- Add notes directly in the interface")
    print("- Click 'Save All Notes' to download notes as JSON")
    print("- Click 'Export to Markdown' to generate a report")
    print("\nNote: To persist notes between sessions, save the JSON and place it")
    print("in the same directory as 'sitemap_review_notes.json'")

if __name__ == '__main__':
    main()