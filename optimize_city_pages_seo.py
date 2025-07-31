#!/usr/bin/env python3
"""
Phase 3 SEO Optimization - City Pages
Optimizes titles and descriptions for city-specific pages
"""

import os
import re
from pathlib import Path

def create_optimized_city_title(city, state, service_type):
    """Create an optimized title for city pages"""
    # State abbreviations
    state_abbr = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
        'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
        'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
        'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
        'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
        'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
        'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
        'Wisconsin': 'WI', 'Wyoming': 'WY'
    }
    
    # Get state abbreviation
    state_short = state_abbr.get(state, state[:2].upper())
    
    # Service type shortcuts
    service_shortcuts = {
        'forensic-economist': 'Forensic Economist',
        'business-valuation': 'Business Valuation',
        'life-care-planner': 'Life Care Planner',
        'vocational-expert': 'Vocational Expert'
    }
    
    service_name = service_shortcuts.get(service_type, 'Expert')
    
    # Build optimized title (aim for under 60 chars)
    # Format: "City STATE Service | Skerritt"
    title = f"{city} {state_short} {service_name} | Skerritt"
    
    # If still too long, try shorter versions
    if len(title) > 60:
        title = f"{city} {state_short} {service_name}"
    
    return title

def create_optimized_city_description(city, state):
    """Create an optimized description for city pages"""
    # Keep it concise and under 160 chars
    desc = f"Expert forensic economics and business valuation services in {city}, {state}. Court-qualified expert witness. Free consultation."
    
    if len(desc) > 160:
        desc = f"Forensic economics and business valuation in {city}, {state}. Court-qualified expert. Free consultation."
    
    return desc

def process_city_file(filepath):
    """Process a city page HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes_made = False
    
    # Extract city and state from filename
    filename = os.path.basename(filepath)
    match = re.match(r'(.+?)-([a-z]{2})-(.+?)\.html', filename)
    
    if not match:
        return False
    
    city_slug = match.group(1)
    state_abbr = match.group(2).upper()
    service_type = match.group(3)
    
    # Convert slug to proper city name
    city_name = city_slug.replace('-', ' ').title()
    
    # Map state abbreviation to full name (simplified - you'd need complete mapping)
    state_names = {
        'CA': 'California', 'TX': 'Texas', 'FL': 'Florida', 'NY': 'New York',
        'PA': 'Pennsylvania', 'IL': 'Illinois', 'OH': 'Ohio', 'GA': 'Georgia',
        'NC': 'North Carolina', 'MI': 'Michigan', 'NJ': 'New Jersey', 'VA': 'Virginia',
        'WA': 'Washington', 'AZ': 'Arizona', 'MA': 'Massachusetts', 'TN': 'Tennessee',
        'IN': 'Indiana', 'MO': 'Missouri', 'MD': 'Maryland', 'WI': 'Wisconsin',
        'CO': 'Colorado', 'MN': 'Minnesota', 'SC': 'South Carolina', 'AL': 'Alabama',
        'LA': 'Louisiana', 'KY': 'Kentucky', 'OR': 'Oregon', 'OK': 'Oklahoma',
        'CT': 'Connecticut', 'UT': 'Utah', 'IA': 'Iowa', 'NV': 'Nevada',
        'AR': 'Arkansas', 'MS': 'Mississippi', 'KS': 'Kansas', 'NM': 'New Mexico',
        'NE': 'Nebraska', 'WV': 'West Virginia', 'ID': 'Idaho', 'HI': 'Hawaii',
        'NH': 'New Hampshire', 'ME': 'Maine', 'RI': 'Rhode Island', 'MT': 'Montana',
        'DE': 'Delaware', 'SD': 'South Dakota', 'ND': 'North Dakota', 'AK': 'Alaska',
        'VT': 'Vermont', 'WY': 'Wyoming'
    }
    
    state_name = state_names.get(state_abbr, state_abbr)
    
    # Create optimized title
    optimized_title = create_optimized_city_title(city_name, state_name, service_type)
    
    # Replace title
    title_pattern = r'<title>([^<]+)</title>'
    title_match = re.search(title_pattern, content)
    
    if title_match:
        original_title = title_match.group(1)
        if len(original_title) > 60:
            content = re.sub(title_pattern, f'<title>{optimized_title}</title>', content)
            changes_made = True
            print(f"  Title: {len(original_title)} → {len(optimized_title)} chars")
    
    # Create optimized description
    optimized_desc = create_optimized_city_description(city_name, state_name)
    
    # Replace description
    desc_pattern = r'<meta\s+name="description"\s+content="([^"]+)"'
    desc_match = re.search(desc_pattern, content)
    
    if not desc_match:
        desc_pattern = r'<meta\s+content="([^"]+)"\s+name="description"'
        desc_match = re.search(desc_pattern, content)
    
    if desc_match:
        original_desc = desc_match.group(1)
        if len(original_desc) > 160:
            new_meta = desc_match.group(0).replace(original_desc, optimized_desc)
            content = content.replace(desc_match.group(0), new_meta)
            changes_made = True
            print(f"  Description: {len(original_desc)} → {len(optimized_desc)} chars")
    
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Process city pages in batches"""
    base_path = Path('/Users/chrisskerritt/SEC')
    cities_path = base_path / 'locations' / 'cities'
    
    if not cities_path.exists():
        print("Cities directory not found!")
        return
    
    # Get all city HTML files
    city_files = list(cities_path.glob('*.html'))
    total_files = len(city_files)
    
    print(f"Phase 3 SEO Optimization - City Pages")
    print(f"Found {total_files} city pages to process")
    print("=" * 60)
    
    # Process in batches to show progress
    batch_size = 100
    files_processed = 0
    files_changed = 0
    
    for i in range(0, total_files, batch_size):
        batch = city_files[i:i+batch_size]
        print(f"\nProcessing batch {i//batch_size + 1} ({i+1}-{min(i+batch_size, total_files)} of {total_files})")
        
        for filepath in batch:
            if process_city_file(filepath):
                files_changed += 1
            files_processed += 1
        
        # Show progress
        print(f"Progress: {files_processed}/{total_files} files ({files_changed} changed)")
    
    print("\n" + "=" * 60)
    print(f"Phase 3 SEO Optimization Complete!")
    print(f"Total files processed: {files_processed}")
    print(f"Total files changed: {files_changed}")

if __name__ == '__main__':
    main()