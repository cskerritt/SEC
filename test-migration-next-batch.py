#!/usr/bin/env python3
"""
Test migration on next batch of city pages to verify all fixes are working
"""

import os
import sys

# Import the complete migrator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
exec(open('migrate-city-pages-complete.py').read())
# Use the CompleteCityPageMigrator class that was just loaded

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