#!/usr/bin/env python3
"""
Comprehensive script to fix all remaining NYC template issues in city pages
"""
import os
import re
import glob

def get_state_info(filename):
    """Extract state info from filename"""
    basename = os.path.basename(filename)
    parts = basename.replace('-forensic-economist.html', '').split('-')
    
    if len(parts) >= 2:
        state_abbr = parts[-1].upper()
        city_name = ' '.join(parts[:-1]).title()
        
        state_names = {
            'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
            'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
            'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
            'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
            'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
            'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
            'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
            'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
            'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
            'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
        }
        
        state_name = state_names.get(state_abbr, state_abbr)
        return city_name, state_abbr, state_name
    
    return None, None, None

def fix_remaining_issues(filepath):
    """Fix all remaining NYC template content"""
    city_name, state_abbr, state_name = get_state_info(filepath)
    
    if not city_name or not state_abbr:
        return False
    
    # Skip NYC files
    if state_abbr == 'NY' and any(borough in filepath.lower() for borough in ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten-island']):
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Comprehensive replacements for remaining issues
        replacements = [
            # Five boroughs references - most critical fix
            (r'throughout the five boroughs', f'throughout {state_name}'),
            (r'across the five boroughs', f'across {state_name}'),
            (r'within the five boroughs', f'within {state_name}'),
            (r'the five boroughs', f'{state_name}'),
            
            # More specific NYC references that might have been missed
            (r'serving attorneys throughout the five boroughs', f'serving attorneys throughout {state_name}'),
            (r'variations across the five boroughs', f'variations across {state_name}'),
            (r'cost of living variations across the five boroughs', f'regional market conditions across {state_name}'),
            
            # Economic challenge descriptions that reference NYC specifics
            (r'The highest wages in the nation, complex career trajectories, substantial benefits packages, and significant cost of living variations across the five boroughs all require specialized expertise',
             f'The diverse local economy, varying industry sectors, and regional market conditions all require specialized expertise'),
            
            # Any remaining NYC-specific economic descriptions
            (r'highest wages in the nation.*?across the five boroughs.*?specialized expertise',
             f'diverse local economy, varying industry sectors, and regional market conditions all require specialized expertise'),
            
            # Additional patterns that might have been missed
            (r'demanding requirements of NYC litigation', f'demanding requirements of {state_name} litigation'),
            (r'NYC\'s complex legal environment', f'{state_name}\'s complex legal environment'),
            (r'nation\'s largest legal market', f'{state_name} legal market'),
            
            # Metro area corrections for specific problematic patterns
            (f'{city_name} Metro Area, Greater {city_name}, {city_name} Business District', 
             f'{city_name} metropolitan area and surrounding {state_name} region'),
        ]
        
        # Apply all replacements
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
        
        # Additional cleanup for any remaining problematic phrases
        # Remove any references to "Manhattan," "Brooklyn," etc. that might remain
        borough_pattern = r'\b(Manhattan|Brooklyn|Queens|Bronx|Staten Island)[^,]*,'
        content = re.sub(borough_pattern, '', content, flags=re.IGNORECASE)
        
        # Clean up any double spaces or formatting issues from removals
        content = re.sub(r'\s+', ' ', content)
        content = re.sub(r'\s*,\s*,', ',', content)
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function"""
    cities_dir = "/Users/chrisskerritt/SEC/locations/cities"
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(cities_dir, "*.html"))
    
    # Filter out NYC borough files
    nyc_boroughs = ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten-island']
    non_nyc_files = [f for f in html_files if not any(borough in f.lower() for borough in nyc_boroughs)]
    
    print(f"Found {len(non_nyc_files)} non-NYC city files to process")
    
    fixed_count = 0
    for filepath in non_nyc_files:
        if fix_remaining_issues(filepath):
            fixed_count += 1
            city_name = os.path.basename(filepath).split('-')[0].title()
            print(f"Fixed: {city_name}")
    
    print(f"\nCompleted! Fixed {fixed_count} additional files")

if __name__ == "__main__":
    main()