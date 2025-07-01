#!/usr/bin/env python3
"""
Add technical SEO enhancements to all pages including breadcrumb schema
"""

import os
import re
from bs4 import BeautifulSoup
import json

def get_breadcrumb_path(file_path):
    """Generate breadcrumb path based on file location"""
    rel_path = os.path.relpath(file_path, '/Users/chrisskerritt/SEC')
    parts = rel_path.split('/')
    
    breadcrumbs = [{"name": "Home", "url": "/"}]
    
    if parts[0] == 'locations':
        breadcrumbs.append({"name": "Locations", "url": "/locations/"})
        if len(parts) > 1 and parts[1] == 'cities':
            # Extract city name from filename
            filename = parts[2].replace('.html', '')
            if 'forensic-economist' in filename:
                city_state = filename.replace('-forensic-economist', '')
                service = "Forensic Economist"
            elif 'business-valuation-analyst' in filename:
                city_state = filename.replace('-business-valuation-analyst', '')
                service = "Business Valuation Analyst"
            else:
                city_state = filename
                service = ""
            
            parts_cs = city_state.split('-')
            if len(parts_cs) >= 2:
                state = parts_cs[-1].upper()
                city = ' '.join([p.capitalize() for p in parts_cs[:-1]])
                breadcrumbs.append({"name": f"{city}, {state} - {service}", "url": f"/locations/cities/{filename}.html"})
    
    elif parts[0] == 'services':
        breadcrumbs.append({"name": "Services", "url": "/services/"})
        if len(parts) > 1:
            service_name = parts[1].replace('-', ' ').title()
            breadcrumbs.append({"name": service_name, "url": f"/services/{parts[1]}/"})
    
    elif parts[0] == 'practice-areas':
        breadcrumbs.append({"name": "Practice Areas", "url": "/practice-areas/"})
        if len(parts) > 1:
            area_name = parts[1].replace('-', ' ').title()
            breadcrumbs.append({"name": area_name, "url": f"/practice-areas/{parts[1]}/"})
    
    elif parts[0] == 'about':
        breadcrumbs.append({"name": "About", "url": "/about/"})
    
    elif parts[0] == 'contact':
        breadcrumbs.append({"name": "Contact", "url": "/contact/"})
    
    elif parts[0] == 'case-studies':
        breadcrumbs.append({"name": "Case Studies", "url": "/case-studies/"})
    
    elif parts[0] == 'resources':
        breadcrumbs.append({"name": "Resources", "url": "/resources/"})
    
    return breadcrumbs

def generate_breadcrumb_schema(breadcrumbs):
    """Generate BreadcrumbList schema"""
    items = []
    for i, crumb in enumerate(breadcrumbs):
        items.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": crumb["name"],
            "item": f"https://skerritteconomics.com{crumb['url']}"
        })
    
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def add_breadcrumb_schema(file_path):
    """Add breadcrumb schema to HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check if breadcrumb schema already exists
        scripts = soup.find_all('script', type='application/ld+json')
        has_breadcrumb = False
        for script in scripts:
            if script.string and 'BreadcrumbList' in script.string:
                has_breadcrumb = True
                break
        
        if not has_breadcrumb:
            # Generate breadcrumb data
            breadcrumbs = get_breadcrumb_path(file_path)
            if len(breadcrumbs) > 1:  # Only add if there's a path
                schema = generate_breadcrumb_schema(breadcrumbs)
                
                # Create new script tag
                new_script = soup.new_tag('script', type='application/ld+json')
                new_script.string = json.dumps(schema, indent=4)
                
                # Insert after existing structured data or in head
                head = soup.find('head')
                if head:
                    # Find last script tag with structured data
                    last_ld_script = None
                    for script in scripts:
                        last_ld_script = script
                    
                    if last_ld_script:
                        last_ld_script.insert_after(new_script)
                    else:
                        head.append(new_script)
                    
                    # Save the file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    return True
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    
    return False

def enhance_seo_for_all_pages():
    """Add SEO enhancements to all HTML pages"""
    base_dir = '/Users/chrisskerritt/SEC'
    updated_count = 0
    
    # Process all HTML files
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden and special directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]
        
        for file in files:
            if file.endswith('.html') and not any(skip in file for skip in ['test-', 'review-', 'manual-', 'navigator']):
                file_path = os.path.join(root, file)
                if add_breadcrumb_schema(file_path):
                    updated_count += 1
                    print(f"Updated: {os.path.relpath(file_path, base_dir)}")
    
    print(f"\nTotal files updated: {updated_count}")

def create_state_hub_pages():
    """Create state-level hub pages that link to all cities in that state"""
    states_data = {}
    cities_dir = '/Users/chrisskerritt/SEC/locations/cities'
    
    # Collect cities by state
    for filename in os.listdir(cities_dir):
        if filename.endswith('-forensic-economist.html'):
            parts = filename.replace('-forensic-economist.html', '').split('-')
            if len(parts) >= 2 and len(parts[-1]) == 2:
                state_abbr = parts[-1].upper()
                city = ' '.join([p.capitalize() for p in parts[:-1]])
                
                if state_abbr not in states_data:
                    states_data[state_abbr] = []
                
                states_data[state_abbr].append({
                    'city': city,
                    'slug': '-'.join(parts)
                })
    
    # Create state directory if it doesn't exist
    states_dir = '/Users/chrisskerritt/SEC/locations/states'
    os.makedirs(states_dir, exist_ok=True)
    
    # State names mapping
    state_names = {
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
    
    # Create a hub page for each state
    for state_abbr, cities in states_data.items():
        if state_abbr in state_names:
            state_name = state_names[state_abbr]
            create_state_hub_page(state_abbr, state_name, sorted(cities, key=lambda x: x['city']), states_dir)
            print(f"Created state hub page for {state_name}")

def create_state_hub_page(state_abbr, state_name, cities, output_dir):
    """Create a single state hub page"""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{state_name} Forensic Economist & Business Valuation Services | Skerritt Economics</title>
    <meta name="description" content="Expert forensic economics and business valuation services throughout {state_name}. Find qualified economic experts in {len(cities)} cities across {state_abbr}.">
    <link rel="canonical" href="https://skerritteconomics.com/locations/states/{state_abbr.lower()}.html">
    <link rel="stylesheet" href="../../css/styles.css">
    <link rel="stylesheet" href="../../css/locations.css">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Skerritt Economics - {state_name}",
        "description": "Forensic economics and business valuation services in {state_name}",
        "url": "https://skerritteconomics.com/locations/states/{state_abbr.lower()}.html",
        "areaServed": {{
            "@type": "State",
            "name": "{state_name}",
            "addressCountry": "US"
        }}
    }}
    </script>
    
    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {{
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://skerritteconomics.com/"
            }},
            {{
                "@type": "ListItem",
                "position": 2,
                "name": "Locations",
                "item": "https://skerritteconomics.com/locations/"
            }},
            {{
                "@type": "ListItem",
                "position": 3,
                "name": "{state_name}",
                "item": "https://skerritteconomics.com/locations/states/{state_abbr.lower()}.html"
            }}
        ]
    }}
    </script>
</head>
<body>
    <header>
        <nav>
            <div class="nav-container">
                <a href="/" class="logo">Skerritt Economics Consulting</a>
                <ul class="nav-menu">
                    <li><a href="/about/">About</a></li>
                    <li><a href="/services/">Services</a></li>
                    <li><a href="/practice-areas/">Practice Areas</a></li>
                    <li><a href="/case-studies/">Case Studies</a></li>
                    <li><a href="/resources/">Resources</a></li>
                    <li><a href="/contact/">Contact</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <main>
        <div class="hero-section">
            <div class="hero-content">
                <h1>{state_name} Forensic Economist & Business Valuation Expert</h1>
                <p>Serving attorneys and businesses throughout {state_name} with expert economic analysis</p>
            </div>
        </div>

        <div class="container">
            <div class="breadcrumb">
                <a href="/">Home</a> › <a href="/locations/">Locations</a> › {state_name}
            </div>

            <section class="content-section">
                <h2>Expert Economic Services in {state_name}</h2>
                <p>Skerritt Economics Consulting provides comprehensive forensic economics and business valuation services throughout {state_name}. Our expertise includes economic damage calculations, business valuations, and expert witness testimony for litigation support.</p>
                
                <h3>Cities We Serve in {state_name}</h3>
                <div class="city-grid">
"""
    
    # Add cities
    for city in cities:
        html_content += f"""
                    <div class="city-card">
                        <h4>{city['city']}</h4>
                        <ul>
                            <li><a href="/locations/cities/{city['slug']}-forensic-economist.html">Forensic Economist</a></li>
                            <li><a href="/locations/cities/{city['slug']}-business-valuation-analyst.html">Business Valuation</a></li>
                        </ul>
                    </div>
"""
    
    html_content += """
                </div>
            </section>

            <section class="cta-section">
                <h2>Need Expert Economic Analysis in """ + state_name + """?</h2>
                <p>Contact us today for a consultation</p>
                <a href="/contact/" class="cta-button">Get Started</a>
            </section>
        </div>
    </main>

    <footer>
        <div class="footer-content">
            <p>&copy; 2024 Skerritt Economics Consulting. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>"""
    
    # Write the file
    output_path = os.path.join(output_dir, f"{state_abbr.lower()}.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    print("Adding SEO enhancements to all pages...")
    enhance_seo_for_all_pages()
    
    print("\nCreating state hub pages...")
    create_state_hub_pages()