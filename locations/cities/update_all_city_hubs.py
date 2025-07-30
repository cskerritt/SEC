#!/usr/bin/env python3
"""
Update all city hub pages with the new consistent design template
"""

import os
import re

# Updated template based on the NYC redesign
def create_updated_city_hub(city_name, state_abbr, state_full):
    """Generate updated city hub page with new design"""
    
    # URL-friendly city name
    city_slug = city_name.lower().replace(' ', '-')
    filename = f"{city_slug}-{state_abbr.lower()}.html"
    
    # Get state courts info (simplified for this example - would need full mapping)
    federal_district = get_federal_district(city_name, state_abbr)
    state_courts = get_state_courts(city_name, state_abbr)
    neighborhoods = get_neighborhoods(city_name, state_abbr)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} Expert Witness Services | {state_abbr} Forensic Economics & Business Valuation | Skerritt Economics</title>
    <meta name="description" content="Expert witness services for {city_name} law firms. Forensic economics, business valuation, vocational assessment, and life care planning. Court-qualified experts serving {city_name}, {state_abbr}.">
    <meta name="keywords" content="{city_name} expert witness, {city_name} forensic economist, {city_name} business valuation, {city_name} economic expert">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="../../css/styles.css">
    <link rel="stylesheet" href="../../css/locations.css">
    <link rel="stylesheet" href="../../css/city-pages-enhanced.css">
    <link rel="stylesheet" href="../../css/city-footer-sections.css">
    <link rel="stylesheet" href="../../css/mobile-optimized.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Skerritt Economics - {city_name} Expert Witness Services",
        "description": "Expert witness services including forensic economics, business valuation, vocational assessment, and life care planning for {city_name} attorneys.",
        "url": "https://skerritteconomics.com/locations/cities/{filename}",
        "telephone": "+12036052814",
        "email": "chris@skerritteconomics.com",
        "address": {{
            "@type": "PostalAddress",
            "streetAddress": "400 Putnam Pike Ste J",
            "addressLocality": "Smithfield",
            "addressRegion": "RI",
            "postalCode": "02917",
            "addressCountry": "US"
        }},
        "areaServed": {{
            "@type": "City",
            "name": "{city_name}",
            "addressRegion": "{state_abbr}",
            "addressCountry": "US"
        }}
    }}
    </script>
</head>
<body>
    <!-- Navigation -->
    <nav class="main-nav">
        <div class="container">
            <div class="nav-wrapper">
                <a href="../../" class="logo">
                    <strong>Skerritt Economics</strong>
                    <span>& Consulting</span>
                </a>
                <button class="mobile-menu-toggle" aria-label="Toggle menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="../../">Home</a></li>
                    <li class="has-dropdown">
                        <a href="../../services/">Services</a>
                        <ul class="dropdown">
                            <li><a href="../../services/forensic-economics/">Forensic Economics</a></li>
                            <li><a href="../../services/business-valuation/">Business Valuation</a></li>
                            <li><a href="../../services/vocational-expert/">Vocational Expert</a></li>
                            <li><a href="../../services/life-care-planning/">Life Care Planning</a></li>
                        </ul>
                    </li>
                    <li class="has-dropdown">
                        <a href="../../practice-areas/">Practice Areas</a>
                        <ul class="dropdown">
                            <li><a href="../../practice-areas/personal-injury/">Personal Injury & Wrongful Death</a></li>
                            <li><a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a></li>
                            <li><a href="../../practice-areas/employment/">Employment Litigation</a></li>
                            <li><a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a></li>
                        </ul>
                    </li>
                    <li><a href="../../case-studies/">Case Studies</a></li>
                    <li><a href="../../about/">About</a></li>
                    <li><a href="../../blog/">Blog</a></li>
                    <li><a href="../../contact/" class="nav-cta">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="city-hero">
        <div class="container">
            <h1>Expert Witness Services for {city_name} Law Firms</h1>
            <p class="lead">Court-qualified forensic economics and valuation experts serving {city_name} and surrounding {state_full} areas.</p>
            
            <div class="quick-contact">
                <div class="contact-item">
                    <strong>Call:</strong>
                    <a href="tel:203-605-2814">(203) 605-2814</a>
                </div>
                <div class="contact-item">
                    <strong>Email:</strong>
                    <a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a>
                </div>
                <div class="contact-item">
                    <strong>Available:</strong>
                    <span>All {city_name} Courts</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Overview Section -->
    <section class="services-overview">
        <div class="container">
            <h2>Expert Witness Services for {city_name} Litigation</h2>
            <p class="services-intro">Comprehensive economic analysis and expert testimony for law firms throughout {city_name}. Our experts combine rigorous methodology with deep understanding of {state_full}'s economic landscape.</p>
            
            <div class="services-grid">
                <!-- Forensic Economics - Featured -->
                <div class="service-card featured">
                    <div class="service-card-header">
                        <div class="service-icon">📊</div>
                        <h3>Forensic Economics</h3>
                    </div>
                    <div class="service-card-content">
                        <p>Economic damage calculations for personal injury, wrongful death, and employment litigation in {city_name} courts.</p>
                        <ul>
                            <li>Lost earnings and benefits analysis</li>
                            <li>{city_name}-specific wage data</li>
                            <li>Business interruption losses</li>
                            <li>Employment discrimination damages</li>
                        </ul>
                        <a href="{city_slug}-{state_abbr.lower()}-forensic-economist.html" class="service-link">{city_name} Forensic Economics →</a>
                    </div>
                </div>

                <!-- Business Valuation -->
                <div class="service-card">
                    <div class="service-card-header">
                        <div class="service-icon">💼</div>
                        <h3>Business Valuation</h3>
                    </div>
                    <div class="service-card-content">
                        <p>Professional business appraisals for {city_name} litigation and transactions.</p>
                        <ul>
                            <li>Divorce & marital dissolution</li>
                            <li>Shareholder disputes</li>
                            <li>Estate & gift tax</li>
                            <li>M&A transactions</li>
                        </ul>
                        <a href="{city_slug}-{state_abbr.lower()}-business-valuation-analyst.html" class="service-link">{city_name} Business Valuation →</a>
                    </div>
                </div>

                <!-- Vocational Expert -->
                <div class="service-card">
                    <div class="service-card-header">
                        <div class="service-icon">👔</div>
                        <h3>Vocational Expert</h3>
                    </div>
                    <div class="service-card-content">
                        <p>Employability and earning capacity assessments for disability cases.</p>
                        <ul>
                            <li>Residual earning capacity</li>
                            <li>{city_name} labor market analysis</li>
                            <li>Vocational rehabilitation</li>
                            <li>Transferable skills</li>
                        </ul>
                        <a href="{city_slug}-{state_abbr.lower()}-vocational-expert.html" class="service-link">{city_name} Vocational Expert →</a>
                    </div>
                </div>

                <!-- Life Care Planning -->
                <div class="service-card">
                    <div class="service-card-header">
                        <div class="service-icon">🏥</div>
                        <h3>Life Care Planning</h3>
                    </div>
                    <div class="service-card-content">
                        <p>Future medical cost projections for catastrophic injury cases.</p>
                        <ul>
                            <li>Medical needs assessment</li>
                            <li>{city_name} healthcare costs</li>
                            <li>Home modifications</li>
                            <li>Long-term care planning</li>
                        </ul>
                        <a href="{city_slug}-{state_abbr.lower()}-life-care-planner.html" class="service-link">{city_name} Life Care Planning →</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Courts Section -->
    <section class="local-courts">
        <div class="container">
            <h2>Serving All {city_name} Courts</h2>
            
            <div class="courts-container">
                <div class="courts-grid">
                    <!-- State Courts -->
                    <div class="court-category">
                        <h3>
                            <span class="court-icon">⚖️</span>
                            {state_full} State Courts
                        </h3>
                        <ul>
                            {state_courts}
                        </ul>
                    </div>

                    <!-- Federal Courts -->
                    <div class="court-category">
                        <h3>
                            <span class="court-icon">🏛️</span>
                            Federal Courts
                        </h3>
                        <ul>
                            <li>{federal_district}</li>
                            <li>U.S. Bankruptcy Court</li>
                        </ul>
                    </div>
                </div>

                {neighborhoods}
            </div>
        </div>
    </section>

    <!-- Why Choose Section -->
    <section class="why-choose">
        <div class="container">
            <h2>Why {city_name} Law Firms Choose Skerritt Economics</h2>
            
            <div class="benefits-grid">
                <div class="benefit-item">
                    <div class="benefit-icon">🏙️</div>
                    <h3>{city_name} Market Knowledge</h3>
                    <p>Deep understanding of {city_name}'s unique economic landscape and local business environment.</p>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">⚖️</div>
                    <h3>Court Experience</h3>
                    <p>Extensive testimony experience in {city_name} courts including state and federal jurisdictions.</p>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">⚡</div>
                    <h3>Rapid Response</h3>
                    <p>Quick turnaround for {city_name}'s litigation environment with expedited services available.</p>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">📈</div>
                    <h3>Local Economic Data</h3>
                    <p>Access to {city_name}-specific wage data, cost of living indices, and labor market statistics.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="city-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Need an Expert Witness for Your {city_name} Case?</h2>
                <p>Get experienced economic analysis and expert testimony for your litigation matter. Available for cases throughout {city_name} and {state_full}.</p>
                
                <div class="cta-buttons">
                    <a href="../../contact/" class="btn btn-large btn-white">Schedule {city_name} Consultation</a>
                    <a href="tel:203-605-2814" class="btn btn-large btn-outline-white">Call (203) 605-2814</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Service Links Footer -->
    <section class="service-links-section">
        <div class="container">
            <div class="service-links-grid">
                <a href="{city_slug}-{state_abbr.lower()}-forensic-economist.html" class="service-link-card">
                    <span class="service-link-icon">📊</span>
                    <h4>{city_name} Forensic Economics</h4>
                    <p>Economic damage calculations</p>
                </a>
                
                <a href="{city_slug}-{state_abbr.lower()}-business-valuation-analyst.html" class="service-link-card">
                    <span class="service-link-icon">💼</span>
                    <h4>{city_name} Business Valuation</h4>
                    <p>Professional appraisals</p>
                </a>
                
                <a href="{city_slug}-{state_abbr.lower()}-vocational-expert.html" class="service-link-card">
                    <span class="service-link-icon">👔</span>
                    <h4>{city_name} Vocational Expert</h4>
                    <p>Employability assessments</p>
                </a>
                
                <a href="{city_slug}-{state_abbr.lower()}-life-care-planner.html" class="service-link-card">
                    <span class="service-link-icon">🏥</span>
                    <h4>{city_name} Life Care Planning</h4>
                    <p>Future medical costs</p>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>{city_name} Expert Witness Services</h4>
                    <p>Skerritt Economics & Consulting</p>
                    <p class="footer-contact">
                        400 Putnam Pike Ste J<br>
                        Smithfield, RI 02917<br>
                        <a href="tel:203-605-2814">(203) 605-2814</a><br>
                        <a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a>
                    </p>
                </div>
                <div class="footer-col">
                    <h4>{city_name} Services</h4>
                    <ul>
                        <li><a href="{city_slug}-{state_abbr.lower()}-forensic-economist.html">Forensic Economics</a></li>
                        <li><a href="{city_slug}-{state_abbr.lower()}-business-valuation-analyst.html">Business Valuation</a></li>
                        <li><a href="{city_slug}-{state_abbr.lower()}-vocational-expert.html">Vocational Expert</a></li>
                        <li><a href="{city_slug}-{state_abbr.lower()}-life-care-planner.html">Life Care Planning</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Nearby Locations</h4>
                    <ul>
                        <li><a href="../{state_abbr.lower()}.html">{state_full}</a></li>
                        {get_nearby_states(state_abbr)}
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="../../case-studies/">Case Studies</a></li>
                        <li><a href="../../blog/">Blog</a></li>
                        <li><a href="../../about/">About</a></li>
                        <li><a href="../../contact/">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Skerritt Economics & Consulting. Expert witness services throughout {city_name}, {state_full}.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/main.js"></script>
</body>
</html>"""
    
    return filename, html_content

def get_federal_district(city, state):
    """Get federal district court for city"""
    federal_districts = {
        ("Los Angeles", "CA"): "U.S. District Court for the Central District of California",
        ("San Francisco", "CA"): "U.S. District Court for the Northern District of California",
        ("San Diego", "CA"): "U.S. District Court for the Southern District of California",
        ("Sacramento", "CA"): "U.S. District Court for the Eastern District of California",
        ("Chicago", "IL"): "U.S. District Court for the Northern District of Illinois",
        ("Houston", "TX"): "U.S. District Court for the Southern District of Texas",
        ("Dallas", "TX"): "U.S. District Court for the Northern District of Texas",
        ("Austin", "TX"): "U.S. District Court for the Western District of Texas",
        ("Phoenix", "AZ"): "U.S. District Court for the District of Arizona",
        ("Philadelphia", "PA"): "U.S. District Court for the Eastern District of Pennsylvania",
        ("Boston", "MA"): "U.S. District Court for the District of Massachusetts",
        ("Miami", "FL"): "U.S. District Court for the Southern District of Florida",
        ("Jacksonville", "FL"): "U.S. District Court for the Middle District of Florida",
        ("Atlanta", "GA"): "U.S. District Court for the Northern District of Georgia",
        ("Seattle", "WA"): "U.S. District Court for the Western District of Washington",
        ("Denver", "CO"): "U.S. District Court for the District of Colorado",
        ("Detroit", "MI"): "U.S. District Court for the Eastern District of Michigan",
        # Add more as needed
    }
    
    return federal_districts.get((city, state), f"U.S. District Court for {state}")

def get_state_courts(city, state):
    """Get state court listings for city"""
    # This would be expanded with full court information
    if state == "CA":
        return f"""<li>{city} County Superior Court</li>
                            <li>California Court of Appeal</li>
                            <li>Small Claims Court</li>
                            <li>Family Court</li>"""
    elif state == "TX":
        return f"""<li>{city} County District Court</li>
                            <li>County Court at Law</li>
                            <li>Justice of the Peace Court</li>
                            <li>Municipal Court</li>"""
    elif state == "NY":
        return f"""<li>Supreme Court - {city} County</li>
                            <li>County Court</li>
                            <li>Family Court</li>
                            <li>Surrogate's Court</li>"""
    else:
        return f"""<li>{city} County Court</li>
                            <li>Circuit Court</li>
                            <li>District Court</li>
                            <li>Family Court</li>"""

def get_neighborhoods(city, state):
    """Get neighborhoods section if applicable"""
    # Only show for major cities
    major_cities = ["Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", 
                    "San Antonio", "San Diego", "Dallas", "San Francisco", "Boston",
                    "Seattle", "Denver", "Atlanta", "Miami", "Washington"]
    
    if city not in major_cities:
        return ""
    
    return f"""
                <!-- Neighborhoods Section -->
                <div class="neighborhoods-section">
                    <h3>{city} Areas Served</h3>
                    <div class="neighborhoods-grid">
                        <div class="borough-item">
                            <h4>Downtown & Central</h4>
                            <p>Financial District, Downtown Core, Business District, Civic Center</p>
                        </div>
                        <div class="borough-item">
                            <h4>Surrounding Areas</h4>
                            <p>Suburban communities, neighboring cities, and metropolitan region</p>
                        </div>
                    </div>
                </div>"""

def get_nearby_states(state):
    """Get nearby states for footer"""
    nearby = {
        "CA": ["<li><a href='../nevada.html'>Nevada</a></li>", "<li><a href='../arizona.html'>Arizona</a></li>", "<li><a href='../oregon.html'>Oregon</a></li>"],
        "TX": ["<li><a href='../oklahoma.html'>Oklahoma</a></li>", "<li><a href='../louisiana.html'>Louisiana</a></li>", "<li><a href='../new-mexico.html'>New Mexico</a></li>"],
        "NY": ["<li><a href='../new-jersey.html'>New Jersey</a></li>", "<li><a href='../connecticut.html'>Connecticut</a></li>", "<li><a href='../pennsylvania.html'>Pennsylvania</a></li>"],
        "FL": ["<li><a href='../georgia.html'>Georgia</a></li>", "<li><a href='../alabama.html'>Alabama</a></li>", "<li><a href='../south-carolina.html'>South Carolina</a></li>"],
    }
    
    return "\n                        ".join(nearby.get(state, ["<li><a href='../index.html'>All States</a></li>"]))

# List of all cities to update
cities = [
    ("Los Angeles", "CA", "California"),
    ("Chicago", "IL", "Illinois"),
    ("Houston", "TX", "Texas"),
    ("Phoenix", "AZ", "Arizona"),
    ("Philadelphia", "PA", "Pennsylvania"),
    ("San Antonio", "TX", "Texas"),
    ("San Diego", "CA", "California"),
    ("Dallas", "TX", "Texas"),
    ("San Jose", "CA", "California"),
    ("Austin", "TX", "Texas"),
    ("Jacksonville", "FL", "Florida"),
    ("San Francisco", "CA", "California"),
    ("Columbus", "OH", "Ohio"),
    ("Fort Worth", "TX", "Texas"),
    ("Indianapolis", "IN", "Indiana"),
    ("Charlotte", "NC", "North Carolina"),
    ("Seattle", "WA", "Washington"),
    ("Denver", "CO", "Colorado"),
    ("Washington", "DC", "District of Columbia"),
    ("Boston", "MA", "Massachusetts"),
    ("El Paso", "TX", "Texas"),
    ("Nashville", "TN", "Tennessee"),
    ("Detroit", "MI", "Michigan"),
    ("Oklahoma City", "OK", "Oklahoma"),
    ("Portland", "OR", "Oregon"),
    ("Las Vegas", "NV", "Nevada"),
    ("Memphis", "TN", "Tennessee"),
    ("Louisville", "KY", "Kentucky"),
    ("Baltimore", "MD", "Maryland"),
    ("Milwaukee", "WI", "Wisconsin"),
    ("Albuquerque", "NM", "New Mexico"),
    ("Tucson", "AZ", "Arizona"),
    ("Fresno", "CA", "California"),
    ("Sacramento", "CA", "California"),
    ("Mesa", "AZ", "Arizona"),
    ("Kansas City", "MO", "Missouri"),
    ("Atlanta", "GA", "Georgia"),
    ("Omaha", "NE", "Nebraska"),
    ("Colorado Springs", "CO", "Colorado"),
    ("Raleigh", "NC", "North Carolina"),
    ("Long Beach", "CA", "California"),
    ("Virginia Beach", "VA", "Virginia"),
    ("Miami", "FL", "Florida"),
    ("Oakland", "CA", "California"),
    ("Minneapolis", "MN", "Minnesota"),
    ("Tulsa", "OK", "Oklahoma"),
    ("Bakersfield", "CA", "California"),
    ("Wichita", "KS", "Kansas"),
    ("Arlington", "TX", "Texas"),
    ("Aurora", "CO", "Colorado"),
]

# Update all city hub pages
updated_count = 0
for city_data in cities:
    city_name, state_abbr, state_full = city_data
    filename, html_content = create_updated_city_hub(city_name, state_abbr, state_full)
    
    # Skip NYC since we already updated it
    if city_name == "New York City":
        continue
    
    try:
        with open(filename, 'w') as f:
            f.write(html_content)
        print(f"Updated: {filename}")
        updated_count += 1
    except Exception as e:
        print(f"Error updating {filename}: {e}")

print(f"\nTotal city hub pages updated: {updated_count}")