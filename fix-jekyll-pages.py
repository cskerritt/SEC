#!/usr/bin/env python3
"""
Fix Jekyll-based pages (services, practice areas, etc.) to use the new layout
"""

import os
import re
import shutil
from datetime import datetime

def update_jekyll_page(file_path):
    """Update a Jekyll page to use the new layout"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it's a Jekyll page (has front matter)
        if not content.strip().startswith('---'):
            return False
        
        # Find the end of front matter
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False
        
        front_matter = parts[1]
        body = parts[2]
        
        # Update layout if needed
        updated = False
        if 'layout:' in front_matter:
            # Check which layout it uses
            if 'layout: default' in front_matter and 'default-optimized' not in front_matter:
                # Already using updated default layout
                updated = True
            elif 'layout: service' in front_matter:
                # Service pages should use default layout now
                front_matter = front_matter.replace('layout: service', 'layout: default')
                updated = True
        
        # Add Bootstrap classes to the body content if needed
        if updated or 'layout: default' in front_matter:
            # Add container class to main content
            if '<div class="content">' in body:
                body = body.replace('<div class="content">', '<div class="content container py-5">')
                updated = True
            
            # Update button classes
            button_replacements = {
                'class="button"': 'class="btn btn-primary"',
                'class="cta-button"': 'class="btn btn-primary btn-lg"',
                'class="button-secondary"': 'class="btn btn-secondary"',
            }
            
            for old, new in button_replacements.items():
                if old in body:
                    body = body.replace(old, new)
                    updated = True
            
            # Update grid classes
            if 'class="grid"' in body:
                body = body.replace('class="grid"', 'class="row g-4"')
                body = body.replace('class="grid-item"', 'class="col-md-4"')
                updated = True
        
        if updated:
            # Create backup
            backup_path = file_path + '.pre-ui-backup'
            if not os.path.exists(backup_path):
                shutil.copy2(file_path, backup_path)
            
            # Write updated content
            new_content = f"---{front_matter}---{body}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated Jekyll page: {file_path}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {str(e)}")
        return False

def main():
    """Fix all Jekyll pages"""
    print("Fixing Jekyll pages...")
    
    # Directories with Jekyll pages
    jekyll_dirs = [
        'services',
        'practice-areas',
        'locations',
        'tools',
        'about',
        'contact',
        'resources',
        'blog'
    ]
    
    updated_count = 0
    
    for directory in jekyll_dirs:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.html') or file.endswith('.md'):
                        file_path = os.path.join(root, file)
                        if update_jekyll_page(file_path):
                            updated_count += 1
    
    # Also check root directory
    for file in os.listdir('.'):
        if (file.endswith('.html') or file.endswith('.md')) and os.path.isfile(file):
            if update_jekyll_page(file):
                updated_count += 1
    
    print(f"\n✅ Updated {updated_count} Jekyll pages")
    print("\nNow rebuilding the site...")
    
    # Rebuild the site
    os.system('bundle exec jekyll build')
    
    print("\n✅ Site rebuilt with new layouts!")

if __name__ == "__main__":
    main()