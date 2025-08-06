#!/usr/bin/env python3
"""
Post-migration quality verification tool
"""

import os
import random
import re
from datetime import datetime

def verify_migration_quality():
    """Verify the quality of migrated pages"""
    
    print("""
╔════════════════════════════════════════════════════════════╗
║           POST-MIGRATION QUALITY VERIFICATION              ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    city_dir = 'locations/cities'
    
    # Get all migrated files
    migrated_files = []
    for filename in os.listdir(city_dir):
        if filename.endswith('.html') and not filename.endswith('.pre-ui-backup'):
            backup_exists = os.path.exists(os.path.join(city_dir, filename + '.pre-ui-backup'))
            if backup_exists:
                migrated_files.append(os.path.join(city_dir, filename))
    
    print(f"Total migrated files found: {len(migrated_files)}")
    
    # Sample random files for verification
    sample_size = min(10, len(migrated_files))
    sample_files = random.sample(migrated_files, sample_size)
    
    print(f"\nVerifying {sample_size} random files...\n")
    
    verification_results = {
        'bootstrap': 0,
        'alpine': 0,
        'animate': 0,
        'fontawesome': 0,
        'ui_library': 0,
        'contrast_fix': 0,
        'relative_paths': 0,
        'hero_gradient': 0,
        'responsive_meta': 0,
        'proper_classes': 0
    }
    
    issues_found = []
    
    for i, file_path in enumerate(sample_files, 1):
        print(f"[{i}/{sample_size}] Checking: {os.path.basename(file_path)}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for Bootstrap
            if 'bootstrap@5.3.2' in content:
                verification_results['bootstrap'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing Bootstrap")
            
            # Check for Alpine.js
            if 'alpinejs@3.13.3' in content:
                verification_results['alpine'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing Alpine.js")
            
            # Check for Animate.css
            if 'animate.css/4.1.1' in content:
                verification_results['animate'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing Animate.css")
            
            # Check for Font Awesome
            if 'font-awesome/6.5.1' in content:
                verification_results['fontawesome'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing Font Awesome")
            
            # Check for UI library CSS
            if 'ui-library-bootstrap.css' in content:
                verification_results['ui_library'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing UI library CSS")
            
            # Check for contrast fix
            if 'text-contrast-fix-v2.css' in content:
                verification_results['contrast_fix'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing contrast fix CSS")
            
            # Check for relative paths
            if '../../css/' in content:
                verification_results['relative_paths'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Not using relative paths")
            
            # Check for hero gradient class
            if 'class="location-hero"' in content or 'class="hero"' in content:
                verification_results['hero_gradient'] += 1
            
            # Check for responsive meta tag
            if '<meta name="viewport"' in content:
                verification_results['responsive_meta'] += 1
            else:
                issues_found.append(f"{os.path.basename(file_path)}: Missing viewport meta tag")
            
            # Check for proper Bootstrap classes
            if 'btn btn-primary' in content or 'container' in content:
                verification_results['proper_classes'] += 1
            
        except Exception as e:
            issues_found.append(f"{os.path.basename(file_path)}: Error reading file - {str(e)}")
    
    # Generate report
    print("\n" + "="*60)
    print("VERIFICATION RESULTS")
    print("="*60)
    
    print(f"\n✅ Bootstrap 5.3.2: {verification_results['bootstrap']}/{sample_size}")
    print(f"✅ Alpine.js 3.13.3: {verification_results['alpine']}/{sample_size}")
    print(f"✅ Animate.css 4.1.1: {verification_results['animate']}/{sample_size}")
    print(f"✅ Font Awesome 6.5.1: {verification_results['fontawesome']}/{sample_size}")
    print(f"✅ UI Library CSS: {verification_results['ui_library']}/{sample_size}")
    print(f"✅ Text Contrast Fix v2: {verification_results['contrast_fix']}/{sample_size}")
    print(f"✅ Relative CSS Paths: {verification_results['relative_paths']}/{sample_size}")
    print(f"✅ Hero Section Classes: {verification_results['hero_gradient']}/{sample_size}")
    print(f"✅ Responsive Meta Tag: {verification_results['responsive_meta']}/{sample_size}")
    print(f"✅ Bootstrap Classes: {verification_results['proper_classes']}/{sample_size}")
    
    # Calculate overall quality score
    total_checks = sum(verification_results.values())
    max_possible = sample_size * len(verification_results)
    quality_score = (total_checks / max_possible) * 100
    
    print(f"\n📊 Overall Quality Score: {quality_score:.1f}%")
    
    if issues_found:
        print(f"\n⚠️  Issues Found ({len(issues_found)}):")
        for issue in issues_found[:10]:  # Show first 10 issues
            print(f"   • {issue}")
        if len(issues_found) > 10:
            print(f"   ... and {len(issues_found) - 10} more issues")
    else:
        print("\n✅ No issues found in sample!")
    
    # Save detailed report
    report_content = f"""Post-Migration Quality Verification Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Sample Size: {sample_size} files
Total Migrated: {len(migrated_files)} files

Verification Results:
- Bootstrap 5.3.2: {verification_results['bootstrap']}/{sample_size}
- Alpine.js 3.13.3: {verification_results['alpine']}/{sample_size}
- Animate.css 4.1.1: {verification_results['animate']}/{sample_size}
- Font Awesome 6.5.1: {verification_results['fontawesome']}/{sample_size}
- UI Library CSS: {verification_results['ui_library']}/{sample_size}
- Text Contrast Fix v2: {verification_results['contrast_fix']}/{sample_size}
- Relative CSS Paths: {verification_results['relative_paths']}/{sample_size}
- Hero Section Classes: {verification_results['hero_gradient']}/{sample_size}
- Responsive Meta Tag: {verification_results['responsive_meta']}/{sample_size}
- Bootstrap Classes: {verification_results['proper_classes']}/{sample_size}

Overall Quality Score: {quality_score:.1f}%

Files Checked:
"""
    
    for file_path in sample_files:
        report_content += f"- {os.path.basename(file_path)}\n"
    
    if issues_found:
        report_content += f"\nIssues Found ({len(issues_found)}):\n"
        for issue in issues_found:
            report_content += f"- {issue}\n"
    
    with open('post-migration-quality-report.txt', 'w') as f:
        f.write(report_content)
    
    print("\n📄 Detailed report saved to: post-migration-quality-report.txt")
    
    return quality_score

if __name__ == "__main__":
    score = verify_migration_quality()
    
    if score >= 95:
        print("\n🎉 Excellent migration quality!")
    elif score >= 90:
        print("\n✅ Good migration quality")
    elif score >= 80:
        print("\n⚠️  Acceptable migration quality, but some improvements needed")
    else:
        print("\n❌ Poor migration quality, investigation required")