#!/usr/bin/env python3
"""
UI Library Migration Script with Relative Path Support
Handles different directory depths for proper CSS path references
"""

import os
import re
import shutil
from datetime import datetime

class UILibraryMigrator:
    def __init__(self):
        self.migrated_count = 0
        self.skipped_count = 0
        self.error_count = 0
        self.backup_suffix = '.pre-ui-backup'
        
    def get_relative_path_prefix(self, file_path):
        """Calculate the relative path prefix based on file depth"""
        # Count directory depth from root
        depth = file_path.count(os.sep)
        
        # For files in root directory, no prefix needed
        if depth == 0:
            return ""
        # For files one level deep (e.g., services/index.html)
        elif depth == 1:
            return "../"
        # For files two levels deep (e.g., locations/cities/file.html)
        elif depth == 2:
            return "../../"
        # For files three levels deep
        elif depth == 3:
            return "../../../"
        else:
            # Calculate dynamically for deeper nesting
            return "../" * depth
    
    def migrate_file(self, file_path):
        """Migrate a single HTML file to use UI libraries with correct paths"""
        try:
            # Skip if already has a backup (already migrated)
            if os.path.exists(file_path + self.backup_suffix):
                print(f"⏭ Skipping (already migrated): {file_path}")
                self.skipped_count += 1
                return False
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has Bootstrap
            if 'bootstrap@5.3.2' in content or 'bootstrap.min.css' in content:
                print(f"⏭ Skipping (already has Bootstrap): {file_path}")
                self.skipped_count += 1
                return False
            
            # Create backup
            shutil.copy2(file_path, file_path + self.backup_suffix)
            
            # Get the correct relative path prefix
            rel_path = self.get_relative_path_prefix(file_path)
            
            # Add UI libraries
            updated_content = self.add_ui_libraries(content, rel_path)
            
            # Update classes
            updated_content = self.update_classes(updated_content)
            
            # Add animations
            updated_content = self.add_animations(updated_content)
            
            # Write the updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Migrated: {file_path}")
            self.migrated_count += 1
            return True
            
        except Exception as e:
            print(f"❌ Error migrating {file_path}: {str(e)}")
            self.error_count += 1
            return False
    
    def add_ui_libraries(self, content, rel_path):
        """Add UI library links to HTML head with correct relative paths"""
        # Check if </head> exists
        if '</head>' in content:
            # Add UI libraries with correct paths
            ui_libs = f'''<!-- Bootstrap 5 UI Library -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="{rel_path}css/ui-library-bootstrap.css">
<link rel="stylesheet" href="{rel_path}css/text-contrast-fix.css">
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
            'class="service-card"': 'class="card shadow-sm service-card h-100"',
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
            'class="meta-item"': 'class="text-muted"',
            'class="alert"': 'class="alert alert-info"',
            'class="error"': 'class="alert alert-danger"',
            'class="success"': 'class="alert alert-success"',
            'class="warning"': 'class="alert alert-warning"',
            'class="table"': 'class="table table-striped"',
            'class="form"': 'class="needs-validation"',
            'class="form-group"': 'class="mb-3"',
            'class="form-control"': 'class="form-control"',
            'class="nav"': 'class="navbar navbar-expand-lg navbar-light"',
            'class="nav-menu"': 'class="navbar-nav"',
            'class="nav-item"': 'class="nav-item"',
            'class="nav-link"': 'class="nav-link"'
        }
        
        for old_class, new_class in replacements.items():
            content = content.replace(old_class, new_class)
        
        # Update button variations
        content = re.sub(r'class="btn btn-primary hover-lift"', 'class="btn btn-primary hover-lift"', content)
        content = re.sub(r'class="btn btn-secondary hover-lift"', 'class="btn btn-secondary hover-lift"', content)
        
        return content
    
    def add_animations(self, content):
        """Add subtle animations to key elements"""
        # Add animations to hero titles
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
        
        # Add animations to lead paragraphs
        content = re.sub(
            r'(<p[^>]*class="lead"[^>]*>)',
            r'\1<span class="animate__animated animate__fadeInUp animate__delay-1s">',
            content
        )
        
        return content
    
    def migrate_directory(self, directory_path):
        """Migrate all HTML files in a directory"""
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.html') and not file.endswith(self.backup_suffix):
                    file_path = os.path.join(root, file)
                    # Calculate relative path from project root
                    rel_file_path = os.path.relpath(file_path)
                    self.migrate_file(rel_file_path)
    
    def migrate_single_file(self, file_path):
        """Migrate a single file"""
        if os.path.exists(file_path) and file_path.endswith('.html'):
            self.migrate_file(file_path)
        else:
            print(f"❌ Error: File not found or not an HTML file: {file_path}")
    
    def generate_report(self):
        """Generate migration report"""
        total = self.migrated_count + self.skipped_count + self.error_count
        print("\n" + "="*50)
        print("UI LIBRARY MIGRATION REPORT")
        print("="*50)
        print(f"Total files processed: {total}")
        print(f"✅ Migrated: {self.migrated_count}")
        print(f"⏭ Skipped: {self.skipped_count}")
        print(f"❌ Errors: {self.error_count}")
        print("="*50)
        
        # Save report to file
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "files_processed": total,
                "files_migrated": self.migrated_count,
                "files_skipped": self.skipped_count,
                "files_error": self.error_count
            }
        }
        
        import json
        with open('ui-migration-report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Report saved to: ui-migration-report.json")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Migrate HTML files to use modern UI libraries')
    parser.add_argument('target', help='File or directory to migrate')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be migrated without making changes')
    
    args = parser.parse_args()
    
    migrator = UILibraryMigrator()
    
    print(f"🚀 Starting UI Library Migration")
    print(f"Target: {args.target}\n")
    
    if os.path.isfile(args.target):
        migrator.migrate_single_file(args.target)
    elif os.path.isdir(args.target):
        migrator.migrate_directory(args.target)
    else:
        print(f"❌ Error: {args.target} is not a valid file or directory")
        return
    
    migrator.generate_report()

if __name__ == "__main__":
    main()