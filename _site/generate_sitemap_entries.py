#!/usr/bin/env python3
"""
Generate sitemap entries for all location pages
"""

import os
from datetime import datetime

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# Base URL
base_url = "https://skerritteconomics.com"

def generate_location_entries():
    """Generate sitemap entries for all location pages"""
    
    entries = []
    
    # State pages
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
        "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
        "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",
        "maine", "maryland", "massachusetts", "michigan", "minnesota",
        "mississippi", "missouri", "montana", "nebraska", "nevada",
        "new-hampshire", "new-jersey", "new-mexico", "new-york",
        "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon",
        "pennsylvania", "rhode-island", "south-carolina", "south-dakota",
        "tennessee", "texas", "utah", "vermont", "virginia", "washington",
        "washington-dc", "west-virginia", "wisconsin", "wyoming"
    ]
    
    # Add state pages
    for state in states:
        entries.append(f"""  <url>
    <loc>{base_url}/locations/{state}.html</loc>
    <lastmod>{today}</lastmod>
    <priority>0.7</priority>
  </url>""")
    
    # Get all city pages
    cities_dir = "/Users/chrisskerritt/SEC/locations/cities"
    if os.path.exists(cities_dir):
        city_files = [f for f in os.listdir(cities_dir) if f.endswith('.html') and f != 'preview-system.html']
        
        # Sort by type for better organization
        city_hubs = []
        service_pages = []
        
        for file in city_files:
            if any(service in file for service in ['-forensic-economist.html', '-business-valuation-analyst.html', 
                                                   '-vocational-expert.html', '-life-care-planner.html']):
                service_pages.append(file)
            else:
                city_hubs.append(file)
        
        # Add city hub pages (higher priority)
        for file in sorted(city_hubs):
            entries.append(f"""  <url>
    <loc>{base_url}/locations/cities/{file}</loc>
    <lastmod>{today}</lastmod>
    <priority>0.6</priority>
  </url>""")
        
        # Add service-specific pages (lower priority)
        for file in sorted(service_pages):
            entries.append(f"""  <url>
    <loc>{base_url}/locations/cities/{file}</loc>
    <lastmod>{today}</lastmod>
    <priority>0.5</priority>
  </url>""")
    
    return entries

# Generate entries
location_entries = generate_location_entries()

# Write to file
with open('sitemap_location_entries.txt', 'w') as f:
    f.write('\n'.join(location_entries))

print(f"Generated {len(location_entries)} location page entries")
print("Entries saved to sitemap_location_entries.txt")