#!/usr/bin/env python3
"""
Generate city hub pages that consolidate all 4 services for each city
"""

import os
import re

# Major cities to create hub pages for (city, state abbreviation, state full name)
major_cities = [
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
    ("Tampa", "FL", "Florida"),
    ("New Orleans", "LA", "Louisiana"),
    ("Cleveland", "OH", "Ohio"),
    ("Anaheim", "CA", "California"),
    ("Honolulu", "HI", "Hawaii"),
    ("Henderson", "NV", "Nevada"),
    ("Lexington", "KY", "Kentucky"),
    ("Stockton", "CA", "California"),
    ("Corpus Christi", "TX", "Texas"),
    ("Riverside", "CA", "California"),
    ("Santa Ana", "CA", "California"),
    ("Cincinnati", "OH", "Ohio"),
    ("Irvine", "CA", "California"),
    ("Newark", "NJ", "New Jersey"),
    ("Orlando", "FL", "Florida"),
    ("Pittsburgh", "PA", "Pennsylvania"),
    ("St. Louis", "MO", "Missouri"),
    ("Lincoln", "NE", "Nebraska"),
    ("Plano", "TX", "Texas"),
    ("Anchorage", "AK", "Alaska"),
    ("Durham", "NC", "North Carolina"),
    ("Jersey City", "NJ", "New Jersey"),
    ("Chandler", "AZ", "Arizona"),
    ("Chula Vista", "CA", "California"),
    ("Buffalo", "NY", "New York"),
    ("Madison", "WI", "Wisconsin"),
    ("Lubbock", "TX", "Texas"),
    ("Scottsdale", "AZ", "Arizona"),
    ("Reno", "NV", "Nevada"),
    ("Gilbert", "AZ", "Arizona"),
    ("Glendale", "AZ", "Arizona"),
    ("North Las Vegas", "NV", "Nevada"),
    ("Norfolk", "VA", "Virginia"),
    ("Chesapeake", "VA", "Virginia"),
    ("Garland", "TX", "Texas"),
    ("Irving", "TX", "Texas"),
    ("Hialeah", "FL", "Florida"),
    ("Fremont", "CA", "California"),
    ("Boise", "ID", "Idaho"),
    ("Richmond", "VA", "Virginia"),
    ("Baton Rouge", "LA", "Louisiana"),
    ("Spokane", "WA", "Washington"),
    ("Des Moines", "IA", "Iowa"),
    ("Tacoma", "WA", "Washington"),
    ("San Bernardino", "CA", "California"),
    ("Modesto", "CA", "California"),
    ("Fontana", "CA", "California"),
    ("Santa Clarita", "CA", "California"),
    ("Birmingham", "AL", "Alabama"),
    ("Oxnard", "CA", "California"),
    ("Fayetteville", "NC", "North Carolina"),
    ("Moreno Valley", "CA", "California"),
    ("Rochester", "NY", "New York"),
    ("Glendale", "CA", "California"),
    ("Huntington Beach", "CA", "California"),
    ("Salt Lake City", "UT", "Utah"),
    ("Grand Rapids", "MI", "Michigan"),
    ("Amarillo", "TX", "Texas"),
    ("Yonkers", "NY", "New York"),
    ("Aurora", "IL", "Illinois"),
    ("Montgomery", "AL", "Alabama"),
    ("Akron", "OH", "Ohio"),
    ("Little Rock", "AR", "Arkansas"),
    ("Huntsville", "AL", "Alabama"),
    ("Augusta", "GA", "Georgia"),
    ("Port St. Lucie", "FL", "Florida"),
    ("Grand Prairie", "TX", "Texas"),
    ("Columbus", "GA", "Georgia"),
    ("Tallahassee", "FL", "Florida"),
    ("Overland Park", "KS", "Kansas"),
    ("Tempe", "AZ", "Arizona"),
    ("McKinney", "TX", "Texas"),
    ("Mobile", "AL", "Alabama"),
    ("Cape Coral", "FL", "Florida"),
    ("Knoxville", "TN", "Tennessee"),
    ("Shreveport", "LA", "Louisiana"),
    ("Frisco", "TX", "Texas"),
    ("Brownsville", "TX", "Texas"),
    ("Vancouver", "WA", "Washington"),
    ("Fort Lauderdale", "FL", "Florida"),
    ("Sioux Falls", "SD", "South Dakota"),
    ("Ontario", "CA", "California"),
    ("Chattanooga", "TN", "Tennessee"),
    ("Providence", "RI", "Rhode Island"),
    ("Newport News", "VA", "Virginia"),
    ("Rancho Cucamonga", "CA", "California"),
    ("Santa Rosa", "CA", "California"),
    ("Oceanside", "CA", "California"),
    ("Salem", "OR", "Oregon"),
    ("Fort Collins", "CO", "Colorado"),
    ("Garden Grove", "CA", "California"),
    ("Pembroke Pines", "FL", "Florida"),
    ("Eugene", "OR", "Oregon"),
    ("Corona", "CA", "California"),
    ("Cary", "NC", "North Carolina"),
    ("Springfield", "MO", "Missouri"),
    ("Jackson", "MS", "Mississippi"),
    ("Alexandria", "VA", "Virginia"),
    ("Hayward", "CA", "California"),
    ("Lancaster", "CA", "California"),
    ("Lakewood", "CO", "Colorado"),
    ("Clarksville", "TN", "Tennessee"),
    ("Palmdale", "CA", "California"),
    ("Salinas", "CA", "California"),
    ("Springfield", "MA", "Massachusetts"),
    ("Hollywood", "FL", "Florida"),
    ("Pasadena", "TX", "Texas"),
    ("Sunnyvale", "CA", "California"),
    ("Macon", "GA", "Georgia"),
    ("Kansas City", "KS", "Kansas"),
    ("Pomona", "CA", "California"),
    ("Escondido", "CA", "California"),
    ("Killeen", "TX", "Texas"),
    ("Naperville", "IL", "Illinois"),
    ("Joliet", "IL", "Illinois"),
    ("Bellevue", "WA", "Washington"),
    ("Rockford", "IL", "Illinois"),
    ("Savannah", "GA", "Georgia"),
    ("Paterson", "NJ", "New Jersey"),
    ("Torrance", "CA", "California"),
    ("Bridgeport", "CT", "Connecticut"),
    ("McAllen", "TX", "Texas"),
    ("Mesquite", "TX", "Texas"),
    ("Syracuse", "NY", "New York"),
    ("Midland", "TX", "Texas"),
    ("Pasadena", "CA", "California"),
    ("Murfreesboro", "TN", "Tennessee"),
    ("Miramar", "FL", "Florida"),
    ("Dayton", "OH", "Ohio"),
    ("Fullerton", "CA", "California"),
    ("Olathe", "KS", "Kansas"),
    ("Orange", "CA", "California"),
    ("Thornton", "CO", "Colorado"),
    ("Roseville", "CA", "California"),
    ("Denton", "TX", "Texas"),
    ("Waco", "TX", "Texas"),
    ("Surprise", "AZ", "Arizona"),
    ("Carrollton", "TX", "Texas"),
    ("West Valley City", "UT", "Utah"),
    ("Charleston", "SC", "South Carolina"),
    ("Warren", "MI", "Michigan"),
    ("Hampton", "VA", "Virginia"),
    ("Gainesville", "FL", "Florida"),
    ("Visalia", "CA", "California"),
    ("Coral Springs", "FL", "Florida"),
    ("Columbia", "SC", "South Carolina"),
    ("Cedar Rapids", "IA", "Iowa"),
    ("Sterling Heights", "MI", "Michigan"),
    ("New Haven", "CT", "Connecticut"),
    ("Stamford", "CT", "Connecticut"),
    ("Concord", "CA", "California"),
    ("Kent", "WA", "Washington"),
    ("Elizabeth", "NJ", "New Jersey"),
    ("Thousand Oaks", "CA", "California"),
    ("Lafayette", "LA", "Louisiana"),
    ("Athens", "GA", "Georgia"),
    ("Topeka", "KS", "Kansas"),
    ("Simi Valley", "CA", "California"),
    ("Round Rock", "TX", "Texas"),
    ("Hartford", "CT", "Connecticut"),
    ("Norman", "OK", "Oklahoma"),
    ("Victorville", "CA", "California"),
    ("Fargo", "ND", "North Dakota"),
    ("Berkeley", "CA", "California"),
    ("Vallejo", "CA", "California"),
    ("Clearwater", "FL", "Florida"),
    ("Carlsbad", "CA", "California"),
    ("Cambridge", "MA", "Massachusetts"),
    ("Meridian", "ID", "Idaho"),
    ("Allentown", "PA", "Pennsylvania"),
    ("Manchester", "NH", "New Hampshire"),
    ("Waterbury", "CT", "Connecticut"),
    ("Westminster", "CO", "Colorado"),
    ("Lowell", "MA", "Massachusetts"),
    ("Provo", "UT", "Utah"),
    ("West Palm Beach", "FL", "Florida"),
    ("Broken Arrow", "OK", "Oklahoma"),
    ("Lakeland", "FL", "Florida"),
    ("Evansville", "IN", "Indiana"),
    ("Independence", "MO", "Missouri"),
    ("Peoria", "IL", "Illinois"),
    ("Lansing", "MI", "Michigan"),
    ("El Monte", "CA", "California"),
    ("Abilene", "TX", "Texas"),
    ("Springfield", "IL", "Illinois"),
    ("Columbia", "MO", "Missouri"),
    ("Ann Arbor", "MI", "Michigan"),
    ("Downey", "CA", "California"),
    ("Beaumont", "TX", "Texas"),
    ("Wichita Falls", "TX", "Texas"),
    ("Wilmington", "NC", "North Carolina"),
    ("Arvada", "CO", "Colorado"),
    ("San Buenaventura", "CA", "California"),
    ("Billings", "MT", "Montana"),
    ("Clovis", "CA", "California"),
    ("Green Bay", "WI", "Wisconsin"),
    ("Davenport", "IA", "Iowa"),
    ("Rochester", "MN", "Minnesota"),
    ("Fairfield", "CA", "California"),
    ("Elgin", "IL", "Illinois"),
    ("Renton", "WA", "Washington"),
    ("South Bend", "IN", "Indiana"),
    ("Vista", "CA", "California"),
    ("Rialto", "CA", "California"),
    ("West Covina", "CA", "California"),
    ("Inglewood", "CA", "California"),
    ("Sparks", "NV", "Nevada"),
    ("Miami Gardens", "FL", "Florida"),
    ("Everett", "WA", "Washington"),
    ("Flint", "MI", "Michigan"),
    ("West Jordan", "UT", "Utah"),
    ("Clearwater", "FL", "Florida"),
    ("Manchester", "NH", "New Hampshire"),
    ("Pueblo", "CO", "Colorado"),
    ("Arvada", "CO", "Colorado"),
    ("San Angelo", "TX", "Texas"),
    ("Richardson", "TX", "Texas"),
    ("Wichita Falls", "TX", "Texas"),
    ("High Point", "NC", "North Carolina"),
    ("Richmond", "CA", "California"),
    ("Brandon", "FL", "Florida"),
    ("Pearland", "TX", "Texas"),
    ("College Station", "TX", "Texas"),
    ("Antioch", "CA", "California"),
    ("Temecula", "CA", "California"),
    ("Las Cruces", "NM", "New Mexico"),
    ("Wilmington", "DE", "Delaware"),
    ("Albany", "NY", "New York"),
    ("Greensboro", "NC", "North Carolina"),
    ("Chico", "CA", "California"),
    ("Lewisville", "TX", "Texas"),
    ("San Mateo", "CA", "California"),
    ("Tyler", "TX", "Texas"),
    ("Sandy Springs", "GA", "Georgia"),
    ("Gresham", "OR", "Oregon"),
    ("New Bedford", "MA", "Massachusetts"),
    ("Roanoke", "VA", "Virginia"),
    ("Allen", "TX", "Texas"),
    ("Rio Rancho", "NM", "New Mexico"),
    ("Jurupa Valley", "CA", "California"),
    ("Burbank", "CA", "California"),
    ("Daly City", "CA", "California"),
    ("League City", "TX", "Texas"),
    ("Fort Wayne", "IN", "Indiana"),
]

# Template for city hub page
def create_city_hub_page(city_name, state_abbr, state_full):
    # Create filename (lowercase, replace spaces with hyphens)
    filename = f"{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}.html"
    
    # Skip NYC since we already created it
    if filename == "new-york-ny.html":
        return
    
    # Handle special cases for state names in URLs
    state_url = state_full.lower().replace(' ', '-')
    
    # Generate unique city features based on location
    if state_abbr in ["CA", "NY", "IL", "TX"]:
        badge_text = "Major Metro"
    elif city_name in ["Washington", "Boston", "Philadelphia", "Atlanta", "Denver", "Seattle"]:
        badge_text = "Regional Hub"
    else:
        badge_text = "Growing Market"
    
    # Courts section varies by state
    federal_district = {
        "CA": ["Northern District", "Central District", "Southern District", "Eastern District"],
        "TX": ["Northern District", "Southern District", "Eastern District", "Western District"],
        "FL": ["Northern District", "Middle District", "Southern District"],
        "NY": ["Southern District", "Eastern District", "Northern District", "Western District"],
        "IL": ["Northern District", "Central District", "Southern District"],
        "PA": ["Eastern District", "Middle District", "Western District"],
        "OH": ["Northern District", "Southern District"],
        "MI": ["Eastern District", "Western District"],
        "GA": ["Northern District", "Middle District", "Southern District"],
        "NC": ["Eastern District", "Middle District", "Western District"],
        "VA": ["Eastern District", "Western District"],
        "MA": ["District of Massachusetts"],
        "WA": ["Eastern District", "Western District"],
        "AZ": ["District of Arizona"],
        "CO": ["District of Colorado"],
        "NV": ["District of Nevada"],
        "OR": ["District of Oregon"],
        "LA": ["Eastern District", "Middle District", "Western District"],
        "MO": ["Eastern District", "Western District"],
        "TN": ["Eastern District", "Middle District", "Western District"],
        "IN": ["Northern District", "Southern District"],
        "WI": ["Eastern District", "Western District"],
        "MN": ["District of Minnesota"],
        "NJ": ["District of New Jersey"],
        "MD": ["District of Maryland"],
        "DC": ["District of Columbia"],
    }.get(state_abbr, [f"District of {state_full}"])
    
    # State court names vary
    state_court_name = {
        "NY": "Supreme Court",
        "CA": "Superior Court",
        "TX": "District Court",
        "FL": "Circuit Court",
        "IL": "Circuit Court",
        "PA": "Court of Common Pleas",
        "OH": "Court of Common Pleas",
        "GA": "Superior Court",
        "NC": "Superior Court",
        "MI": "Circuit Court",
        "NJ": "Superior Court",
        "VA": "Circuit Court",
        "MA": "Superior Court",
        "IN": "Circuit Court",
        "MO": "Circuit Court",
        "TN": "Circuit Court",
        "MD": "Circuit Court",
        "WI": "Circuit Court",
        "MN": "District Court",
        "WA": "Superior Court",
        "AZ": "Superior Court",
        "CO": "District Court",
        "OR": "Circuit Court",
        "NV": "District Court",
        "SC": "Circuit Court",
        "AL": "Circuit Court",
        "LA": "District Court",
        "KY": "Circuit Court",
        "OK": "District Court",
        "CT": "Superior Court",
        "IA": "District Court",
        "MS": "Circuit Court",
        "AR": "Circuit Court",
        "UT": "District Court",
        "KS": "District Court",
        "NM": "District Court",
        "NE": "District Court",
        "ID": "District Court",
        "WV": "Circuit Court",
        "HI": "Circuit Court",
        "NH": "Superior Court",
        "ME": "Superior Court",
        "RI": "Superior Court",
        "MT": "District Court",
        "DE": "Superior Court",
        "SD": "Circuit Court",
        "ND": "District Court",
        "AK": "Superior Court",
        "VT": "Superior Court",
        "DC": "Superior Court",
        "WY": "District Court",
    }.get(state_abbr, "Superior Court")
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} Economic Expert Services | Forensic Economics & Business Valuation | Skerritt Economics</title>
    <meta name="description" content="Comprehensive economic expert services in {city_name}, {state_abbr}. Forensic economics, business valuation, vocational assessment, and life care planning for {city_name} attorneys and law firms.">
    <meta name="keywords" content="{city_name} economic expert, {city_name} forensic economist, {city_name} business valuation, {city_name} vocational expert, life care planner {city_name}, expert witness {city_name}">
    <link rel="canonical" href="https://skerritteconomics.com/locations/cities/{filename}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{city_name} Economic Expert Services | Skerritt Economics">
    <meta property="og:description" content="Complete economic expert services for {city_name} attorneys. Forensic economics, business valuation, vocational assessment, and life care planning.">
    <meta property="og:url" content="https://skerritteconomics.com/locations/cities/{filename}">
    <meta property="og:type" content="website">
    
    <!-- Geo Tags -->
    <meta name="geo.region" content="US-{state_abbr}">
    <meta name="geo.placename" content="{city_name}">
    
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
        "name": "Skerritt Economics - {city_name}",
        "description": "Economic expert services for {city_name} attorneys including forensic economics, business valuation, vocational assessment, and life care planning.",
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
            "addressCountry": "US",
            "containedInPlace": {{
                "@type": "State",
                "name": "{state_full}",
                "addressCountry": "US"
            }}
        }},
        "hasOfferCatalog": {{
            "@type": "OfferCatalog",
            "name": "{city_name} Economic Expert Services",
            "itemListElement": [
                {{
                    "@type": "Service",
                    "name": "Forensic Economics",
                    "url": "https://skerritteconomics.com/locations/cities/{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html"
                }},
                {{
                    "@type": "Service",
                    "name": "Business Valuation",
                    "url": "https://skerritteconomics.com/locations/cities/{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html"
                }},
                {{
                    "@type": "Service",
                    "name": "Vocational Expert",
                    "url": "https://skerritteconomics.com/locations/cities/{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-vocational-expert.html"
                }},
                {{
                    "@type": "Service",
                    "name": "Life Care Planning",
                    "url": "https://skerritteconomics.com/locations/cities/{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-life-care-planner.html"
                }}
            ]
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
                "name": "{state_full}",
                "item": "https://skerritteconomics.com/locations/{state_url}.html"
            }},
            {{
                "@type": "ListItem",
                "position": 4,
                "name": "{city_name}",
                "item": "https://skerritteconomics.com/locations/cities/{filename}"
            }}
        ]
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

    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="breadcrumb-container">
            <ol class="breadcrumb-list">
                <li class="breadcrumb-item">
                    <a class="breadcrumb-link" href="../../">Home</a>
                </li>
                <li class="breadcrumb-item">
                    <a class="breadcrumb-link" href="../../locations/">Locations</a>
                </li>
                <li class="breadcrumb-item">
                    <a class="breadcrumb-link" href="../{state_url}.html">{state_full}</a>
                </li>
                <li class="breadcrumb-item">
                    <span class="breadcrumb-current">{city_name}</span>
                </li>
            </ol>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="city-hero">
        <div class="container">
            <h1>Economic Expert Services in {city_name}</h1>
            <p class="lead">Comprehensive forensic economics and litigation support for {city_name} attorneys. Court-qualified expert witness services for all {state_full} courts.</p>
            <div class="hero-features">
                <div class="feature">
                    <span class="feature-icon">⚖️</span>
                    <span>Court-Qualified Expert</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">📊</span>
                    <span>4 Core Services</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">🏛️</span>
                    <span>{badge_text}</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Grid -->
    <section class="city-services">
        <div class="container">
            <h2>Expert Economic Services for {city_name} Attorneys</h2>
            <p class="section-intro">Choose from our comprehensive suite of economic expert services tailored for {city_name} litigation needs.</p>
            
            <div class="services-grid">
                <!-- Forensic Economics -->
                <div class="service-card featured">
                    <div class="service-header">
                        <h3>Forensic Economics</h3>
                        <span class="service-badge">Most Popular</span>
                    </div>
                    <p>Economic damage calculations for personal injury, wrongful death, and employment cases in {city_name} courts.</p>
                    <ul class="service-features">
                        <li>Lost earnings projections</li>
                        <li>Fringe benefits valuation</li>
                        <li>Household services losses</li>
                        <li>Present value calculations</li>
                        <li>Hedonic damages assessment</li>
                    </ul>
                    <div class="service-courts">
                        <strong>Courts Served:</strong>
                        <p>{state_court_name}, Federal Courts, Workers' Compensation</p>
                    </div>
                    <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html" class="btn btn-primary">{city_name} Forensic Economics →</a>
                </div>

                <!-- Business Valuation -->
                <div class="service-card">
                    <div class="service-header">
                        <h3>Business Valuation</h3>
                    </div>
                    <p>Expert business appraisals for {city_name} companies in divorce, shareholder disputes, and commercial litigation.</p>
                    <ul class="service-features">
                        <li>Fair market value assessments</li>
                        <li>Shareholder dispute valuations</li>
                        <li>Divorce business appraisals</li>
                        <li>Buy-sell agreement valuations</li>
                        <li>Economic damages for businesses</li>
                    </ul>
                    <div class="service-courts">
                        <strong>Specialties:</strong>
                        <p>Local businesses, Professional practices, Real estate</p>
                    </div>
                    <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html" class="btn btn-secondary">{city_name} Business Valuation →</a>
                </div>

                <!-- Vocational Expert -->
                <div class="service-card">
                    <div class="service-header">
                        <h3>Vocational Expert</h3>
                    </div>
                    <p>Earning capacity assessments and employability evaluations for disability and personal injury cases.</p>
                    <ul class="service-features">
                        <li>Residual earning capacity</li>
                        <li>Labor market analysis</li>
                        <li>Transferable skills assessment</li>
                        <li>Job placement probability</li>
                        <li>Vocational rehabilitation plans</li>
                    </ul>
                    <div class="service-courts">
                        <strong>Case Types:</strong>
                        <p>Personal injury, Workers' comp, Social Security disability</p>
                    </div>
                    <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-vocational-expert.html" class="btn btn-secondary">{city_name} Vocational Expert →</a>
                </div>

                <!-- Life Care Planning -->
                <div class="service-card">
                    <div class="service-header">
                        <h3>Life Care Planning</h3>
                    </div>
                    <p>Comprehensive future medical cost projections for catastrophic injury cases in {city_name}.</p>
                    <ul class="service-features">
                        <li>Future medical needs assessment</li>
                        <li>Healthcare cost analysis</li>
                        <li>Home modification costs</li>
                        <li>Assistive technology needs</li>
                        <li>Long-term care projections</li>
                    </ul>
                    <div class="service-courts">
                        <strong>Expertise:</strong>
                        <p>TBI, SCI, Birth injuries, Burn injuries, Amputations</p>
                    </div>
                    <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-life-care-planner.html" class="btn btn-secondary">{city_name} Life Care Planning →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Courts Section -->
    <section class="courts-section">
        <div class="container">
            <h2>Serving {city_name} Area Courts</h2>
            <div class="courts-grid">
                <div class="court-group">
                    <h3>{state_full} State Courts</h3>
                    <ul>
                        <li>{state_court_name} - {city_name} County</li>
                        <li>Family Court</li>
                        <li>Probate Court</li>
                        <li>Workers' Compensation Court</li>
                    </ul>
                </div>
                <div class="court-group">
                    <h3>Federal Courts</h3>
                    <ul>
                        {"<li>U.S. District Court - " + "</li><li>U.S. District Court - ".join(federal_district) + "</li>" if federal_district else "<li>U.S. District Court</li>"}
                        <li>U.S. Bankruptcy Court</li>
                    </ul>
                </div>
                <div class="court-group">
                    <h3>Service Area</h3>
                    <ul>
                        <li>{city_name} Metro Area</li>
                        <li>Surrounding Counties</li>
                        <li>Statewide {state_full} Cases</li>
                        <li>Remote Testimony Available</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Section -->
    <section class="why-choose-city">
        <div class="container">
            <h2>Why {city_name} Law Firms Choose Skerritt Economics</h2>
            <div class="benefits-grid">
                <div class="benefit">
                    <h3>Local Market Knowledge</h3>
                    <p>Deep understanding of {city_name}'s economic landscape and labor markets for accurate damage calculations.</p>
                </div>
                <div class="benefit">
                    <h3>Court Experience</h3>
                    <p>Extensive testimony experience in {state_full} courts with a proven track record of admissibility.</p>
                </div>
                <div class="benefit">
                    <h3>Rapid Response</h3>
                    <p>Quick turnaround for {city_name} attorneys with expedited services available for trial preparation.</p>
                </div>
                <div class="benefit">
                    <h3>Comprehensive Analysis</h3>
                    <p>Full-service economic expert support from initial consultation through trial testimony.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="city-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Need an Economic Expert in {city_name}?</h2>
                <p>Get experienced litigation support for your {city_name} case. Available for consultations at your office or via secure video conference.</p>
                <div class="cta-buttons">
                    <a href="../../contact/" class="btn btn-primary btn-large">Schedule {city_name} Consultation</a>
                    <a href="tel:203-605-2814" class="btn btn-secondary btn-large">Call (203) 605-2814</a>
                </div>
                <p class="cta-note">Serving all {city_name} area law firms with in-person and remote testimony options</p>
            </div>
        </div>
    </section>

    <!-- Related Services -->
    <section class="related-services">
        <div class="container">
            <h3>Explore Our {city_name} Services</h3>
            <div class="related-links">
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html" class="related-link">
                    <span class="link-icon">📊</span>
                    <span>{city_name} Forensic Economics</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html" class="related-link">
                    <span class="link-icon">💼</span>
                    <span>{city_name} Business Valuation</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-vocational-expert.html" class="related-link">
                    <span class="link-icon">👔</span>
                    <span>{city_name} Vocational Expert</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-life-care-planner.html" class="related-link">
                    <span class="link-icon">🏥</span>
                    <span>{city_name} Life Care Planning</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>{city_name} Economic Expert</h4>
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
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html">Forensic Economics</a></li>
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html">Business Valuation</a></li>
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-vocational-expert.html">Vocational Expert</a></li>
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-{state_abbr.lower()}-life-care-planner.html">Life Care Planning</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>{state_full} Locations</h4>
                    <ul>
                        <li><a href="../{state_url}.html">{state_full}</a></li>
                        <li>{city_name}</li>
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
                <p>&copy; 2025 Skerritt Economics & Consulting. Serving {city_name} and all of {state_full}.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/main.js"></script>
</body>
</html>"""
    
    # Write the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created: {filename}")

# Create hub pages for first 50 major cities
if __name__ == "__main__":
    count = 0
    for city, state_abbr, state_full in major_cities[:50]:
        create_city_hub_page(city, state_abbr, state_full)
        count += 1
    
    print(f"\nCreated {count} city hub pages successfully!")