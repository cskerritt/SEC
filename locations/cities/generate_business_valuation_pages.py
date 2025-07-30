#!/usr/bin/env python3

import os

def create_business_valuation_page(city_name, state_abbr, state_full, federal_district, state_courts):
    """Generate a city-specific business valuation page"""
    
    filename = f"{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-business-valuation-analyst.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{city_name} Business Valuation Analyst | Business Appraisal Expert | Skerritt Economics</title>
    <meta name="description" content="Expert business valuation analyst serving {city_name}, {state_abbr}. Business appraisals for litigation, divorce, tax, and transaction purposes. Court-qualified valuation expert.">
    <meta name="keywords" content="{city_name} business valuation, {city_name} business appraiser, {city_name} business valuation expert, {city_name} company valuation, {city_name} business worth">
    <link rel="canonical" href="https://skerritteconomics.com/locations/cities/{filename}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{city_name} Business Valuation Analyst | Skerritt Economics">
    <meta property="og:description" content="Court-qualified business valuation expert serving {city_name} attorneys. Divorce, shareholder disputes, and commercial litigation valuations.">
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
        "name": "Skerritt Economics - {city_name} Business Valuation",
        "description": "Business valuation and appraisal expert services for {city_name} attorneys and businesses.",
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
            "name": "Business Valuation",
            "description": "Professional business appraisal and valuation services for legal and financial purposes"
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
                "name": "What types of businesses do you value in {city_name}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "We value all types of businesses in {city_name}, including professional practices, manufacturing companies, service businesses, retail operations, restaurants, and technology firms. Our expertise covers closely-held businesses, professional corporations, and partnership interests."
                }}
            }},
            {{
                "@type": "Question",
                "name": "When is business valuation needed in {state_full}?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "Business valuation is required for divorce proceedings, shareholder disputes, buy-sell agreements, estate planning, gift tax reporting, mergers and acquisitions, and commercial litigation in {state_full} courts."
                }}
            }},
            {{
                "@type": "Question",
                "name": "What valuation methods do you use?",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "We apply income approaches (DCF, capitalization), market approaches (guideline companies, transactions), and asset approaches following professional standards including USPAP, ASA, and AICPA guidelines."
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
                    <span class="breadcrumb-current">Business Valuation</span>
                </li>
            </ol>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="service-hero">
        <div class="container">
            <h1>{city_name} Business Valuation Analyst</h1>
            <p class="lead">Court-qualified business appraisal expert serving {city_name} attorneys. Specializing in divorce, shareholder disputes, tax matters, and commercial litigation valuations.</p>
            <div class="hero-features">
                <div class="feature">
                    <span class="feature-icon">📊</span>
                    <span>Business Appraisals</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">⚖️</span>
                    <span>Expert Testimony</span>
                </div>
                <div class="feature">
                    <span class="feature-icon">💼</span>
                    <span>All Business Types</span>
                </div>
            </div>
            <div class="hero-cta">
                <a href="../../contact/" class="btn btn-primary btn-large">Get {city_name} Valuation Quote</a>
                <a href="tel:203-605-2814" class="btn btn-secondary btn-large">Call (203) 605-2814</a>
            </div>
        </div>
    </section>

    <!-- Services Detail Section -->
    <section class="service-details">
        <div class="container">
            <div class="service-grid">
                <div class="service-content">
                    <h2>Business Valuation Services in {city_name}</h2>
                    <p>Our business valuation practice provides comprehensive appraisal services for litigation and transactional matters throughout {city_name} and {state_full}. We combine rigorous valuation methodology with local market knowledge to deliver accurate, defensible business valuations.</p>
                    
                    <h3>Divorce & Marital Dissolution</h3>
                    <p>Business valuations for equitable distribution in {city_name} divorce cases:</p>
                    <ul>
                        <li>Closely-held business interests</li>
                        <li>Professional practice valuations</li>
                        <li>Partnership and LLC interests</li>
                        <li>Stock options and restricted stock</li>
                        <li>Separate vs. marital property analysis</li>
                        <li>Personal goodwill considerations</li>
                    </ul>

                    <h3>Shareholder & Partnership Disputes</h3>
                    <p>Valuation services for business ownership disputes:</p>
                    <ul>
                        <li>Shareholder oppression cases</li>
                        <li>Buy-sell agreement valuations</li>
                        <li>Dissenting shareholder appraisals</li>
                        <li>Partnership dissolution values</li>
                        <li>Minority interest discounts</li>
                        <li>Marketability discount analysis</li>
                    </ul>

                    <h3>Tax & Estate Planning</h3>
                    <p>Business appraisals for tax compliance and planning:</p>
                    <ul>
                        <li>Estate and gift tax valuations</li>
                        <li>Charitable contribution appraisals</li>
                        <li>Purchase price allocations</li>
                        <li>S-corp to C-corp conversions</li>
                        <li>409A valuations for stock options</li>
                        <li>ESOPs and phantom stock plans</li>
                    </ul>
                </div>

                <div class="service-sidebar">
                    <div class="sidebar-card">
                        <h3>{city_name} Courts Served</h3>
                        <ul>
                            <li>{state_courts}</li>
                            <li>{federal_district}</li>
                            <li>Family/divorce courts</li>
                            <li>Tax court proceedings</li>
                        </ul>
                    </div>

                    <div class="sidebar-card">
                        <h3>Why Choose Our {city_name} Valuation Experts</h3>
                        <ul>
                            <li>Credentialed valuation professionals</li>
                            <li>Local {city_name} market expertise</li>
                            <li>Court testimony experience</li>
                            <li>Professional standards compliance</li>
                            <li>Defensible valuation reports</li>
                            <li>Competitive professional fees</li>
                        </ul>
                    </div>

                    <div class="sidebar-card cta-card">
                        <h3>Get Started Today</h3>
                        <p>Need business valuation support for your {city_name} case?</p>
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
            <h2>Our Business Valuation Process</h2>
            <div class="methodology-grid">
                <div class="method-card">
                    <h3>1. Initial Assessment</h3>
                    <p>Review of business operations, financial statements, and relevant documents to understand the company and valuation requirements.</p>
                </div>
                <div class="method-card">
                    <h3>2. Financial Analysis</h3>
                    <p>Detailed analysis of historical performance, {city_name} market conditions, industry trends, and company-specific factors.</p>
                </div>
                <div class="method-card">
                    <h3>3. Valuation Approaches</h3>
                    <p>Application of income, market, and asset approaches following professional standards to determine business value.</p>
                </div>
                <div class="method-card">
                    <h3>4. Report & Testimony</h3>
                    <p>Comprehensive valuation reports meeting {state_full} court requirements with clear, persuasive expert testimony.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Industries Section -->
    <section class="local-expertise">
        <div class="container">
            <h2>{city_name} Industry Expertise</h2>
            <div class="expertise-content">
                <p>Our business valuation practice combines national expertise with deep knowledge of {city_name} businesses and industries. We understand the local market conditions, competitive dynamics, and economic factors that impact business values in {state_full}.</p>
                
                <div class="expertise-grid">
                    <div class="expertise-item">
                        <h3>Professional Services</h3>
                        <p>Medical practices, law firms, accounting firms, consulting businesses, and other professional service companies.</p>
                    </div>
                    <div class="expertise-item">
                        <h3>Manufacturing & Distribution</h3>
                        <p>Manufacturing operations, wholesale distributors, logistics companies, and supply chain businesses.</p>
                    </div>
                    <div class="expertise-item">
                        <h3>Retail & Hospitality</h3>
                        <p>Retail stores, restaurants, hotels, entertainment venues, and consumer service businesses.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="service-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Need a Business Valuation Expert in {city_name}?</h2>
                <p>Get professional business appraisal services for your litigation or transactional needs. Available for cases throughout {city_name} and {state_full}.</p>
                <div class="cta-buttons">
                    <a href="../../contact/" class="btn btn-primary btn-large">Request {city_name} Valuation</a>
                    <a href="tel:203-605-2814" class="btn btn-secondary btn-large">Call (203) 605-2814</a>
                </div>
                <p class="cta-note">Serving {city_name} attorneys with comprehensive business valuation expertise</p>
            </div>
        </div>
    </section>

    <!-- Related Services -->
    <section class="related-services">
        <div class="container">
            <h3>Other {city_name} Expert Services</h3>
            <div class="related-links">
                <a href="{city_name.lower().replace(' ', '-')}-{state_abbr.lower()}-forensic-economist.html" class="related-link">
                    <span class="link-icon">📈</span>
                    <span>{city_name} Forensic Economics</span>
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
                    <h4>{city_name} Business Valuation</h4>
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
                <p>&copy; 2025 Skerritt Economics & Consulting. Expert business valuation services in {city_name}, {state_full}.</p>
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
        
    filename = create_business_valuation_page(city_name, state_abbr, state_full, federal_district, state_courts)
    print(f"Created: {filename}")
    count += 1
    
    if count >= 50:
        break

print(f"\nCreated {count} business valuation pages successfully!")