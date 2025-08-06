#!/usr/bin/env python3
"""
UI Component Testing Framework
Tests Bootstrap 5 implementation across Skerritt Economics pages
"""

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path

class UIComponentTester:
    def __init__(self):
        self.results = {
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'errors': []
        }
        self.required_classes = {
            'bootstrap': ['btn', 'card', 'container', 'row', 'col'],
            'responsive': ['col-md-', 'col-lg-', 'col-sm-'],
            'custom': ['hover-lift', 'bg-gradient-hero', 'text-accent']
        }

    def test_file(self, filepath):
        """Test a single HTML file"""
        print(f"Testing: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if file is too small (likely empty or redirect)
            if len(content) < 100:
                return
            
            has_errors = False
            
            # Test 1: Check for Bootstrap CSS
            if not self.has_bootstrap_css(content):
                self.add_error(filepath, 'Missing Bootstrap CSS link')
                has_errors = True
            
            # Test 2: Check for responsive meta tag
            if not self.has_responsive_meta(content):
                self.add_error(filepath, 'Missing responsive viewport meta tag')
                has_errors = True
            
            # Test 3: Check for Bootstrap classes
            bootstrap_score = self.check_bootstrap_classes(content)
            if bootstrap_score < 0.3:
                self.add_warning(filepath, f'Low Bootstrap usage: {int(bootstrap_score * 100)}%')
            
            # Test 4: Check for accessibility
            self.check_accessibility(content, filepath)
            
            # Test 5: Check for proper button styling
            if self.check_old_buttons(content):
                self.add_error(filepath, 'Found old button classes - needs migration')
                has_errors = True
            
            # Test 6: Check for responsive images
            self.check_images(content, filepath)
            
            # Test 7: Check for proper heading structure
            self.check_headings(content, filepath)
            
            if not has_errors:
                self.results['passed'] += 1
            else:
                self.results['failed'] += 1
                
        except Exception as e:
            self.add_error(filepath, f'Failed to test: {str(e)}')
            self.results['failed'] += 1

    def has_bootstrap_css(self, content):
        """Check if Bootstrap CSS is included"""
        return any([
            'bootstrap@5.3.2' in content,
            'bootstrap.min.css' in content,
            'ui-library-setup.html' in content,
            'ui-library-bootstrap.css' in content
        ])

    def has_responsive_meta(self, content):
        """Check for responsive viewport meta tag"""
        return 'viewport' in content and 'width=device-width' in content

    def check_bootstrap_classes(self, content):
        """Calculate Bootstrap class usage score"""
        found_classes = 0
        total_classes = 0
        
        # Extract all class attributes
        class_matches = re.findall(r'class=["\']([^"\']*)["\']', content)
        all_classes = ' '.join(class_matches)
        
        # Check for Bootstrap classes
        for class_name in self.required_classes['bootstrap']:
            total_classes += 1
            if class_name in all_classes:
                found_classes += 1
        
        # Check for responsive classes
        for class_prefix in self.required_classes['responsive']:
            total_classes += 1
            if class_prefix in all_classes:
                found_classes += 1
        
        return found_classes / total_classes if total_classes > 0 else 0

    def check_accessibility(self, content, filepath):
        """Check accessibility features"""
        # Check for alt text on images
        img_matches = re.findall(r'<img[^>]*>', content)
        for img in img_matches:
            if 'alt=' not in img:
                self.add_warning(filepath, 'Image missing alt text')
        
        # Check for ARIA labels on buttons
        button_matches = re.findall(r'<button[^>]*>', content)
        for button in button_matches:
            if 'aria-' not in button and 'title=' not in button:
                self.add_warning(filepath, 'Button missing ARIA label')
        
        # Check for form labels
        input_matches = re.findall(r'<input[^>]*type=["\'](?!hidden|submit)[^"\']*["\'][^>]*>', content)
        for input_tag in input_matches:
            if 'id=' in input_tag:
                input_id = re.search(r'id=["\']([^"\']*)["\']', input_tag)
                if input_id and f'for="{input_id.group(1)}"' not in content:
                    self.add_warning(filepath, f'Input missing associated label')

    def check_old_buttons(self, content):
        """Check for old button styling"""
        old_patterns = [
            r'class=["\']button["\']',
            r'class=["\']button\s',
            r'class=["\'][^"\']*\sbutton["\']',
            r'class=["\'][^"\']*\sbutton\s'
        ]
        
        for pattern in old_patterns:
            if re.search(pattern, content):
                return True
        return False

    def check_images(self, content, filepath):
        """Check responsive images"""
        img_matches = re.findall(r'<img[^>]*>', content)
        for img in img_matches:
            if 'img-fluid' not in img and 'class=' in img:
                self.add_warning(filepath, 'Image may not be responsive (missing img-fluid class)')

    def check_headings(self, content, filepath):
        """Check heading hierarchy"""
        headings = re.findall(r'<h([1-6])[^>]*>', content)
        if headings:
            last_level = 0
            for heading in headings:
                level = int(heading)
                if last_level > 0 and level - last_level > 1:
                    self.add_warning(filepath, f'Skipped heading level: h{last_level} to h{level}')
                last_level = level

    def add_error(self, filepath, message):
        """Add error to results"""
        self.results['errors'].append({
            'type': 'error',
            'file': filepath,
            'message': message
        })

    def add_warning(self, filepath, message):
        """Add warning to results"""
        self.results['warnings'] += 1
        self.results['errors'].append({
            'type': 'warning',
            'file': filepath,
            'message': message
        })

    def test_directory(self, dir_path, pattern='*.html'):
        """Test all files in a directory"""
        files = list(Path(dir_path).rglob(pattern))
        
        # Exclude _site directory
        files = [f for f in files if '_site' not in str(f)]
        
        print(f"\nTesting {len(files)} files...\n")
        
        for file in files:
            self.test_file(str(file))
        
        self.print_results()

    def print_results(self):
        """Print test results"""
        print('\n' + '=' * 60)
        print('UI Component Test Results')
        print('=' * 60)
        
        total_tested = self.results['passed'] + self.results['failed']
        print(f"\nTotal Files Tested: {total_tested}")
        print(f"✅ Passed: {self.results['passed']}")
        print(f"❌ Failed: {self.results['failed']}")
        print(f"⚠️  Warnings: {self.results['warnings']}")
        
        if self.results['errors']:
            print('\nIssues Found:')
            print('-' * 60)
            
            # Group by file
            file_issues = {}
            for error in self.results['errors']:
                file = error['file']
                if file not in file_issues:
                    file_issues[file] = []
                file_issues[file].append(error)
            
            # Sort files by number of issues
            sorted_files = sorted(file_issues.items(), 
                                key=lambda x: len(x[1]), 
                                reverse=True)
            
            for file, issues in sorted_files[:20]:  # Show top 20 files with issues
                print(f"\n{file}:")
                for issue in issues:
                    icon = '❌' if issue['type'] == 'error' else '⚠️'
                    print(f"  {icon} {issue['message']}")
            
            if len(sorted_files) > 20:
                print(f"\n... and {len(sorted_files) - 20} more files with issues")
        
        # Calculate success rate
        if total_tested > 0:
            success_rate = (self.results['passed'] / total_tested) * 100
            print(f"\n📊 Success Rate: {success_rate:.1f}%")
        
        # Generate report file
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_tested': total_tested,
                'passed': self.results['passed'],
                'failed': self.results['failed'],
                'warnings': self.results['warnings']
            },
            'issues': self.results['errors'][:100]  # Limit to first 100 issues
        }
        
        with open('ui-test-report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        print('\n📄 Detailed report saved to: ui-test-report.json')

def main():
    parser = argparse.ArgumentParser(description='Test UI components in HTML files')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Path to test (file or directory)')
    parser.add_argument('--pattern', default='*.html',
                       help='File pattern to match')
    
    args = parser.parse_args()
    
    tester = UIComponentTester()
    
    print('🧪 UI Component Testing Framework')
    print('Testing Bootstrap 5 implementation...\n')
    
    if os.path.isfile(args.path):
        tester.test_file(args.path)
        tester.print_results()
    else:
        tester.test_directory(args.path, args.pattern)

if __name__ == '__main__':
    main()