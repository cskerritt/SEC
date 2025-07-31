#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Mapping of file patterns to the correct state codes
file_state_mapping = {
    'columbus-ga-ga-': 'GA',
    'smyrna-ga-ga-': 'GA',
    'smyrna-tn-tn-': 'TN',
    'springfield-oh-oh-': 'OH',
    'springfield-or-or-': 'OR',
    'st-albans-wv-wv-': 'WV',
    'troy-ny-ny-': 'NY',
    'wilmington-de-de-': 'DE'
}

def get_state_code(filename):
    """Determine the correct state code based on filename"""
    for pattern, state_code in file_state_mapping.items():
        if pattern in filename:
            return state_code
    return None

def fix_file(filepath, state_code):
    """Replace XX placeholders with the correct state code"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count replacements for reporting
        count = len(re.findall(r'\bXX\b', content))
        
        if count > 0:
            # Replace XX with the correct state code
            # Using word boundaries to avoid replacing parts of other words
            new_content = re.sub(r'\bXX\b', state_code, content)
            
            # Write the fixed content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return count
        return 0
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

def main():
    locations_dir = Path('/Users/chrisskerritt/SEC/locations')
    
    # Files to fix (from our previous analysis)
    files_to_fix = [
        'cities/columbus-ga-ga-life-care-planner.html',
        'cities/columbus-ga-ga-vocational-expert.html',
        'cities/smyrna-ga-ga-life-care-planner.html',
        'cities/smyrna-ga-ga-vocational-expert.html',
        'cities/smyrna-tn-tn-life-care-planner.html',
        'cities/smyrna-tn-tn-vocational-expert.html',
        'cities/springfield-oh-oh-life-care-planner.html',
        'cities/springfield-oh-oh-vocational-expert.html',
        'cities/springfield-or-or-life-care-planner.html',
        'cities/springfield-or-or-vocational-expert.html',
        'cities/st-albans-wv-wv-life-care-planner.html',
        'cities/st-albans-wv-wv-vocational-expert.html',
        'cities/troy-ny-ny-life-care-planner.html',
        'cities/troy-ny-ny-vocational-expert.html',
        'cities/wilmington-de-de-life-care-planner.html',
        'cities/wilmington-de-de-vocational-expert.html'
    ]
    
    total_replacements = 0
    files_fixed = 0
    
    print("Fixing XX placeholders in location files...")
    print("=" * 50)
    
    for file_path in files_to_fix:
        full_path = locations_dir / file_path
        filename = os.path.basename(file_path)
        state_code = get_state_code(filename)
        
        if state_code:
            replacements = fix_file(full_path, state_code)
            if replacements > 0:
                files_fixed += 1
                total_replacements += replacements
                print(f"✓ Fixed {file_path}")
                print(f"  Replaced {replacements} occurrences of XX with {state_code}")
        else:
            print(f"✗ Could not determine state code for {file_path}")
    
    print("\n" + "=" * 50)
    print(f"Summary:")
    print(f"- Files processed: {len(files_to_fix)}")
    print(f"- Files fixed: {files_fixed}")
    print(f"- Total XX replacements: {total_replacements}")
    
    # Verify the fixes
    print("\n" + "=" * 50)
    print("Verifying fixes...")
    
    remaining_issues = 0
    for file_path in files_to_fix:
        full_path = locations_dir / file_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            xx_count = len(re.findall(r'\bXX\b', content))
            if xx_count > 0:
                print(f"⚠️  {file_path} still has {xx_count} XX placeholders")
                remaining_issues += xx_count
        except Exception as e:
            print(f"Error verifying {file_path}: {e}")
    
    if remaining_issues == 0:
        print("✓ All XX placeholders have been successfully fixed!")
    else:
        print(f"⚠️  {remaining_issues} XX placeholders still remain")

if __name__ == "__main__":
    main()