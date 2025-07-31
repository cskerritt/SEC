#!/usr/bin/env python3
"""
Web-based Sitemap Review System
Provides a browser interface for reviewing pages and adding notes
"""

import xml.etree.ElementTree as ET
import json
import os
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template_string, request, jsonify, send_file
import webbrowser
from threading import Timer
from urllib.parse import urlparse

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
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
        button:disabled {
            background: #9ca3af;
            cursor: not-allowed;
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
        .note-actions {
            display: flex;
            gap: 5px;
            margin-top: 5px;
        }
        .note-btn {
            padding: 4px 8px;
            font-size: 12px;
            border-radius: 4px;
        }
        .save-btn {
            background: #059669;
        }
        .save-btn:hover {
            background: #047857;
        }
        .cancel-btn {
            background: #ef4444;
        }
        .cancel-btn:hover {
            background: #dc2626;
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
        .existing-note {
            background: #fef3c7;
            padding: 6px 10px;
            border-radius: 4px;
            font-size: 13px;
            margin-bottom: 5px;
        }
        .preview-link {
            color: #1e3a8a;
            text-decoration: none;
            font-size: 12px;
        }
        .preview-link:hover {
            text-decoration: underline;
        }
        #loading {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sitemap Review System</h1>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-value" id="totalPages">0</div>
                <div class="stat-label">Total Pages</div>
            </div>
            <div class="stat">
                <div class="stat-value" id="reviewedPages">0</div>
                <div class="stat-label">Pages with Notes</div>
            </div>
            <div class="stat">
                <div class="stat-value" id="currentFilter">all</div>
                <div class="stat-label">Current Filter</div>
            </div>
        </div>
        
        <div class="controls">
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Search by URL or path..." />
            </div>
            <button onclick="exportMarkdown()">Export to Markdown</button>
            <button onclick="saveNotes()">Save All Notes</button>
        </div>
        
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterPages('all')">All</button>
            <button class="filter-btn" onclick="filterPages('city')">Cities</button>
            <button class="filter-btn" onclick="filterPages('state')">States</button>
            <button class="filter-btn" onclick="filterPages('service')">Services</button>
            <button class="filter-btn" onclick="filterPages('practice-area')">Practice Areas</button>
            <button class="filter-btn" onclick="filterPages('blog')">Blog</button>
            <button class="filter-btn" onclick="filterPages('other')">Other</button>
            <button class="filter-btn" onclick="filterPages('with-notes')">With Notes</button>
            <button class="filter-btn" onclick="filterPages('without-notes')">Without Notes</button>
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
                <!-- Pages will be loaded here -->
            </tbody>
        </table>
        
        <div class="pagination">
            <button id="prevBtn" onclick="changePage(-1)">← Previous</button>
            <span class="page-info" id="pageInfo">Page 1 of 1</span>
            <button id="nextBtn" onclick="changePage(1)">Next →</button>
        </div>
    </div>
    
    <div id="loading">Loading...</div>
    
    <script>
        let allPages = [];
        let filteredPages = [];
        let currentPage = 1;
        let pageSize = 20;
        let currentFilter = 'all';
        let notes = {};
        
        async function loadPages() {
            document.getElementById('loading').style.display = 'block';
            try {
                const response = await fetch('/api/pages');
                const data = await response.json();
                allPages = data.pages;
                notes = data.notes;
                filterPages('all');
                updateStats();
            } finally {
                document.getElementById('loading').style.display = 'none';
            }
        }
        
        function updateStats() {
            document.getElementById('totalPages').textContent = allPages.length;
            document.getElementById('reviewedPages').textContent = Object.keys(notes).length;
            document.getElementById('currentFilter').textContent = currentFilter;
        }
        
        function filterPages(filter) {
            currentFilter = filter;
            currentPage = 1;
            
            // Update active button
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');
            
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
            
            // Apply search if active
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            if (searchTerm) {
                filteredPages = filteredPages.filter(p => 
                    p.url.toLowerCase().includes(searchTerm) || 
                    p.path.toLowerCase().includes(searchTerm)
                );
            }
            
            displayPages();
            updateStats();
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
                        <div id="note-container-${i}">
                            ${note ? `<div class="existing-note">${note}</div>` : ''}
                            <input type="text" 
                                   class="note-input" 
                                   id="note-${i}" 
                                   value="${note}"
                                   placeholder="Add note..." 
                                   onkeypress="if(event.key==='Enter') saveNote(${i})"
                            />
                            <div class="note-actions">
                                <button class="note-btn save-btn" onclick="saveNote(${i})">Save</button>
                                <button class="note-btn cancel-btn" onclick="cancelNote(${i})">Cancel</button>
                            </div>
                        </div>
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
        
        async function saveNote(index) {
            const page = filteredPages[index];
            const noteValue = document.getElementById(`note-${index}`).value;
            
            const response = await fetch('/api/note', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    url: page.url,
                    note: noteValue
                })
            });
            
            if (response.ok) {
                notes[page.url] = noteValue;
                displayPages();
                updateStats();
            }
        }
        
        function cancelNote(index) {
            const page = filteredPages[index];
            const originalNote = notes[page.url] || '';
            document.getElementById(`note-${index}`).value = originalNote;
        }
        
        async function saveNotes() {
            const response = await fetch('/api/save');
            if (response.ok) {
                alert('Notes saved successfully!');
            }
        }
        
        async function exportMarkdown() {
            window.location.href = '/api/export';
        }
        
        // Search functionality
        document.addEventListener('DOMContentLoaded', () => {
            const searchInput = document.getElementById('searchInput');
            let searchTimeout;
            
            searchInput.addEventListener('input', (e) => {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    filterPages(currentFilter);
                }, 300);
            });
            
            loadPages();
        });
    </script>
</body>
</html>
'''

class WebSitemapReviewer:
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
    
    def save_notes(self):
        """Save notes to file"""
        with open(self.notes_file, 'w') as f:
            json.dump(self.notes, f, indent=2)
    
    def export_to_markdown(self):
        """Export notes to markdown"""
        output_file = f'sitemap_review_{datetime.now().strftime("%Y%m%d_%H%M%S")}.md'
        
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
                        f.write(f"- **Note**: {self.notes[page['url']]}\n\n")
        
        return output_file

# Global reviewer instance
reviewer = None

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/pages')
def get_pages():
    return jsonify({
        'pages': reviewer.pages,
        'notes': reviewer.notes
    })

@app.route('/api/note', methods=['POST'])
def save_note():
    data = request.json
    url = data.get('url')
    note = data.get('note')
    
    if note:
        reviewer.notes[url] = note
    elif url in reviewer.notes:
        del reviewer.notes[url]
    
    return jsonify({'success': True})

@app.route('/api/save')
def save_all():
    reviewer.save_notes()
    return jsonify({'success': True})

@app.route('/api/export')
def export():
    filename = reviewer.export_to_markdown()
    return send_file(filename, as_attachment=True)

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

def main():
    global reviewer
    reviewer = WebSitemapReviewer()
    
    # Open browser after a short delay
    Timer(1.5, open_browser).start()
    
    # Run Flask app
    print("Starting web interface at http://127.0.0.1:5000/")
    app.run(debug=False, port=5000)

if __name__ == '__main__':
    main()