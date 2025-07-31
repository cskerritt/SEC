#!/usr/bin/env python3
"""
Fix all XX placeholders in city pages
"""

import os
import re
from pathlib import Path

def extract_city_state_from_filename(filename):
    """Extract city and state from filename like 'bellevue-wa-forensic-economist.html'"""
    match = re.match(r'(.+?)-([a-z]{2})-(.+?)\.html', filename)
    if match:
        city = match.group(1).replace('-', ' ').title()
        state_abbr = match.group(2).upper()
        return city, state_abbr
    return None, None

def get_state_name(abbr):
    """Get full state name from abbreviation"""
    states = {
        'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
        'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
        'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas',
        'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
        'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
        'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada',
        'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
        'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
        'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
        'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
        'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
        'WI': 'Wisconsin', 'WY': 'Wyoming'
    }
    return states.get(abbr, abbr)

def fix_xx_placeholders(filepath):
    """Fix all XX placeholders in a file"""
    filename = os.path.basename(filepath)
    city, state_abbr = extract_city_state_from_filename(filename)
    
    if not city or not state_abbr:
        return False, []
    
    state_name = get_state_name(state_abbr)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # Define replacements with context
    replacements = [
        # Simple XX replacements
        ('XX Coverage Area', f'{city}, {state_name} Coverage Area'),
        (f'{city}, XX Coverage Area', f'{city}, {state_name} Coverage Area'),
        (f'{city}, XX -', f'{city}, {state_abbr} -'),
        (f'{city} and XX', f'{city} and {state_name}'),
        ('throughout XX', f'throughout {state_name}'),
        ('XX court', f'{state_name} court'),
        ('XX Medicaid', f'{state_name} Medicaid'),
        ('XX family court', f'{state_name} family court'),
        ('XX vocational rehabilitation', f'{state_name} vocational rehabilitation'),
        ('XX pediatric', f'{state_name} pediatric'),
        ('meet XX court standards', f'meet {state_name} court standards'),
        (f'Serving {city}, XX', f'Serving {city}, {state_name}'),
        ('life care planning XX,', f'life care planning {state_abbr},'),
        ('vocational expert XX,', f'vocational expert {state_abbr},'),
        
        # Standalone XX (be careful with this)
        ('>XX<', f'>{state_name}<'),
        (' XX.', f' {state_name}.'),
        (' XX ', f' {state_name} '),
    ]
    
    # Apply replacements
    for old_text, new_text in replacements:
        if old_text in content:
            count = content.count(old_text)
            content = content.replace(old_text, new_text)
            changes.append(f"Replaced '{old_text}' with '{new_text}' ({count} times)")
    
    # Special case for files with double state code (auburn-wa-wa-life-care-planner.html)
    if f'-{state_abbr.lower()}-{state_abbr.lower()}-' in filename:
        # This is a duplicate state code in filename, fix it
        changes.append(f"Note: File has duplicate state code in name: {filename}")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    
    return False, []

def main():
    """Main function"""
    cities_path = Path('/Users/chrisskerritt/SEC/locations/cities')
    
    print("Fixing all XX placeholders in city pages...")
    print("=" * 80)
    
    files_fixed = 0
    files_checked = 0
    total_changes = 0
    
    # Get all HTML files
    for filepath in sorted(cities_path.glob('*.html')):
        files_checked += 1
        fixed, changes = fix_xx_placeholders(filepath)
        
        if fixed:
            files_fixed += 1
            total_changes += len(changes)
            city, state = extract_city_state_from_filename(filepath.name)
            print(f"\n{filepath.name}")
            print(f"  City: {city}, State: {get_state_name(state)}")
            for change in changes:
                print(f"  - {change}")
    
    print("\n" + "=" * 80)
    print(f"Files checked: {files_checked}")
    print(f"Files fixed: {files_fixed}")
    print(f"Total replacements made: {total_changes}")

if __name__ == '__main__':
    main()