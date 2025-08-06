#!/usr/bin/env python3
"""
Comprehensive site audit to check which pages have the new layout
"""

import os
import re
from datetime import datetime
import json

class ComprehensiveSiteAuditor:
    def __init__(self):
        self.pages_with_new_layout = []
        self.pages_without_new_layout = []
        self.pages_with_issues = []
        self.total_pages = 0
        
    def check_for_new_layout(self, file_path, content):
        """Check if a page has the new UI library components"""
        checks = {
            'bootstrap': 'bootstrap@5.3.2' in content or 'bootstrap.min.css' in content,
            'alpine': 'alpinejs@3.13.3' in content,
            'animate': 'animate.css' in content,
            'fontawesome': 'font-awesome' in content,
            'ui_library': 'ui-library-bootstrap.css' in content,
            'text_contrast_fix': 'text-contrast-fix' in content,
            'viewport_meta': '<meta name="viewport"' in content
        }
        
        # Count how many checks pass
        passed_checks = sum(checks.values())
        total_checks = len(checks)
        
        # Determine layout status
        if passed_checks >= 5:  # Most checks pass
            return 'new_layout', checks
        elif passed_checks >= 1:  # Some checks pass
            return 'partial_layout', checks
        else:
            return 'old_layout', checks
    
    def audit_file(self, file_path):
        """Audit a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip backup files
            if '.pre-ui-backup' in file_path:
                return
                
            self.total_pages += 1
            
            # Check layout status
            status, checks = self.check_for_new_layout(file_path, content)
            
            # Create relative path for reporting
            rel_path = file_path.replace('/Users/chrisskerritt/SEC/', '')
            
            page_info = {
                'path': rel_path,
                'status': status,
                'checks': checks,
                'file_type': self.categorize_page(rel_path)
            }
            
            if status == 'new_layout':
                self.pages_with_new_layout.append(page_info)
            elif status == 'partial_layout':
                self.pages_with_issues.append(page_info)
            else:
                self.pages_without_new_layout.append(page_info)
                
        except Exception as e:
            self.pages_with_issues.append({
                'path': file_path,
                'status': 'error',
                'error': str(e)
            })
    
    def categorize_page(self, path):
        """Categorize page type based on path"""
        if 'locations/cities/' in path:
            return 'city_page'
        elif '_site/' in path:
            return 'generated'
        elif 'services/' in path:
            return 'service_page'
        elif 'locations/' in path and 'cities' not in path:
            return 'location_page'
        elif 'practice-areas/' in path:
            return 'practice_area'
        elif 'tools/' in path:
            return 'tool_page'
        elif 'blog/' in path:
            return 'blog'
        elif 'index.html' in path or 'index.md' in path:
            return 'index_page'
        else:
            return 'other'
    
    def audit_directory(self, directory):
        """Recursively audit all HTML files in directory"""
        for root, dirs, files in os.walk(directory):
            # Skip certain directories
            if any(skip in root for skip in ['.git', 'node_modules', '.jekyll-cache', '_site']):
                continue
                
            for file in files:
                if file.endswith('.html') and not file.endswith('.pre-ui-backup'):
                    file_path = os.path.join(root, file)
                    self.audit_file(file_path)
    
    def generate_report(self):
        """Generate comprehensive audit report"""
        print(f"""
╔════════════════════════════════════════════════════════════╗
║           COMPREHENSIVE SITE LAYOUT AUDIT                  ║
╚════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

SUMMARY:
========
Total HTML pages audited: {self.total_pages}
✅ Pages with new layout: {len(self.pages_with_new_layout)}
⚠️  Pages with partial layout: {len(self.pages_with_issues)}
❌ Pages without new layout: {len(self.pages_without_new_layout)}

""")
        
        # Group pages without new layout by type
        pages_by_type = {}
        for page in self.pages_without_new_layout:
            page_type = page['file_type']
            if page_type not in pages_by_type:
                pages_by_type[page_type] = []
            pages_by_type[page_type].append(page)
        
        if self.pages_without_new_layout:
            print("PAGES WITHOUT NEW LAYOUT (Need Migration):")
            print("=" * 50)
            for page_type, pages in sorted(pages_by_type.items()):
                print(f"\n{page_type.upper()} ({len(pages)} pages):")
                for page in pages[:10]:  # Show first 10
                    print(f"  - {page['path']}")
                if len(pages) > 10:
                    print(f"  ... and {len(pages) - 10} more")
        
        # Show pages with partial layout
        if self.pages_with_issues:
            print("\n\nPAGES WITH PARTIAL LAYOUT (Need Fixing):")
            print("=" * 50)
            for page in self.pages_with_issues[:20]:
                if 'checks' in page:
                    missing = [k for k, v in page['checks'].items() if not v]
                    print(f"\n{page['path']}:")
                    print(f"  Missing: {', '.join(missing)}")
        
        # Save detailed JSON report
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_pages': self.total_pages,
                'with_new_layout': len(self.pages_with_new_layout),
                'with_partial_layout': len(self.pages_with_issues),
                'without_new_layout': len(self.pages_without_new_layout)
            },
            'pages_without_layout': self.pages_without_new_layout,
            'pages_with_issues': self.pages_with_issues,
            'pages_by_type': pages_by_type
        }
        
        with open('site-layout-audit-report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: site-layout-audit-report.json")
        
        return len(self.pages_without_new_layout) + len(self.pages_with_issues)

def main():
    auditor = ComprehensiveSiteAuditor()
    
    print("🔍 Starting comprehensive site audit...")
    
    # Audit main directories
    directories_to_audit = [
        '.',  # Root directory
        'services',
        'locations',
        'practice-areas',
        'tools',
        'blog',
        'about',
        'contact',
        'resources'
    ]
    
    for directory in directories_to_audit:
        if os.path.exists(directory):
            print(f"  Auditing {directory}/...")
            auditor.audit_directory(directory)
    
    # Generate report
    pages_needing_work = auditor.generate_report()
    
    if pages_needing_work > 0:
        print(f"\n⚠️  {pages_needing_work} pages need the new layout applied!")
        print("\nRun 'python3 apply-layout-to-all-pages.py' to fix all pages.")
    else:
        print("\n✅ All pages have the new layout!")

if __name__ == "__main__":
    main()