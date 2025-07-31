#!/usr/bin/env python3
"""
Fix special city pages that don't have state codes in filenames
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Map of cities without state codes to their states
CITY_STATE_MAP = {
    'atlanta': ('Atlanta', 'GA'),
    'austin': ('Austin', 'TX'),
    'boston': ('Boston', 'MA'),
    'charlotte': ('Charlotte', 'NC'),
    'chicago': ('Chicago', 'IL'),
    'columbus': ('Columbus', 'OH'),
    'dallas': ('Dallas', 'TX'),
    'denver': ('Denver', 'CO'),
    'detroit': ('Detroit', 'MI'),
    'hartford': ('Hartford', 'CT'),
    'houston': ('Houston', 'TX'),
    'los-angeles': ('Los Angeles', 'CA'),
    'miami': ('Miami', 'FL'),
    'new-york': ('New York', 'NY'),
    'philadelphia': ('Philadelphia', 'PA'),
    'seattle': ('Seattle', 'WA')
}

def update_navigation_services(soup):
    """Update navigation to include all 4 services"""
    nav_services = soup.find('a', href='../../services/')
    if nav_services:
        dropdown = nav_services.find_next_sibling('ul', class_='dropdown')
        if dropdown:
            # Clear existing items
            dropdown.clear()
            
            # Add all 4 services
            services = [
                ('Forensic Economics', '../../services/forensic-economics/'),
                ('Business Valuation', '../../services/business-valuation/'),
                ('Vocational Expert', '../../services/vocational-expert/'),
                ('Life Care Planning', '../../services/life-care-planning/')
            ]
            
            for service_name, service_url in services:
                li = soup.new_tag('li')
                a = soup.new_tag('a', href=service_url)
                a.string = service_name
                li.append(a)
                dropdown.append(li)
    
    return soup

def update_footer_services(soup):
    """Update footer to include all 4 services"""
    footer = soup.find('footer', class_='main-footer')
    if footer:
        # Find the services section in footer
        for h4 in footer.find_all('h4'):
            if h4.string and 'Services' in h4.string:
                ul = h4.find_next_sibling('ul')
                if ul:
                    # Clear existing items
                    ul.clear()
                    
                    # Add all 4 services
                    services = [
                        ('Forensic Economics', '../../services/forensic-economics/'),
                        ('Business Valuation', '../../services/business-valuation/'),
                        ('Vocational Expert', '../../services/vocational-expert/'),
                        ('Life Care Planning', '../../services/life-care-planning/')
                    ]
                    
                    for service_name, service_url in services:
                        li = soup.new_tag('li')
                        a = soup.new_tag('a', href=service_url)
                        a.string = service_name
                        li.append(a)
                        ul.append(li)
    
    return soup

def add_comprehensive_services_section(soup, city, state):
    """Add a section that mentions all 4 services"""
    # Find where to insert the new section
    content_section = soup.find('section', class_='content-section')
    if not content_section:
        return soup
    
    # Check if section already exists
    existing_section = soup.find('section', class_='comprehensive-services')
    if existing_section:
        return soup
    
    # Create new comprehensive services section
    new_section = soup.new_tag('section', class_='comprehensive-services')
    container = soup.new_tag('div', class_='container')
    
    h2 = soup.new_tag('h2')
    h2.string = f'Comprehensive Expert Services in {city}'
    container.append(h2)
    
    intro = soup.new_tag('p')
    intro.string = f'Skerritt Economics & Consulting provides a full spectrum of expert services to attorneys and businesses throughout {city} and {state}. Our integrated approach ensures comprehensive support for all your litigation and business needs.'
    container.append(intro)
    
    # Create service cards grid
    services_grid = soup.new_tag('div', class_='services-grid')
    
    services_info = [
        {
            'title': 'Forensic Economics',
            'icon': '📊',
            'desc': f'Expert economic damage analysis for personal injury, wrongful death, employment litigation, and commercial disputes in {city}. Court-qualified expert witness with extensive federal and state court experience.',
            'link': '../../services/forensic-economics/'
        },
        {
            'title': 'Business Valuation',
            'icon': '💼',
            'desc': f'Certified business valuation analyst providing comprehensive valuations for litigation, M&A, divorce, and tax purposes. Expert knowledge of {state}\'s business environment and market conditions.',
            'link': '../../services/business-valuation/'
        },
        {
            'title': 'Vocational Expert Services',
            'icon': '👔',
            'desc': f'Professional vocational assessments, employability analysis, and labor market evaluations for disability and personal injury cases. Understanding of {city}\'s employment landscape and opportunities.',
            'link': '../../services/vocational-expert/'
        },
        {
            'title': 'Life Care Planning',
            'icon': '🏥',
            'desc': f'Comprehensive life care plans and future medical cost projections for catastrophic injury cases. Collaboration with {city}\'s medical providers for accurate cost assessments.',
            'link': '../../services/life-care-planning/'
        }
    ]
    
    for service in services_info:
        card = soup.new_tag('div', class_='service-card')
        
        icon_div = soup.new_tag('div', class_='service-icon')
        icon_div.string = service['icon']
        card.append(icon_div)
        
        h3 = soup.new_tag('h3')
        h3.string = service['title']
        card.append(h3)
        
        p = soup.new_tag('p')
        p.string = service['desc']
        card.append(p)
        
        a = soup.new_tag('a', href=service['link'], class_='service-link')
        a.string = 'Learn More →'
        card.append(a)
        
        services_grid.append(card)
    
    container.append(services_grid)
    new_section.append(container)
    
    # Insert after the main content section
    content_section.insert_after(new_section)
    
    return soup

def update_structured_data(soup):
    """Update structured data to include all services"""
    scripts = soup.find_all('script', type='application/ld+json')
    
    for script in scripts:
        try:
            # Parse JSON content
            content = script.string
            if '"@type": "ProfessionalService"' in content:
                # Update knowsAbout to include all services
                new_knows_about = '''[
            "Forensic Economics",
            "Economic Damage Analysis",
            "Business Valuation",
            "Vocational Expert Services",
            "Life Care Planning",
            "Personal Injury Economics",
            "Wrongful Death Analysis", 
            "Employment Litigation",
            "Medical Malpractice Economics",
            "Commercial Damages"
        ]'''
                
                # Replace the knowsAbout section
                content = re.sub(r'"knowsAbout":\s*\[[\s\S]*?\]', f'"knowsAbout": {new_knows_about}', content)
                
                script.string = content
        except:
            continue
    
    return soup

def add_comprehensive_services_css(soup):
    """Add CSS for the comprehensive services section"""
    # Check if CSS already exists
    existing_style = None
    for style in soup.find_all('style'):
        if style.string and '.comprehensive-services' in style.string:
            return soup
    
    style_tag = soup.new_tag('style')
    style_tag.string = '''
        .comprehensive-services {
            background: #f8fafc;
            padding: 80px 0;
        }
        
        .comprehensive-services h2 {
            text-align: center;
            color: #1e40af;
            margin-bottom: 20px;
            font-size: 2.5rem;
        }
        
        .comprehensive-services > .container > p {
            text-align: center;
            max-width: 800px;
            margin: 0 auto 60px;
            color: #4b5563;
            font-size: 1.125rem;
            line-height: 1.8;
        }
        
        .comprehensive-services .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .comprehensive-services .service-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            text-align: center;
        }
        
        .comprehensive-services .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        }
        
        .comprehensive-services .service-icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        
        .comprehensive-services .service-card h3 {
            color: #1e40af;
            margin-bottom: 15px;
            font-size: 1.5rem;
        }
        
        .comprehensive-services .service-card p {
            color: #6b7280;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .comprehensive-services .service-link {
            color: #1e40af;
            font-weight: 600;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .comprehensive-services .service-link:hover {
            color: #1e3a8a;
        }
    '''
    
    # Add style to head
    head = soup.find('head')
    if head:
        head.append(style_tag)
    
    return soup

def process_file(filepath, city_slug):
    """Process a single city page file"""
    try:
        # Get city and state info
        if city_slug not in CITY_STATE_MAP:
            print(f"Unknown city: {city_slug}")
            return False
        
        city, state = CITY_STATE_MAP[city_slug]
        
        # Read the file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Apply updates
        soup = update_navigation_services(soup)
        soup = update_footer_services(soup)
        soup = add_comprehensive_services_section(soup, city, state)
        soup = update_structured_data(soup)
        soup = add_comprehensive_services_css(soup)
        
        # Write back the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        
        print(f"Successfully updated {filepath}")
        return True
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return False

def main():
    """Main function to process special city pages"""
    cities_dir = Path('locations/cities')
    
    processed = 0
    errors = 0
    
    for city_slug in CITY_STATE_MAP.keys():
        filepath = cities_dir / f"{city_slug}-forensic-economist.html"
        if filepath.exists():
            if process_file(filepath, city_slug):
                processed += 1
            else:
                errors += 1
    
    print(f"\nCompleted! Processed {processed} files successfully, {errors} errors")

if __name__ == '__main__':
    main()