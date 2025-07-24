#!/usr/bin/env python3
import os

# New Hampshire, Maine, and Vermont cities with business valuation focus
northern_ne_cities = [
    # NEW HAMPSHIRE
    {
        "name": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "115,644",
        "county": "Hillsborough County",
        "distance_miles": 80,
        "major_business_sectors": "Healthcare organizations, technology companies, financial services, educational institutions",
        "court_info": "Hillsborough County Superior Court, U.S. District Court for New Hampshire",
        "economy": "New Hampshire's largest city with diverse businesses including hospitals, tech firms, and financial services",
        "proximity_message": "Serving Manchester businesses with comprehensive valuation services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Nashua",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "91,322",
        "county": "Hillsborough County",
        "distance_miles": 75,
        "major_business_sectors": "Technology companies, defense contractors, financial services, healthcare practices",
        "court_info": "Hillsborough County Superior Court (Nashua), Nashua District Court",
        "economy": "Technology hub with defense contractors, software companies, and financial services businesses",
        "proximity_message": "Serving Nashua businesses with expert valuation services through flexible virtual consultations and in-person meetings"
    },
    {
        "name": "Concord",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "43,976",
        "county": "Merrimack County",
        "distance_miles": 95,
        "major_business_sectors": "Government services, healthcare facilities, insurance companies, professional practices",
        "court_info": "Merrimack County Superior Court, New Hampshire Supreme Court",
        "economy": "State capital with government-related businesses, healthcare systems, and insurance companies",
        "proximity_message": "Serving Concord businesses with comprehensive valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Dover",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,741",
        "county": "Strafford County",
        "distance_miles": 100,
        "major_business_sectors": "Healthcare organizations, insurance companies, educational services, professional practices",
        "court_info": "Strafford County Superior Court, Dover District Court",
        "economy": "Historic seacoast city with healthcare, insurance, and professional service businesses",
        "proximity_message": "Serving Dover businesses with expert valuation services through virtual consultations and in-person meetings when required"
    },
    {
        "name": "Rochester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,492",
        "county": "Strafford County",
        "distance_miles": 95,
        "major_business_sectors": "Healthcare facilities, manufacturing companies, technology firms, retail businesses",
        "court_info": "Strafford County Superior Court, Rochester District Court",
        "economy": "Manufacturing and healthcare center with growing technology businesses",
        "proximity_message": "Serving Rochester businesses with comprehensive valuation services through virtual meetings and in-person consultations"
    },
    {
        "name": "Keene",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,409",
        "county": "Cheshire County",
        "distance_miles": 110,
        "major_business_sectors": "Healthcare organizations, educational institutions, distribution companies, retail businesses",
        "court_info": "Cheshire County Superior Court, Keene District Court",
        "economy": "Regional center with healthcare, education, and distribution businesses",
        "proximity_message": "Serving Keene businesses with expert valuation services through virtual evaluations and in-person meetings at trial"
    },
    {
        "name": "Derry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "34,317",
        "county": "Rockingham County",
        "distance_miles": 80,
        "major_business_sectors": "Healthcare practices, retail businesses, professional services, local companies",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "economy": "Suburban community with healthcare providers, retail centers, and local businesses",
        "proximity_message": "Serving Derry businesses with comprehensive valuation services through flexible consultation arrangements"
    },
    {
        "name": "Portsmouth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "21,956",
        "county": "Rockingham County",
        "distance_miles": 110,
        "major_business_sectors": "Tourism businesses, healthcare organizations, marine-related companies, professional services",
        "court_info": "Rockingham County Superior Court, Portsmouth District Court",
        "economy": "Historic seaport with tourism, healthcare, and marine industry businesses",
        "proximity_message": "Serving Portsmouth businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Laconia",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "16,871",
        "county": "Belknap County",
        "distance_miles": 115,
        "major_business_sectors": "Healthcare facilities, tourism businesses, manufacturing companies, retail establishments",
        "court_info": "Belknap County Superior Court, Laconia District Court",
        "economy": "Lakes Region center with healthcare, seasonal tourism, and manufacturing businesses",
        "proximity_message": "Serving Laconia businesses with comprehensive valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Salem",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "30,089",
        "county": "Rockingham County",
        "distance_miles": 75,
        "major_business_sectors": "Retail centers, business parks, professional services, technology companies",
        "court_info": "Rockingham County Superior Court, Salem District Court",
        "economy": "Border town with major retail centers and growing business parks",
        "proximity_message": "Serving Salem businesses with expert valuation services through flexible consultation options"
    },
    
    # MAINE
    {
        "name": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "68,408",
        "county": "Cumberland County",
        "distance_miles": 160,
        "major_business_sectors": "Healthcare organizations, biotechnology companies, financial services, tourism businesses",
        "court_info": "Cumberland County Superior Court, U.S. District Court for Maine",
        "economy": "Maine's largest city with diverse businesses including hospitals, biotech firms, and tourism companies",
        "proximity_message": "Serving Portland businesses with comprehensive valuation services through virtual evaluations and in-person meetings at trial"
    },
    {
        "name": "Lewiston",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "36,592",
        "county": "Androscoggin County",
        "distance_miles": 130,
        "major_business_sectors": "Healthcare facilities, educational institutions, manufacturing companies, professional services",
        "court_info": "Androscoggin County Superior Court, Lewiston District Court",
        "economy": "Healthcare and education center with light manufacturing and service businesses",
        "proximity_message": "Serving Lewiston businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Bangor",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "31,753",
        "county": "Penobscot County",
        "distance_miles": 220,
        "major_business_sectors": "Healthcare organizations, retail businesses, financial services, professional practices",
        "court_info": "Penobscot County Superior Court, Bangor District Court",
        "economy": "Regional healthcare and service center for northern Maine businesses",
        "proximity_message": "Serving Bangor businesses with comprehensive valuation services through virtual evaluations and scheduled in-person meetings"
    },
    {
        "name": "South Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "26,498",
        "county": "Cumberland County",
        "distance_miles": 165,
        "major_business_sectors": "Retail businesses, healthcare administration, oil storage companies, professional services",
        "court_info": "Cumberland County Superior Court",
        "economy": "Retail center with healthcare administration and petroleum storage businesses",
        "proximity_message": "Serving South Portland businesses with expert valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Auburn",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "24,061",
        "county": "Androscoggin County",
        "distance_miles": 130,
        "major_business_sectors": "Healthcare services, manufacturing companies, retail businesses, professional practices",
        "court_info": "Androscoggin County Superior Court",
        "economy": "Twin city with Lewiston featuring manufacturing and healthcare businesses",
        "proximity_message": "Serving Auburn businesses with comprehensive valuation services through virtual meetings and in-person consultations"
    },
    {
        "name": "Biddeford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "22,552",
        "county": "York County",
        "distance_miles": 140,
        "major_business_sectors": "Healthcare organizations, educational institutions, mill district businesses, professional services",
        "court_info": "York County Superior Court, Biddeford District Court",
        "economy": "Healthcare and education center with revitalized mill district businesses",
        "proximity_message": "Serving Biddeford businesses with expert valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Augusta",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "18,899",
        "county": "Kennebec County",
        "distance_miles": 165,
        "major_business_sectors": "Government services, healthcare facilities, professional practices, local businesses",
        "court_info": "Kennebec County Superior Court, Maine Supreme Judicial Court",
        "economy": "State capital with government-related businesses and healthcare organizations",
        "proximity_message": "Serving Augusta businesses with comprehensive valuation services through virtual consultations and in-person meetings at trial"
    },
    {
        "name": "Saco",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,381",
        "county": "York County",
        "distance_miles": 140,
        "major_business_sectors": "Defense contractors, retail businesses, tourism companies, professional services",
        "court_info": "York County Superior Court",
        "economy": "Defense manufacturing, retail, and coastal tourism businesses",
        "proximity_message": "Serving Saco businesses with expert valuation services through virtual meetings and in-person consultations"
    },
    {
        "name": "Westbrook",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,400",
        "county": "Cumberland County",
        "distance_miles": 155,
        "major_business_sectors": "Biotechnology companies, healthcare services, retail businesses, professional practices",
        "court_info": "Cumberland County Superior Court",
        "economy": "Biotechnology, behavioral health services, and retail businesses",
        "proximity_message": "Serving Westbrook businesses with comprehensive valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Waterville",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "15,722",
        "county": "Kennebec County",
        "distance_miles": 175,
        "major_business_sectors": "Healthcare organizations, educational institutions, manufacturing companies, local businesses",
        "court_info": "Kennebec County Superior Court, Waterville District Court",
        "economy": "Healthcare, higher education, and manufacturing businesses",
        "proximity_message": "Serving Waterville businesses with expert valuation services through virtual consultations and scheduled in-person meetings"
    },
    
    # VERMONT
    {
        "name": "Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "44,743",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_business_sectors": "Healthcare organizations, educational institutions, technology companies, professional services",
        "court_info": "Chittenden County Superior Court, U.S. District Court for Vermont",
        "economy": "Vermont's largest city with healthcare systems, universities, and technology businesses",
        "proximity_message": "Serving Burlington businesses with comprehensive valuation services through virtual evaluations and in-person meetings at trial"
    },
    {
        "name": "South Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "20,292",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_business_sectors": "Airport businesses, retail centers, corporate offices, professional services",
        "court_info": "Chittenden County Superior Court",
        "economy": "Commercial center with airport-related businesses and corporate headquarters",
        "proximity_message": "Serving South Burlington businesses with expert valuation services through virtual consultations and scheduled in-person meetings"
    },
    {
        "name": "Rutland",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,807",
        "county": "Rutland County",
        "distance_miles": 190,
        "major_business_sectors": "Healthcare facilities, manufacturing companies, retail businesses, professional services",
        "court_info": "Rutland County Superior Court, Rutland District Court",
        "economy": "Regional center with healthcare, manufacturing, and service businesses",
        "proximity_message": "Serving Rutland businesses with comprehensive valuation services through virtual evaluations and in-person meetings when required"
    },
    {
        "name": "Essex Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "10,761",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_business_sectors": "Technology manufacturers, semiconductor companies, professional services, local businesses",
        "court_info": "Chittenden County Superior Court",
        "economy": "Technology manufacturing hub with semiconductor production facilities",
        "proximity_message": "Serving Essex Junction businesses with expert valuation services through virtual meetings and scheduled in-person consultations"
    },
    {
        "name": "Barre",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "8,491",
        "county": "Washington County",
        "distance_miles": 240,
        "major_business_sectors": "Healthcare organizations, granite industry businesses, retail establishments, professional services",
        "court_info": "Washington County Superior Court",
        "economy": "Granite capital with healthcare facilities and stone industry businesses",
        "proximity_message": "Serving Barre businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "Montpelier",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "8,074",
        "county": "Washington County",
        "distance_miles": 235,
        "major_business_sectors": "Government services, insurance companies, professional practices, local businesses",
        "court_info": "Washington County Superior Court, Vermont Supreme Court",
        "economy": "State capital with government services and insurance company headquarters",
        "proximity_message": "Serving Montpelier businesses with expert valuation services through virtual evaluations and scheduled in-person meetings"
    },
    {
        "name": "St. Albans",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "6,877",
        "county": "Franklin County",
        "distance_miles": 300,
        "major_business_sectors": "Healthcare facilities, pharmaceutical companies, retail businesses, professional services",
        "court_info": "Franklin County Superior Court",
        "economy": "Healthcare and pharmaceutical manufacturing businesses",
        "proximity_message": "Serving St. Albans businesses with comprehensive valuation services through virtual consultations and scheduled court appearances"
    },
    {
        "name": "Brattleboro",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "12,184",
        "county": "Windham County",
        "distance_miles": 150,
        "major_business_sectors": "Healthcare organizations, mental health facilities, arts businesses, retail establishments",
        "court_info": "Windham County Superior Court",
        "economy": "Healthcare, mental health services, and arts community businesses",
        "proximity_message": "Serving Brattleboro businesses with expert valuation services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Bennington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,333",
        "county": "Bennington County",
        "distance_miles": 170,
        "major_business_sectors": "Healthcare facilities, educational institutions, manufacturing companies, professional services",
        "court_info": "Bennington County Superior Court",
        "economy": "Healthcare, education, and manufacturing businesses",
        "proximity_message": "Serving Bennington businesses with comprehensive valuation services through virtual consultations and in-person meetings"
    },
    {
        "name": "St. Johnsbury",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "7,364",
        "county": "Caledonia County",
        "distance_miles": 270,
        "major_business_sectors": "Healthcare organizations, manufacturing companies, retail businesses, professional services",
        "court_info": "Caledonia County Superior Court",
        "economy": "Healthcare, manufacturing, and regional service businesses",
        "proximity_message": "Serving St. Johnsbury businesses with expert valuation services through virtual meetings and scheduled court appearances"
    }
]

# Template for Northern New England business valuation pages
def generate_northern_ne_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-{city['state_abbr'].lower()}-business-valuation.html"
    
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
<title>Business Valuation {city['name']} {city['state_abbr']} | Business Appraiser | Chris Skerritt</title>
<meta content="Expert business valuation services in {city['name']}, {city['state']}. Professional business appraiser for divorce, buy-sell, estate planning. Free consultation 203-605-2814" name="description"/>
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
    "name": "Business Valuation Services in {city['name']}, {city['state_abbr']}",
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
    "description": "Expert business valuation and appraisal services for {city['name']}, {city['state']} businesses. Professional appraiser for divorce, shareholder disputes, estate planning, and buy-sell agreements.",
    "areaServed": {{
        "@type": "City",
        "name": "{city['name']}",
        "containedInPlace": {{
            "@type": "State",
            "name": "{city['state']}"
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
            "name": "What types of businesses do you value in {city['name']}, {city['state_abbr']}?",
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
                "text": "Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. {city['state']} courts require independent, credentialed appraisers for litigation matters."
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
            "name": "{city['name']}, {city['state_abbr']}",
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
<span class="breadcrumb-current">Business Valuation {city['name']} {city['state_abbr']}</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Business Valuation in {city['name']}, {city['state']}</h1>
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
<li><strong>Divorce Business Valuations:</strong> Marital asset valuations for equitable distribution in {city['state']} Family Court</li>
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
<p>Our firm has extensive experience providing expert testimony in {city['state']} courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences for business disputes</li>
</ul>
<p>Our valuation reports meet {city['state']} court standards and we work closely with {city['name']} attorneys to ensure clear, defensible opinions.</p>
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
<summary>What types of businesses do you value in {city['name']}, {city['state_abbr']}?</summary>
<p>We value all types of {city['name']} businesses including {city['major_business_sectors']}. Our professional expertise ensures accurate valuations for businesses of all sizes, from small family-owned companies to larger enterprises throughout {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How much does a business valuation cost in {city['name']}?</summary>
<p>Business valuation fees in {city['name']} typically range from $3,500 to $15,000 depending on business complexity, purpose, and size. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When do {city['name']} businesses need professional valuations?</summary>
<p>Professional valuations are needed for divorce proceedings in {city['court_info']}, buy-sell agreements, estate planning, shareholder disputes, SBA loans, and strategic planning. {city['state']} courts require independent, credentialed appraisers for litigation matters.</p>
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

# Generate all Northern New England city pages
for city in northern_ne_cities:
    generate_northern_ne_page(city)

print(f"\nGenerated {len(northern_ne_cities)} Northern New England business valuation pages!")
print("\nPages created for:")
print("\nNew Hampshire:")
for city in northern_ne_cities:
    if city['state_abbr'] == 'NH':
        print(f"- {city['name']}, NH ({city['distance_miles']} miles from Smithfield)")
print("\nMaine:")
for city in northern_ne_cities:
    if city['state_abbr'] == 'ME':
        print(f"- {city['name']}, ME ({city['distance_miles']} miles from Smithfield)")
print("\nVermont:")
for city in northern_ne_cities:
    if city['state_abbr'] == 'VT':
        print(f"- {city['name']}, VT ({city['distance_miles']} miles from Smithfield)")