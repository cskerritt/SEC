#!/usr/bin/env python3
"""
Analyze title and meta description lengths using regex (no external dependencies).
"""

import os
import re
import glob

def extract_title(content):
    """Extract title from HTML content."""
    match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if match:
        # Clean up the title text
        title = match.group(1).strip()
        title = re.sub(r'\s+', ' ', title)  # Normalize whitespace
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
        print(f"Error analyzing {file_path}: {e}")
        return None

def main():
    """Main function to analyze SEO lengths across all HTML files."""
    
    # Find all HTML files (excluding certain directories)
    html_files = []
    for root, dirs, files in os.walk('/Users/chrisskerritt/SEC'):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '_site', 'vendor', '_includes']]
        
        for file in files:
            if file.endswith('.html') and not file.startswith('.'):
                html_files.append(os.path.join(root, file))
    
    print(f"Analyzing {len(html_files)} HTML files for SEO length issues...")
    print()
    
    issues_found = []
    
    for file_path in sorted(html_files):
        result = analyze_file(file_path)
        if not result:
            continue
        
        # Skip files with template syntax or empty titles
        if not result['title'] or '{{' in result['title'] or '{%' in result['title']:
            continue
            
        # Check for issues
        title_issue = result['title_length'] > 60
        desc_issue = result['desc_length'] > 160
        
        if title_issue or desc_issue:
            issues_found.append(result)
            
            rel_path = os.path.relpath(file_path, '/Users/chrisskerritt/SEC')
            print(f"📄 {rel_path}")
            
            if title_issue:
                print(f"  ❌ Title: {result['title_length']} chars (>60)")
                print(f"     \"{result['title'][:80]}{'...' if len(result['title']) > 80 else ''}\"")
            else:
                print(f"  ✅ Title: {result['title_length']} chars")
            
            if desc_issue:
                print(f"  ❌ Description: {result['desc_length']} chars (>160)")
                print(f"     \"{result['description'][:100]}{'...' if len(result['description']) > 100 else ''}\"")
            elif result['description']:
                print(f"  ✅ Description: {result['desc_length']} chars")
            else:
                print(f"  ⚠️  No meta description")
            
            print()
    
    print(f"📊 SEO Analysis Results:")
    print(f"   Total files: {len(html_files)}")
    print(f"   Issues found: {len(issues_found)} files")
    
    # Summary by type
    title_long = sum(1 for f in issues_found if f['title_length'] > 60)
    desc_long = sum(1 for f in issues_found if f['desc_length'] > 160)
    
    print(f"   - Titles >60 chars: {title_long}")
    print(f"   - Descriptions >160 chars: {desc_long}")
    
    if issues_found:
        print(f"\n🔧 Recommendation: Consider shortening these titles and descriptions")
        print(f"   - Titles should be 30-60 characters")
        print(f"   - Meta descriptions should be 120-160 characters")

if __name__ == '__main__':
    main()