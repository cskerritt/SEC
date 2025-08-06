#!/usr/bin/env python3
"""
UI Library Migration Script for Skerritt Economics
Migrates existing HTML pages to use the new Bootstrap-based UI library
"""

import os
import re
import argparse
from bs4 import BeautifulSoup
import json
from datetime import datetime

class UILibraryMigrator:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.changes_made = []
        self.files_processed = 0
        self.files_changed = 0
        
        # Mapping of old classes to new Bootstrap classes
        self.class_mappings = {
            # Buttons
            'button': 'btn btn-primary',
            'btn-cta': 'btn btn-accent btn-lg',
            'button-primary': 'btn btn-primary',
            'button-secondary': 'btn btn-secondary',
            'button-outline': 'btn btn-outline-primary',
            
            # Cards
            'card': 'card shadow-sm hover-lift',
            'service-card': 'card service-card h-100',
            'feature-card': 'card h-100',
            
            # Layout
            'container': 'container',
            'wrapper': 'container',
            'content-wrapper': 'container py-5',
            'hero': 'hero bg-gradient-hero text-white',
            'hero-content': 'hero-content text-center',
            
            # Typography
            'heading': 'display-4',
            'subheading': 'h3',
            'lead-text': 'lead',
            
            # Grid
            'grid': 'row g-4',
            'grid-item': 'col-md-4',
            'two-column': 'row',
            'column': 'col-md-6',
            
            # Forms
            'form-input': 'form-control',
            'form-select': 'form-select',
            'form-textarea': 'form-control',
            'form-label': 'form-label',
            'form-group': 'mb-3',
            
            # Utilities
            'text-center': 'text-center',
            'text-left': 'text-start',
            'text-right': 'text-end',
            'hidden': 'd-none',
            'show': 'd-block',
        }
        
        # Component patterns to replace
        self.component_patterns = {
            'service_card': {
                'pattern': r'<div class="service-card">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*(?:<a href="(.*?)".*?</a>)?\s*</div>',
                'replacement': '{% include components/service-card.html title="\\1" description="\\2" link="\\3" %}'
            },
            'contact_section': {
                'pattern': r'<div class="contact-info".*?</div>',
                'replacement': '{% include components/contact-card.html %}'
            }
        }

    def migrate_file(self, filepath):
        """Migrate a single HTML file to use the new UI library"""
        print(f"Processing: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Check if already migrated
            if 'ui-library-setup.html' in content:
                print(f"  → Already migrated, skipping")
                return False
            
            # Add UI library include to head
            content = self.add_ui_library_include(content)
            
            # Update classes
            content = self.update_classes(content)
            
            # Replace components
            content = self.replace_components(content)
            
            # Update buttons
            content = self.update_buttons(content)
            
            # Update forms
            content = self.update_forms(content)
            
            # Add animations
            content = self.add_animations(content)
            
            if content != original_content:
                if not self.dry_run:
                    # Backup original
                    backup_path = filepath + '.pre-ui-backup'
                    if not os.path.exists(backup_path):
                        with open(backup_path, 'w', encoding='utf-8') as f:
                            f.write(original_content)
                    
                    # Write updated content
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                self.files_changed += 1
                self.changes_made.append({
                    'file': filepath,
                    'changes': self.get_changes_summary(original_content, content)
                })
                print(f"  ✓ Migrated successfully")
                return True
            else:
                print(f"  → No changes needed")
                return False
                
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            return False
        finally:
            self.files_processed += 1

    def add_ui_library_include(self, content):
        """Add UI library include to the head section"""
        # For Jekyll templates
        if '---' in content[:4] and '</head>' in content:
            return content.replace('</head>', '{% include ui-library-setup.html %}\n</head>')
        # For raw HTML
        elif '<head>' in content and '</head>' in content:
            return content.replace('</head>', 
                '<!-- UI Library Setup -->\n'
                '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">\n'
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">\n'
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">\n'
                '<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>\n'
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n'
                '</head>')
        return content

    def update_classes(self, content):
        """Update old classes to Bootstrap classes"""
        for old_class, new_class in self.class_mappings.items():
            # Update class attributes
            content = re.sub(
                rf'class="([^"]*\b){old_class}(\b[^"]*)"',
                lambda m: f'class="{m.group(1)}{new_class}{m.group(2)}"',
                content
            )
            # Update class attributes with single quotes
            content = re.sub(
                rf"class='([^']*\b){old_class}(\b[^']*)'",
                lambda m: f"class='{m.group(1)}{new_class}{m.group(2)}'",
                content
            )
        return content

    def update_buttons(self, content):
        """Update button elements to use Bootstrap classes"""
        # Update <a> tags that look like buttons
        content = re.sub(
            r'<a([^>]*?)class="([^"]*?)button([^"]*?)"([^>]*?)>',
            r'<a\1class="\2btn btn-primary\3"\4>',
            content
        )
        
        # Update <button> elements
        content = re.sub(
            r'<button([^>]*?)class="([^"]*?)"([^>]*?)>',
            lambda m: f'<button{m.group(1)}class="{m.group(2)} btn btn-primary"{m.group(3)}>',
            content
        )
        
        # Add hover effects to buttons
        content = re.sub(
            r'class="([^"]*?)btn btn-primary([^"]*?)"',
            r'class="\1btn btn-primary hover-lift\2"',
            content
        )
        
        return content

    def update_forms(self, content):
        """Update form elements to use Bootstrap classes"""
        # Update input fields
        content = re.sub(
            r'<input([^>]*?)class="([^"]*?)"',
            lambda m: f'<input{m.group(1)}class="{m.group(2)} form-control"'
            if 'form-control' not in m.group(2) else m.group(0),
            content
        )
        
        # Update select elements
        content = re.sub(
            r'<select([^>]*?)class="([^"]*?)"',
            lambda m: f'<select{m.group(1)}class="{m.group(2)} form-select"'
            if 'form-select' not in m.group(2) else m.group(0),
            content
        )
        
        # Update textarea elements
        content = re.sub(
            r'<textarea([^>]*?)class="([^"]*?)"',
            lambda m: f'<textarea{m.group(1)}class="{m.group(2)} form-control"'
            if 'form-control' not in m.group(2) else m.group(0),
            content
        )
        
        # Wrap form groups
        content = re.sub(
            r'<label([^>]*?)>(.*?)</label>\s*<input([^>]*?)>',
            r'<div class="mb-3">\n  <label\1 class="form-label">\2</label>\n  <input\3>\n</div>',
            content,
            flags=re.DOTALL
        )
        
        return content

    def replace_components(self, content):
        """Replace old component patterns with new includes"""
        for component_name, component_data in self.component_patterns.items():
            content = re.sub(
                component_data['pattern'],
                component_data['replacement'],
                content,
                flags=re.DOTALL
            )
        return content

    def add_animations(self, content):
        """Add animation classes to key elements"""
        # Add animations to hero sections
        content = re.sub(
            r'<h1([^>]*?)class="([^"]*?)"',
            r'<h1\1class="\2 animate__animated animate__fadeInDown"',
            content
        )
        
        # Add animations to cards
        content = re.sub(
            r'class="([^"]*?)card([^"]*?)"',
            r'class="\1card\2 animate-on-scroll"',
            content
        )
        
        return content

    def get_changes_summary(self, original, updated):
        """Get a summary of changes made"""
        changes = []
        
        if 'ui-library-setup.html' in updated and 'ui-library-setup.html' not in original:
            changes.append("Added UI library includes")
        
        # Count class changes
        original_classes = len(re.findall(r'class="[^"]*"', original))
        updated_classes = len(re.findall(r'class="[^"]*"', updated))
        if original_classes != updated_classes:
            changes.append(f"Updated {abs(updated_classes - original_classes)} class attributes")
        
        # Check for component replacements
        if '{% include components/' in updated and '{% include components/' not in original:
            changes.append("Replaced HTML components with Jekyll includes")
        
        return changes

    def generate_report(self):
        """Generate a migration report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'files_processed': self.files_processed,
                'files_changed': self.files_changed,
                'dry_run': self.dry_run
            },
            'changes': self.changes_made
        }
        
        report_path = 'ui-migration-report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"Migration {'Preview' if self.dry_run else 'Complete'}!")
        print(f"{'='*60}")
        print(f"Files processed: {self.files_processed}")
        print(f"Files changed: {self.files_changed}")
        print(f"Report saved to: {report_path}")
        
        if self.dry_run:
            print("\n⚠️  This was a dry run. No files were actually modified.")
            print("Run without --dry-run to apply changes.")

def main():
    parser = argparse.ArgumentParser(description='Migrate Skerritt Economics pages to new UI library')
    parser.add_argument('path', nargs='?', default='.', help='Path to migrate (file or directory)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files')
    parser.add_argument('--include', help='File pattern to include (e.g., "*.html")')
    parser.add_argument('--exclude', help='File pattern to exclude (e.g., "*backup*")')
    
    args = parser.parse_args()
    
    migrator = UILibraryMigrator(dry_run=args.dry_run)
    
    # Process files
    if os.path.isfile(args.path):
        # Single file
        migrator.migrate_file(args.path)
    else:
        # Directory
        for root, dirs, files in os.walk(args.path):
            # Skip hidden directories and common build directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['_site', 'node_modules']]
            
            for file in files:
                if file.endswith('.html'):
                    # Apply include/exclude filters
                    if args.include and not file.endswith(args.include):
                        continue
                    if args.exclude and args.exclude in file:
                        continue
                    
                    filepath = os.path.join(root, file)
                    migrator.migrate_file(filepath)
    
    # Generate report
    migrator.generate_report()

if __name__ == '__main__':
    main()