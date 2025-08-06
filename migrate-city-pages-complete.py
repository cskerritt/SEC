#!/usr/bin/env python3
"""
Complete UI Library Migration Script for City Pages
Includes all fixes: Bootstrap 5, relative paths, and text contrast fix v2
"""

import os
import re
import shutil
from datetime import datetime
import json

class CompleteCityPageMigrator:
    def __init__(self):
        self.migrated_count = 0
        self.skipped_count = 0
        self.error_count = 0
        self.backup_suffix = '.pre-ui-backup'
        self.log_file = 'migration-log.txt'
        self.batch_size = 50
        
    def log(self, message):
        """Log message to console and file"""
        print(message)
        with open(self.log_file, 'a') as f:
            f.write(f"{datetime.now().isoformat()} - {message}\n")
    
    def get_relative_path_prefix(self, file_path):
        """Calculate the relative path prefix based on file depth"""
        # For city pages in locations/cities/, use ../../
        if 'locations/cities/' in file_path:
            return "../../"
        # Adjust for other paths as needed
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
    
    def migrate_batch(self, files, batch_name):
        """Migrate a batch of files"""
        self.log(f"\n{'='*60}")
        self.log(f"Starting batch: {batch_name}")
        self.log(f"Files in batch: {len(files)}")
        self.log(f"{'='*60}\n")
        
        batch_start = datetime.now()
        
        for file_path in files:
            self.migrate_file(file_path)
        
        batch_duration = (datetime.now() - batch_start).total_seconds()
        self.log(f"\nBatch completed in {batch_duration:.2f} seconds")
    
    def get_city_pages_by_state(self, state_code):
        """Get all city pages for a specific state"""
        city_dir = 'locations/cities'
        if not os.path.exists(city_dir):
            return []
        
        pattern = f'-{state_code.lower()}-'
        files = []
        
        for filename in os.listdir(city_dir):
            if (filename.endswith('.html') and 
                pattern in filename and 
                not filename.endswith(self.backup_suffix)):
                files.append(os.path.join(city_dir, filename))
        
        return sorted(files)
    
    def migrate_state(self, state_code, state_name):
        """Migrate all pages for a specific state"""
        self.log(f"\n{'#'*60}")
        self.log(f"MIGRATING {state_name.upper()} ({state_code})")
        self.log(f"{'#'*60}")
        
        files = self.get_city_pages_by_state(state_code)
        if not files:
            self.log(f"No files found for {state_name}")
            return
        
        self.log(f"Found {len(files)} files for {state_name}")
        
        # Process in batches
        for i in range(0, len(files), self.batch_size):
            batch = files[i:i + self.batch_size]
            batch_name = f"{state_name} Batch {i//self.batch_size + 1}"
            self.migrate_batch(batch, batch_name)
    
    def generate_report(self):
        """Generate comprehensive migration report"""
        total = self.migrated_count + self.skipped_count + self.error_count
        
        report_content = f"""
{'='*60}
COMPLETE UI LIBRARY MIGRATION REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*60}

SUMMARY:
--------
Total files processed: {total}
✅ Successfully migrated: {self.migrated_count}
⏭ Skipped (already migrated): {self.skipped_count}
❌ Errors: {self.error_count}

Success Rate: {(self.migrated_count / total * 100) if total > 0 else 0:.1f}%

FEATURES APPLIED:
-----------------
✓ Bootstrap 5.3.2 CSS Framework
✓ Alpine.js 3.13.3 for interactivity
✓ Animate.css 4.1.1 for animations
✓ Font Awesome 6.5.1 for icons
✓ Custom UI library CSS
✓ Text contrast fix v2 (blue gradients with white text)
✓ Responsive design improvements
✓ Accessibility enhancements

{'='*60}
"""
        
        # Save text report
        with open('migration-complete-report.txt', 'w') as f:
            f.write(report_content)
        
        # Save JSON report
        report_json = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "files_processed": total,
                "files_migrated": self.migrated_count,
                "files_skipped": self.skipped_count,
                "files_error": self.error_count,
                "success_rate": (self.migrated_count / total * 100) if total > 0 else 0
            },
            "features_applied": [
                "Bootstrap 5.3.2",
                "Alpine.js 3.13.3",
                "Animate.css 4.1.1",
                "Font Awesome 6.5.1",
                "Custom UI library CSS",
                "Text contrast fix v2",
                "Responsive design",
                "Accessibility enhancements"
            ]
        }
        
        with open('migration-complete-report.json', 'w') as f:
            json.dump(report_json, f, indent=2)
        
        print(report_content)
        self.log(f"\n📄 Reports saved:")
        self.log(f"  - Text: migration-complete-report.txt")
        self.log(f"  - JSON: migration-complete-report.json")
        self.log(f"  - Log: {self.log_file}")

def main():
    """Main migration function"""
    migrator = CompleteCityPageMigrator()
    
    print("""
╔════════════════════════════════════════════════════════════╗
║          COMPLETE UI LIBRARY MIGRATION FOR CITY PAGES      ║
║                                                            ║
║  This will migrate all city pages with:                   ║
║  • Bootstrap 5.3.2 responsive framework                   ║
║  • Alpine.js for interactivity                           ║
║  • Animate.css for smooth animations                     ║
║  • Font Awesome icons                                     ║
║  • Custom UI library CSS                                  ║
║  • Text contrast fix v2 (blue gradients, white text)     ║
║                                                            ║
║  Automatic backups will be created for all files         ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Define states to migrate (ordered by importance/size)
    states_to_migrate = [
        # Already partially migrated
        ('ri', 'Rhode Island'),
        
        # Major states
        ('ca', 'California'),
        ('tx', 'Texas'),
        ('fl', 'Florida'),
        ('ny', 'New York'),
        ('pa', 'Pennsylvania'),
        ('il', 'Illinois'),
        ('oh', 'Ohio'),
        ('ga', 'Georgia'),
        ('nc', 'North Carolina'),
        ('mi', 'Michigan'),
        
        # Continue with other states...
        ('nj', 'New Jersey'),
        ('va', 'Virginia'),
        ('wa', 'Washington'),
        ('az', 'Arizona'),
        ('ma', 'Massachusetts'),
        ('tn', 'Tennessee'),
        ('in', 'Indiana'),
        ('mo', 'Missouri'),
        ('md', 'Maryland'),
        ('wi', 'Wisconsin'),
        ('co', 'Colorado'),
        ('mn', 'Minnesota'),
        ('sc', 'South Carolina'),
        ('al', 'Alabama'),
        ('la', 'Louisiana'),
        ('ky', 'Kentucky'),
        ('or', 'Oregon'),
        ('ok', 'Oklahoma'),
        ('ct', 'Connecticut'),
        ('ut', 'Utah'),
        ('ia', 'Iowa'),
        ('nv', 'Nevada'),
        ('ar', 'Arkansas'),
        ('ms', 'Mississippi'),
        ('ks', 'Kansas'),
        ('nm', 'New Mexico'),
        ('ne', 'Nebraska'),
        ('wv', 'West Virginia'),
        ('id', 'Idaho'),
        ('hi', 'Hawaii'),
        ('nh', 'New Hampshire'),
        ('me', 'Maine'),
        ('mt', 'Montana'),
        ('de', 'Delaware'),
        ('sd', 'South Dakota'),
        ('nd', 'North Dakota'),
        ('ak', 'Alaska'),
        ('vt', 'Vermont'),
        ('wy', 'Wyoming')
    ]
    
    # Confirm before proceeding
    response = input("\nProceed with migration? (yes/no): ")
    if response.lower() != 'yes':
        print("Migration cancelled.")
        return
    
    migrator.log(f"Starting complete migration at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Migrate each state
    for state_code, state_name in states_to_migrate:
        migrator.migrate_state(state_code, state_name)
        
        # Optional: Add a small delay between states to prevent overwhelming the system
        import time
        time.sleep(1)
    
    # Generate final report
    migrator.generate_report()
    
    print(f"\n🎉 Migration complete!")
    print(f"Check {migrator.log_file} for detailed logs.")

if __name__ == "__main__":
    main()