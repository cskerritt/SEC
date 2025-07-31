#!/usr/bin/env python3
import os

# New Hampshire, Maine, and Vermont cities with detailed information
northern_ne_cities = [
    # NEW HAMPSHIRE
    {
        "name": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "115,644",
        "county": "Hillsborough County",
        "distance_miles": 80,
        "major_employers": "Elliot Hospital, Catholic Medical Center, Southern New Hampshire University, Dyn",
        "court_info": "Hillsborough County Superior Court, U.S. District Court for New Hampshire",
        "economy": "New Hampshire's largest city with healthcare, education, technology, and financial services sectors",
        "proximity_message": "Serving Manchester attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Nashua",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "91,322",
        "county": "Hillsborough County",
        "distance_miles": 75,
        "major_employers": "BAE Systems, Fidelity Investments, Oracle, Southern New Hampshire Medical Center",
        "court_info": "Hillsborough County Superior Court (Nashua), Nashua District Court",
        "economy": "Technology hub with defense contractors, software companies, and financial services near Massachusetts border",
        "proximity_message": "Serving Nashua attorneys with expert forensic economic services through flexible virtual consultations and in-person meetings"
    },
    {
        "name": "Concord",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "43,976",
        "county": "Merrimack County",
        "distance_miles": 95,
        "major_employers": "State of New Hampshire, Concord Hospital, Lincoln Financial Group",
        "court_info": "Merrimack County Superior Court, New Hampshire Supreme Court, Federal Court",
        "economy": "State capital with government employment, healthcare, and insurance sectors",
        "proximity_message": "Serving Concord attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Dover",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,741",
        "county": "Strafford County",
        "distance_miles": 100,
        "major_employers": "Wentworth-Douglass Hospital, Liberty Mutual, Measured Progress",
        "court_info": "Strafford County Superior Court, Dover District Court",
        "economy": "Historic seacoast city with healthcare, insurance, and educational testing industries",
        "proximity_message": "Serving Dover attorneys with expert forensic economic services through virtual consultations and in-person testimony when required"
    },
    {
        "name": "Rochester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,492",
        "county": "Strafford County",
        "distance_miles": 95,
        "major_employers": "Frisbie Memorial Hospital, Albany International, Spaulding Composites",
        "court_info": "Strafford County Superior Court, Rochester District Court",
        "economy": "Manufacturing and healthcare center with growing technology sector",
        "proximity_message": "Serving Rochester attorneys with comprehensive forensic economic services through virtual meetings and in-person testimony"
    },
    {
        "name": "Keene",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,409",
        "county": "Cheshire County",
        "distance_miles": 110,
        "major_employers": "Cheshire Medical Center, Keene State College, C&S Wholesale Grocers",
        "court_info": "Cheshire County Superior Court, Keene District Court",
        "economy": "Regional center with healthcare, education, and distribution",
        "proximity_message": "Serving Keene attorneys with expert forensic economic services through virtual evaluations and in-person testimony at trial"
    },
    {
        "name": "Derry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "34,317",
        "county": "Rockingham County",
        "distance_miles": 80,
        "major_employers": "Parkland Medical Center, local businesses and retail",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "economy": "Suburban community with healthcare and retail sectors",
        "proximity_message": "Serving Derry attorneys with comprehensive forensic economic services through flexible consultation arrangements"
    },
    {
        "name": "Portsmouth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "21,956",
        "county": "Rockingham County",
        "distance_miles": 110,
        "major_employers": "Portsmouth Naval Shipyard (nearby), Portsmouth Regional Hospital",
        "court_info": "Rockingham County Superior Court, Portsmouth District Court",
        "economy": "Historic seaport with tourism, healthcare, and naval shipyard employment",
        "proximity_message": "Serving Portsmouth attorneys with expert forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Laconia",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "16,871",
        "county": "Belknap County",
        "distance_miles": 115,
        "major_employers": "Lakes Region General Hospital, automotive and manufacturing",
        "court_info": "Belknap County Superior Court, Laconia District Court",
        "economy": "Lakes Region center with healthcare, manufacturing, and tourism",
        "proximity_message": "Serving Laconia attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Salem",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "30,089",
        "county": "Rockingham County",
        "distance_miles": 75,
        "major_employers": "Retail centers, Enterprise Technology Center",
        "court_info": "Rockingham County Superior Court, Salem District Court",
        "economy": "Border town with major retail and growing business parks",
        "proximity_message": "Serving Salem attorneys with expert forensic economic services through flexible consultation options"
    },
    
    # MAINE
    {
        "name": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "68,408",
        "county": "Cumberland County",
        "distance_miles": 160,
        "major_employers": "Maine Medical Center, Mercy Hospital, IDEXX Laboratories, WEX",
        "court_info": "Cumberland County Superior Court, U.S. District Court for Maine",
        "economy": "Maine's largest city and economic hub with healthcare, biotechnology, financial services, and tourism",
        "proximity_message": "Serving Portland attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony at trial"
    },
    {
        "name": "Lewiston",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "36,592",
        "county": "Androscoggin County",
        "distance_miles": 130,
        "major_employers": "Central Maine Medical Center, Bates College, Geiger Brothers",
        "court_info": "Androscoggin County Superior Court, Lewiston District Court",
        "economy": "Healthcare, education, and light manufacturing with French-Canadian heritage",
        "proximity_message": "Serving Lewiston attorneys with expert forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Bangor",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "31,753",
        "county": "Penobscot County",
        "distance_miles": 220,
        "major_employers": "Northern Light Eastern Maine Medical Center, Husson University, Cross Insurance",
        "court_info": "Penobscot County Superior Court, Bangor District Court",
        "economy": "Regional healthcare and service center for northern and eastern Maine",
        "proximity_message": "Serving Bangor attorneys with comprehensive forensic economic services through virtual evaluations and scheduled in-person testimony"
    },
    {
        "name": "South Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "26,498",
        "county": "Cumberland County",
        "distance_miles": 165,
        "major_employers": "Maine Mall area retail, Anthem Blue Cross, oil terminals",
        "court_info": "Cumberland County Superior Court",
        "economy": "Retail center, healthcare administration, and petroleum storage",
        "proximity_message": "Serving South Portland attorneys with expert forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Auburn",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "24,061",
        "county": "Androscoggin County",
        "distance_miles": 130,
        "major_employers": "Central Maine Medical Center (shared with Lewiston), manufacturing",
        "court_info": "Androscoggin County Superior Court",
        "economy": "Twin city with Lewiston, manufacturing and healthcare services",
        "proximity_message": "Serving Auburn attorneys with comprehensive forensic economic services through virtual meetings and in-person testimony"
    },
    {
        "name": "Biddeford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "22,552",
        "county": "York County",
        "distance_miles": 140,
        "major_employers": "Southern Maine Health Care, University of New England",
        "court_info": "York County Superior Court, Biddeford District Court",
        "economy": "Healthcare, higher education, and revitalized mill district",
        "proximity_message": "Serving Biddeford attorneys with expert forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Augusta",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "18,899",
        "county": "Kennebec County",
        "distance_miles": 165,
        "major_employers": "State of Maine, MaineGeneral Medical Center, Togus VA",
        "court_info": "Kennebec County Superior Court, Maine Supreme Judicial Court",
        "economy": "State capital with government, healthcare, and veterans services",
        "proximity_message": "Serving Augusta attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Saco",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,381",
        "county": "York County",
        "distance_miles": 140,
        "major_employers": "General Dynamics, Saco Defense, retail and tourism",
        "court_info": "York County Superior Court",
        "economy": "Defense manufacturing, retail, and coastal tourism",
        "proximity_message": "Serving Saco attorneys with expert forensic economic services through virtual meetings and in-person testimony"
    },
    {
        "name": "Westbrook",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,400",
        "county": "Cumberland County",
        "distance_miles": 155,
        "major_employers": "IDEXX Laboratories, Spring Harbor Hospital, retail",
        "court_info": "Cumberland County Superior Court",
        "economy": "Biotechnology, behavioral health services, and retail",
        "proximity_message": "Serving Westbrook attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Waterville",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "15,722",
        "county": "Kennebec County",
        "distance_miles": 175,
        "major_employers": "MaineGeneral Medical Center, Colby College, Huhtamaki",
        "court_info": "Kennebec County Superior Court, Waterville District Court",
        "economy": "Healthcare, higher education, and manufacturing",
        "proximity_message": "Serving Waterville attorneys with expert forensic economic services through virtual consultations and scheduled in-person testimony"
    },
    
    # VERMONT
    {
        "name": "Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "44,743",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_employers": "University of Vermont Medical Center, University of Vermont, GlobalFoundries",
        "court_info": "Chittenden County Superior Court, U.S. District Court for Vermont",
        "economy": "Vermont's largest city with healthcare, education, and technology manufacturing",
        "proximity_message": "Serving Burlington attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony at trial"
    },
    {
        "name": "South Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "20,292",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_employers": "Burlington International Airport, retail centers, corporate offices",
        "court_info": "Chittenden County Superior Court",
        "economy": "Commercial center with airport, retail, and corporate headquarters",
        "proximity_message": "Serving South Burlington attorneys with expert forensic economic services through virtual consultations and scheduled in-person testimony"
    },
    {
        "name": "Rutland",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,807",
        "county": "Rutland County",
        "distance_miles": 190,
        "major_employers": "Rutland Regional Medical Center, General Electric, Casella Waste Systems",
        "court_info": "Rutland County Superior Court, Rutland District Court",
        "economy": "Regional center with healthcare, manufacturing, and service industries",
        "proximity_message": "Serving Rutland attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony when required"
    },
    {
        "name": "Essex Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "10,761",
        "county": "Chittenden County",
        "distance_miles": 280,
        "major_employers": "GlobalFoundries, IBM (historical), technology companies",
        "court_info": "Chittenden County Superior Court",
        "economy": "Technology manufacturing hub with semiconductor production",
        "proximity_message": "Serving Essex Junction attorneys with expert forensic economic services through virtual meetings and scheduled in-person testimony"
    },
    {
        "name": "Barre",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "8,491",
        "county": "Washington County",
        "distance_miles": 240,
        "major_employers": "Central Vermont Medical Center, granite industry",
        "court_info": "Washington County Superior Court",
        "economy": "Granite capital with healthcare and stone industry",
        "proximity_message": "Serving Barre attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Montpelier",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "8,074",
        "county": "Washington County",
        "distance_miles": 235,
        "major_employers": "State of Vermont, National Life Group, Vermont Mutual",
        "court_info": "Washington County Superior Court, Vermont Supreme Court",
        "economy": "State capital with government and insurance company headquarters",
        "proximity_message": "Serving Montpelier attorneys with expert forensic economic services through virtual evaluations and scheduled in-person testimony"
    },
    {
        "name": "St. Albans",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "6,877",
        "county": "Franklin County",
        "distance_miles": 300,
        "major_employers": "Northwestern Medical Center, Mylan Technologies",
        "court_info": "Franklin County Superior Court",
        "economy": "Healthcare and pharmaceutical manufacturing",
        "proximity_message": "Serving St. Albans attorneys with comprehensive forensic economic services through virtual consultations and scheduled court appearances"
    },
    {
        "name": "Brattleboro",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "12,184",
        "county": "Windham County",
        "distance_miles": 150,
        "major_employers": "Brattleboro Memorial Hospital, Brattleboro Retreat",
        "court_info": "Windham County Superior Court",
        "economy": "Healthcare, mental health services, and arts community",
        "proximity_message": "Serving Brattleboro attorneys with expert forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Bennington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,333",
        "county": "Bennington County",
        "distance_miles": 170,
        "major_employers": "Southwestern Vermont Medical Center, Bennington College",
        "court_info": "Bennington County Superior Court",
        "economy": "Healthcare, education, and manufacturing",
        "proximity_message": "Serving Bennington attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "St. Johnsbury",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "7,364",
        "county": "Caledonia County",
        "distance_miles": 270,
        "major_employers": "Northeastern Vermont Regional Hospital, Fairbanks Scales",
        "court_info": "Caledonia County Superior Court",
        "economy": "Healthcare, manufacturing, and regional services",
        "proximity_message": "Serving St. Johnsbury attorneys with expert forensic economic services through virtual meetings and scheduled court appearances"
    }
]

# Template for Northern New England forensic economics pages
def generate_northern_ne_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-{city['state_abbr'].lower()}-forensic-economist.html"
    
    # Determine the proximity/service message based on distance
    if city['distance_miles'] <= 20:
        location_flexibility = "immediate response times and flexible meeting locations"
    elif city['distance_miles'] <= 50:
        location_flexibility = "both in-person and virtual consultation options"
    else:
        location_flexibility = "comprehensive service through virtual consultations and in-person testimony"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Forensic Economist {city['name']} {city['state_abbr']} | Economic Damage Expert | Chris Skerritt</title>
<meta content="Expert forensic economist serving {city['name']}, {city['state']} attorneys. Economic damage calculations, lost earnings analysis, expert testimony. Free consultation 203-605-2814" name="description"/>
<link href="../../css/styles.css" rel="stylesheet"/>
<link href="../../css/services.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://skerritteconomics.com/locations/forensic-economics/{filename}" rel="canonical"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Structured Data -->
<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Forensic Economics Services in {city['name']}, {city['state_abbr']}",
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
    "description": "Expert forensic economist providing economic damage analysis, lost earnings calculations, and expert testimony for attorneys in {city['name']}, {city['state']}.",
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
            "name": "What types of economic damages do you calculate for {city['name']} attorneys?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with {city['state']} law and are tailored to local wage data and economic conditions in {city['county']}."
            }}
        }},
        {{
            "@type": "Question",
            "name": "How quickly can you provide economic damage reports in {city['name']}?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{city['proximity_message']}. Preliminary damage assessments are typically available within 3-5 business days, with comprehensive reports completed within 2-3 weeks depending on case complexity."
            }}
        }},
        {{
            "@type": "Question",
            "name": "Do you testify in {city['county']} courts?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout {city['state']}'s court system."
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
            "name": "Forensic Economics",
            "item": "https://skerritteconomics.com/locations/forensic-economics/"
        }},
        {{
            "@type": "ListItem",
            "position": 4,
            "name": "{city['name']}, {city['state_abbr']}",
            "item": "https://skerritteconomics.com/locations/forensic-economics/{filename}"
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
<span class="breadcrumb-current">Forensic Economist {city['name']} {city['state_abbr']}</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Forensic Economist in {city['name']}, {city['state']}</h1>
<div class="meta">
<span>Economic Damage Expert</span>
<span>Court-Qualified</span>
<span>Serving {city['county']}</span>
</div>
<p class="lead">Expert forensic economics services for {city['name']} attorneys. Comprehensive economic damage calculations, lost earnings analysis, and expert testimony for personal injury, wrongful death, and employment cases. {city['proximity_message']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Forensic Economics Services in {city['name']}</h2>
<p>As a leading forensic economist serving {city['name']}, we provide comprehensive economic damage analysis for attorneys throughout {city['county']}. With a population of {city['population']}, {city['name']} is home to major employers including {city['major_employers']}, creating a unique economic landscape that requires specialized knowledge for accurate damage calculations.</p>
<p>{city['economy']}. Our forensic economic analyses incorporate this local economic context, ensuring that damage calculations reflect the actual earning opportunities and economic conditions in the {city['name']} area.</p>
</div>
<!-- Services for Local Attorneys -->
<div class="service-section">
<h2>Economic Damage Analysis for {city['name']} Attorneys</h2>
<p>We provide {city['name']} law firms with reliable economic analysis for cases in {city['court_info']}. Our comprehensive services include:</p>
<ul>
<li><strong>Lost Earnings Calculations:</strong> Past and future wage loss analysis using {city['county']} wage data and employment statistics</li>
<li><strong>Earning Capacity Evaluations:</strong> Assessment of diminished earning potential based on local labor market conditions</li>
<li><strong>Household Services Valuation:</strong> Market-based replacement cost analysis for lost household contributions</li>
<li><strong>Fringe Benefits Analysis:</strong> Comprehensive evaluation of lost employment benefits typical in {city['name']} employers</li>
<li><strong>Business Loss Quantification:</strong> Lost profits and business value diminution for commercial cases</li>
<li><strong>Present Value Calculations:</strong> Proper discounting to present value using accepted methodologies</li>
</ul>
</div>
<!-- Local Economic Factors -->
<div class="service-section">
<h2>Understanding {city['name']}'s Economic Landscape</h2>
<p>Accurate economic damage calculations require deep understanding of local economic conditions. Key factors in {city['name']} include:</p>
<ul>
<li><strong>Major Employers:</strong> {city['major_employers']}</li>
<li><strong>Labor Market:</strong> Employment patterns and wage scales specific to {city['county']}</li>
<li><strong>Industry Mix:</strong> Understanding of dominant industries and their compensation structures</li>
<li><strong>Cost of Living:</strong> Local cost factors that impact damage calculations</li>
<li><strong>Future Growth:</strong> Economic development trends affecting long-term earning projections</li>
</ul>
<p>This local expertise ensures that economic damage calculations accurately reflect the reality of working and living in {city['name']}, not just state or national averages.</p>
</div>
<!-- Court Experience -->
<div class="service-section">
<h2>Court Experience in {city['county']}</h2>
<p>Our firm has extensive experience providing expert testimony in {city['state']} courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences and negotiations</li>
</ul>
<p>Our reports are designed to meet {city['state']}'s evidentiary standards, and we work closely with {city['name']} attorneys to ensure all economic damage calculations are clearly presented and defensible.</p>
</div>
<!-- Common Case Types -->
<div class="service-section">
<h2>Common {city['name']} Forensic Economics Cases</h2>
<h3>Personal Injury & Wrongful Death:</h3>
<ul>
<li>Motor vehicle accidents on local roads and highways</li>
<li>Workplace injuries at {city['name']} employers</li>
<li>Medical malpractice at area healthcare facilities</li>
<li>Premises liability at retail and commercial properties</li>
</ul>
<h3>Employment Litigation:</h3>
<ul>
<li>Wrongful termination from major employers</li>
<li>Discrimination and harassment cases</li>
<li>Wage and hour disputes</li>
<li>Non-compete and trade secret violations</li>
</ul>
<h3>Commercial Damages:</h3>
<ul>
<li>Business interruption losses</li>
<li>Breach of contract damages</li>
<li>Partnership and shareholder disputes</li>
<li>Professional malpractice economic losses</li>
</ul>
</div>
<!-- Service Delivery -->
<div class="service-section">
<h2>How We Serve {city['name']} Attorneys</h2>
<p>{city['proximity_message']}, offering {location_flexibility}. Our service delivery includes:</p>
<ul>
<li><strong>Initial Consultation:</strong> Free case evaluation to determine economic issues and damage potential</li>
<li><strong>Flexible Meeting Options:</strong> In-person meetings at your office, our Smithfield office, or via secure video conference</li>
<li><strong>Rapid Response:</strong> Preliminary damage estimates within 3-5 business days</li>
<li><strong>Comprehensive Reports:</strong> Detailed written reports with supporting documentation and exhibits</li>
<li><strong>Expert Testimony:</strong> Clear, persuasive presentation of economic damages in deposition and trial</li>
</ul>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Forensic Economics</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What types of economic damages do you calculate for {city['name']} attorneys?</summary>
<p>For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with {city['state']} law and are tailored to local wage data and economic conditions in {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How quickly can you provide economic damage reports in {city['name']}?</summary>
<p>{city['proximity_message']}. Preliminary damage assessments are typically available within 3-5 business days, with comprehensive reports completed within 2-3 weeks depending on case complexity.</p>
</details>
<details class="faq-item">
<summary>Do you testify in {city['county']} courts?</summary>
<p>Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout {city['state']}'s court system.</p>
</details>
<details class="faq-item">
<summary>What makes your {city['name']} economic damage calculations reliable?</summary>
<p>Our calculations use local {city['county']} wage data, employment statistics, and economic conditions specific to the {city['name']} area. We employ accepted forensic economic methodologies while incorporating deep knowledge of the local economy, major employers, and labor market conditions.</p>
</details>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need a Forensic Economist in {city['name']}?</h2>
<p>Free consultation for {city['name']} attorneys. Get expert economic damage analysis for your personal injury, wrongful death, or employment cases.</p>
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
<p>Expert forensic economics for {city['name']} attorneys.</p>
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
</body>
</html>"""
    
    # Write the file
    filepath = f"/Users/chrisskerritt/SEC/locations/forensic-economics/{filename}"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

# Generate all Northern New England city pages
for city in northern_ne_cities:
    generate_northern_ne_page(city)

print(f"\nGenerated {len(northern_ne_cities)} Northern New England forensic economics pages!")
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