#!/usr/bin/env python3
"""
Optimize blog post titles and descriptions
Removes redundant suffixes from blog post titles
"""

import os
import re
from pathlib import Path

def optimize_blog_file(filepath):
    """Process a blog post file to optimize frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's a markdown file with frontmatter
    if not content.startswith('---'):
        return False
    
    # Split frontmatter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    frontmatter = parts[1]
    body = parts[2]
    
    changes_made = False
    lines = frontmatter.strip().split('\n')
    new_lines = []
    
    for line in lines:
        if line.startswith('title:'):
            # Extract title
            title_match = re.match(r'title:\s*["\']?(.+?)["\']?\s*$', line)
            if title_match:
                title = title_match.group(1)
                original_title = title
                
                # Remove blog suffix if present
                title = re.sub(r'\s*\|\s*Skerritt Economics Blog$', '', title)
                
                # If title is still too long, apply more optimizations
                if len(title) > 60:
                    # Try abbreviations
                    title = title.replace('Forensic Economics', 'Forensic Econ')
                    title = title.replace('Business Valuation', 'Biz Valuation')
                    title = title.replace('Economic Damages', 'Econ Damages')
                    title = title.replace('Life Care Planning', 'Life Care Plan')
                    title = title.replace('Vocational Expert', 'Voc Expert')
                
                if title != original_title:
                    new_lines.append(f'title: "{title}"')
                    changes_made = True
                    print(f"  Title: {len(original_title)} → {len(title)} chars")
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        elif line.startswith('description:') or line.startswith('excerpt:'):
            # Extract description
            desc_match = re.match(r'(description|excerpt):\s*["\']?(.+?)["\']?\s*$', line)
            if desc_match:
                field = desc_match.group(1)
                desc = desc_match.group(2)
                
                if len(desc) > 160:
                    # Truncate at sentence boundary
                    if '. ' in desc[:160]:
                        cut_point = desc[:160].rfind('. ') + 1
                        new_desc = desc[:cut_point].strip()
                    else:
                        # Cut at word boundary
                        cut_point = desc[:157].rfind(' ')
                        new_desc = desc[:cut_point] + '...'
                    
                    new_lines.append(f'{field}: "{new_desc}"')
                    changes_made = True
                    print(f"  Description: {len(desc)} → {len(new_desc)} chars")
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    if changes_made:
        # Reconstruct the file
        new_content = '---\n' + '\n'.join(new_lines) + '\n---' + body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Process blog posts"""
    base_path = Path('/Users/chrisskerritt/SEC')
    blog_path = base_path / 'blog'
    posts_path = base_path / '_posts'
    
    files_processed = 0
    files_changed = 0
    
    print("Optimizing Blog Post SEO...")
    print("=" * 60)
    
    # Process files in blog directory
    if blog_path.exists():
        for filepath in blog_path.glob('**/*.md'):
            if filepath.name != 'index.md':
                print(f"\nProcessing: {filepath.relative_to(base_path)}")
                if optimize_blog_file(filepath):
                    files_changed += 1
                files_processed += 1
    
    # Process files in _posts directory (Jekyll convention)
    if posts_path.exists():
        for filepath in posts_path.glob('**/*.md'):
            print(f"\nProcessing: {filepath.relative_to(base_path)}")
            if optimize_blog_file(filepath):
                files_changed += 1
            files_processed += 1
    
    print("\n" + "=" * 60)
    print(f"Blog SEO Optimization Complete!")
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")

if __name__ == '__main__':
    main()