#!/usr/bin/env python3
"""
Generate city-pages-data.js with comprehensive city data for the sitemap
"""

import os
import re
import json
from pathlib import Path

def extract_city_state_from_filename(filename):
    """Extract city and state from filename like 'albany-ny-forensic-economist.html'"""
    # Remove .html extension
    name = filename.replace('.html', '')
    
    # Remove service type suffixes
    name = name.replace('-forensic-economist', '').replace('-business-valuation-analyst', '')
    
    # Skip files without state abbreviations (like 'atlanta-forensic-economist.html')
    if len(name.split('-')) < 2:
        return None, None, None
    
    # Extract state abbreviation (last part)
    parts = name.split('-')
    last_part = parts[-1].upper()
    
    # Check if last part is a valid state abbreviation (2 letters)
    if len(last_part) == 2 and last_part.isalpha():
        state_abbr = last_part
        city_parts = parts[:-1]
        city = ' '.join([part.capitalize() for part in city_parts])
        return city, state_abbr, '-'.join(parts)
    
    return None, None, None

def get_state_name(abbr):
    """Convert state abbreviation to full name"""
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

BASE_DIR = Path(__file__).resolve().parent

def generate_city_data():
    """Generate comprehensive city data"""
    cities_dir = BASE_DIR / 'locations' / 'cities'
    city_data = {}
    
    # Get all HTML files in cities directory
    for filename in os.listdir(cities_dir):
        if filename.endswith('.html') and 'forensic-economist' in filename:
            city, state_abbr, slug = extract_city_state_from_filename(filename)
            
            if city and state_abbr:
                # Use city-state as key to avoid duplicates
                key = f"{city}, {state_abbr}"
                if key not in city_data:
                    city_data[key] = {
                        'city': city,
                        'state': get_state_name(state_abbr),
                        'stateAbbr': state_abbr,
                        'slug': slug
                    }
    
    # Convert to list and sort by state, then city
    city_list = list(city_data.values())
    city_list.sort(key=lambda x: (x['state'], x['city']))
    
    # Generate JavaScript file
    js_content = 'window.cityData = ' + json.dumps(city_list, indent=2) + ';'

    output_path = BASE_DIR / 'city-pages-data.js'
    with open(output_path, 'w') as f:
        f.write(js_content)
    
    print(f"Generated city-pages-data.js with {len(city_list)} cities")
    
    # Print summary by state
    states_summary = {}
    for city in city_list:
        state = city['state']
        if state not in states_summary:
            states_summary[state] = 0
        states_summary[state] += 1
    
    print("\nCities by state:")
    for state in sorted(states_summary.keys()):
        print(f"  {state}: {states_summary[state]} cities")

if __name__ == "__main__":
    generate_city_data()