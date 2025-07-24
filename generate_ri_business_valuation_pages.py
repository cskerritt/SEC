#!/usr/bin/env python3
import os

# Rhode Island cities with business valuation focus
ri_cities = [
    {
        "name": "Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "190,934",
        "county": "Providence County",
        "distance_miles": 10,
        "major_business_sectors": "Healthcare systems, educational institutions, financial services, hospitality businesses",
        "court_info": "Rhode Island Superior Court (Licht Judicial Complex), U.S. District Court, Rhode Island Family Court",
        "economy": "State capital with diverse business landscape including professional services, healthcare practices, restaurants, and retail establishments",
        "proximity_message": "Located just 10 miles from our Smithfield office, we provide prompt, in-person business valuation services and can quickly respond to urgent valuation needs"
    },
    {
        "name": "Warwick",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,823",
        "county": "Kent County",
        "distance_miles": 15,
        "major_business_sectors": "Retail businesses, hospitality near T.F. Green Airport, healthcare practices, service companies",
        "court_info": "Kent County Courthouse, Rhode Island Family Court",
        "economy": "Second-largest city with strong retail sector, airport-related businesses, and professional services",
        "proximity_message": "Located just 15 miles from our Smithfield office, we provide timely, in-person business valuation services to Warwick business owners and attorneys"
    },
    {
        "name": "Cranston",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,934",
        "county": "Providence County",
        "distance_miles": 12,
        "major_business_sectors": "Manufacturing companies, retail centers, restaurants, healthcare practices",
        "court_info": "Cases typically heard in Providence County Superior Court",
        "economy": "Mix of family-owned businesses, light manufacturing, retail establishments, and professional services",
        "proximity_message": "Just 12 miles from our Smithfield office, we offer immediate response and in-person consultations for Cranston business valuations"
    },
    {
        "name": "Pawtucket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "75,604",
        "county": "Providence County",
        "distance_miles": 8,
        "major_business_sectors": "Manufacturing businesses, creative industries, healthcare practices, retail establishments",
        "court_info": "Cases heard in Providence County Superior Court",
        "economy": "Historic manufacturing center with growing arts district, small businesses, and professional services",
        "proximity_message": "Only 8 miles from our Smithfield office, we provide immediate, cost-effective business valuation services with quick turnaround times"
    },
    {
        "name": "East Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "47,139",
        "county": "Providence County",
        "distance_miles": 12,
        "major_business_sectors": "Waterfront businesses, retail establishments, professional services, healthcare practices",
        "court_info": "Providence County Superior Court jurisdiction",
        "economy": "Suburban community with revitalized waterfront district, local businesses, and professional services",
        "proximity_message": "Just 12 miles from our Smithfield office, we offer convenient in-person meetings and rapid valuation services"
    },
    {
        "name": "Woonsocket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "43,240",
        "county": "Providence County",
        "distance_miles": 10,
        "major_business_sectors": "Healthcare practices, retail businesses, manufacturing companies, professional services",
        "court_info": "Providence County Superior Court, Woonsocket District Court",
        "economy": "Former mill city with healthcare facilities, retail businesses, and light manufacturing",
        "proximity_message": "Located just 10 miles from our Smithfield office, we provide quick, in-person business valuations for Woonsocket businesses and attorneys"
    },
    {
        "name": "Newport",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "25,163",
        "county": "Newport County",
        "distance_miles": 30,
        "major_business_sectors": "Tourism businesses, hospitality industry, marine-related companies, retail establishments",
        "court_info": "Newport County Superior Court, Newport County Family Court",
        "economy": "Tourism-driven economy with restaurants, hotels, marine businesses, and high-end retail",
        "proximity_message": "Located 30 miles from our Smithfield office, we regularly serve Newport businesses with both in-person meetings and efficient remote consultations"
    },
    {
        "name": "Westerly",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "23,359",
        "county": "Washington County",
        "distance_miles": 45,
        "major_business_sectors": "Tourism and hospitality businesses, healthcare practices, retail establishments",
        "court_info": "Washington County Superior Court (Wakefield)",
        "economy": "Coastal community with seasonal businesses, tourism industry, and year-round professional services",
        "proximity_message": "Serving Westerly businesses with flexible consultation options, including in-person meetings at your office or ours, and comprehensive virtual evaluations"
    }
]

# Template for Rhode Island business valuation pages
def generate_ri_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ri-business-valuation.html"
    
    # Determine the proximity/service message based on distance
    if city['distance_miles'] <= 20:
        location_flexibility = "immediate response times and flexible meeting locations"
    elif city['distance_miles'] <= 40:
        location_flexibility = "both in-person and virtual consultation options"
    else:
        location_flexibility = "comprehensive service through virtual consultations and in-person meetings"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Business Valuation {city['name']} RI | Business Appraiser | Chris Skerritt</title>
<meta content="Expert business valuation services in {city['name']}, Rhode Island. Professional business appraiser for divorce, buy-sell, estate planning. Free consultation 203-605-2814" name="description"/>
<link href="../../css/styles.css" rel="stylesheet"/>
<link href="../../css/services.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://skerritteconomics.com/locations/business-valuation/{filename}" rel="canonical"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Structured Data -->
<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Business Valuation Services in {city['name']}, RI",
    "provider": {{
        "@type": "ProfessionalService",
        "name": "Skerritt Economics & Consulting",
        "address": {{
            "@type": "PostalAddress",
            "streetAddress": "400 Putnam Pike Ste J",
            "addressLocality": "Smithfield",
            "addressRegion": "RI",
            "postalCode": "02917",
            "addressCountry": "US"
        }},
        "telephone": "203-605-2814",
        "email": "chris@skerritteconomics.com"
    }},
    "description": "Expert business valuation and appraisal services for {city['name']}, Rhode Island businesses. Professional appraiser for divorce, shareholder disputes, estate planning, and buy-sell agreements.",
    "areaServed": {{
        "@type": "City",
        "name": "{city['name']}",
        "containedInPlace": {{
            "@type": "State",
            "name": "Rhode Island"
        }}
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
            "name": "What types of businesses do you value in {city['name']}, RI?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "We value all types of {city['name']} businesses including {city['major_business_sectors']}. Our professional expertise ensures accurate valuations for businesses of all sizes, from small family-owned companies to larger enterprises throughout {city['county']}."
            }}
        }},
        {{
            "@type": "Question",
            "name": "How much does a business valuation cost in {city['name']}?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Business valuation fees in {city['name']} typically range from $3,500 to $15,000 depending on business complexity, purpose, and size. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation."
            }}
        }},
        {{
            "@type": "Question",
            "name": "When do {city['name']} businesses need professional valuations?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Rhode Island courts require independent, credentialed appraisers for litigation matters."
            }}
        }}
    ]
}}
</script>
<script type="application/ld+json">{{
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
            "name": "Business Valuation",
            "item": "https://skerritteconomics.com/locations/business-valuation/"
        }},
        {{
            "@type": "ListItem",
            "position": 4,
            "name": "{city['name']}, RI",
            "item": "https://skerritteconomics.com/locations/business-valuation/{filename}"
        }}
    ]
}}</script>
</head>
<body>
<!-- Navigation -->
<nav class="main-nav">
<div class="container">
<div class="nav-wrapper">
<a class="logo" href="../../index.html">
<strong>Skerritt Economics</strong>
<span>&amp; Consulting</span>
</a>
<button aria-label="Toggle menu" class="mobile-menu-toggle">
<span></span>
<span></span>
<span></span>
</button>
<ul class="nav-menu">
<li><a href="../../index.html">Home</a></li>
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
<li><a href="../../practice-areas/personal-injury/">Personal Injury &amp; Wrongful Death</a></li>
<li><a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a></li>
<li><a href="../../practice-areas/employment/">Employment Litigation</a></li>
<li><a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a></li>
</ul>
</li>
<li><a href="../../case-studies/">Case Studies</a></li>
<li><a href="../../about/">About</a></li>
<li><a href="../../resources/">Resources</a></li>
<li><a class="nav-cta" href="../../contact/">Contact</a></li>
</ul>
</div>
</div>
</nav>
<!-- Breadcrumb Navigation -->
<nav class="breadcrumb" aria-label="Breadcrumb">
<div class="breadcrumb-container">
<ol class="breadcrumb-list">
<li class="breadcrumb-item">
<a class="breadcrumb-link" href="../../index.html">Home</a>
</li>
<li class="breadcrumb-item">
<a class="breadcrumb-link" href="../../locations/">Locations</a>
</li>
<li class="breadcrumb-item">
<span class="breadcrumb-current">Business Valuation {city['name']} RI</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Business Valuation in {city['name']}, Rhode Island</h1>
<div class="meta">
<span>Business Valuation Expert</span>
<span>Court-Qualified Expert</span>
<span>Serving {city['county']}</span>
</div>
<p class="lead">Expert business valuation services for {city['name']} businesses and attorneys. Professional business appraiser providing valuations for divorce, shareholder disputes, estate planning, and strategic transactions. {city['proximity_message']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Business Valuation Services in {city['name']}</h2>
<p>As a leading business valuation expert serving {city['name']}, we provide comprehensive business appraisal services throughout {city['county']}. With a population of {city['population']}, {city['name']} features diverse businesses including {city['major_business_sectors']}, each requiring specialized valuation expertise.</p>
<p>{city['economy']}. Our business valuations incorporate deep understanding of the local market conditions, industry trends, and economic factors specific to {city['name']} businesses.</p>
</div>
<!-- Services for Local Businesses -->
<div class="service-section">
<h2>Business Valuation for {city['name']} Companies</h2>
<p>We provide {city['name']} businesses and their advisors with credible valuations for matters in {city['court_info']}. Our comprehensive services include:</p>
<ul>
<li><strong>Divorce Business Valuations:</strong> Marital asset valuations for equitable distribution in Rhode Island Family Court</li>
<li><strong>Shareholder Dispute Valuations:</strong> Fair value determinations for buyouts and dissenting shareholder matters</li>
<li><strong>Estate & Gift Tax Valuations:</strong> IRS-compliant valuations for estate planning and wealth transfer</li>
<li><strong>Buy-Sell Agreement Valuations:</strong> Transaction pricing for partner buyouts and ownership transfers</li>
<li><strong>SBA Loan Valuations:</strong> Business appraisals meeting SBA requirements for acquisition financing</li>
<li><strong>Strategic Planning Valuations:</strong> Value assessments for growth planning and exit strategies</li>
</ul>
</div>
<!-- Local Business Landscape -->
<div class="service-section">
<h2>Understanding {city['name']}'s Business Environment</h2>
<p>Accurate business valuations require deep understanding of local market conditions. Key factors in {city['name']} include:</p>
<ul>
<li><strong>Business Sectors:</strong> {city['major_business_sectors']}</li>
<li><strong>Market Dynamics:</strong> Local competition, customer demographics, and growth trends</li>
<li><strong>Economic Factors:</strong> Regional economic conditions affecting business performance</li>
<li><strong>Real Estate Values:</strong> Commercial property values impacting asset-based valuations</li>
<li><strong>Industry Multiples:</strong> Transaction comparables from similar {city['name']} area businesses</li>
</ul>
<p>This local expertise ensures valuations reflect the true market value of {city['name']} businesses, not just theoretical calculations.</p>
</div>
<!-- Court Experience -->
<div class="service-section">
<h2>Court Experience in {city['county']}</h2>
<p>Our firm has extensive experience providing expert testimony in Rhode Island courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences for business disputes</li>
</ul>
<p>Our valuation reports meet Rhode Island court standards and we work closely with {city['name']} attorneys to ensure clear, defensible opinions.</p>
</div>
<!-- Common Valuation Purposes -->
<div class="service-section">
<h2>Common {city['name']} Business Valuation Needs</h2>
<h3>Divorce & Family Law:</h3>
<ul>
<li>Professional practices (medical, dental, legal)</li>
<li>Family-owned businesses</li>
<li>Closely-held corporations</li>
<li>Partnership interests</li>
</ul>
<h3>Business Disputes:</h3>
<ul>
<li>Shareholder oppression cases</li>
<li>Partnership dissolutions</li>
<li>Buy-sell agreement disputes</li>
<li>Breach of fiduciary duty damages</li>
</ul>
<h3>Tax & Estate Planning:</h3>
<ul>
<li>Estate tax valuations</li>
<li>Gift tax compliance</li>
<li>Charitable contribution valuations</li>
<li>Buy-sell agreement funding</li>
</ul>
</div>
<!-- Valuation Process -->
<div class="service-section">
<h2>Our {city['name']} Business Valuation Process</h2>
<p>{city['proximity_message']}, offering {location_flexibility}. Our proven process includes:</p>
<ul>
<li><strong>Initial Consultation:</strong> Free evaluation to understand valuation needs and provide fee estimate</li>
<li><strong>Information Gathering:</strong> Collection of financial statements, tax returns, and operational data</li>
<li><strong>Site Visit:</strong> On-site business inspection when appropriate (convenient given our proximity)</li>
<li><strong>Financial Analysis:</strong> Detailed review of historical performance and future projections</li>
<li><strong>Market Research:</strong> Analysis of industry trends and comparable transactions</li>
<li><strong>Valuation Report:</strong> Comprehensive written report with detailed support for conclusions</li>
<li><strong>Expert Testimony:</strong> Clear presentation of findings in deposition or trial</li>
</ul>
</div>
<!-- Industries Served -->
<div class="service-section">
<h2>Industries We Value in {city['name']}</h2>
<div class="industry-grid">
<div class="industry-item">
<h4>Healthcare Practices</h4>
<p>Medical, dental, veterinary practices</p>
</div>
<div class="industry-item">
<h4>Professional Services</h4>
<p>Law firms, accounting practices, consultancies</p>
</div>
<div class="industry-item">
<h4>Manufacturing</h4>
<p>Light manufacturing, specialty producers</p>
</div>
<div class="industry-item">
<h4>Retail & Restaurants</h4>
<p>Stores, restaurants, franchises</p>
</div>
<div class="industry-item">
<h4>Construction</h4>
<p>Contractors, specialty trades</p>
</div>
<div class="industry-item">
<h4>Technology</h4>
<p>Software, IT services, tech startups</p>
</div>
</div>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Business Valuation</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What types of businesses do you value in {city['name']}, RI?</summary>
<p>We value all types of {city['name']} businesses including {city['major_business_sectors']}. Our professional expertise ensures accurate valuations for businesses of all sizes, from small family-owned companies to larger enterprises throughout {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How much does a business valuation cost in {city['name']}?</summary>
<p>Business valuation fees in {city['name']} typically range from $3,500 to $15,000 depending on business complexity, purpose, and size. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When do {city['name']} businesses need professional valuations?</summary>
<p>Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Rhode Island courts require independent, credentialed appraisers for litigation matters.</p>
</details>
<details class="faq-item">
<summary>How long does a business valuation take?</summary>
<p>Most {city['name']} business valuations are completed within 2-4 weeks, depending on complexity and information availability. Expedited service is available for urgent matters. Our proximity allows for quick site visits and in-person meetings to accelerate the process.</p>
</details>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need a Business Valuation in {city['name']}?</h2>
<p>Free consultation for {city['name']} business owners and attorneys. Get a credible, defensible business valuation from an experienced expert.</p>
<a class="btn btn-primary btn-large" href="../../contact/">Schedule Consultation</a>
<p class="cta-phone">Or call directly: <a href="tel:203-605-2814">(203) 605-2814</a></p>
</div>
</div>
</div>
</section>
<!-- Footer -->
<footer class="main-footer">
<div class="container">
<div class="footer-grid">
<div class="footer-col">
<h4>Skerritt Economics &amp; Consulting</h4>
<p>Expert business valuations for {city['name']} companies.</p>
<p class="footer-contact">
400 Putnam Pike Ste J<br/>
Smithfield, RI 02917<br/>
<a href="tel:203-605-2814">(203) 605-2814</a><br/>
<a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a>
</p>
</div>
<div class="footer-col">
<h4>Services</h4>
<ul>
<li><a href="../../services/forensic-economics/">Forensic Economics</a></li>
<li><a href="../../services/business-valuation/">Business Valuation</a></li>
<li><a href="../../services/vocational-expert/">Vocational Expert</a></li>
<li><a href="../../services/life-care-planning/">Life Care Planning</a></li>
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
<li><a href="../../resources/">Articles &amp; Insights</a></li>
<li><a href="../../about/">About Chris Skerritt</a></li>
<li><a href="../../contact/">Contact</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p>© 2025 Skerritt Economics &amp; Consulting. All rights reserved.</p>
</div>
</div>
</footer>
<script src="../../js/main.js"></script>
<style>
.industry-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
}}

.industry-item {{
    background: var(--light-bg);
    padding: 1.5rem;
    border-radius: 8px;
}}

.industry-item h4 {{
    color: var(--primary);
    margin-bottom: 0.5rem;
}}

.industry-item p {{
    margin: 0;
    font-size: 0.9rem;
    color: var(--text-light);
}}
</style>
</body>
</html>"""
    
    # Write the file
    filepath = f"/Users/chrisskerritt/SEC/locations/business-valuation/{filename}"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

# Create directory if it doesn't exist
os.makedirs("/Users/chrisskerritt/SEC/locations/business-valuation", exist_ok=True)

# Generate all Rhode Island city pages
for city in ri_cities:
    generate_ri_page(city)

print(f"\nGenerated {len(ri_cities)} Rhode Island business valuation pages!")
print("\nPages created for:")
for city in ri_cities:
    print(f"- {city['name']}, RI ({city['distance_miles']} miles from Smithfield)")