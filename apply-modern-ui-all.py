#!/usr/bin/env python3
"""
Apply modern UI to all city pages
"""

import os
import glob
import json
from migrate_city_pages_simple import process_city_page

def main():
    print("Applying Modern UI to All City Pages")
    print("=" * 50)
    
    # Find all city pages
    city_pages_dir = '/Users/chrisskerritt/SEC/locations/cities'
    city_pages = glob.glob(os.path.join(city_pages_dir, '*.html'))
    
    total_pages = len(city_pages)
    print(f"Found {total_pages} city pages to update")
    
    response = input("\nDo you want to proceed with updating ALL pages? (yes/no): ")
    if response.lower() != 'yes':
        print("Migration cancelled.")
        return
    
    print("\nProcessing all pages...")
    success_count = 0
    error_count = 0
    errors = []
    
    for i, page in enumerate(city_pages):
        success, message = process_city_page(page)
        
        if success:
            success_count += 1
        else:
            error_count += 1
            errors.append(message)
        
        # Progress update every 100 pages
        if (i + 1) % 100 == 0:
            print(f"Progress: {i + 1}/{total_pages} pages processed ({success_count} successful, {error_count} errors)")
    
    # Final summary
    print("\n" + "=" * 50)
    print("Migration Complete!")
    print(f"Total pages: {total_pages}")
    print(f"Successful: {success_count}")
    print(f"Errors: {error_count}")
    
    # Save results
    results = {
        'total_pages': total_pages,
        'successful': success_count,
        'errors': error_count,
        'error_details': errors[:10]  # Save first 10 errors
    }
    
    with open('modern-ui-migration-results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\nResults saved to modern-ui-migration-results.json")

if __name__ == "__main__":
    main()