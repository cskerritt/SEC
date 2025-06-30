#!/usr/bin/env python3
import os
import glob
import re
import json

def generate_city_data():
    """Generate complete city data for the review tool"""
    cities_dir = "/Users/chrisskerritt/SEC/locations/cities"
    city_files = glob.glob(os.path.join(cities_dir, "*-forensic-economist.html"))
    city_files.sort()
    
    all_pages = []
    
    for file_path in city_files:
        filename = os.path.basename(file_path)
        # Remove the .html extension and -forensic-economist suffix
        base_name = filename.replace('.html', '').replace('-forensic-economist', '')
        
        # Split by hyphens and get state (last part)
        parts = base_name.split('-')
        if len(parts) >= 2:
            state = parts[-1].upper()
            city_parts = parts[:-1]
            
            # Convert city name parts to proper case
            city_name = ' '.join([part.capitalize() for part in city_parts])
            
            # Special handling for certain city names
            city_name = city_name.replace(' City', ' City')
            city_name = city_name.replace(' Falls', ' Falls')
            city_name = city_name.replace(' Springs', ' Springs')
            city_name = city_name.replace(' Beach', ' Beach')
            city_name = city_name.replace(' Island', ' Island')
            city_name = city_name.replace(' Park', ' Park')
            city_name = city_name.replace(' Heights', ' Heights')
            city_name = city_name.replace(' Lake', ' Lake')
            city_name = city_name.replace(' Valley', ' Valley')
            city_name = city_name.replace(' Ridge', ' Ridge')
            city_name = city_name.replace(' Point', ' Point')
            city_name = city_name.replace(' Hills', ' Hills')
            city_name = city_name.replace(' Town', ' Town')
            
            # Handle special cases
            if 'saint-' in base_name or 'st-' in base_name:
                city_name = city_name.replace('Saint ', 'St. ')
                city_name = city_name.replace('St ', 'St. ')
            
            if 'new-' in base_name:
                city_name = city_name.replace('New ', 'New ')
            
            if 'north-' in base_name:
                city_name = city_name.replace('North ', 'North ')
                
            if 'south-' in base_name:
                city_name = city_name.replace('South ', 'South ')
                
            if 'east-' in base_name:
                city_name = city_name.replace('East ', 'East ')
                
            if 'west-' in base_name:
                city_name = city_name.replace('West ', 'West ')
            
            relative_path = f"locations/cities/{filename}"
            
            all_pages.append({
                "name": f"{city_name}, {state}",
                "file": relative_path,
                "state": state
            })
    
    return all_pages

def create_complete_review_tool():
    """Create a complete review tool with all city data embedded"""
    
    all_pages = generate_city_data()
    
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>City Pages Review Tool - Complete</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
            font-size: 14px;
        }
        .stat-item {
            background: #e9ecef;
            padding: 8px 16px;
            border-radius: 4px;
        }
        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 5px;
        }
        .nav-controls {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        button {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }
        .btn-primary {
            background: #007bff;
            color: white;
        }
        .btn-primary:hover {
            background: #0056b3;
        }
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
        .btn-secondary:hover {
            background: #545b62;
        }
        .btn-success {
            background: #28a745;
            color: white;
        }
        .btn-success:hover {
            background: #1e7e34;
        }
        .btn-warning {
            background: #ffc107;
            color: #212529;
        }
        .btn-warning:hover {
            background: #e0a800;
        }
        .page-info {
            font-weight: bold;
            color: #495057;
        }
        .current-page {
            width: 100%;
            height: 700px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .page-list {
            margin-top: 20px;
            max-height: 300px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 10px;
        }
        .page-item {
            padding: 8px 12px;
            cursor: pointer;
            border-radius: 3px;
            margin: 2px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .page-item:hover {
            background: #e9ecef;
        }
        .page-item.active {
            background: #007bff;
            color: white;
        }
        .search-box {
            width: 200px;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .filter-controls {
            margin-bottom: 15px;
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
        }
        select {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .status-indicators {
            display: flex;
            gap: 15px;
            margin-left: auto;
        }
        .status-item {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 12px;
        }
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .status-reviewing { background: #ffc107; }
        .status-approved { background: #28a745; }
        .status-needs-fix { background: #dc3545; }
        .keyboard-help {
            margin-top: 10px;
            font-size: 12px;
            color: #6c757d;
            text-align: center;
        }
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #28a745, #20c997);
            transition: width 0.3s ease;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>City Pages Review Tool</h1>
            <p>Review and navigate through all {total_pages} forensic economist city pages</p>
            <div class="progress-bar">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="stats">
                <div class="stat-item">Total: <span id="totalPages">{total_pages}</span></div>
                <div class="stat-item">Reviewed: <span id="reviewedPages">0</span></div>
                <div class="stat-item">Approved: <span id="approvedPages">0</span></div>
                <div class="stat-item">Needs Fix: <span id="needsFixPages">0</span></div>
            </div>
        </div>

        <div class="filter-controls">
            <label>Filter by State:</label>
            <select id="stateFilter">
                <option value="">All States</option>
            </select>
            
            <label>Search:</label>
            <input type="text" id="searchBox" class="search-box" placeholder="Search city names...">
            
            <label>Status:</label>
            <select id="statusFilter">
                <option value="">All Statuses</option>
                <option value="reviewing">Reviewing</option>
                <option value="approved">Approved</option>
                <option value="needs-fix">Needs Fix</option>
            </select>
            
            <button onclick="resetFilters()" class="btn-secondary">Reset</button>
            
            <div class="status-indicators">
                <div class="status-item">
                    <div class="status-dot status-reviewing"></div>
                    <span>Reviewing</span>
                </div>
                <div class="status-item">
                    <div class="status-dot status-approved"></div>
                    <span>Approved</span>
                </div>
                <div class="status-item">
                    <div class="status-dot status-needs-fix"></div>
                    <span>Needs Fix</span>
                </div>
            </div>
        </div>

        <div class="navigation">
            <div class="nav-controls">
                <button onclick="firstPage()" class="btn-secondary" title="Go to first page">« First</button>
                <button onclick="previousPage()" class="btn-secondary" title="Previous page (←)">‹ Previous</button>
                <span class="page-info" id="pageInfo">Page 1 of 1</span>
                <button onclick="nextPage()" class="btn-primary" title="Next page (→)">Next ›</button>
                <button onclick="lastPage()" class="btn-secondary" title="Go to last page">Last »</button>
            </div>
            <div class="nav-controls">
                <button onclick="markAsApproved()" class="btn-success" title="Mark as approved (A)">✓ Approve</button>
                <button onclick="markAsNeedsFix()" class="btn-warning" title="Mark as needs fix (F)">⚠ Needs Fix</button>
                <button onclick="openInNewTab()" class="btn-primary" title="Open in new tab">Open in New Tab</button>
            </div>
        </div>

        <iframe id="currentPage" class="current-page" src=""></iframe>

        <div class="page-list" id="pageList">
            <!-- Page list will be populated by JavaScript -->
        </div>
        
        <div class="keyboard-help">
            <strong>Keyboard shortcuts:</strong> ← Previous | → Next | Home First | End Last | A Approve | F Needs Fix
        </div>
    </div>

    <script>
        const allPages = {all_pages_json};
        
        let filteredPages = [];
        let currentIndex = 0;
        let pageStatuses = {{}}; // Store approval status for each page

        // Load page statuses from localStorage
        function loadPageStatuses() {{
            const saved = localStorage.getItem('cityPageStatuses');
            if (saved) {{
                pageStatuses = JSON.parse(saved);
            }}
        }}

        // Save page statuses to localStorage
        function savePageStatuses() {{
            localStorage.setItem('cityPageStatuses', JSON.stringify(pageStatuses));
            updateStats();
        }}

        function updateStats() {{
            const total = allPages.length;
            let approved = 0;
            let needsFix = 0;
            let reviewed = 0;
            
            for (const status of Object.values(pageStatuses)) {{
                if (status === 'approved') approved++;
                else if (status === 'needs-fix') needsFix++;
                if (status !== 'reviewing') reviewed++;
            }}
            
            document.getElementById('totalPages').textContent = total;
            document.getElementById('reviewedPages').textContent = reviewed;
            document.getElementById('approvedPages').textContent = approved;
            document.getElementById('needsFixPages').textContent = needsFix;
            
            // Update progress bar
            const progress = total > 0 ? (reviewed / total) * 100 : 0;
            document.getElementById('progressFill').style.width = progress + '%';
        }}

        // Initialize the page list
        function initializePages() {{
            loadPageStatuses();
            populateStateFilter();
            applyFilters();
            loadPage();
            updateStats();
        }}

        function populateStateFilter() {{
            const states = [...new Set(allPages.map(page => page.state))].sort();
            const stateFilter = document.getElementById('stateFilter');
            
            states.forEach(state => {{
                const option = document.createElement('option');
                option.value = state;
                option.textContent = state;
                stateFilter.appendChild(option);
            }});
        }}

        function applyFilters() {{
            const stateFilter = document.getElementById('stateFilter').value;
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const statusFilter = document.getElementById('statusFilter').value;

            filteredPages = allPages.filter(page => {{
                const matchesState = !stateFilter || page.state === stateFilter;
                const matchesSearch = !searchTerm || page.name.toLowerCase().includes(searchTerm);
                const status = pageStatuses[page.file] || 'reviewing';
                const matchesStatus = !statusFilter || status === statusFilter;
                
                return matchesState && matchesSearch && matchesStatus;
            }});

            currentIndex = 0;
            updatePageList();
            updateNavigation();
            loadPage();
        }}

        function resetFilters() {{
            document.getElementById('stateFilter').value = '';
            document.getElementById('searchBox').value = '';
            document.getElementById('statusFilter').value = '';
            applyFilters();
        }}

        function updatePageList() {{
            const pageList = document.getElementById('pageList');
            pageList.innerHTML = '';

            filteredPages.forEach((page, index) => {{
                const div = document.createElement('div');
                div.className = `page-item ${{index === currentIndex ? 'active' : ''}}`;
                
                const status = pageStatuses[page.file] || 'reviewing';
                const statusDot = `<div class="status-dot status-${{status}}" style="margin-right: 8px;"></div>`;
                
                div.innerHTML = `
                    <div style="display: flex; align-items: center;">
                        ${{statusDot}}
                        <span>${{page.name}}</span>
                    </div>
                    <small style="color: #6c757d;">${{index + 1}} of ${{filteredPages.length}}</small>
                `;
                div.onclick = () => goToPage(index);
                pageList.appendChild(div);
            }});
        }}

        function updateNavigation() {{
            const pageInfo = document.getElementById('pageInfo');
            if (filteredPages.length === 0) {{
                pageInfo.textContent = 'No pages found';
            }} else {{
                pageInfo.textContent = `Page ${{currentIndex + 1}} of ${{filteredPages.length}}`;
            }}
        }}

        function loadPage() {{
            if (filteredPages.length === 0) return;
            
            const currentPage = filteredPages[currentIndex];
            const iframe = document.getElementById('currentPage');
            iframe.src = currentPage.file;
            
            updatePageList();
            updateNavigation();
        }}

        function goToPage(index) {{
            if (index >= 0 && index < filteredPages.length) {{
                currentIndex = index;
                loadPage();
            }}
        }}

        function firstPage() {{
            goToPage(0);
        }}

        function previousPage() {{
            goToPage(currentIndex - 1);
        }}

        function nextPage() {{
            goToPage(currentIndex + 1);
        }}

        function lastPage() {{
            goToPage(filteredPages.length - 1);
        }}

        function markAsApproved() {{
            if (filteredPages.length === 0) return;
            const currentPage = filteredPages[currentIndex];
            pageStatuses[currentPage.file] = 'approved';
            savePageStatuses();
            updatePageList();
        }}

        function markAsNeedsFix() {{
            if (filteredPages.length === 0) return;
            const currentPage = filteredPages[currentIndex];
            pageStatuses[currentPage.file] = 'needs-fix';
            savePageStatuses();
            updatePageList();
        }}

        function openInNewTab() {{
            if (filteredPages.length === 0) return;
            const currentPage = filteredPages[currentIndex];
            window.open(currentPage.file, '_blank');
        }}

        // Event listeners
        document.getElementById('stateFilter').addEventListener('change', applyFilters);
        document.getElementById('searchBox').addEventListener('input', applyFilters);
        document.getElementById('statusFilter').addEventListener('change', applyFilters);

        // Keyboard navigation
        document.addEventListener('keydown', function(e) {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
            
            switch(e.key) {{
                case 'ArrowLeft':
                    e.preventDefault();
                    previousPage();
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    nextPage();
                    break;
                case 'Home':
                    e.preventDefault();
                    firstPage();
                    break;
                case 'End':
                    e.preventDefault();
                    lastPage();
                    break;
                case 'a':
                case 'A':
                    if (e.ctrlKey || e.metaKey) return;
                    e.preventDefault();
                    markAsApproved();
                    break;
                case 'f':
                case 'F':
                    if (e.ctrlKey || e.metaKey) return;
                    e.preventDefault();
                    markAsNeedsFix();
                    break;
            }}
        }});

        // Initialize when page loads
        initializePages();
    </script>
</body>
</html>'''

    # Generate the JavaScript array
    all_pages_json = json.dumps(all_pages, indent=2)
    
    # Replace placeholders in template
    html_content = html_template.replace('{total_pages}', str(len(all_pages)))
    html_content = html_content.replace('{all_pages_json}', all_pages_json)
    
    return html_content

if __name__ == "__main__":
    html_content = create_complete_review_tool()
    
    output_file = "/Users/chrisskerritt/SEC/city-pages-review-complete.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Complete review tool created: {output_file}")
    print(f"Total pages: {len(generate_city_data())}")