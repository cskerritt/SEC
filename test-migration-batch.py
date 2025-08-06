#!/usr/bin/env python3
"""
Test migration on next batch of city pages
"""

import os
import re
import shutil
from datetime import datetime
import json

# Copy the migrator class definition
class CompleteCityPageMigrator:
    def __init__(self):
        self.migrated_count = 0
        self.skipped_count = 0
        self.error_count = 0
        self.backup_suffix = '.pre-ui-backup'
        self.log_file = 'migration-test-log.txt'
        self.batch_size = 50
        
    def log(self, message):
        """Log message to console and file"""
        print(message)
        with open(self.log_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} - {message}\n")
    
    def get_relative_path_prefix(self, file_path):
        """Calculate the relative path prefix based on file depth"""
        if 'locations/cities/' in file_path:
            return "../../"
        depth = file_path.count(os.sep)
        if depth == 0:
            return ""
        elif depth == 1:
            return "../"
        elif depth == 2:
            return "../../"
        else:
            return "../" * depth
    
    def migrate_file(self, file_path):
        """Migrate a single HTML file with all UI improvements"""
        try:
            # Skip if already has a backup (already migrated)
            if os.path.exists(file_path + self.backup_suffix):
                self.log(f"⏭ Skipping (already migrated): {file_path}")
                self.skipped_count += 1
                return False
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has Bootstrap
            if 'bootstrap@5.3.2' in content or 'bootstrap.min.css' in content:
                self.log(f"⏭ Skipping (already has Bootstrap): {file_path}")
                self.skipped_count += 1
                return False
            
            # Create backup BEFORE making changes
            shutil.copy2(file_path, file_path + self.backup_suffix)
            self.log(f"📁 Created backup: {file_path + self.backup_suffix}")
            
            # Get the correct relative path prefix
            rel_path = self.get_relative_path_prefix(file_path)
            
            # Apply all migrations
            updated_content = self.add_ui_libraries(content, rel_path)
            updated_content = self.update_classes(updated_content)
            updated_content = self.add_animations(updated_content)
            updated_content = self.fix_button_classes(updated_content)
            updated_content = self.ensure_responsive_meta(updated_content)
            
            # Write the updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            self.log(f"✅ Migrated: {file_path}")
            self.migrated_count += 1
            return True
            
        except Exception as e:
            self.log(f"❌ Error migrating {file_path}: {str(e)}")
            self.error_count += 1
            # Try to restore from backup if migration failed
            if os.path.exists(file_path + self.backup_suffix):
                shutil.copy2(file_path + self.backup_suffix, file_path)
                os.remove(file_path + self.backup_suffix)
                self.log(f"🔄 Restored original file due to error")
            return False
    
    def add_ui_libraries(self, content, rel_path):
        """Add UI library links with correct paths including contrast fix v2"""
        if '</head>' in content:
            # Remove any existing UI library references first
            content = re.sub(r'<!-- Bootstrap 5 UI Library -->.*?</script>\s*', '', content, flags=re.DOTALL)
            
            # Add complete UI libraries with text contrast fix v2
            ui_libs = f'''<!-- Bootstrap 5 UI Library -->
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
                content = content.replace('</body>', 
                    '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>\n'
                    '</body>')
        
        return content
    
    def update_classes(self, content):
        """Update old classes to Bootstrap 5 classes"""
        replacements = {
            # Button classes
            'class="button"': 'class="btn btn-primary"',
            'class="button-primary"': 'class="btn btn-primary"',
            'class="button-secondary"': 'class="btn btn-secondary"',
            'class="button-outline"': 'class="btn btn-outline-primary"',
            'class="cta-button"': 'class="btn btn-accent btn-lg hover-lift"',
            
            # Card classes
            'class="card"': 'class="card shadow-sm"',
            'class="service-card"': 'class="card shadow-sm service-card h-100"',
            'class="feature-card"': 'class="card h-100"',
            
            # Layout classes
            'class="container"': 'class="container"',
            'class="wrapper"': 'class="container py-5"',
            'class="grid"': 'class="row g-4"',
            'class="grid-item"': 'class="col-md-4"',
            'class="two-column"': 'class="row"',
            'class="column"': 'class="col-md-6"',
            
            # Hero classes - ensure proper gradient application
            'class="hero-section"': 'class="hero-section"',
            'class="hero"': 'class="hero"',
            'class="location-hero"': 'class="location-hero"',
            'class="hero-content"': 'class="hero-content text-center"',
            
            # Typography
            'class="section-title"': 'class="display-4 text-primary mb-4"',
            'class="subsection-title"': 'class="h3 mb-3"',
            'class="lead-text"': 'class="lead"',
            
            # Components
            'class="meta"': 'class="d-flex gap-3 justify-content-center mb-4"',
            'class="meta-item"': 'class="text-muted"',
            'class="alert"': 'class="alert alert-info"',
            'class="error"': 'class="alert alert-danger"',
            'class="success"': 'class="alert alert-success"',
            'class="warning"': 'class="alert alert-warning"',
            'class="table"': 'class="table table-striped"',
            
            # Forms
            'class="form"': 'class="needs-validation"',
            'class="form-group"': 'class="mb-3"',
            'class="form-control"': 'class="form-control"',
            
            # Navigation
            'class="nav"': 'class="navbar navbar-expand-lg navbar-light"',
            'class="nav-menu"': 'class="navbar-nav"',
            'class="nav-item"': 'class="nav-item"',
            'class="nav-link"': 'class="nav-link"'
        }
        
        for old_class, new_class in replacements.items():
            content = content.replace(old_class, new_class)
        
        return content
    
    def fix_button_classes(self, content):
        """Fix button classes that might have been corrupted"""
        # Fix the specific issue with hover-lift duplication
        content = re.sub(r'class=\s*hover-lift"btn\s+btn-primary\s+hover-lift"', 
                        'class="btn btn-primary hover-lift"', content)
        content = re.sub(r'class=\s*hover-lift"btn\s+btn-secondary\s+hover-lift"', 
                        'class="btn btn-secondary hover-lift"', content)
        content = re.sub(r'class=\s*hover-lift"btn\s+btn-primary\s+btn-block\s+hover-lift"', 
                        'class="btn btn-primary btn-block hover-lift"', content)
        
        # Fix any other malformed button classes
        content = re.sub(r'class=\s*"?hover-lift"?([^>]*?)>', 
                        r'class="\1 hover-lift">', content)
        
        return content
    
    def add_animations(self, content):
        """Add subtle animations to key elements"""
        # Add animations to hero titles
        if '<h1>' in content and 'animate__animated' not in content:
            content = re.sub(
                r'(<h1[^>]*>)',
                r'\1<span class="animate__animated animate__fadeInDown">',
                content,
                count=1  # Only animate the first h1
            )
            content = re.sub(
                r'(</h1>)',
                r'</span>\1',
                content,
                count=1
            )
        
        # Add animations to lead paragraphs in hero sections
        hero_lead_pattern = r'(<p[^>]*class="lead"[^>]*>)'
        if re.search(hero_lead_pattern, content) and 'animate__animated' not in content:
            content = re.sub(
                hero_lead_pattern,
                r'\1<span class="animate__animated animate__fadeInUp animate__delay-1s">',
                content,
                count=1
            )
            # Close the span at the end of the paragraph
            content = re.sub(
                r'(</p>)',
                r'</span>\1',
                content,
                count=1
            )
        
        return content
    
    def ensure_responsive_meta(self, content):
        """Ensure viewport meta tag is present"""
        if '<meta name="viewport"' not in content and '<head>' in content:
            viewport_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            content = content.replace('<head>', '<head>\n    ' + viewport_meta)
        
        return content

def test_next_batch():
    """Test migration on a small batch of unmigrated pages"""
    migrator = CompleteCityPageMigrator()
    
    print("""
╔════════════════════════════════════════════════════════════╗
║              TEST MIGRATION - NEXT BATCH                   ║
║                                                            ║
║  Testing complete migration on 5 more city pages           ║
║  to verify all fixes are working correctly                ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Find some unmigrated pages
    city_dir = 'locations/cities'
    test_files = []
    
    if os.path.exists(city_dir):
        for filename in sorted(os.listdir(city_dir)):
            if (filename.endswith('.html') and 
                not filename.endswith('.pre-ui-backup') and
                not os.path.exists(os.path.join(city_dir, filename + '.pre-ui-backup'))):
                
                file_path = os.path.join(city_dir, filename)
                # Read file to check if already migrated
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    if 'bootstrap@5.3.2' not in content and 'bootstrap.min.css' not in content:
                        test_files.append(file_path)
                        if len(test_files) >= 5:
                            break
                except:
                    pass
    
    if not test_files:
        print("No unmigrated files found for testing!")
        return
    
    print(f"\nFound {len(test_files)} unmigrated files for testing:")
    for f in test_files:
        print(f"  • {os.path.basename(f)}")
    
    print("\nStarting test migration...\n")
    
    # Migrate the test files
    for file_path in test_files:
        migrator.migrate_file(file_path)
    
    # Generate mini report
    print(f"\n{'='*60}")
    print("TEST MIGRATION RESULTS")
    print(f"{'='*60}")
    print(f"✅ Successfully migrated: {migrator.migrated_count}")
    print(f"⏭ Skipped: {migrator.skipped_count}")
    print(f"❌ Errors: {migrator.error_count}")
    print(f"{'='*60}")
    
    if migrator.migrated_count > 0:
        print("\n✅ Test migration successful!")
        print("The following features were applied:")
        print("  • Bootstrap 5.3.2 responsive CSS")
        print("  • Alpine.js 3.13.3 for interactivity")
        print("  • Animate.css 4.1.1 for animations")
        print("  • Font Awesome 6.5.1 icons")
        print("  • Custom UI library CSS")
        print("  • Text contrast fix v2 (blue gradients with white text)")
        print("  • Relative CSS paths (../../css/)")
        print("  • Responsive meta viewport tag")
        print("  • Fixed button classes")
        
        print("\n📋 Next steps:")
        print("1. Open one of the migrated pages to verify appearance")
        print("2. Check that blue gradient backgrounds are showing")
        print("3. Verify white text is readable")
        print("4. Test responsive behavior")
        print("5. If all looks good, run the full migration")

if __name__ == "__main__":
    test_next_batch()