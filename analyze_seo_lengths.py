#!/usr/bin/env python3
"""
Analyze title and meta description lengths across all HTML files.
Identify files that exceed SEO best practices (titles >60 chars, descriptions >160 chars).
"""

import os
import re
import glob
from bs4 import BeautifulSoup

def analyze_file(file_path):
    """Analyze title and meta description lengths in a single HTML file."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else ''
        
        # Extract meta description
        meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc_tag.get('content', '').strip() if meta_desc_tag else ''
        
        return {
            'file': file_path,
            'title': title,
            'title_length': len(title),
            'description': description,
            'desc_length': len(description)
        }
        
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def main():
    """Main function to analyze SEO lengths across all HTML files."""
    
    # Find all HTML files (excluding certain directories)
    html_files = []
    for root, dirs, files in os.walk('/Users/chrisskerritt/SEC'):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '_site', 'vendor']]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    print(f"Analyzing {len(html_files)} HTML files...")
    print()
    
    issues_found = []
    
    for file_path in sorted(html_files):
        result = analyze_file(file_path)
        if not result:
            continue
            
        # Check for issues
        title_issue = result['title_length'] > 60
        desc_issue = result['desc_length'] > 160
        
        if title_issue or desc_issue:
            issues_found.append(result)
            
            rel_path = os.path.relpath(file_path, '/Users/chrisskerritt/SEC')
            print(f"📄 {rel_path}")
            
            if title_issue:
                print(f"  ❌ Title too long: {result['title_length']} chars (max 60)")
                print(f"     \"{result['title'][:80]}{'...' if len(result['title']) > 80 else ''}\"")
            else:
                print(f"  ✅ Title OK: {result['title_length']} chars")
            
            if desc_issue:
                print(f"  ❌ Description too long: {result['desc_length']} chars (max 160)")
                print(f"     \"{result['description'][:100]}{'...' if len(result['description']) > 100 else ''}\"")
            elif result['description']:
                print(f"  ✅ Description OK: {result['desc_length']} chars")
            else:
                print(f"  ⚠️  No meta description found")
            
            print()
    
    print(f"📊 SEO Length Analysis Complete")
    print(f"   Total files analyzed: {len(html_files)}")
    print(f"   Files with issues: {len(issues_found)}")
    
    # Group by issue type
    title_issues = [f for f in issues_found if f['title_length'] > 60]
    desc_issues = [f for f in issues_found if f['desc_length'] > 160]
    
    print(f"   - Title too long: {len(title_issues)} files")
    print(f"   - Description too long: {len(desc_issues)} files")

if __name__ == '__main__':
    main()