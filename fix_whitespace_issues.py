#!/usr/bin/env python3
"""
Script to fix whitespace issues in HTML files while preserving necessary formatting.

This script will:
1. Remove trailing whitespace from lines
2. Collapse multiple consecutive blank lines to single blank lines
3. Remove excessive spaces between HTML tags (while preserving intentional formatting)
4. Preserve proper indentation and necessary spaces within content
"""

import os
import re
import glob
from pathlib import Path

def clean_whitespace(content):
    """
    Clean excessive whitespace while preserving necessary formatting.
    """
    lines = content.split('\n')
    cleaned_lines = []
    
    # Track consecutive blank lines
    consecutive_blanks = 0
    
    for line in lines:
        # Remove trailing whitespace
        cleaned_line = line.rstrip()
        
        # Check if line is blank (empty or only whitespace)
        if not cleaned_line.strip():
            consecutive_blanks += 1
            # Only keep one blank line when we have consecutive blanks
            if consecutive_blanks == 1:
                cleaned_lines.append('')
        else:
            consecutive_blanks = 0
            # Clean up excessive spaces between HTML tags while preserving intentional formatting
            # This pattern looks for cases like "> <" and reduces multiple spaces to single space
            # but preserves spaces within tag content and attributes
            cleaned_line = re.sub(r'>\s{2,}<', '><', cleaned_line)
            cleaned_line = re.sub(r'>\s{2,}([^<])', r'> \1', cleaned_line)
            cleaned_line = re.sub(r'([^>])\s{2,}<', r'\1 <', cleaned_line)
            
            cleaned_lines.append(cleaned_line)
    
    # Remove trailing blank lines
    while cleaned_lines and not cleaned_lines[-1].strip():
        cleaned_lines.pop()
    
    # Ensure file ends with single newline
    if cleaned_lines:
        return '\n'.join(cleaned_lines) + '\n'
    else:
        return ''

def process_html_file(file_path):
    """
    Process a single HTML file to clean whitespace issues.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Clean the content
        cleaned_content = clean_whitespace(original_content)
        
        # Only write if content changed
        if original_content != cleaned_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            # Calculate changes
            original_lines = len(original_content.split('\n'))
            cleaned_lines = len(cleaned_content.split('\n'))
            
            return {
                'file': file_path,
                'original_lines': original_lines,
                'cleaned_lines': cleaned_lines,
                'lines_saved': original_lines - cleaned_lines,
                'changed': True
            }
        else:
            return {
                'file': file_path,
                'original_lines': len(original_content.split('\n')),
                'cleaned_lines': len(original_content.split('\n')),
                'lines_saved': 0,
                'changed': False
            }
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def find_html_files(root_dir):
    """
    Find all HTML files in the project, excluding certain directories.
    """
    html_files = []
    exclude_dirs = {'.git', 'node_modules', 'vendor', '_site'}
    
    for root, dirs, files in os.walk(root_dir):
        # Remove excluded directories from dirs list to avoid walking them
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    return html_files

def main():
    """
    Main function to process all HTML files in the project.
    """
    print("🧹 Starting HTML whitespace cleanup...")
    print("=" * 60)
    
    # Get the project root directory
    project_root = '/Users/chrisskerritt/SEC'
    
    # Find all HTML files
    html_files = find_html_files(project_root)
    
    print(f"Found {len(html_files)} HTML files to process")
    print()
    
    # Process each file
    results = []
    changed_files = 0
    total_lines_saved = 0
    
    for file_path in html_files:
        result = process_html_file(file_path)
        if result:
            results.append(result)
            if result['changed']:
                changed_files += 1
                total_lines_saved += result['lines_saved']
                relative_path = os.path.relpath(file_path, project_root)
                print(f"✅ {relative_path}")
                if result['lines_saved'] > 0:
                    print(f"   Removed {result['lines_saved']} excessive blank lines")
                else:
                    print(f"   Cleaned whitespace formatting")
    
    print()
    print("=" * 60)
    print("📊 CLEANUP SUMMARY")
    print("=" * 60)
    print(f"Total HTML files processed: {len(results)}")
    print(f"Files modified: {changed_files}")
    print(f"Files unchanged: {len(results) - changed_files}")
    print(f"Total lines saved: {total_lines_saved}")
    
    if changed_files > 0:
        print()
        print("🎉 Whitespace cleanup completed successfully!")
        print("All HTML files now have clean, consistent formatting.")
    else:
        print()
        print("✨ All HTML files were already properly formatted!")

if __name__ == "__main__":
    main()