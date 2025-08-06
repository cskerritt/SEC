#!/usr/bin/env python3
"""
Simple UI Library Migration Script for Skerritt Economics
No external dependencies required
"""

import os
import re
import argparse
import json
from datetime import datetime

class SimpleUILibraryMigrator:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.changes_made = []
        self.files_processed = 0
        self.files_changed = 0

    def migrate_file(self, filepath):
        """Migrate a single HTML file to use the new UI library"""
        print(f"Processing: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Check if already migrated
            if 'bootstrap@5.3.2' in content or 'ui-library-setup.html' in content:
                print(f"  → Already migrated, skipping")
                return False
            
            # Apply migrations
            content = self.add_ui_library(content)
            content = self.update_classes(content)
            content = self.update_buttons(content)
            content = self.add_responsive_classes(content)
            content = self.update_hero_sections(content)
            
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

    def add_ui_library(self, content):
        """Add UI library includes to the HTML"""
        # Check if this is a Jekyll template (has front matter)
        if content.startswith('---'):
            # Jekyll template - add include
            if '</head>' in content:
                content = content.replace('</head>', 
                    '<!-- UI Library -->\n'
                    '{% include ui-library-setup.html %}\n'
                    '</head>')
        else:
            # Raw HTML - add CDN links
            if '</head>' in content:
                ui_libs = '''<!-- Bootstrap 5 UI Library -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="/css/ui-library-bootstrap.css">
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>
'''
                content = content.replace('</head>', ui_libs + '</head>')
                
                # Add Bootstrap JS before closing body
                if '</body>' in content:
                    content = content.replace('</body>', 
                        '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n'
                        '</body>')
        
        return content

    def update_classes(self, content):
        """Update old classes to Bootstrap 5 classes"""
        replacements = {
            'class="button"': 'class="btn btn-primary"',
            'class="button-primary"': 'class="btn btn-primary"',
            'class="button-secondary"': 'class="btn btn-secondary"',
            'class="button-outline"': 'class="btn btn-outline-primary"',
            'class="cta-button"': 'class="btn btn-accent btn-lg hover-lift"',
            'class="card"': 'class="card shadow-sm"',
            'class="service-card"': 'class="card service-card h-100"',
            'class="feature-card"': 'class="card h-100"',
            'class="container"': 'class="container"',
            'class="wrapper"': 'class="container py-5"',
            'class="grid"': 'class="row g-4"',
            'class="grid-item"': 'class="col-md-4"',
            'class="two-column"': 'class="row"',
            'class="column"': 'class="col-md-6"',
            'class="hero-section"': 'class="hero bg-gradient-hero text-white py-5"',
            'class="hero-content"': 'class="hero-content text-center"',
            'class="section-title"': 'class="display-4 text-primary mb-4"',
            'class="subsection-title"': 'class="h3 mb-3"',
            'class="lead-text"': 'class="lead"',
            'class="meta"': 'class="d-flex gap-3 justify-content-center mb-4"',
            'class="badge"': 'class="badge bg-primary"',
            'class="alert"': 'class="alert alert-primary"',
            'class="table"': 'class="table table-hover"',
            'class="form-input"': 'class="form-control"',
            'class="form-group"': 'class="mb-3"'
        }
        
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Update multiple classes
        content = re.sub(r'class="([^"]*\s+)?button(\s+[^"]*)"', r'class="\1btn btn-primary\2"', content)
        content = re.sub(r'class="([^"]*\s+)?card(\s+[^"]*)"', r'class="\1card shadow-sm\2"', content)
        
        return content

    def update_buttons(self, content):
        """Update button elements with Bootstrap classes and icons"""
        # Add hover effects to buttons
        content = re.sub(
            r'(class="[^"]*btn[^"]*")',
            lambda m: m.group(1).replace('"', ' hover-lift"') if 'hover-lift' not in m.group(1) else m.group(1),
            content
        )
        
        # Add icons to CTA buttons
        content = re.sub(
            r'(class="[^"]*btn-primary[^"]*">)([^<]+)(</a>)',
            r'\1\2 <i class="fas fa-arrow-right ms-2"></i>\3',
            content
        )
        
        return content

    def add_responsive_classes(self, content):
        """Add responsive Bootstrap classes"""
        # Make images responsive
        content = re.sub(
            r'<img([^>]*?)>',
            lambda m: '<img' + m.group(1) + ' class="img-fluid">' if 'class=' not in m.group(1) else m.group(0),
            content
        )
        
        # Add responsive spacing
        content = re.sub(
            r'class="section"',
            'class="section py-5"',
            content
        )
        
        return content

    def update_hero_sections(self, content):
        """Update hero sections with modern styling"""
        # Update hero section structure
        if '<section class="hero' in content:
            # Add animation classes to hero content
            content = re.sub(
                r'(<h1[^>]*>)',
                r'\1<span class="animate__animated animate__fadeInDown">',
                content
            )
            content = re.sub(
                r'(</h1>)',
                r'</span>\1',
                content
            )
            
            # Add animation to lead text
            content = re.sub(
                r'(<p class="lead[^>]*>)',
                r'\1<span class="animate__animated animate__fadeInUp animate__delay-1s">',
                content
            )
        
        return content

    def generate_report(self):
        """Generate a migration report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'files_processed': self.files_processed,
                'files_changed': self.files_changed,
                'dry_run': self.dry_run
            }
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
    parser = argparse.ArgumentParser(description='Migrate Skerritt Economics pages to Bootstrap 5 UI library')
    parser.add_argument('path', help='Path to migrate (file or directory)')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without modifying files')
    parser.add_argument('--pattern', help='File pattern to match (e.g., "*-ga-*.html")', default='*.html')
    
    args = parser.parse_args()
    
    migrator = SimpleUILibraryMigrator(dry_run=args.dry_run)
    
    # Process files
    if os.path.isfile(args.path):
        # Single file
        migrator.migrate_file(args.path)
    else:
        # Directory
        import glob
        pattern = os.path.join(args.path, args.pattern)
        files = glob.glob(pattern)
        
        print(f"Found {len(files)} files matching pattern: {args.pattern}")
        
        for filepath in files:
            migrator.migrate_file(filepath)
    
    # Generate report
    migrator.generate_report()

if __name__ == '__main__':
    main()