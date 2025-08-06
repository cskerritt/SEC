#!/usr/bin/env python3
"""
Rollback UI migration by restoring from backup files
"""

import os
import shutil
from datetime import datetime

def rollback_migration():
    """Rollback the UI migration"""
    
    print("""
╔════════════════════════════════════════════════════════════╗
║              UI MIGRATION ROLLBACK UTILITY                 ║
║                                                            ║
║  This will restore all files from their backups           ║
║  Only use this if you need to undo the migration         ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    city_dir = 'locations/cities'
    backup_suffix = '.pre-ui-backup'
    
    # Count backup files
    backup_files = []
    for filename in os.listdir(city_dir):
        if filename.endswith(backup_suffix):
            backup_files.append(filename)
    
    if not backup_files:
        print("❌ No backup files found. Nothing to rollback.")
        return
    
    print(f"\nFound {len(backup_files)} backup files")
    
    # Confirm rollback
    print("\n⚠️  WARNING: This will undo all UI migrations!")
    print("All current files will be replaced with their pre-migration versions.")
    response = input("\nAre you sure you want to rollback? (yes/no): ")
    
    if response.lower() != 'yes':
        print("Rollback cancelled.")
        return
    
    print(f"\nStarting rollback at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    success_count = 0
    error_count = 0
    errors = []
    
    for backup_filename in backup_files:
        try:
            backup_path = os.path.join(city_dir, backup_filename)
            original_filename = backup_filename.replace(backup_suffix, '')
            original_path = os.path.join(city_dir, original_filename)
            
            # Restore from backup
            shutil.copy2(backup_path, original_path)
            
            # Remove backup file
            os.remove(backup_path)
            
            success_count += 1
            
            if success_count % 100 == 0:
                print(f"  Restored {success_count} files...")
                
        except Exception as e:
            error_count += 1
            errors.append(f"{backup_filename}: {str(e)}")
    
    # Generate report
    print("\n" + "="*60)
    print("ROLLBACK COMPLETE")
    print("="*60)
    print(f"✅ Successfully restored: {success_count} files")
    print(f"❌ Errors: {error_count}")
    
    if errors:
        print("\nErrors encountered:")
        for error in errors[:10]:
            print(f"  • {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    
    # Save rollback log
    log_content = f"""UI Migration Rollback Log
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Files Restored: {success_count}
Errors: {error_count}

"""
    if errors:
        log_content += "Errors:\n"
        for error in errors:
            log_content += f"- {error}\n"
    
    with open('rollback-log.txt', 'w') as f:
        f.write(log_content)
    
    print(f"\n📄 Rollback log saved to: rollback-log.txt")
    
    if success_count > 0:
        print("\n✅ Rollback completed successfully!")
        print("All files have been restored to their pre-migration state.")
    else:
        print("\n❌ Rollback failed - no files were restored.")

if __name__ == "__main__":
    rollback_migration()