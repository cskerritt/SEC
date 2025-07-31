#!/usr/bin/env python3
import os
import re
from pathlib import Path

placeholder_patterns = [
    (r'\bXX\b', 'XX state code placeholder'),
    (r'\bTODO\b', 'TODO marker'),
    (r'\bPLACEHOLDER\b', 'PLACEHOLDER text'),
    (r'\bTBD\b', 'TBD marker'),
    (r'\bFIXME\b', 'FIXME marker'),
    (r'\bXXX\b', 'XXX marker'),
    (r'\[placeholder\]', '[placeholder] bracket'),
    (r'\{placeholder\}', '{placeholder} bracket'),
    (r'\{\{[^}]+\}\}', 'Double bracket template'),
    (r'Lorem ipsum', 'Lorem ipsum text'),
    (r'dummy text', 'Dummy text'),
    (r'sample text', 'Sample text'),
    (r'test content', 'Test content'),
]

def check_file(filepath):
    """Check a single file for placeholders"""
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        for pattern, description in placeholder_patterns:
            for line_num, line in enumerate(lines, 1):
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append({
                        'file': filepath,
                        'line': line_num,
                        'type': description,
                        'content': line.strip()
                    })
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return issues

def main():
    locations_dir = Path('/Users/chrisskerritt/SEC/locations')
    all_issues = []
    file_count = 0
    
    # Check all HTML files recursively
    for html_file in locations_dir.rglob('*.html'):
        file_count += 1
        issues = check_file(html_file)
        all_issues.extend(issues)
    
    # Group issues by type
    issues_by_type = {}
    for issue in all_issues:
        issue_type = issue['type']
        if issue_type not in issues_by_type:
            issues_by_type[issue_type] = []
        issues_by_type[issue_type].append(issue)
    
    # Print summary
    print(f"=== Placeholder Check Report ===")
    print(f"Total files checked: {file_count}")
    print(f"Total issues found: {len(all_issues)}")
    print()
    
    if all_issues:
        print("Issues by type:")
        for issue_type, issues in sorted(issues_by_type.items()):
            print(f"\n{issue_type}: {len(issues)} occurrences")
            # Show first 5 examples
            for i, issue in enumerate(issues[:5]):
                rel_path = Path(issue['file']).relative_to(locations_dir)
                print(f"  - {rel_path}:{issue['line']}")
                print(f"    {issue['content'][:100]}...")
            if len(issues) > 5:
                print(f"  ... and {len(issues) - 5} more")
    else:
        print("No placeholder issues found!")
    
    # Save detailed report
    report_path = locations_dir / 'placeholder_report.txt'
    with open(report_path, 'w') as f:
        f.write("Detailed Placeholder Report\n")
        f.write("=" * 50 + "\n\n")
        
        for issue_type, issues in sorted(issues_by_type.items()):
            f.write(f"\n{issue_type} ({len(issues)} occurrences):\n")
            f.write("-" * 40 + "\n")
            for issue in issues:
                rel_path = Path(issue['file']).relative_to(locations_dir)
                f.write(f"{rel_path}:{issue['line']}\n")
                f.write(f"{issue['content']}\n\n")
    
    print(f"\nDetailed report saved to: {report_path}")

if __name__ == "__main__":
    main()