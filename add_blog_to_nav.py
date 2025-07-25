#!/usr/bin/env python3
"""
Script to add Blog link to navigation menus across all HTML pages.
"""

import os
import re
import glob

def add_blog_to_navigation(filepath):
    """Add Blog link to navigation menu in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has blog link in navigation
        if re.search(r'<li><a[^>]*href="[^"]*blog[^"]*"[^>]*>Blog</a></li>', content, re.IGNORECASE):
            return False
            
        # Pattern 1: Look for Resources followed by Contact (most common pattern)
        pattern1 = r'(<li><a[^>]*href="[^"]*resources[^"]*"[^>]*>Resources</a></li>\s*)'
        pattern1 += r'(<li><a[^>]*class="nav-cta"[^>]*href="[^"]*contact[^"]*"[^>]*>Contact</a></li>)'
        
        if re.search(pattern1, content, re.IGNORECASE):
            # Calculate the correct relative path to blog based on file location
            depth = filepath.count('/') - filepath.count('SEC/') - 1
            blog_path = '../' * depth + 'blog/' if depth > 0 else 'blog/'
            
            replacement = r'\1<li><a href="' + blog_path + '">Blog</a></li>\n\2'
            new_content = re.sub(pattern1, replacement, content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        
        # Pattern 2: Look for Resources at end of nav (without Contact button)
        pattern2 = r'(<li><a[^>]*href="[^"]*resources[^"]*"[^>]*>Resources</a></li>\s*)(</ul>)'
        
        if re.search(pattern2, content, re.IGNORECASE):
            depth = filepath.count('/') - filepath.count('SEC/') - 1
            blog_path = '../' * depth + 'blog/' if depth > 0 else 'blog/'
            
            replacement = r'\1<li><a href="' + blog_path + '">Blog</a></li>\n\2'
            new_content = re.sub(pattern2, replacement, content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
                
        return False
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def process_directory(pattern):
    """Process all HTML files matching a pattern."""
    files = glob.glob(pattern, recursive=True)
    updated_count = 0
    
    for filepath in files:
        # Skip blog pages themselves as they already have the link
        if '/blog/' in filepath:
            continue
            
        if add_blog_to_navigation(filepath):
            updated_count += 1
            
    return updated_count, len(files)

def main():
    """Main function to process all HTML files."""
    patterns = [
        'services/**/*.html',
        'practice-areas/**/*.html',
        'locations/**/*.html',
        'about/**/*.html',
        'resources/**/*.html',
        'contact/**/*.html',
        'case-studies/**/*.html',
        '*.html',  # Root level files
    ]
    
    total_updated = 0
    total_files = 0
    
    for pattern in patterns:
        print(f"\nProcessing: {pattern}")
        updated, total = process_directory(pattern)
        total_updated += updated
        total_files += total
        print(f"  Updated {updated} of {total} files")
    
    print(f"\nTotal: Updated {total_updated} of {total_files} files")

if __name__ == "__main__":
    main()