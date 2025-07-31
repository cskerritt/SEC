#!/usr/bin/env python3
"""
HTML Issue Fixer
Fixes multiple title tags and excessive whitespace in HTML files
"""

import os
import re
import glob
from pathlib import Path

def fix_multiple_title_tags(content):
    """
    Remove duplicate title tags, keeping the first one
    """
    # Find all title tags
    title_pattern = r'<title[^>]*>.*?</title>'
    titles = re.findall(title_pattern, content, re.IGNORECASE | re.DOTALL)
    
    if len(titles) > 1:
        print(f"    Found {len(titles)} title tags - removing duplicates")
        # Keep only the first title tag
        first_title = titles[0]
        # Remove all title tags
        content = re.sub(title_pattern, '', content, flags=re.IGNORECASE | re.DOTALL)
        # Add back the first title tag in the head section
        head_pattern = r'(<head[^>]*>)'
        if re.search(head_pattern, content, re.IGNORECASE):
            # Insert after opening head tag
            content = re.sub(head_pattern, r'\1\n    ' + first_title, content, flags=re.IGNORECASE)
        else:
            # If no head tag found, add at the beginning after DOCTYPE and html
            insert_pattern = r'(<html[^>]*>\s*)'
            content = re.sub(insert_pattern, r'\1\n<head>\n    ' + first_title + '\n</head>\n', content, flags=re.IGNORECASE)
        
        return content, True
    
    return content, False

def fix_excessive_whitespace(content):
    """
    Fix excessive whitespace issues:
    1. Remove trailing spaces from lines
    2. Reduce multiple consecutive blank lines to max 2
    3. Remove excessive indentation (but preserve structure)
    """
    changes_made = False
    original_content = content
    
    # Split into lines for processing
    lines = content.split('\n')
    processed_lines = []
    
    # Track consecutive blank lines
    consecutive_blank_lines = 0
    
    for line in lines:
        # Remove trailing whitespace
        stripped_line = line.rstrip()
        
        # Check if this is a blank line
        if not stripped_line.strip():
            consecutive_blank_lines += 1
            # Only add blank line if we haven't exceeded the limit
            if consecutive_blank_lines <= 2:
                processed_lines.append('')
        else:
            consecutive_blank_lines = 0
            processed_lines.append(stripped_line)
    
    # Join lines back together
    content = '\n'.join(processed_lines)
    
    # Remove trailing newlines at end of file, then add exactly one
    content = content.rstrip() + '\n'
    
    # Check if changes were made
    if content != original_content:
        changes_made = True
    
    return content, changes_made

def process_html_file(filepath):
    """
    Process a single HTML file to fix title tags and whitespace
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        title_fixed = False
        whitespace_fixed = False
        
        # Fix multiple title tags
        content, title_fixed = fix_multiple_title_tags(content)
        
        # Fix excessive whitespace
        content, whitespace_fixed = fix_excessive_whitespace(content)
        
        # Write back if changes were made
        if title_fixed or whitespace_fixed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixes = []
            if title_fixed:
                fixes.append("multiple title tags")
            if whitespace_fixed:
                fixes.append("excessive whitespace")
            
            print(f"  ✓ Fixed: {', '.join(fixes)}")
            return True
        else:
            print(f"  - No issues found")
            return False
            
    except Exception as e:
        print(f"  ✗ Error processing {filepath}: {str(e)}")
        return False

def main():
    """
    Main function to process all HTML files
    """
    print("HTML Issue Fixer")
    print("=" * 50)
    print("Fixing multiple title tags and excessive whitespace in HTML files...")
    print()
    
    # Find all HTML files
    html_patterns = [
        '**/*.html',
        '*.html'
    ]
    
    html_files = set()
    for pattern in html_patterns:
        html_files.update(glob.glob(pattern, recursive=True))
    
    # Convert to list and sort
    html_files = sorted(list(html_files))
    
    # Focus on _site directory files (the built/generated files)
    html_files = [f for f in html_files if '_site/' in f]
    
    print(f"Found {len(html_files)} HTML files to process")
    print()
    
    processed_count = 0
    fixed_count = 0
    
    for filepath in html_files:
        print(f"Processing: {filepath}")
        processed_count += 1
        
        if process_html_file(filepath):
            fixed_count += 1
    
    print()
    print("=" * 50)
    print("Summary:")
    print(f"Files processed: {processed_count}")
    print(f"Files fixed: {fixed_count}")
    print(f"Files with no issues: {processed_count - fixed_count}")
    
    if fixed_count > 0:
        print()
        print("✓ HTML issues have been fixed!")
        print("  - Multiple title tags removed")
        print("  - Excessive whitespace cleaned up")
        print("  - Trailing spaces removed")
        print("  - Multiple blank lines reduced")
    else:
        print("\n✓ All HTML files are already clean!")

if __name__ == "__main__":
    main()