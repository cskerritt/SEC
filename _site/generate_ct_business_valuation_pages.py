#!/usr/bin/env python3
import os

# Connecticut cities with business valuation focus
ct_cities = [
    {
        "name": "Bridgeport",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "148,654",
        "county": "Fairfield County",
        "distance_miles": 100,
        "major_business_sectors": "Healthcare practices, financial services, educational institutions, professional services",
        "court_info": "Fairfield County Superior Court, U.S. District Court for Connecticut",
        "economy": "Connecticut's largest city with diverse businesses including healthcare systems, banks, and professional practices",
        "proximity_message": "Serving Bridgeport businesses with comprehensive valuation services through virtual consultations and in-person meetings when required"
    },
    {
        "name": "New Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "134,023",
        "county": "New Haven County",
        "distance_miles": 85,
        "major_business_sectors": "Healthcare organizations, biotechnology companies, educational services, professional practices",
        "court_info": "New Haven County Superior Court, U.S. District Court",
        "economy": "Major academic and medical center with biotechnology startups, healthcare practices, and professional services",
        "proximity_message": "Serving New Haven businesses with expert valuation services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Stamford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "135,470",
        "county": "Fairfield County",
        "distance_miles": 120,
        "major_business_sectors": "Corporate headquarters, financial services firms, technology companies, professional services",
        "court_info": "Stamford Superior Court, Stamford-Norwalk Judicial District",
        "economy": "Major corporate center with Fortune 500 headquarters, financial firms, and diverse professional services",
        "proximity_message": "Serving Stamford businesses with comprehensive valuation services through virtual evaluations and in-person meetings at trial"
    },
    {
        "name": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "121,054",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_business_sectors": "Insurance companies, healthcare organizations, financial services, professional practices",
        "court_info": "Hartford Superior Court, Connecticut Supreme Court, U.S. District Court",
        "economy": "State capital and insurance capital with major insurance companies, healthcare systems, and government-related businesses",
        "proximity_message": "Serving Hartford businesses with expert valuation services through flexible virtual consultations and in-person meetings"
    },
    {
        "name": "Waterbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "114,403",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_business_sectors": "Healthcare facilities, financial services, manufacturing companies, retail businesses",
        "court_info": "Waterbury Superior Court, Waterbury Judicial District",
        "economy": "Regional center with healthcare systems, banks, and diverse manufacturing and retail businesses",
        "proximity_message": "Serving Waterbury businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Norwalk",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "91,184",
        "county": "Fairfield County",
        "distance_miles": 110,
        "major_business_sectors": "Corporate headquarters, technology companies, healthcare practices, professional services",
        "court_info": "Stamford-Norwalk Judicial District Court",
        "economy": "Corporate headquarters location with technology firms, healthcare providers, and professional services",
        "proximity_message": "Serving Norwalk businesses with expert valuation services through virtual evaluations and in-person meetings as needed"
    },
    {
        "name": "Danbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "86,518",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_business_sectors": "Healthcare organizations, pharmaceutical companies, educational institutions, retail businesses",
        "court_info": "Danbury Superior Court, Danbury Judicial District",
        "economy": "Healthcare and pharmaceutical hub with hospital systems, biotech companies, and diverse businesses",
        "proximity_message": "Serving Danbury businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "New Britain",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "74,135",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_business_sectors": "Manufacturing companies, healthcare practices, educational services, retail businesses",
        "court_info": "New Britain Superior Court, New Britain Judicial District",
        "economy": "Hardware City with manufacturing heritage, healthcare facilities, and educational institutions",
        "proximity_message": "Serving New Britain businesses with expert valuation services through flexible consultation options"
    },
    {
        "name": "West Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "55,584",
        "county": "New Haven County",
        "distance_miles": 85,
        "major_business_sectors": "Healthcare services, educational institutions, biotechnology companies, retail businesses",
        "court_info": "New Haven County Superior Court",
        "economy": "Healthcare and education center with VA facilities, university presence, and growing biotech sector",
        "proximity_message": "Serving West Haven businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Bristol",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "60,640",
        "county": "Hartford County",
        "distance_miles": 60,
        "major_business_sectors": "Media companies, healthcare facilities, manufacturing businesses, professional services",
        "court_info": "Bristol Superior Court, New Britain Judicial District",
        "economy": "Home to ESPN with strong media presence, healthcare services, and manufacturing companies",
        "proximity_message": "Serving Bristol businesses with expert valuation services through flexible virtual and in-person consultations"
    },
    {
        "name": "Meriden",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,512",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_business_sectors": "Healthcare organizations, manufacturing companies, educational services, retail businesses",
        "court_info": "Meriden Superior Court, New Haven Judicial District",
        "economy": "Healthcare and manufacturing center with medical facilities and specialized manufacturing",
        "proximity_message": "Serving Meriden businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Milford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "50,558",
        "county": "New Haven County",
        "distance_miles": 90,
        "major_business_sectors": "Corporate headquarters, healthcare practices, retail businesses, marine-related companies",
        "court_info": "Milford Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate headquarters location with healthcare providers, retail centers, and coastal businesses",
        "proximity_message": "Serving Milford businesses with expert valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Stratford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "52,355",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_business_sectors": "Aerospace companies, manufacturing businesses, healthcare practices, retail establishments",
        "court_info": "Bridgeport Superior Court, Fairfield Judicial District",
        "economy": "Aerospace manufacturing center with Sikorsky and related suppliers, plus healthcare and retail",
        "proximity_message": "Serving Stratford businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "East Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "51,045",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_business_sectors": "Aerospace manufacturers, technology companies, educational institutions, professional services",
        "court_info": "Hartford Superior Court",
        "economy": "Aerospace manufacturing hub with Pratt & Whitney and related technology companies",
        "proximity_message": "Serving East Hartford businesses with expert valuation services through flexible consultation arrangements"
    },
    {
        "name": "Middletown",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "47,717",
        "county": "Middlesex County",
        "distance_miles": 65,
        "major_business_sectors": "Healthcare organizations, educational institutions, insurance companies, professional services",
        "court_info": "Middlesex Superior Court, Middletown Judicial District",
        "economy": "Healthcare, education, and insurance center with hospital systems and university presence",
        "proximity_message": "Serving Middletown businesses with comprehensive valuation services through virtual and in-person consultations"
    },
    {
        "name": "Manchester",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,713",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_business_sectors": "Healthcare facilities, retail centers, printing companies, professional services",
        "court_info": "Manchester Superior Court, Hartford Judicial District",
        "economy": "Healthcare and retail hub with hospital systems, shopping centers, and printing industry",
        "proximity_message": "Serving Manchester businesses with expert valuation services through flexible meeting options"
    },
    {
        "name": "Enfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "42,269",
        "county": "Hartford County",
        "distance_miles": 75,
        "major_business_sectors": "Distribution companies, financial services, retail businesses, manufacturing firms",
        "court_info": "Enfield Superior Court, Hartford Judicial District",
        "economy": "Distribution and logistics center with financial services and retail near Massachusetts border",
        "proximity_message": "Serving Enfield businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Shelton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "40,869",
        "county": "Fairfield County",
        "distance_miles": 90,
        "major_business_sectors": "Life sciences companies, corporate headquarters, manufacturing businesses, healthcare practices",
        "court_info": "Derby Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate and life sciences hub with headquarters facilities and specialized manufacturing",
        "proximity_message": "Serving Shelton businesses with expert valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Torrington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,515",
        "county": "Litchfield County",
        "distance_miles": 85,
        "major_business_sectors": "Healthcare facilities, manufacturing companies, clean energy businesses, retail establishments",
        "court_info": "Torrington Superior Court, Litchfield Judicial District",
        "economy": "Healthcare and manufacturing center with hospital systems and clean energy technology companies",
        "proximity_message": "Serving Torrington businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Trumbull",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "36,827",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_business_sectors": "Corporate offices, healthcare practices, professional services, retail businesses",
        "court_info": "Bridgeport Superior Court",
        "economy": "Suburban business community with corporate offices, medical practices, and professional services",
        "proximity_message": "Serving Trumbull businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Glastonbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,159",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_business_sectors": "Professional services, healthcare practices, technology companies, local businesses",
        "court_info": "Hartford Superior Court",
        "economy": "Affluent community with professional service firms, medical practices, and technology companies",
        "proximity_message": "Serving Glastonbury businesses with comprehensive valuation services through flexible consultation options"
    },
    {
        "name": "Naugatuck",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "31,519",
        "county": "New Haven County",
        "distance_miles": 75,
        "major_business_sectors": "Manufacturing companies, healthcare practices, retail businesses, chemical companies",
        "court_info": "Waterbury Superior Court",
        "economy": "Manufacturing center with rubber and chemical production plus healthcare services",
        "proximity_message": "Serving Naugatuck businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Newington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "30,536",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_business_sectors": "Government services, retail centers, healthcare practices, professional services",
        "court_info": "Hartford Superior Court",
        "economy": "Government and retail center with state facilities and shopping districts",
        "proximity_message": "Serving Newington businesses with comprehensive valuation services through flexible meeting arrangements"
    },
    {
        "name": "Wallingford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "44,396",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_business_sectors": "Manufacturing companies, pharmaceutical firms, technology businesses, healthcare practices",
        "court_info": "Meriden Superior Court",
        "economy": "Manufacturing and pharmaceutical center with technology companies and healthcare providers",
        "proximity_message": "Serving Wallingford businesses with expert valuation services through virtual and in-person consultations"
    },
    {
        "name": "Wethersfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "27,298",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_business_sectors": "Government services, professional practices, local businesses, retail establishments",
        "court_info": "Hartford Superior Court",
        "economy": "Historic community with government services and established local businesses",
        "proximity_message": "Serving Wethersfield businesses with comprehensive valuation services through flexible consultation options"
    },
    {
        "name": "Greenwich",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "63,518",
        "county": "Fairfield County",
        "distance_miles": 130,
        "major_business_sectors": "Hedge funds, private equity firms, financial services, professional practices",
        "court_info": "Stamford Superior Court",
        "economy": "Wealthy community with concentration of hedge funds, private equity, and financial services",
        "proximity_message": "Serving Greenwich businesses with expert valuation services through virtual evaluations and in-person meetings at trial"
    }
]

# Template for Connecticut business valuation pages
def generate_ct_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ct-business-valuation.html"
    
    # Determine the proximity/service message based on distance
    if city['distance_miles'] <= 20:
        location_flexibility = "immediate response times and flexible meeting locations"
    elif city['distance_miles'] <= 50:
        location_flexibility = "both in-person and virtual consultation options"
    else:
        location_flexibility = "comprehensive service through virtual consultations and in-person meetings"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Business Valuation {city['name']} CT | Business Appraiser | Chris Skerritt</title>
<meta content="Expert business valuation services in {city['name']}, Connecticut. Professional business appraiser for divorce, buy-sell, estate planning. Free consultation 203-605-2814" name="description"/>
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
    "name": "Business Valuation Services in {city['name']}, CT",
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
    "description": "Expert business valuation and appraisal services for {city['name']}, Connecticut businesses. Professional appraiser for divorce, shareholder disputes, estate planning, and buy-sell agreements.",
    "areaServed": {{
        "@type": "City",
        "name": "{city['name']}",
        "containedInPlace": {{
            "@type": "State",
            "name": "Connecticut"
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
            "name": "What types of businesses do you value in {city['name']}, CT?",
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
                "text": "Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Connecticut courts require independent, credentialed appraisers for litigation matters."
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
            "name": "{city['name']}, CT",
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
<span class="breadcrumb-current">Business Valuation {city['name']} CT</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Business Valuation in {city['name']}, Connecticut</h1>
<div class="meta">
<span>Business Valuation Expert</span>
<span>Court-Qualified</span>
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
<li><strong>Divorce Business Valuations:</strong> Marital asset valuations for equitable distribution in Connecticut Family Court</li>
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
<p>Our firm has extensive experience providing expert testimony in Connecticut courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences for business disputes</li>
</ul>
<p>Our valuation reports meet Connecticut court standards and we work closely with {city['name']} attorneys to ensure clear, defensible opinions.</p>
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
<li><strong>Site Visit:</strong> On-site business inspection when appropriate</li>
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
<summary>What types of businesses do you value in {city['name']}, CT?</summary>
<p>We value all types of {city['name']} businesses including {city['major_business_sectors']}. Our professional expertise ensures accurate valuations for businesses of all sizes, from small family-owned companies to larger enterprises throughout {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How much does a business valuation cost in {city['name']}?</summary>
<p>Business valuation fees in {city['name']} typically range from $3,500 to $15,000 depending on business complexity, purpose, and size. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When do {city['name']} businesses need professional valuations?</summary>
<p>Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Connecticut courts require independent, credentialed appraisers for litigation matters.</p>
</details>
<details class="faq-item">
<summary>How long does a business valuation take?</summary>
<p>Most {city['name']} business valuations are completed within 2-4 weeks, depending on complexity and information availability. Expedited service is available for urgent matters.</p>
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

# Generate all Connecticut city pages
for city in ct_cities:
    generate_ct_page(city)

print(f"\nGenerated {len(ct_cities)} Connecticut business valuation pages!")
print("\nPages created for:")
for city in ct_cities:
    print(f"- {city['name']}, CT ({city['distance_miles']} miles from Smithfield)")