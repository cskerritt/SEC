#!/usr/bin/env python3
"""
Script to fix NYC template content on non-NYC city pages
"""
import os
import re
import glob
from pathlib import Path

def get_state_info(filename):
    """Extract state info from filename"""
    # Extract city and state from filename like "city-state-forensic-economist.html"
    basename = os.path.basename(filename)
    parts = basename.replace('-forensic-economist.html', '').split('-')
    
    if len(parts) >= 2:
        state_abbr = parts[-1].upper()
        city_name = ' '.join(parts[:-1]).title()
        
        # State name mapping
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

def get_federal_court_district(state_abbr):
    """Get federal court district for state"""
    federal_courts = {
        'AL': 'Northern, Middle, and Southern Districts of Alabama',
        'AK': 'District of Alaska',
        'AZ': 'District of Arizona',
        'AR': 'Eastern and Western Districts of Arkansas',
        'CA': 'Northern, Central, Eastern, and Southern Districts of California',
        'CO': 'District of Colorado',
        'CT': 'District of Connecticut',
        'DE': 'District of Delaware',
        'FL': 'Northern, Middle, and Southern Districts of Florida',
        'GA': 'Northern, Middle, and Southern Districts of Georgia',
        'HI': 'District of Hawaii',
        'ID': 'District of Idaho',
        'IL': 'Northern, Central, and Southern Districts of Illinois',
        'IN': 'Northern and Southern Districts of Indiana',
        'IA': 'Northern and Southern Districts of Iowa',
        'KS': 'District of Kansas',
        'KY': 'Eastern and Western Districts of Kentucky',
        'LA': 'Eastern, Middle, and Western Districts of Louisiana',
        'ME': 'District of Maine',
        'MD': 'District of Maryland',
        'MA': 'District of Massachusetts',
        'MI': 'Eastern and Western Districts of Michigan',
        'MN': 'District of Minnesota',
        'MS': 'Northern and Southern Districts of Mississippi',
        'MO': 'Eastern and Western Districts of Missouri',
        'MT': 'District of Montana',
        'NE': 'District of Nebraska',
        'NV': 'District of Nevada',
        'NH': 'District of New Hampshire',
        'NJ': 'District of New Jersey',
        'NM': 'District of New Mexico',
        'NY': 'Southern, Eastern, Northern, and Western Districts of New York',
        'NC': 'Eastern, Middle, and Western Districts of North Carolina',
        'ND': 'District of North Dakota',
        'OH': 'Northern and Southern Districts of Ohio',
        'OK': 'Eastern, Northern, and Western Districts of Oklahoma',
        'OR': 'District of Oregon',
        'PA': 'Eastern, Middle, and Western Districts of Pennsylvania',
        'RI': 'District of Rhode Island',
        'SC': 'District of South Carolina',
        'SD': 'District of South Dakota',
        'TN': 'Eastern, Middle, and Western Districts of Tennessee',
        'TX': 'Northern, Southern, Eastern, and Western Districts of Texas',
        'UT': 'District of Utah',
        'VT': 'District of Vermont',
        'VA': 'Eastern and Western Districts of Virginia',
        'WA': 'Eastern and Western Districts of Washington',
        'WV': 'Northern and Southern Districts of West Virginia',
        'WI': 'Eastern and Western Districts of Wisconsin',
        'WY': 'District of Wyoming'
    }
    return federal_courts.get(state_abbr, f'District of {state_abbr}')

def fix_city_file(filepath):
    """Fix NYC template content in a city file"""
    city_name, state_abbr, state_name = get_state_info(filepath)
    
    if not city_name or not state_abbr:
        print(f"Could not parse city/state from {filepath}")
        return False
    
    # Skip NYC files
    if state_abbr == 'NY' and any(borough in filepath.lower() for borough in ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten-island']):
        return False
    
    print(f"Fixing {city_name}, {state_abbr}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Store original content for comparison
        original_content = content
        
        # Fix NYC-specific references
        replacements = [
            # Hero section borough references
            (r'throughout Manhattan, Brooklyn, Queens, Bronx, and Staten Island', f'throughout {state_name}'),
            
            # General NYC litigation references
            (r'NYC litigation', f'{state_name} litigation'),
            (r'New York litigation', f'{state_name} litigation'),
            (r'demanding requirements of NYC litigation', f'demanding requirements of {state_name} litigation'),
            (r'serving attorneys throughout the five boroughs', f'serving attorneys throughout {state_name}'),
            
            # Economic landscape references
            (r'Woonsocket presents unique challenges for economic damage calculations\. The highest wages in the nation, complex career trajectories, substantial benefits packages, and significant cost of living variations across the five boroughs all require specialized expertise\. Our forensic economic analysis accounts for:',
             f'{city_name} and the surrounding {state_name} region present unique challenges for economic damage calculations. The diverse local economy, varying industry sectors, and regional market conditions all require specialized expertise. Our forensic economic analysis accounts for:'),
            
            # Borough-specific industry lists
            (r'<li><strong>Manhattan Premium Wages:</strong> Financial services, law firms, and corporate headquarters</li>\s*<li><strong>Brooklyn Industries:</strong> Manufacturing, healthcare, technology, and creative sectors</li>\s*<li><strong>Queens Economic Diversity:</strong> Healthcare, education, small business, and international trade</li>\s*<li><strong>Bronx Growth Sectors:</strong> Healthcare, education, government, and emerging tech</li>\s*<li><strong>Staten Island Economy:</strong> Healthcare, government, small business, and manufacturing</li>',
             f'<li><strong>Local Economy:</strong> Diverse industry sectors including healthcare, education, and business services</li>\n                            <li><strong>Regional Markets:</strong> Manufacturing, retail, government, and professional services</li>\n                            <li><strong>Employment Base:</strong> Public and private sector employment opportunities</li>\n                            <li><strong>Market Integration:</strong> Connections to regional and national markets</li>'),
            
            # Court system references
            (r'New York\'s federal and state court systems', f'{state_name}\'s federal and state court systems'),
            (r'New York federal court experience', f'{state_name} federal court experience'),
            (r'New York state court experience', f'{state_name} state court experience'),
            (r'specific to New York litigation', f'specific to {state_name} litigation'),
            
            # Case type headers
            (r'Why Choose a Forensic Economist for Your New York Case\?', f'Why Choose a Forensic Economist for Your {state_name} Case?'),
            (r'Our practice covers the full spectrum of forensic economics applications in New York litigation:', f'Our practice covers the full spectrum of forensic economics applications in {state_name} litigation:'),
            
            # Business valuation headers
            (r'Business Valuation for NYC Markets', f'Business Valuation for {state_name} Markets'),
        ]
        
        # Apply replacements
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            print(f"No changes needed for {filepath}")
            return False
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function"""
    cities_dir = Path(__file__).resolve().parent / 'locations' / 'cities'
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(cities_dir, "*.html"))
    
    # Filter out NYC borough files
    nyc_boroughs = ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten-island']
    non_nyc_files = [f for f in html_files if not any(borough in f.lower() for borough in nyc_boroughs)]
    
    print(f"Found {len(non_nyc_files)} non-NYC city files to process")
    
    fixed_count = 0
    for filepath in non_nyc_files:
        if fix_city_file(filepath):
            fixed_count += 1
    
    print(f"\nCompleted! Fixed {fixed_count} files")

if __name__ == "__main__":
    main()