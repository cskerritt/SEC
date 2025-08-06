#!/usr/bin/env python3
"""
Run the full migration of all city pages
"""

import subprocess
import sys
import os
from datetime import datetime

def run_full_migration():
    """Execute the complete migration"""
    print("""
╔════════════════════════════════════════════════════════════╗
║           FULL UI LIBRARY MIGRATION EXECUTION              ║
║                                                            ║
║  This will migrate approximately 3,150 city pages with:   ║
║  • Bootstrap 5.3.2                                        ║
║  • Text contrast fix v2 (blue gradients, white text)     ║
║  • Responsive design improvements                         ║
║  • All UI enhancements                                    ║
║                                                            ║
║  Estimated time: 15-20 minutes                           ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Confirm
    response = input("\n⚠️  This will modify ~3,150 files. Continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Migration cancelled.")
        return
    
    print(f"\n🚀 Starting full migration at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Run the migration script
    try:
        # Use subprocess to handle the interactive prompt automatically
        process = subprocess.Popen(
            ['python3', 'migrate-city-pages-complete.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Send 'yes' to the confirmation prompt
        process.stdin.write('yes\n')
        process.stdin.flush()
        
        # Read output line by line
        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(line.rstrip())
        
        # Wait for completion
        process.wait()
        
        if process.returncode == 0:
            print("\n✅ Migration completed successfully!")
            print("\n📊 Check the following files for results:")
            print("  • migration-complete-report.txt")
            print("  • migration-complete-report.json")
            print("  • migration-log.txt")
        else:
            print(f"\n❌ Migration failed with exit code: {process.returncode}")
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Migration interrupted by user")
        process.terminate()
        process.wait()
    except Exception as e:
        print(f"\n❌ Error running migration: {str(e)}")

if __name__ == "__main__":
    run_full_migration()