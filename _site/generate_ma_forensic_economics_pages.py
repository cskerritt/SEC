#!/usr/bin/env python3
import os

# Massachusetts cities with detailed information and distances from Smithfield, RI
ma_cities = [
    {
        "name": "Boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "675,647",
        "county": "Suffolk County",
        "distance_miles": 50,
        "major_employers": "Massachusetts General Hospital, Brigham and Women's Hospital, State Street, Liberty Mutual, Boston University",
        "court_info": "Suffolk County Superior Court, U.S. District Court for Massachusetts, Massachusetts Appeals Court",
        "economy": "As the state capital and largest city, Boston has a diverse economy anchored by healthcare, education, financial services, and biotechnology",
        "proximity_message": "Located 50 miles from our Smithfield office, we provide comprehensive forensic economic services to Boston attorneys with flexible in-person and virtual consultation options"
    },
    {
        "name": "Worcester",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "206,518",
        "county": "Worcester County",
        "distance_miles": 35,
        "major_employers": "UMass Medical School, Saint Vincent Hospital, Worcester Polytechnic Institute, Hanover Insurance",
        "court_info": "Worcester County Superior Court, Worcester District Court",
        "economy": "Central Massachusetts hub with strong healthcare, education, and insurance sectors, along with growing biotechnology presence",
        "proximity_message": "Located 35 miles from our Smithfield office, we regularly serve Worcester attorneys with both in-person meetings and efficient remote consultations"
    },
    {
        "name": "Springfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "155,929",
        "county": "Hampden County",
        "distance_miles": 60,
        "major_employers": "Baystate Health, MassMutual, Smith & Wesson, MGM Springfield",
        "court_info": "Hampden County Superior Court, Springfield District Court",
        "economy": "Western Massachusetts economic center with healthcare, insurance, manufacturing, and entertainment sectors",
        "proximity_message": "Serving Springfield attorneys with comprehensive forensic economic services through both in-person consultations and virtual meetings"
    },
    {
        "name": "Cambridge",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "118,403",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "MIT, Harvard University, Biogen, Novartis, Microsoft Research",
        "court_info": "Middlesex County Superior Court, Cambridge District Court",
        "economy": "Global innovation hub with world-class universities and concentrated biotechnology and technology sectors",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide timely forensic economic services to Cambridge attorneys with flexible meeting options"
    },
    {
        "name": "Lowell",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "115,554",
        "county": "Middlesex County",
        "distance_miles": 55,
        "major_employers": "Lowell General Hospital, UMass Lowell, IBM, Kronos",
        "court_info": "Middlesex County Superior Court (Lowell), Lowell District Court",
        "economy": "Former mill city transformed into education and technology center with growing healthcare sector",
        "proximity_message": "Serving Lowell attorneys with expert forensic economic services through convenient in-person and virtual consultation options"
    },
    {
        "name": "Brockton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "105,643",
        "county": "Plymouth County",
        "distance_miles": 40,
        "major_employers": "Good Samaritan Medical Center, Brockton Area Transit Authority, Harbor One Bank",
        "court_info": "Plymouth County Superior Court (Brockton), Brockton District Court",
        "economy": "Diverse economy with healthcare, transportation, and financial services, serving as regional center for southeastern Massachusetts",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Brockton attorneys with both in-person and virtual consultations"
    },
    {
        "name": "New Bedford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,079",
        "county": "Bristol County",
        "distance_miles": 35,
        "major_employers": "Southcoast Health, fishing industry, Titleist, Acushnet Company",
        "court_info": "Bristol County Superior Court (New Bedford), New Bedford District Court",
        "economy": "Historic seaport with active fishing industry, healthcare, and manufacturing, including marine commerce",
        "proximity_message": "Located 35 miles from our Smithfield office, we provide prompt forensic economic services to New Bedford attorneys with flexible meeting arrangements"
    },
    {
        "name": "Quincy",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,636",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_employers": "State Street Corporation, Stop & Shop headquarters, Boston Scientific",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban city with strong financial services, retail headquarters, and medical device manufacturing",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Quincy attorneys with timely forensic economic evaluations and flexible consultation options"
    },
    {
        "name": "Lynn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,253",
        "county": "Essex County",
        "distance_miles": 60,
        "major_employers": "General Electric, Lynn Community Health Center, North Shore Community College",
        "court_info": "Essex County Superior Court (Salem), Lynn District Court",
        "economy": "Industrial heritage with jet engine manufacturing, healthcare, and education sectors",
        "proximity_message": "Serving Lynn attorneys with comprehensive forensic economic services through both in-person consultations and virtual meetings"
    },
    {
        "name": "Fall River",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "94,000",
        "county": "Bristol County",
        "distance_miles": 25,
        "major_employers": "Charlton Memorial Hospital, Amazon Fulfillment Center, Bristol Community College",
        "court_info": "Bristol County Superior Court (Fall River), Fall River District Court",
        "economy": "Former textile center with growing healthcare, distribution, and education sectors",
        "proximity_message": "Located just 25 miles from our Smithfield office, we provide immediate response and in-person forensic economic services to Fall River attorneys"
    },
    {
        "name": "Newton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "88,923",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "Newton-Wellesley Hospital, Boston College, TripAdvisor",
        "court_info": "Middlesex County Superior Court, Newton District Court",
        "economy": "Affluent suburban city with healthcare, higher education, and technology company headquarters",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Newton attorneys with expert forensic economic analysis and flexible meeting options"
    },
    {
        "name": "Somerville",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "81,045",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "Tufts University, Cambridge Health Alliance, American Repertory Theater",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "economy": "Dense urban community with education, healthcare, and growing tech startup ecosystem",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide timely forensic economic services to Somerville attorneys"
    },
    {
        "name": "Framingham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "72,362",
        "county": "Middlesex County",
        "distance_miles": 40,
        "major_employers": "TJX Companies, Staples headquarters, Bose Corporation, MetroWest Medical Center",
        "court_info": "Middlesex County Superior Court, Framingham District Court",
        "economy": "Major retail and corporate headquarters location with strong healthcare and technology sectors",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Framingham attorneys with both in-person and virtual consultation options"
    },
    {
        "name": "Haverhill",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "67,787",
        "county": "Essex County",
        "distance_miles": 70,
        "major_employers": "Holy Family Hospital, Northern Essex Community College, Southwick",
        "court_info": "Essex County Superior Court, Haverhill District Court",
        "economy": "Merrimack Valley city with healthcare, education, and manufacturing base",
        "proximity_message": "Serving Haverhill attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony as needed"
    },
    {
        "name": "Waltham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "65,218",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "Brandeis University, Bentley University, Raytheon Technologies",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "economy": "Education and high-tech corridor with defense contractors and research facilities",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide expert forensic economic services to Waltham attorneys with flexible consultation options"
    },
    {
        "name": "Malden",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "66,263",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_employers": "Hallmark Health, Piantedosi Baking Company",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Diverse urban community with healthcare and food production industries",
        "proximity_message": "Serving Malden attorneys with comprehensive forensic economic evaluations through both in-person and virtual meetings"
    },
    {
        "name": "Medford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,659",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_employers": "Tufts University (partial), Lawrence Memorial Hospital",
        "court_info": "Middlesex County Superior Court, Medford District Court",
        "economy": "Residential community with education and healthcare anchors",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Medford attorneys with timely forensic economic services"
    },
    {
        "name": "Taunton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,408",
        "county": "Bristol County",
        "distance_miles": 20,
        "major_employers": "Morton Hospital, Taunton State Hospital, GE Lighting",
        "court_info": "Bristol County Superior Court (Taunton), Taunton District Court",
        "economy": "Regional center with healthcare, state facilities, and manufacturing",
        "proximity_message": "Located just 20 miles from our Smithfield office, we provide immediate, in-person forensic economic services to Taunton attorneys"
    },
    {
        "name": "Weymouth",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "57,213",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_employers": "South Shore Hospital, Siemens Healthcare",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban community with healthcare and medical technology focus",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Weymouth attorneys with expert forensic economic analysis"
    },
    {
        "name": "Revere",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "62,186",
        "county": "Suffolk County",
        "distance_miles": 55,
        "major_employers": "Massachusetts Gaming Commission, various hospitality businesses",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "economy": "Coastal city with gaming, hospitality, and service industries",
        "proximity_message": "Serving Revere attorneys with comprehensive forensic economic services through flexible consultation arrangements"
    },
    {
        "name": "Peabody",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "54,481",
        "county": "Essex County",
        "distance_miles": 60,
        "major_employers": "Lahey Hospital & Medical Center (nearby), Analogic Corporation",
        "court_info": "Essex County Superior Court, Peabody District Court",
        "economy": "Former leather industry center now focused on healthcare and technology",
        "proximity_message": "Serving Peabody attorneys with expert forensic economic evaluations through virtual consultations and in-person testimony"
    },
    {
        "name": "Methuen",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "53,059",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "Holy Family Hospital, The Nevins Center",
        "court_info": "Essex County Superior Court, Lawrence District Court",
        "economy": "Merrimack Valley city with healthcare and social services focus",
        "proximity_message": "Serving Methuen attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony as needed"
    },
    {
        "name": "Barnstable",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "48,916",
        "county": "Barnstable County",
        "distance_miles": 70,
        "major_employers": "Cape Cod Hospital, Cape Cod Community College, retail/tourism",
        "court_info": "Barnstable County Superior Court, Barnstable District Court",
        "economy": "Cape Cod's commercial hub with healthcare, education, and seasonal tourism",
        "proximity_message": "Serving Cape Cod attorneys with expert forensic economic services through virtual consultations and in-person testimony when required"
    },
    {
        "name": "Pittsfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,927",
        "county": "Berkshire County",
        "distance_miles": 120,
        "major_employers": "Berkshire Medical Center, General Dynamics, Berkshire Bank",
        "court_info": "Berkshire County Superior Court, Pittsfield District Court",
        "economy": "Berkshires regional center with healthcare, defense contracting, and cultural institutions",
        "proximity_message": "Serving Berkshire County attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony at trial"
    },
    {
        "name": "Attleboro",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "46,461",
        "county": "Bristol County",
        "distance_miles": 15,
        "major_employers": "Sturdy Memorial Hospital, Sensata Technologies, jewelry manufacturers",
        "court_info": "Bristol County Superior Court, Attleboro District Court",
        "economy": "Historic jewelry manufacturing center with healthcare and technology sectors",
        "proximity_message": "Located just 15 miles from our Smithfield office, we provide immediate, cost-effective forensic economic services to Attleboro attorneys"
    },
    {
        "name": "Westfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,301",
        "county": "Hampden County",
        "distance_miles": 75,
        "major_employers": "Baystate Noble Hospital, Westfield State University, Savage Arms",
        "court_info": "Hampden County Superior Court, Westfield District Court",
        "economy": "Western Massachusetts city with healthcare, education, and manufacturing",
        "proximity_message": "Serving Westfield attorneys with expert forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Chicopee",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "55,560",
        "county": "Hampden County",
        "distance_miles": 65,
        "major_employers": "Baystate Medical Center (nearby), Westover Air Reserve Base",
        "court_info": "Hampden County Superior Court, Chicopee District Court",
        "economy": "Military presence with healthcare and manufacturing base",
        "proximity_message": "Serving Chicopee attorneys with comprehensive forensic economic services through flexible consultation options"
    },
    {
        "name": "Holyoke",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "38,238",
        "county": "Hampden County",
        "distance_miles": 70,
        "major_employers": "Holyoke Medical Center, Holyoke Community College, ISO New England",
        "court_info": "Hampden County Superior Court, Holyoke District Court",
        "economy": "Former paper mill city with healthcare, education, and energy sectors",
        "proximity_message": "Serving Holyoke attorneys with expert forensic economic evaluations through virtual consultations and in-person testimony"
    },
    {
        "name": "Beverly",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "42,670",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "Beverly Hospital, Endicott College",
        "court_info": "Essex County Superior Court, Salem District Court",
        "economy": "North Shore community with healthcare and higher education",
        "proximity_message": "Serving Beverly attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Everett",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "49,075",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_employers": "Encore Boston Harbor, Cambridge Health Alliance",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Urban community with gaming/entertainment and healthcare sectors",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Everett attorneys with timely forensic economic services"
    }
]

# Template for Massachusetts forensic economics pages
def generate_ma_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ma-forensic-economist.html"
    
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
<title>Forensic Economist {city['name']} MA | Economic Damage Expert | Chris Skerritt</title>
<meta content="Expert forensic economist serving {city['name']}, Massachusetts attorneys. Economic damage calculations, lost earnings analysis, expert testimony. Free consultation 203-605-2814" name="description"/>
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
    "name": "Forensic Economics Services in {city['name']}, MA",
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
    "description": "Expert forensic economist providing economic damage analysis, lost earnings calculations, and expert testimony for attorneys in {city['name']}, Massachusetts.",
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
            "name": "What types of economic damages do you calculate for {city['name']} attorneys?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with Massachusetts law and are tailored to local wage data and economic conditions in {city['county']}."
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
                "text": "Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout Massachusetts's court system."
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
            "name": "{city['name']}, MA",
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
<span class="breadcrumb-current">Forensic Economist {city['name']} MA</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Forensic Economist in {city['name']}, Massachusetts</h1>
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
<p>Our firm has extensive experience providing expert testimony in Massachusetts courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences and negotiations</li>
</ul>
<p>Our reports are designed to meet Massachusetts's evidentiary standards, and we work closely with {city['name']} attorneys to ensure all economic damage calculations are clearly presented and defensible.</p>
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
<p>For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with Massachusetts law and are tailored to local wage data and economic conditions in {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How quickly can you provide economic damage reports in {city['name']}?</summary>
<p>{city['proximity_message']}. Preliminary damage assessments are typically available within 3-5 business days, with comprehensive reports completed within 2-3 weeks depending on case complexity.</p>
</details>
<details class="faq-item">
<summary>Do you testify in {city['county']} courts?</summary>
<p>Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout Massachusetts's court system.</p>
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

# Generate all Massachusetts city pages
for city in ma_cities:
    generate_ma_page(city)

print(f"\nGenerated {len(ma_cities)} Massachusetts forensic economics pages!")
print("\nPages created for:")
for city in ma_cities:
    print(f"- {city['name']}, MA ({city['distance_miles']} miles from Smithfield)")