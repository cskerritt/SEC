#!/usr/bin/env python3

import os

def create_forensic_economist_page(city_name, state_abbr, state_full, federal_district, state_courts):
    """Generate a city-specific forensic economist page"""
    
    filename = f"{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} Forensic Economist | Economic Damage Expert | Skerritt Economics</title>
    <meta name="description" content="Expert forensic economist serving {city_name}, {state_abbr}. Economic damage calculations for personal injury, wrongful death, and employment litigation. Court-qualified expert witness.">
    <meta name="keywords" content="{city_name} forensic economist, {city_name} economic expert, {city_name} economic damages, {city_name} lost wages expert, {city_name} expert witness">
    <link rel="canonical" href="https://skerritteconomics.com/locations/cities/{filename}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{city_name} Forensic Economist | Skerritt Economics">
    <meta property="og:description" content="Court-qualified forensic economist serving {city_name} attorneys. Personal injury, wrongful death, and employment economic damages.">
    <meta property="og:url" content="https://skerritteconomics.com/locations/cities/{filename}">
    <meta property="og:type" content="website">
    
    <!-- Geo Tags -->
    <meta name="geo.region" content="US-{state_abbr}">
    <meta name="geo.placename" content="{city_name}">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="../../css/styles.css">
    <link rel="stylesheet" href="../../css/locations.css">
    <link rel="stylesheet" href="../../css/city-service-pages.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Skerritt Economics - {city_name} Forensic Economist",
        "description": "Forensic economics and economic damage expert services for {city_name} attorneys.",
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
        }},
        "hasOfferCatalog": {{
            "@type": "Service",
            "name": "Forensic Economics",
            "description": "Economic damage calculations and expert testimony for litigation"
        }}
    }}
    </script>
    
    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {{
                "@type": "Question",
                "name": "What types of cases does a forensic economist handle in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "Our forensic economists handle personal injury, wrongful death, medical malpractice, employment discrimination, wrongful termination, and commercial damages cases in {city_name} courts."
                }}
            }},
            {{
                "@type": "Question",
                "name": "How do you calculate economic damages in {state_full}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "We calculate lost earnings, fringe benefits, household services, and future economic losses using {state_full}-specific data, wage trends, and employment statistics relevant to the {city_name} market."
                }}
            }},
            {{
                "@type": "Question",
                "name": "Are you qualified to testify in {city_name} courts?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "Yes, our experts are qualified to testify in all {city_name} courts including {state_courts} and {federal_district}."
                }}
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
                    <a class="breadcrumb-link" href="../{state_abbr.lower()}.html">{state_full}</a>
                </li>
                <li class="breadcrumb-item">
                    <a class="breadcrumb-link" href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}.html">{city_name}</a>
                </li>
                <li class="breadcrumb-item">
                    <span class="breadcrumb-current">Forensic Economist</span>
                </li>
            </ol>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="service-hero">
        <div class="container">
            <h1>{city_name} Forensic Economist</h1>
            <p class="lead">Court-qualified economic damage expert serving {city_name} attorneys. Specializing in personal injury, wrongful death, employment, and commercial litigation economic analysis.</p>
            <div class="hero-features">
                <div class="feature">
                    <span class="feature-icon">📊</span>
                    <span>Economic Damage Calculations</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">⚖️</span>
                    <span>Expert Testimony</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">📈</span>
                    <span>Lost Earnings Analysis</span>
                </div>
            </div>
            <div class="hero-cta">
                <a href="../../contact/" class="btn btn-primary btn-large">Get {city_name} Case Evaluation</a>
                <a href="tel:203-605-2814" class="btn btn-secondary btn-large">Call (203) 605-2814</a>
            </div>
        </div>
    </section>

    <!-- Services Detail Section -->
    <section class="service-details">
        <div class="container">
            <div class="service-grid">
                <div class="service-content">
                    <h2>Forensic Economics Services in {city_name}</h2>
                    <p>Our forensic economics practice provides comprehensive economic damage analysis for litigation matters throughout {city_name} and {state_full}. We combine rigorous economic methodology with local market knowledge to deliver accurate, defensible damage calculations.</p>
                    
                    <h3>Personal Injury & Wrongful Death</h3>
                    <p>Economic loss calculations for catastrophic injuries and wrongful death cases in {city_name}:</p>
                    <ul>
                        <li>Lost earnings and earning capacity</li>
                        <li>Fringe benefits valuation</li>
                        <li>Household services losses</li>
                        <li>Loss of parental guidance</li>
                        <li>Present value calculations</li>
                        <li>Life expectancy adjustments</li>
                    </ul>

                    <h3>Employment Litigation</h3>
                    <p>Economic damages for workplace disputes and discrimination cases:</p>
                    <ul>
                        <li>Wrongful termination damages</li>
                        <li>Front pay and back pay calculations</li>
                        <li>Lost benefits and pension values</li>
                        <li>Mitigation analysis</li>
                        <li>Statistical discrimination analysis</li>
                        <li>Wage and hour violations</li>
                    </ul>

                    <h3>Commercial Damages</h3>
                    <p>Business economic losses for commercial litigation:</p>
                    <ul>
                        <li>Lost profits calculations</li>
                        <li>Business interruption losses</li>
                        <li>Breach of contract damages</li>
                        <li>Unfair competition impacts</li>
                        <li>Intellectual property damages</li>
                        <li>Reasonable royalty rates</li>
                    </ul>
                </div>

                <div class="service-sidebar">
                    <div class="sidebar-card">
                        <h3>{city_name} Courts Served</h3>
                        <ul>
                            <li>{state_courts}</li>
                            <li>{federal_district}</li>
                            <li>State appellate courts</li>
                            <li>Alternative dispute resolution</li>
                        </ul>
                    </div>

                    <div class="sidebar-card">
                        <h3>Why Choose Our {city_name} Forensic Economists</h3>
                        <ul>
                            <li>Court-qualified expert witnesses</li>
                            <li>Local {city_name} market knowledge</li>
                            <li>Rigorous economic methodology</li>
                            <li>Clear, compelling testimony</li>
                            <li>Rapid response for trial deadlines</li>
                            <li>Competitive expert witness fees</li>
                        </ul>
                    </div>

                    <div class="sidebar-card cta-card">
                        <h3>Get Started Today</h3>
                        <p>Need forensic economics support for your {city_name} case?</p>
                        <a href="../../contact/" class="btn btn-primary">Schedule Consultation</a>
                        <p class="cta-phone">Or call: <a href="tel:203-605-2814">(203) 605-2814</a></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Methodology Section -->
    <section class="methodology-section">
        <div class="container">
            <h2>Our Forensic Economics Methodology</h2>
            <div class="methodology-grid">
                <div class="method-card">
                    <h3>1. Case Review</h3>
                    <p>Comprehensive review of case materials, medical records, employment history, and relevant economic data specific to {city_name}.</p>
                </div>
                <div class="method-card">
                    <h3>2. Economic Analysis</h3>
                    <p>Detailed calculations using {state_full} wage data, industry statistics, and economic projections relevant to the {city_name} market.</p>
                </div>
                <div class="method-card">
                    <h3>3. Report Preparation</h3>
                    <p>Clear, well-documented expert reports that meet {state_full} court requirements and withstand scrutiny.</p>
                </div>
                <div class="method-card">
                    <h3>4. Expert Testimony</h3>
                    <p>Compelling courtroom testimony that clearly explains complex economic concepts to judges and juries.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Local Expertise Section -->
    <section class="local-expertise">
        <div class="container">
            <h2>{city_name} Economic Expertise</h2>
            <div class="expertise-content">
                <p>Our forensic economics practice combines national expertise with deep knowledge of the {city_name} economy. We understand the local labor market, wage patterns, industry composition, and economic trends that impact damage calculations in {state_full} litigation.</p>
                
                <div class="expertise-grid">
                    <div class="expertise-item">
                        <h3>Local Wage Data</h3>
                        <p>Access to {city_name}-specific wage surveys and compensation data for accurate earnings projections.</p>
                    </div>
                    <div class="expertise-item">
                        <h3>Industry Knowledge</h3>
                        <p>Understanding of major {city_name} employers and industry sectors for relevant economic analysis.</p>
                    </div>
                    <div class="expertise-item">
                        <h3>Court Experience</h3>
                        <p>Extensive testimony experience in {city_name} courts with knowledge of local procedures and preferences.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Need a Forensic Economist in {city_name}?</h2>
                <p>Get expert economic damage analysis for your litigation matter. Available for cases throughout {city_name} and {state_full}.</p>
                <div class="cta-buttons">
                    <a href="../../contact/" class="btn btn-primary btn-large">Request {city_name} Consultation</a>
                    <a href="tel:203-605-2814" class="btn btn-secondary btn-large">Call (203) 605-2814</a>
                </div>
                <p class="cta-note">Serving {city_name} law firms with comprehensive forensic economics expertise</p>
            </div>
        </div>
    </section>

    <!-- Related Services -->
    <section class="related-services">
        <div class="container">
            <h3>Other {city_name} Expert Services</h3>
            <div class="related-links">
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html" class="related-link">
                    <span class="link-icon">💼</span>
                    <span>{city_name} Business Valuation</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-vocational-expert.html" class="related-link">
                    <span class="link-icon">👔</span>
                    <span>{city_name} Vocational Expert</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-life-care-planner.html" class="related-link">
                    <span class="link-icon">🏥</span>
                    <span>{city_name} Life Care Planning</span>
                </a>
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}.html" class="related-link">
                    <span class="link-icon">🏛️</span>
                    <span>All {city_name} Services</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h4>{city_name} Forensic Economist</h4>
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
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-vocational-expert.html">Vocational Expert</a></li>
                        <li><a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-life-care-planner.html">Life Care Planning</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Practice Areas</h4>
                    <ul>
                        <li><a href="../../practice-areas/personal-injury/">Personal Injury</a></li>
                        <li><a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a></li>
                        <li><a href="../../practice-areas/employment/">Employment Litigation</a></li>
                        <li><a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a></li>
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
                <p>&copy; 2025 Skerritt Economics & Consulting. Expert forensic economics services in {city_name}, {state_full}.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/main.js"></script>
</body>
</html>"""

    with open(filename, 'w') as f:
        f.write(html_content)
    
    return filename

# Define cities with their information
cities = [
    # Major cities across the US
    ("New York City", "NY", "New York", "U.S. District Court for the Southern District of New York", "New York Supreme Court"),
    ("Los Angeles", "CA", "California", "U.S. District Court for the Central District of California", "Los Angeles County Superior Court"),
    ("Chicago", "IL", "Illinois", "U.S. District Court for the Northern District of Illinois", "Cook County Circuit Court"),
    ("Houston", "TX", "Texas", "U.S. District Court for the Southern District of Texas", "Harris County District Court"),
    ("Phoenix", "AZ", "Arizona", "U.S. District Court for the District of Arizona", "Maricopa County Superior Court"),
    ("Philadelphia", "PA", "Pennsylvania", "U.S. District Court for the Eastern District of Pennsylvania", "Philadelphia County Court of Common Pleas"),
    ("San Antonio", "TX", "Texas", "U.S. District Court for the Western District of Texas", "Bexar County District Court"),
    ("San Diego", "CA", "California", "U.S. District Court for the Southern District of California", "San Diego County Superior Court"),
    ("Dallas", "TX", "Texas", "U.S. District Court for the Northern District of Texas", "Dallas County District Court"),
    ("San Jose", "CA", "California", "U.S. District Court for the Northern District of California", "Santa Clara County Superior Court"),
    ("Austin", "TX", "Texas", "U.S. District Court for the Western District of Texas", "Travis County District Court"),
    ("Jacksonville", "FL", "Florida", "U.S. District Court for the Middle District of Florida", "Duval County Circuit Court"),
    ("San Francisco", "CA", "California", "U.S. District Court for the Northern District of California", "San Francisco County Superior Court"),
    ("Columbus", "OH", "Ohio", "U.S. District Court for the Southern District of Ohio", "Franklin County Court of Common Pleas"),
    ("Fort Worth", "TX", "Texas", "U.S. District Court for the Northern District of Texas", "Tarrant County District Court"),
    ("Indianapolis", "IN", "Indiana", "U.S. District Court for the Southern District of Indiana", "Marion County Superior Court"),
    ("Charlotte", "NC", "North Carolina", "U.S. District Court for the Western District of North Carolina", "Mecklenburg County Superior Court"),
    ("Seattle", "WA", "Washington", "U.S. District Court for the Western District of Washington", "King County Superior Court"),
    ("Denver", "CO", "Colorado", "U.S. District Court for the District of Colorado", "Denver County District Court"),
    ("Washington", "DC", "District of Columbia", "U.S. District Court for the District of Columbia", "Superior Court of the District of Columbia"),
    ("Boston", "MA", "Massachusetts", "U.S. District Court for the District of Massachusetts", "Suffolk County Superior Court"),
    ("El Paso", "TX", "Texas", "U.S. District Court for the Western District of Texas", "El Paso County District Court"),
    ("Nashville", "TN", "Tennessee", "U.S. District Court for the Middle District of Tennessee", "Davidson County Circuit Court"),
    ("Detroit", "MI", "Michigan", "U.S. District Court for the Eastern District of Michigan", "Wayne County Circuit Court"),
    ("Oklahoma City", "OK", "Oklahoma", "U.S. District Court for the Western District of Oklahoma", "Oklahoma County District Court"),
    ("Portland", "OR", "Oregon", "U.S. District Court for the District of Oregon", "Multnomah County Circuit Court"),
    ("Las Vegas", "NV", "Nevada", "U.S. District Court for the District of Nevada", "Clark County District Court"),
    ("Memphis", "TN", "Tennessee", "U.S. District Court for the Western District of Tennessee", "Shelby County Circuit Court"),
    ("Louisville", "KY", "Kentucky", "U.S. District Court for the Western District of Kentucky", "Jefferson County Circuit Court"),
    ("Baltimore", "MD", "Maryland", "U.S. District Court for the District of Maryland", "Baltimore City Circuit Court"),
    ("Milwaukee", "WI", "Wisconsin", "U.S. District Court for the Eastern District of Wisconsin", "Milwaukee County Circuit Court"),
    ("Albuquerque", "NM", "New Mexico", "U.S. District Court for the District of New Mexico", "Bernalillo County District Court"),
    ("Tucson", "AZ", "Arizona", "U.S. District Court for the District of Arizona", "Pima County Superior Court"),
    ("Fresno", "CA", "California", "U.S. District Court for the Eastern District of California", "Fresno County Superior Court"),
    ("Sacramento", "CA", "California", "U.S. District Court for the Eastern District of California", "Sacramento County Superior Court"),
    ("Mesa", "AZ", "Arizona", "U.S. District Court for the District of Arizona", "Maricopa County Superior Court"),
    ("Kansas City", "MO", "Missouri", "U.S. District Court for the Western District of Missouri", "Jackson County Circuit Court"),
    ("Atlanta", "GA", "Georgia", "U.S. District Court for the Northern District of Georgia", "Fulton County Superior Court"),
    ("Omaha", "NE", "Nebraska", "U.S. District Court for the District of Nebraska", "Douglas County District Court"),
    ("Colorado Springs", "CO", "Colorado", "U.S. District Court for the District of Colorado", "El Paso County District Court"),
    ("Raleigh", "NC", "North Carolina", "U.S. District Court for the Eastern District of North Carolina", "Wake County Superior Court"),
    ("Long Beach", "CA", "California", "U.S. District Court for the Central District of California", "Los Angeles County Superior Court"),
    ("Virginia Beach", "VA", "Virginia", "U.S. District Court for the Eastern District of Virginia", "Virginia Beach Circuit Court"),
    ("Miami", "FL", "Florida", "U.S. District Court for the Southern District of Florida", "Miami-Dade County Circuit Court"),
    ("Oakland", "CA", "California", "U.S. District Court for the Northern District of California", "Alameda County Superior Court"),
    ("Minneapolis", "MN", "Minnesota", "U.S. District Court for the District of Minnesota", "Hennepin County District Court"),
    ("Tulsa", "OK", "Oklahoma", "U.S. District Court for the Northern District of Oklahoma", "Tulsa County District Court"),
    ("Bakersfield", "CA", "California", "U.S. District Court for the Eastern District of California", "Kern County Superior Court"),
    ("Wichita", "KS", "Kansas", "U.S. District Court for the District of Kansas", "Sedgwick County District Court"),
    ("Arlington", "TX", "Texas", "U.S. District Court for the Northern District of Texas", "Tarrant County District Court"),
]

# Process first 50 cities
count = 0
for city_data in cities[:50]:
    city_name, state_abbr, state_full, federal_district, state_courts = city_data
    
    # Skip NYC since we already created it manually
    if city_name == "New York City":
        continue
        
    filename = create_forensic_economist_page(city_name, state_abbr, state_full, federal_district, state_courts)
    print(f"Created: {filename}")
    count += 1
    
    if count >= 50:
        break

print(f"\nCreated {count} forensic economist pages successfully!")