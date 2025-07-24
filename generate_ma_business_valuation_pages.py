#!/usr/bin/env python3
import os

# Massachusetts cities with business valuation focus
ma_cities = [
    {
        "name": "Boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "675,647",
        "county": "Suffolk County",
        "distance_miles": 50,
        "major_business_sectors": "Financial services firms, healthcare practices, technology startups, professional services, restaurants",
        "court_info": "Suffolk County Superior Court, Suffolk Probate and Family Court, U.S. District Court",
        "economy": "Major metropolitan center with diverse businesses from startups to established corporations across all industries",
        "proximity_message": "Located 50 miles from our Smithfield office, we provide comprehensive business valuation services to Boston businesses with flexible in-person and virtual consultation options"
    },
    {
        "name": "Worcester",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "206,518",
        "county": "Worcester County",
        "distance_miles": 35,
        "major_business_sectors": "Healthcare practices, biotechnology companies, educational services, manufacturing businesses",
        "court_info": "Worcester County Superior Court, Worcester Probate and Family Court",
        "economy": "Central Massachusetts hub with strong healthcare, education, and growing biotech sectors",
        "proximity_message": "Located 35 miles from our Smithfield office, we regularly serve Worcester businesses with both in-person meetings and efficient remote consultations"
    },
    {
        "name": "Springfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "155,929",
        "county": "Hampden County",
        "distance_miles": 60,
        "major_business_sectors": "Healthcare organizations, insurance companies, manufacturing firms, hospitality businesses",
        "court_info": "Hampden County Superior Court, Hampden Probate and Family Court",
        "economy": "Western Massachusetts center with established insurance industry, healthcare systems, and entertainment venues",
        "proximity_message": "Serving Springfield businesses with comprehensive valuation services through both in-person consultations and virtual meetings"
    },
    {
        "name": "Cambridge",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "118,403",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_business_sectors": "Biotechnology companies, technology startups, research firms, professional services",
        "court_info": "Middlesex County Superior Court, Cambridge District Court",
        "economy": "Global innovation hub with high concentration of tech startups, biotech firms, and research organizations",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide timely business valuation services to Cambridge companies with flexible meeting options"
    },
    {
        "name": "Lowell",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "115,554",
        "county": "Middlesex County",
        "distance_miles": 55,
        "major_business_sectors": "Healthcare practices, technology companies, educational services, manufacturing businesses",
        "court_info": "Middlesex County Superior Court (Lowell), Lowell District Court",
        "economy": "Revitalized city with growing technology sector, healthcare services, and educational institutions",
        "proximity_message": "Serving Lowell businesses with expert valuation services through convenient in-person and virtual consultation options"
    },
    {
        "name": "Brockton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "105,643",
        "county": "Plymouth County",
        "distance_miles": 40,
        "major_business_sectors": "Healthcare practices, financial services, transportation companies, retail businesses",
        "court_info": "Plymouth County Superior Court (Brockton), Brockton District Court",
        "economy": "Regional center with healthcare facilities, financial services, and diverse small businesses",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Brockton businesses with both in-person and virtual consultations"
    },
    {
        "name": "New Bedford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,079",
        "county": "Bristol County",
        "distance_miles": 35,
        "major_business_sectors": "Fishing industry businesses, healthcare practices, manufacturing companies, marine services",
        "court_info": "Bristol County Superior Court (New Bedford), New Bedford District Court",
        "economy": "Historic seaport with active fishing industry, healthcare sector, and specialized manufacturing",
        "proximity_message": "Located 35 miles from our Smithfield office, we provide prompt business valuation services to New Bedford companies with flexible meeting arrangements"
    },
    {
        "name": "Quincy",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,636",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_business_sectors": "Financial services, medical device companies, retail businesses, professional services",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban city with corporate offices, financial services, and medical device manufacturing",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Quincy businesses with timely valuations and flexible consultation options"
    },
    {
        "name": "Lynn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,253",
        "county": "Essex County",
        "distance_miles": 60,
        "major_business_sectors": "Manufacturing companies, healthcare practices, educational services, retail businesses",
        "court_info": "Essex County Superior Court (Salem), Lynn District Court",
        "economy": "Industrial city with jet engine manufacturing, healthcare services, and diverse businesses",
        "proximity_message": "Serving Lynn businesses with comprehensive valuation services through both in-person consultations and virtual meetings"
    },
    {
        "name": "Fall River",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "94,000",
        "county": "Bristol County",
        "distance_miles": 25,
        "major_business_sectors": "Healthcare practices, distribution companies, educational services, retail businesses",
        "court_info": "Bristol County Superior Court (Fall River), Fall River District Court",
        "economy": "Former textile center with growing healthcare, distribution, and service sectors",
        "proximity_message": "Located just 25 miles from our Smithfield office, we provide immediate response and in-person business valuation services to Fall River companies"
    },
    {
        "name": "Newton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "88,923",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_business_sectors": "Healthcare practices, technology companies, professional services, retail businesses",
        "court_info": "Middlesex County Superior Court, Newton District Court",
        "economy": "Affluent suburban city with professional practices, technology firms, and upscale retail",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Newton businesses with expert valuations and flexible meeting options"
    },
    {
        "name": "Somerville",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "81,045",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_business_sectors": "Technology startups, healthcare services, restaurants, creative businesses",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "economy": "Dense urban community with thriving startup ecosystem and creative industries",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide timely business valuation services to Somerville companies"
    },
    {
        "name": "Framingham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "72,362",
        "county": "Middlesex County",
        "distance_miles": 40,
        "major_business_sectors": "Corporate headquarters, retail businesses, technology companies, healthcare practices",
        "court_info": "Middlesex County Superior Court, Framingham District Court",
        "economy": "Major retail and corporate center with numerous headquarters and distribution operations",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Framingham businesses with both in-person and virtual consultation options"
    },
    {
        "name": "Haverhill",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "67,787",
        "county": "Essex County",
        "distance_miles": 70,
        "major_business_sectors": "Healthcare practices, educational services, manufacturing companies, retail businesses",
        "court_info": "Essex County Superior Court, Haverhill District Court",
        "economy": "Merrimack Valley city with healthcare, education, and diverse manufacturing base",
        "proximity_message": "Serving Haverhill businesses with comprehensive valuation services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Waltham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "65,218",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_business_sectors": "Technology companies, defense contractors, educational institutions, healthcare practices",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "economy": "High-tech corridor with defense contractors, research facilities, and technology firms",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide expert business valuation services to Waltham companies with flexible consultation options"
    },
    {
        "name": "Malden",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "66,263",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_business_sectors": "Healthcare services, food production companies, professional services, retail businesses",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Diverse urban community with healthcare, food production, and service industries",
        "proximity_message": "Serving Malden businesses with comprehensive valuation services through both in-person and virtual meetings"
    },
    {
        "name": "Medford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,659",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_business_sectors": "Educational services, healthcare practices, professional services, local businesses",
        "court_info": "Middlesex County Superior Court, Medford District Court",
        "economy": "Residential community with education, healthcare, and professional service businesses",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Medford businesses with timely valuation services"
    },
    {
        "name": "Taunton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,408",
        "county": "Bristol County",
        "distance_miles": 20,
        "major_business_sectors": "Healthcare facilities, manufacturing companies, retail businesses, professional services",
        "court_info": "Bristol County Superior Court (Taunton), Taunton District Court",
        "economy": "Regional center with healthcare, manufacturing, and diverse service businesses",
        "proximity_message": "Located just 20 miles from our Smithfield office, we provide immediate, in-person business valuation services to Taunton companies"
    },
    {
        "name": "Weymouth",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "57,213",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_business_sectors": "Healthcare services, medical technology companies, retail businesses, professional services",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban community with healthcare, medical technology, and service businesses",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Weymouth businesses with expert valuation services"
    },
    {
        "name": "Revere",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "62,186",
        "county": "Suffolk County",
        "distance_miles": 55,
        "major_business_sectors": "Hospitality businesses, gaming industry, service companies, retail establishments",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "economy": "Coastal city with gaming, hospitality, and diverse service industries",
        "proximity_message": "Serving Revere businesses with comprehensive valuation services through flexible consultation arrangements"
    },
    {
        "name": "Peabody",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "54,481",
        "county": "Essex County",
        "distance_miles": 60,
        "major_business_sectors": "Healthcare services, technology companies, retail businesses, professional services",
        "court_info": "Essex County Superior Court, Peabody District Court",
        "economy": "Former leather industry center now focused on healthcare, technology, and retail",
        "proximity_message": "Serving Peabody businesses with expert valuations through virtual consultations and in-person meetings"
    },
    {
        "name": "Methuen",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "53,059",
        "county": "Essex County",
        "distance_miles": 65,
        "major_business_sectors": "Healthcare practices, retail businesses, service companies, light manufacturing",
        "court_info": "Essex County Superior Court, Lawrence District Court",
        "economy": "Merrimack Valley city with healthcare, retail, and diverse service businesses",
        "proximity_message": "Serving Methuen businesses with comprehensive valuation services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Barnstable",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "48,916",
        "county": "Barnstable County",
        "distance_miles": 70,
        "major_business_sectors": "Tourism businesses, healthcare practices, retail establishments, marine services",
        "court_info": "Barnstable County Superior Court, Barnstable District Court",
        "economy": "Cape Cod's commercial hub with tourism, healthcare, and seasonal businesses",
        "proximity_message": "Serving Cape Cod businesses with expert valuation services through virtual consultations and in-person meetings when required"
    },
    {
        "name": "Pittsfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,927",
        "county": "Berkshire County",
        "distance_miles": 120,
        "major_business_sectors": "Healthcare organizations, defense contractors, financial services, cultural institutions",
        "court_info": "Berkshire County Superior Court, Pittsfield District Court",
        "economy": "Berkshires regional center with healthcare, defense contracting, and cultural businesses",
        "proximity_message": "Serving Berkshire County businesses with comprehensive valuation services through virtual evaluations and in-person meetings at trial"
    },
    {
        "name": "Attleboro",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "46,461",
        "county": "Bristol County",
        "distance_miles": 15,
        "major_business_sectors": "Healthcare practices, technology companies, jewelry manufacturers, retail businesses",
        "court_info": "Bristol County Superior Court, Attleboro District Court",
        "economy": "Historic jewelry center with healthcare, technology, and manufacturing businesses",
        "proximity_message": "Located just 15 miles from our Smithfield office, we provide immediate, cost-effective business valuation services to Attleboro companies"
    },
    {
        "name": "Westfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,301",
        "county": "Hampden County",
        "distance_miles": 75,
        "major_business_sectors": "Healthcare practices, educational services, manufacturing companies, retail businesses",
        "court_info": "Hampden County Superior Court, Westfield District Court",
        "economy": "Western Massachusetts city with healthcare, education, and diverse manufacturing",
        "proximity_message": "Serving Westfield businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Chicopee",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "55,560",
        "county": "Hampden County",
        "distance_miles": 65,
        "major_business_sectors": "Healthcare services, manufacturing companies, retail businesses, defense-related firms",
        "court_info": "Hampden County Superior Court, Chicopee District Court",
        "economy": "City with military presence, healthcare services, and manufacturing base",
        "proximity_message": "Serving Chicopee businesses with comprehensive valuation services through flexible consultation options"
    },
    {
        "name": "Holyoke",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "38,238",
        "county": "Hampden County",
        "distance_miles": 70,
        "major_business_sectors": "Healthcare facilities, educational institutions, energy companies, retail businesses",
        "court_info": "Hampden County Superior Court, Holyoke District Court",
        "economy": "Former paper mill city with healthcare, education, and clean energy sectors",
        "proximity_message": "Serving Holyoke businesses with expert valuations through virtual consultations and in-person meetings"
    },
    {
        "name": "Beverly",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "42,670",
        "county": "Essex County",
        "distance_miles": 65,
        "major_business_sectors": "Healthcare practices, educational services, professional services, retail businesses",
        "court_info": "Essex County Superior Court, Salem District Court",
        "economy": "North Shore community with healthcare, education, and professional services",
        "proximity_message": "Serving Beverly businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Everett",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "49,075",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_business_sectors": "Gaming and entertainment, healthcare services, industrial businesses, retail establishments",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Urban community with casino resort, healthcare, and industrial businesses",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Everett businesses with timely valuation services"
    }
]

# Template for Massachusetts business valuation pages
def generate_ma_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ma-business-valuation.html"
    
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
<title>Business Valuation {city['name']} MA | Business Appraiser | Chris Skerritt</title>
<meta content="Expert business valuation services in {city['name']}, Massachusetts. Professional business appraiser for divorce, buy-sell, estate planning. Free consultation 203-605-2814" name="description"/>
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
    "name": "Business Valuation Services in {city['name']}, MA",
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
    "description": "Expert business valuation and appraisal services for {city['name']}, Massachusetts businesses. Professional appraiser for divorce, shareholder disputes, estate planning, and buy-sell agreements.",
    "areaServed": {{
        "@type": "City",
        "name": "{city['name']}",
        "containedInPlace": {{
            "@type": "State",
            "name": "Massachusetts"
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
            "name": "What types of businesses do you value in {city['name']}, MA?",
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
                "text": "Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Massachusetts courts require independent, credentialed appraisers for litigation matters."
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
            "name": "{city['name']}, MA",
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
<span class="breadcrumb-current">Business Valuation {city['name']} MA</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Business Valuation in {city['name']}, Massachusetts</h1>
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
<li><strong>Divorce Business Valuations:</strong> Marital asset valuations for equitable distribution in Massachusetts Family Court</li>
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
<p>Our firm has extensive experience providing expert testimony in Massachusetts courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences for business disputes</li>
</ul>
<p>Our valuation reports meet Massachusetts court standards and we work closely with {city['name']} attorneys to ensure clear, defensible opinions.</p>
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
<summary>What types of businesses do you value in {city['name']}, MA?</summary>
<p>We value all types of {city['name']} businesses including {city['major_business_sectors']}. Our professional expertise ensures accurate valuations for businesses of all sizes, from small family-owned companies to larger enterprises throughout {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How much does a business valuation cost in {city['name']}?</summary>
<p>Business valuation fees in {city['name']} typically range from $3,500 to $15,000 depending on business complexity, purpose, and size. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When do {city['name']} businesses need professional valuations?</summary>
<p>Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. Massachusetts courts require independent, credentialed appraisers for litigation matters.</p>
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

# Generate all Massachusetts city pages
for city in ma_cities:
    generate_ma_page(city)

print(f"\nGenerated {len(ma_cities)} Massachusetts business valuation pages!")
print("\nPages created for:")
for city in ma_cities:
    print(f"- {city['name']}, MA ({city['distance_miles']} miles from Smithfield)")