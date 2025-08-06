#!/usr/bin/env python3
"""
Apply new UI layout to all pages that don't have it
"""

import os
import re
import shutil
import json
from datetime import datetime

class UniversalLayoutMigrator:
    def __init__(self):
        self.migrated_count = 0
        self.skipped_count = 0
        self.error_count = 0
        self.backup_suffix = '.pre-ui-backup'
        self.log_file = 'universal-migration-log.txt'
        
        # Load the audit report to know which pages need migration
        try:
            with open('site-layout-audit-report.json', 'r') as f:
                self.audit_data = json.load(f)
        except:
            self.audit_data = None
    
    def log(self, message):
        """Log message to console and file"""
        print(message)
        with open(self.log_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} - {message}\n")
    
    def get_relative_path_prefix(self, file_path):
        """Calculate the relative path prefix based on file depth"""
        # Convert to relative path from root
        rel_path = os.path.relpath(file_path, '/Users/chrisskerritt/SEC')
        depth = rel_path.count(os.sep)
        
        if depth == 0:
            return ""
        else:
            return "../" * depth
    
    def should_migrate_file(self, file_path):
        """Check if file should be migrated based on content"""
        # Skip certain files
        skip_patterns = [
            'vendor/bundle',
            '.jekyll-cache',
            '_site/',
            'node_modules',
            '.git/',
            '.pre-ui-backup',
            'netlify-deploy',
            '.next/',
            'test-',
            'migration-',
            'audit-',
            'backup-'
        ]
        
        for pattern in skip_patterns:
            if pattern in file_path:
                return False
        
        return True
    
    def add_ui_libraries(self, content, rel_path, file_type):
        """Add UI library links with correct paths"""
        # Check if already has new layout elements
        if 'bootstrap@5.3.2' in content or 'ui-library-bootstrap.css' in content:
            return content
        
        # For Jekyll pages (with front matter), handle differently
        has_front_matter = content.strip().startswith('---')
        
        if has_front_matter and file_type in ['service_page', 'practice_area', 'location_page']:
            # For Jekyll pages, add to layout instead
            return content
        
        # Find </head> tag
        if '</head>' in content:
            ui_libs = f'''
<!-- Bootstrap 5 UI Library -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="{rel_path}css/ui-library-bootstrap.css">
<link rel="stylesheet" href="{rel_path}css/text-contrast-fix-v2.css">
<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>
'''
            content = content.replace('</head>', ui_libs + '</head>')
        
        # Add Bootstrap JS before closing body
        if '</body>' in content and 'bootstrap.bundle.min.js' not in content:
            bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n'
            content = content.replace('</body>', bootstrap_js + '</body>')
        
        return content
    
    def update_html_structure(self, content, file_type):
        """Update HTML structure for better Bootstrap compatibility"""
        # Add container class to main content areas if missing
        if file_type in ['service_page', 'practice_area', 'tool_page']:
            # Ensure main content is wrapped in container
            if '<main' in content and 'container' not in content:
                content = re.sub(r'<main([^>]*)>', r'<main\1 class="container py-5">', content)
        
        # Update old button classes
        button_replacements = {
            'class="button"': 'class="btn btn-primary"',
            'class="btn-primary"': 'class="btn btn-primary"',
            'class="button-secondary"': 'class="btn btn-secondary"',
            'class="cta-button"': 'class="btn btn-primary btn-lg"',
        }
        
        for old, new in button_replacements.items():
            content = content.replace(old, new)
        
        return content
    
    def fix_navigation(self, content):
        """Ensure navigation uses Bootstrap classes"""
        if '<nav' in content and 'navbar' not in content:
            # Update navigation classes
            content = re.sub(r'<nav([^>]*)class="([^"]*)"', r'<nav\1class="navbar navbar-expand-lg navbar-light bg-light \2"', content)
        
        return content
    
    def migrate_file(self, file_path, file_type='other'):
        """Migrate a single file"""
        try:
            if not self.should_migrate_file(file_path):
                self.skipped_count += 1
                return False
            
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if already migrated
            if 'bootstrap@5.3.2' in content or 'ui-library-bootstrap.css' in content:
                self.skipped_count += 1
                return False
            
            # Create backup
            backup_path = file_path + self.backup_suffix
            if not os.path.exists(backup_path):
                shutil.copy2(file_path, backup_path)
            
            # Calculate relative path
            rel_path = self.get_relative_path_prefix(file_path)
            
            # Apply migrations
            original_content = content
            content = self.add_ui_libraries(content, rel_path, file_type)
            content = self.update_html_structure(content, file_type)
            content = self.fix_navigation(content)
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log(f"✅ Migrated: {file_path}")
                self.migrated_count += 1
                return True
            else:
                self.skipped_count += 1
                return False
                
        except Exception as e:
            self.log(f"❌ Error migrating {file_path}: {str(e)}")
            self.error_count += 1
            return False
    
    def migrate_pages_from_audit(self):
        """Migrate pages identified in the audit"""
        if not self.audit_data:
            self.log("❌ No audit data found. Run comprehensive-site-audit.py first.")
            return
        
        # Migrate pages without layout
        pages_to_migrate = self.audit_data.get('pages_without_layout', [])
        pages_with_issues = self.audit_data.get('pages_with_issues', [])
        
        self.log(f"\nMigrating {len(pages_to_migrate)} pages without layout...")
        
        for page_info in pages_to_migrate:
            file_path = os.path.join('/Users/chrisskerritt/SEC', page_info['path'])
            file_type = page_info.get('file_type', 'other')
            
            if os.path.exists(file_path):
                self.migrate_file(file_path, file_type)
        
        self.log(f"\nFixing {len(pages_with_issues)} pages with partial layout...")
        
        for page_info in pages_with_issues:
            if 'path' in page_info and page_info.get('status') != 'error':
                file_path = os.path.join('/Users/chrisskerritt/SEC', page_info['path'])
                file_type = page_info.get('file_type', 'other')
                
                if os.path.exists(file_path):
                    self.migrate_file(file_path, file_type)
    
    def migrate_jekyll_layouts(self):
        """Update Jekyll layout files to include UI libraries"""
        layouts_dir = '_layouts'
        if not os.path.exists(layouts_dir):
            return
        
        self.log("\nUpdating Jekyll layouts...")
        
        for layout_file in os.listdir(layouts_dir):
            if layout_file.endswith('.html'):
                layout_path = os.path.join(layouts_dir, layout_file)
                
                try:
                    with open(layout_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Skip if already has UI libraries
                    if 'bootstrap@5.3.2' in content:
                        continue
                    
                    # Create backup
                    backup_path = layout_path + '.pre-ui-backup'
                    if not os.path.exists(backup_path):
                        shutil.copy2(layout_path, backup_path)
                    
                    # Add UI libraries to head section
                    if '</head>' in content:
                        ui_libs = '''
  <!-- Bootstrap 5 UI Library -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="{{ '/css/ui-library-bootstrap.css' | relative_url }}">
  <link rel="stylesheet" href="{{ '/css/text-contrast-fix-v2.css' | relative_url }}">
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>
'''
                        content = content.replace('</head>', ui_libs + '  </head>')
                    
                    # Add Bootstrap JS
                    if '</body>' in content and 'bootstrap.bundle.min.js' not in content:
                        bootstrap_js = '  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n'
                        content = content.replace('</body>', bootstrap_js + '</body>')
                    
                    # Write updated layout
                    with open(layout_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    self.log(f"✅ Updated layout: {layout_file}")
                    
                except Exception as e:
                    self.log(f"❌ Error updating layout {layout_file}: {str(e)}")
    
    def generate_report(self):
        """Generate migration report"""
        report = f"""
╔════════════════════════════════════════════════════════════╗
║         UNIVERSAL LAYOUT MIGRATION COMPLETE                ║
╚════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

RESULTS:
========
✅ Successfully migrated: {self.migrated_count}
⏭ Skipped (already migrated): {self.skipped_count}
❌ Errors: {self.error_count}

Total processed: {self.migrated_count + self.skipped_count + self.error_count}

All pages should now have:
• Bootstrap 5.3.2 responsive framework
• Alpine.js 3.13.3 for interactivity
• Animate.css 4.1.1 for animations
• Font Awesome 6.5.1 for icons
• Custom UI library CSS
• Text contrast fix (blue gradients with white text)
• Responsive viewport meta tag

📄 Log file: {self.log_file}
"""
        print(report)
        
        with open('universal-migration-report.txt', 'w') as f:
            f.write(report)

def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║       APPLYING NEW LAYOUT TO ALL PAGES                    ║
║                                                            ║
║  This will update all pages that don't have the new       ║
║  Bootstrap-based layout system                             ║
╚════════════════════════════════════════════════════════════╝
""")
    
    migrator = UniversalLayoutMigrator()
    
    # First update Jekyll layouts
    migrator.migrate_jekyll_layouts()
    
    # Then migrate individual pages
    migrator.migrate_pages_from_audit()
    
    # Generate report
    migrator.generate_report()
    
    print("\n✅ Migration complete!")
    print("\nNext steps:")
    print("1. Run 'bundle exec jekyll build' to rebuild the site")
    print("2. Review the updated pages in your browser")
    print("3. Run the audit again to verify all pages are updated")

if __name__ == "__main__":
    main()