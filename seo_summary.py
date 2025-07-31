#!/usr/bin/env python3
"""
Create a summary of SEO length issues by category.
"""

import os
import re
import glob

def extract_title(content):
    """Extract title from HTML content."""
    match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if match:
        title = match.group(1).strip()
        title = re.sub(r'\s+', ' ', title)
        return title
    return ''

def extract_meta_description(content):
    """Extract meta description from HTML content."""
    match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return ''

def analyze_file(file_path):
    """Analyze title and meta description lengths in a single HTML file."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = extract_title(content)
        description = extract_meta_description(content)
        
        return {
            'file': file_path,
            'title': title,
            'title_length': len(title),
            'description': description,
            'desc_length': len(description)
        }
        
    except Exception as e:
        return None

def main():
    """Main function to summarize SEO issues by category."""
    
    # Find all HTML files (excluding certain directories)
    html_files = []
    for root, dirs, files in os.walk('/Users/chrisskerritt/SEC'):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '_site', 'vendor', '_includes']]
        
        for file in files:
            if file.endswith('.html') and not file.startswith('.'):
                html_files.append(os.path.join(root, file))
    
    print(f"Analyzing {len(html_files)} HTML files for SEO issues...")
    print()
    
    # Categorize files
    categories = {
        'blog': [],
        'locations_state': [],
        'locations_city': [],
        'main_pages': [],
        'other': []
    }
    
    total_title_long = 0
    total_desc_long = 0
    
    for file_path in html_files:
        result = analyze_file(file_path)
        if not result or not result['title'] or '{{' in result['title'] or '{%' in result['title']:
            continue
        
        # Check for issues
        title_issue = result['title_length'] > 60
        desc_issue = result['desc_length'] > 160
        
        if title_issue or desc_issue:
            if title_issue:
                total_title_long += 1
            if desc_issue:
                total_desc_long += 1
            
            rel_path = os.path.relpath(file_path, '/Users/chrisskerritt/SEC')
            
            # Categorize
            if rel_path.startswith('blog/'):
                categories['blog'].append((rel_path, title_issue, desc_issue))
            elif rel_path.startswith('locations/') and rel_path.count('/') == 1:
                categories['locations_state'].append((rel_path, title_issue, desc_issue))
            elif rel_path.startswith('locations/') and rel_path.count('/') > 1:
                categories['locations_city'].append((rel_path, title_issue, desc_issue))
            elif '/' not in rel_path or rel_path.count('/') <= 1:
                categories['main_pages'].append((rel_path, title_issue, desc_issue))
            else:
                categories['other'].append((rel_path, title_issue, desc_issue))
    
    # Print summary
    print("📊 SEO LENGTH ISSUES SUMMARY")
    print("=" * 50)
    print(f"Total files with issues: {total_title_long + total_desc_long - len([f for files in categories.values() for f in files if f[1] and f[2]])}")
    print(f"  - Long titles (>60 chars): {total_title_long}")
    print(f"  - Long descriptions (>160 chars): {total_desc_long}")
    print()
    
    for category, files in categories.items():
        if files:
            print(f"🗂️  {category.upper().replace('_', ' ')} ({len(files)} files)")
            title_issues = sum(1 for _, title_issue, _ in files if title_issue)
            desc_issues = sum(1 for _, _, desc_issue in files if desc_issue)
            print(f"   Title issues: {title_issues}, Description issues: {desc_issues}")
            
            # Show first few examples
            for path, title_issue, desc_issue in files[:3]:
                issues = []
                if title_issue:
                    issues.append("title")
                if desc_issue:
                    issues.append("desc")
                print(f"   - {path} ({', '.join(issues)})")
            
            if len(files) > 3:
                print(f"   ... and {len(files) - 3} more")
            print()
    
    # Recommendations
    print("🔧 RECOMMENDATIONS:")
    print("1. Blog posts: Shorten titles by removing ' | Skerritt Economics Blog'")
    print("2. Location pages: Consider abbreviating state names or service names")
    print("3. City pages: Use shorter service descriptors")
    print("4. Focus on high-impact pages first (main services, popular locations)")

if __name__ == '__main__':
    main()