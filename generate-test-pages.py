#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Test cities data
test_cities = [
    {
        "city": "Providence",
        "city_lower": "providence",
        "city_slug": "providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "state_abbr_lower": "ri",
        "lat": "41.8240",
        "lon": "-71.4128",
        "nearby_cities": ["Warwick", "Cranston", "Pawtucket", "East Providence", "Woonsocket"],
        "city_specific_intro_vocational": "As the capital city of Rhode Island and home to major employers like Brown University, Lifespan Health System, and Citizens Bank, Providence presents unique vocational assessment challenges. Our expertise includes evaluating opportunities in healthcare, education, financial services, and the growing technology sector that has emerged in the Providence metropolitan area.",
        "city_specific_intro_life_care": "Providence is home to world-class medical facilities including Rhode Island Hospital, Hasbro Children's Hospital, and The Miriam Hospital. Our life care plans incorporate the exceptional medical resources available in Providence while accounting for the specific costs and accessibility of specialized care in the Rhode Island healthcare market."
    },
    {
        "city": "Boston",
        "city_lower": "boston",
        "city_slug": "boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "state_abbr_lower": "ma",
        "lat": "42.3601",
        "lon": "-71.0589",
        "nearby_cities": ["Cambridge", "Quincy", "Newton", "Somerville", "Brookline"],
        "city_specific_intro_vocational": "Boston's diverse economy, anchored by world-renowned hospitals, universities, and financial institutions, requires sophisticated vocational analysis. We understand the unique employment landscape of Greater Boston, from biotech corridors in Cambridge to financial districts downtown, enabling accurate assessment of earning capacity across all sectors.",
        "city_specific_intro_life_care": "With premier medical institutions like Massachusetts General Hospital, Brigham and Women's Hospital, and Boston Children's Hospital, Boston offers unparalleled medical care options. Our life care plans leverage these world-class resources while carefully projecting the premium costs associated with Boston's high-quality healthcare market."
    },
    {
        "city": "Hartford",
        "city_lower": "hartford",
        "city_slug": "hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "state_abbr_lower": "ct",
        "lat": "41.7658",
        "lon": "-72.6734",
        "nearby_cities": ["West Hartford", "East Hartford", "Manchester", "New Britain", "Middletown"],
        "city_specific_intro_vocational": "As Connecticut's capital and the 'Insurance Capital of the World,' Hartford's employment market is dominated by insurance, healthcare, and government sectors. Our vocational assessments account for the specialized skills required in Hartford's insurance industry and the competitive job market for professional positions.",
        "city_specific_intro_life_care": "Hartford Hospital, Connecticut Children's Medical Center, and Saint Francis Hospital anchor the region's healthcare system. Our life care plans incorporate Hartford's comprehensive medical resources while considering Connecticut's healthcare costs and insurance regulations that impact long-term care planning."
    },
    {
        "city": "Burlington",
        "city_lower": "burlington",
        "city_slug": "burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "state_abbr_lower": "vt",
        "lat": "44.4759",
        "lon": "-73.2121",
        "nearby_cities": ["South Burlington", "Essex", "Colchester", "Winooski", "Shelburne"],
        "city_specific_intro_vocational": "Burlington's economy, centered on healthcare, education, and technology, presents unique vocational considerations. As Vermont's largest city and home to the University of Vermont Medical Center and UVM, we understand the local employment dynamics and opportunities for vocational rehabilitation in this progressive market.",
        "city_specific_intro_life_care": "The University of Vermont Medical Center serves as the region's only academic medical center, providing specialized care for complex cases. Our life care plans account for Burlington's role as Vermont's medical hub while considering travel requirements for highly specialized treatments that may require out-of-state care."
    },
    {
        "city": "Portland",
        "city_lower": "portland",
        "city_slug": "portland",
        "state": "Maine",
        "state_abbr": "ME",
        "state_abbr_lower": "me",
        "lat": "43.6615",
        "lon": "-70.2553",
        "nearby_cities": ["South Portland", "Westbrook", "Scarborough", "Biddeford", "Saco"],
        "city_specific_intro_vocational": "Portland's diverse economy encompasses healthcare, tourism, technology, and Maine's largest seaport. Our vocational assessments consider the seasonal nature of some employment, the growing tech sector, and the strong healthcare industry anchored by Maine Medical Center, providing comprehensive earning capacity analysis.",
        "city_specific_intro_life_care": "Maine Medical Center, New England's second-largest medical center, provides comprehensive specialty care for the region. Our life care plans utilize Portland's medical resources while accounting for Maine's rural geography and the potential need for travel to Boston for certain ultra-specialized treatments."
    }
]

def create_page(template_path, city_data, service_type):
    """Generate a page from template with city data"""
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Replace all placeholders
    page_content = template
    page_content = page_content.replace("{{CITY}}", city_data["city"])
    page_content = page_content.replace("{{CITY_LOWER}}", city_data["city_lower"])
    page_content = page_content.replace("{{CITY_SLUG}}", city_data["city_slug"])
    page_content = page_content.replace("{{STATE}}", city_data["state"])
    page_content = page_content.replace("{{STATE_ABBR}}", city_data["state_abbr"])
    page_content = page_content.replace("{{STATE_ABBR_LOWER}}", city_data["state_abbr_lower"])
    page_content = page_content.replace("{{LAT}}", city_data["lat"])
    page_content = page_content.replace("{{LON}}", city_data["lon"])
    
    # Create nearby cities list
    nearby_cities_html = "\n".join([f'<li><a href="{city.lower().replace(" ", "-")}-{city_data["state_abbr_lower"]}-{service_type}.html">{city}</a></li>' 
                                   for city in city_data["nearby_cities"]])
    page_content = page_content.replace("{{NEARBY_CITIES_LIST}}", nearby_cities_html)
    
    # Add city-specific intro
    if service_type == "vocational-expert":
        page_content = page_content.replace("{{CITY_SPECIFIC_INTRO}}", city_data["city_specific_intro_vocational"])
    else:
        page_content = page_content.replace("{{CITY_SPECIFIC_INTRO}}", city_data["city_specific_intro_life_care"])
    
    return page_content

def main():
    # Create test-pages directory
    test_dir = Path("/Users/chrisskerritt/SEC/test-pages")
    test_dir.mkdir(exist_ok=True)
    
    # Template paths
    vocational_template = "/Users/chrisskerritt/SEC/templates/city-vocational-expert-template.html"
    life_care_template = "/Users/chrisskerritt/SEC/templates/city-life-care-planning-template.html"
    
    # Generate pages
    generated_files = []
    
    for city_data in test_cities:
        # Generate vocational expert page
        vocational_content = create_page(vocational_template, city_data, "vocational-expert")
        vocational_filename = f"{city_data['city_slug']}-{city_data['state_abbr_lower']}-vocational-expert.html"
        vocational_path = test_dir / vocational_filename
        
        with open(vocational_path, 'w') as f:
            f.write(vocational_content)
        generated_files.append(vocational_filename)
        
        # Generate life care planning page
        life_care_content = create_page(life_care_template, city_data, "life-care-planner")
        life_care_filename = f"{city_data['city_slug']}-{city_data['state_abbr_lower']}-life-care-planner.html"
        life_care_path = test_dir / life_care_filename
        
        with open(life_care_path, 'w') as f:
            f.write(life_care_content)
        generated_files.append(life_care_filename)
    
    print(f"Generated {len(generated_files)} test pages in /test-pages/:")
    for filename in generated_files:
        print(f"  - {filename}")

if __name__ == "__main__":
    main()