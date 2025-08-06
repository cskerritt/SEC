#!/usr/bin/env python3
"""
Monitor migration progress in real-time
"""

import os
import time
from datetime import datetime

def count_files():
    """Count migrated files"""
    city_dir = 'locations/cities'
    if not os.path.exists(city_dir):
        return 0, 0, 0
    
    total = 0
    migrated = 0
    backup_files = 0
    
    for filename in os.listdir(city_dir):
        if filename.endswith('.html') and not filename.endswith('.pre-ui-backup'):
            total += 1
            file_path = os.path.join(city_dir, filename)
            # Check if file has been migrated by looking for backup
            if os.path.exists(file_path + '.pre-ui-backup'):
                migrated += 1
        elif filename.endswith('.pre-ui-backup'):
            backup_files += 1
    
    return total, migrated, backup_files

def monitor_progress():
    """Monitor migration progress"""
    print("📊 Migration Progress Monitor")
    print("Press Ctrl+C to stop monitoring")
    print("=" * 60)
    
    start_time = datetime.now()
    initial_total, initial_migrated, _ = count_files()
    
    try:
        while True:
            total, migrated, backups = count_files()
            elapsed = (datetime.now() - start_time).total_seconds()
            
            # Calculate rate
            new_migrations = migrated - initial_migrated
            rate = new_migrations / elapsed * 60 if elapsed > 0 else 0
            
            # Calculate ETA
            remaining = total - migrated
            eta_seconds = remaining / rate * 60 if rate > 0 else 0
            eta_minutes = int(eta_seconds / 60)
            
            # Progress bar
            progress = migrated / total * 100 if total > 0 else 0
            bar_length = 40
            filled = int(bar_length * progress / 100)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            # Clear line and print status
            print(f"\r[{bar}] {progress:.1f}% | {migrated}/{total} files | "
                  f"Rate: {rate:.0f}/min | ETA: {eta_minutes} min", end='', flush=True)
            
            time.sleep(5)  # Update every 5 seconds
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        print(f"\nFinal status: {migrated}/{total} files migrated")
        print(f"Backup files created: {backups}")

if __name__ == "__main__":
    monitor_progress()