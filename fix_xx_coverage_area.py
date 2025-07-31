#!/usr/bin/env python3
"""
Fix XX Coverage Area placeholder issues in city pages
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

def fix_xx_coverage_area(filepath):
    """Fix XX Coverage Area placeholders in a file"""
    filename = os.path.basename(filepath)
    city, state_abbr = extract_city_state_from_filename(filename)
    
    if not city or not state_abbr:
        return False
    
    state_name = get_state_name(state_abbr)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has XX Coverage Area
    if 'XX Coverage Area' not in content:
        return False
    
    # Replace XX Coverage Area with proper city/state
    original_content = content
    content = content.replace('XX Coverage Area', f'{city}, {state_name} Coverage Area')
    
    # Also check for other potential placeholders
    content = content.replace(f'XX {state_name} Coverage Area', f'{city}, {state_name} Coverage Area')
    content = content.replace(f'XX, {state_name} Coverage Area', f'{city}, {state_name} Coverage Area')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Main function"""
    cities_path = Path('/Users/chrisskerritt/SEC/locations/cities')
    
    print("Fixing XX Coverage Area placeholders...")
    print("=" * 60)
    
    files_fixed = 0
    files_checked = 0
    
    # Get all HTML files
    for filepath in cities_path.glob('*.html'):
        files_checked += 1
        if fix_xx_coverage_area(filepath):
            files_fixed += 1
            city, state = extract_city_state_from_filename(filepath.name)
            print(f"Fixed: {city}, {get_state_name(state)}")
    
    print("\n" + "=" * 60)
    print(f"Files checked: {files_checked}")
    print(f"Files fixed: {files_fixed}")

if __name__ == '__main__':
    main()