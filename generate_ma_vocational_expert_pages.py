#!/usr/bin/env python3
import os

# Massachusetts cities with vocational expert focus - excluding Boston, Worcester, Springfield, Cambridge, Lowell which already exist
ma_cities = [
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
        "name": "Quincy",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,636",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_employers": "State Street Corporation, Stop & Shop headquarters, Boston Scientific",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban city with strong financial services, retail headquarters, and medical device manufacturing",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Quincy attorneys with timely vocational evaluations and flexible consultation options"
    },
    {
        "name": "Lynn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,253",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "General Electric, North Shore Community College, Lynn Community Health Center",
        "court_info": "Essex County Superior Court (Salem), Lynn District Court",
        "economy": "Historic manufacturing center transitioning to healthcare, education, and service industries",
        "proximity_message": "Serving Lynn attorneys with comprehensive vocational services through virtual consultations and in-person meetings when required"
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
        "proximity_message": "Located 35 miles from our Smithfield office, we provide prompt vocational services to New Bedford attorneys with flexible meeting arrangements"
    },
    {
        "name": "Fall River",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "94,000",
        "county": "Bristol County",
        "distance_miles": 25,
        "major_employers": "Saint Anne's Hospital, Amazon Fulfillment Center, BayCoast Bank",
        "court_info": "Bristol County Superior Court (Fall River), Fall River District Court",
        "economy": "Former textile center now focused on healthcare, distribution, and retail with waterfront redevelopment",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person vocational evaluations and court testimony for Fall River cases"
    },
    {
        "name": "Newton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "88,923",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "Newton-Wellesley Hospital, Boston College, TripAdvisor headquarters",
        "court_info": "Middlesex County Superior Court, Newton District Court",
        "economy": "Affluent suburban city with healthcare, higher education, and corporate headquarters",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide expert vocational services to Newton attorneys with flexible scheduling options"
    },
    {
        "name": "Lawrence",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "89,143",
        "county": "Essex County",
        "distance_miles": 60,
        "major_employers": "Lawrence General Hospital, New Balance, Polartec",
        "court_info": "Essex County Superior Court (Lawrence), Lawrence District Court",
        "economy": "Historic mill city with manufacturing, healthcare, and growing immigrant entrepreneurship",
        "proximity_message": "Serving Lawrence attorneys with comprehensive vocational evaluations through both virtual consultations and in-person meetings"
    },
    {
        "name": "Somerville",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "81,360",
        "county": "Middlesex County",
        "distance_miles": 48,
        "major_employers": "Tufts University, Cambridge Health Alliance, numerous tech startups",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "economy": "Dense urban community with education, healthcare, and growing technology sector near Boston",
        "proximity_message": "Located 48 miles from our Smithfield office, we serve Somerville attorneys with timely vocational assessments and court testimony"
    },
    {
        "name": "Framingham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "72,362",
        "county": "Middlesex County",
        "distance_miles": 40,
        "major_employers": "MetroWest Medical Center, Staples headquarters, TJX Companies, Bose Corporation",
        "court_info": "Middlesex County Superior Court, Framingham District Court",
        "economy": "Major retail and corporate center with healthcare, corporate headquarters, and technology companies",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Framingham attorneys with convenient consultation options"
    },
    {
        "name": "Haverhill",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "67,787",
        "county": "Essex County",
        "distance_miles": 70,
        "major_employers": "Holy Family Hospital, Whittier Rehabilitation Hospital, various manufacturers",
        "court_info": "Essex County Superior Court, Haverhill District Court",
        "economy": "Historic shoe manufacturing city now focused on healthcare and diversified manufacturing",
        "proximity_message": "Serving Haverhill attorneys with expert vocational services through virtual consultations and in-person meetings at trial"
    },
    {
        "name": "Waltham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "65,218",
        "county": "Middlesex County",
        "distance_miles": 42,
        "major_employers": "Brandeis University, Bentley University, Raytheon, Boston Dynamics",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "economy": "Technology and education hub with defense contractors and innovative robotics companies",
        "proximity_message": "Located 42 miles from our Smithfield office, we provide timely vocational evaluations to Waltham attorneys"
    },
    {
        "name": "Malden",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "66,263",
        "county": "Middlesex County",
        "distance_miles": 50,
        "major_employers": "Hallmark Health System, Cambridge Health Alliance, retail and service businesses",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Diverse urban community with healthcare, retail, and proximity to Boston employment",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Malden attorneys with flexible vocational assessment options"
    },
    {
        "name": "Medford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,659",
        "county": "Middlesex County",
        "distance_miles": 48,
        "major_employers": "Tufts University, Lawrence Memorial Hospital, various healthcare providers",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "economy": "University city with healthcare, education, and residential community near Boston",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide comprehensive vocational services to Medford attorneys"
    },
    {
        "name": "Taunton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,408",
        "county": "Bristol County",
        "distance_miles": 25,
        "major_employers": "Morton Hospital, Taunton State Hospital, GE Lighting, Kopin Corporation",
        "court_info": "Bristol County Superior Court (Taunton), Taunton District Court",
        "economy": "Regional center with healthcare, state facilities, and light manufacturing",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person vocational evaluations for Taunton cases"
    },
    {
        "name": "Weymouth",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "57,213",
        "county": "Norfolk County",
        "distance_miles": 45,
        "major_employers": "South Shore Hospital, Siemens Healthcare, various retail centers",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Suburban community with healthcare, medical technology, and retail employment",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Weymouth attorneys with timely vocational assessments"
    },
    {
        "name": "Revere",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "62,186",
        "county": "Suffolk County",
        "distance_miles": 55,
        "major_employers": "Massachusetts Gaming Commission, hotels and hospitality, Suffolk Downs redevelopment",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "economy": "Coastal city with gaming, hospitality, and major development projects underway",
        "proximity_message": "Serving Revere attorneys with comprehensive vocational evaluations through flexible consultation arrangements"
    },
    {
        "name": "Peabody",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "54,481",
        "county": "Essex County",
        "distance_miles": 60,
        "major_employers": "Lahey Hospital & Medical Center, Analogic Corporation, Boston Children's at Peabody",
        "court_info": "Essex County Superior Court, Peabody District Court",
        "economy": "Former leather industry center now focused on healthcare and medical technology",
        "proximity_message": "Serving Peabody attorneys with expert vocational services through both virtual and in-person consultations"
    },
    {
        "name": "Methuen",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "53,059",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "Holy Family Hospital, Nevins Nursing Home, various retail centers",
        "court_info": "Essex County Superior Court, Lawrence District Court",
        "economy": "Mix of healthcare, retail, and light manufacturing near New Hampshire border",
        "proximity_message": "Providing vocational evaluations to Methuen attorneys through virtual consultations and in-person meetings when needed"
    },
    {
        "name": "Everett",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "49,075",
        "county": "Middlesex County",
        "distance_miles": 52,
        "major_employers": "Encore Boston Harbor, Cambridge Health Alliance, industrial businesses",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "economy": "Industrial city with new casino resort, healthcare, and transportation logistics",
        "proximity_message": "Located 52 miles from our Smithfield office, we serve Everett attorneys with comprehensive vocational assessments"
    },
    {
        "name": "Salem",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "44,480",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "North Shore Medical Center, Salem State University, tourism industry",
        "court_info": "Essex County Superior Court (Salem), Salem District Court",
        "economy": "Historic seaport with healthcare, education, and significant tourism sector",
        "proximity_message": "Serving Salem attorneys with expert vocational evaluations through flexible scheduling and consultation options"
    },
    {
        "name": "Chicopee",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "55,560",
        "county": "Hampden County",
        "distance_miles": 65,
        "major_employers": "Baystate Medical Center, Westover Air Reserve Base, Callaway Golf",
        "court_info": "Hampden County Superior Court, Chicopee District Court",
        "economy": "Manufacturing and military presence with healthcare and recreational equipment production",
        "proximity_message": "Providing comprehensive vocational services to Chicopee attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Westfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,094",
        "county": "Hampden County",
        "distance_miles": 70,
        "major_employers": "Westfield State University, Barnes Regional Airport, C&S Wholesale Grocers",
        "court_info": "Hampden County Superior Court, Westfield District Court",
        "economy": "Education, aviation, and distribution center for western Massachusetts",
        "proximity_message": "Serving Westfield attorneys with vocational evaluations through virtual consultations and in-person meetings at trial"
    },
    {
        "name": "Beverly",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "42,670",
        "county": "Essex County",
        "distance_miles": 65,
        "major_employers": "Beverly Hospital, Endicott College, Axcelis Technologies",
        "court_info": "Essex County Superior Court, Salem District Court",
        "economy": "Healthcare, education, and technology manufacturing on North Shore",
        "proximity_message": "Providing expert vocational services to Beverly attorneys through flexible consultation arrangements"
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
        "economy": "Paper City transitioning to healthcare, education, and clean energy",
        "proximity_message": "Serving Holyoke attorneys with comprehensive vocational evaluations through virtual and in-person options"
    },
    {
        "name": "Marlborough",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,793",
        "county": "Middlesex County",
        "distance_miles": 38,
        "major_employers": "Boston Scientific, Quest Diagnostics, Raytheon, Hologic",
        "court_info": "Middlesex County Superior Court, Marlborough District Court",
        "economy": "High-tech corridor with medical devices, diagnostics, and defense technology",
        "proximity_message": "Located 38 miles from our Smithfield office, we regularly serve Marlborough attorneys with convenient consultations"
    },
    {
        "name": "Fitchburg",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,946",
        "county": "Worcester County",
        "distance_miles": 50,
        "major_employers": "Fitchburg State University, HealthAlliance Hospital, Fitchburg Art Museum",
        "court_info": "Worcester County Superior Court, Fitchburg District Court",
        "economy": "Education and healthcare anchor economy with arts and cultural sector",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Fitchburg attorneys with timely vocational assessments"
    },
    {
        "name": "Woburn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "40,876",
        "county": "Middlesex County",
        "distance_miles": 48,
        "major_employers": "Monotype Imaging, Skyworks Solutions, McLane Northeast",
        "court_info": "Middlesex County Superior Court, Woburn District Court",
        "economy": "Technology and distribution hub with corporate offices and light manufacturing",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide efficient vocational services to Woburn attorneys"
    },
    {
        "name": "Chelsea",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "40,787",
        "county": "Suffolk County",
        "distance_miles": 52,
        "major_employers": "Massachusetts General Hospital Chelsea, FBI Boston Division, produce market",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "economy": "Dense urban community with healthcare, federal facilities, and food distribution",
        "proximity_message": "Located 52 miles from our Smithfield office, we serve Chelsea attorneys with comprehensive vocational evaluations"
    },
    {
        "name": "Leominster",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,782",
        "county": "Worcester County",
        "distance_miles": 45,
        "major_employers": "HealthAlliance Hospital, Leominster Credit Union, plastics manufacturers",
        "court_info": "Worcester County Superior Court, Leominster District Court",
        "economy": "Pioneer plastics city with healthcare and diversified manufacturing",
        "proximity_message": "Located 45 miles from our Smithfield office, we regularly serve Leominster attorneys with flexible consultations"
    },
    {
        "name": "Pittsfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,927",
        "county": "Berkshire County",
        "distance_miles": 115,
        "major_employers": "Berkshire Medical Center, General Dynamics, Berkshire County government",
        "court_info": "Berkshire County Superior Court, Pittsfield District Court",
        "economy": "Berkshire County seat with healthcare, defense manufacturing, and cultural institutions",
        "proximity_message": "Serving Pittsfield attorneys with vocational evaluations through virtual consultations and in-person testimony at trial"
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
        "economy": "Jewelry City with precision manufacturing, healthcare, and technology",
        "proximity_message": "Located just 15 miles from our Smithfield office, we offer immediate availability for Attleboro vocational evaluations"
    },
    {
        "name": "Barnstable",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "48,916",
        "county": "Barnstable County",
        "distance_miles": 75,
        "major_employers": "Cape Cod Hospital, Cape Cod Community College, retail and tourism",
        "court_info": "Barnstable County Superior Court, Barnstable District Court",
        "economy": "Cape Cod's commercial hub with healthcare, education, and seasonal tourism",
        "proximity_message": "Serving Cape Cod attorneys with comprehensive vocational services through virtual consultations and scheduled visits"
    },
    {
        "name": "Northampton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "29,571",
        "county": "Hampshire County",
        "distance_miles": 75,
        "major_employers": "Cooley Dickinson Hospital, Smith College, Northampton State Hospital",
        "court_info": "Hampshire County Superior Court, Northampton District Court",
        "economy": "Education and healthcare with vibrant arts scene and small business sector",
        "proximity_message": "Serving Northampton attorneys with vocational evaluations through virtual consultations and in-person meetings"
    },
    {
        "name": "Randolph",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "34,984",
        "county": "Norfolk County",
        "distance_miles": 42,
        "major_employers": "Healthcare facilities, Lantheus Medical Imaging, retail businesses",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "economy": "Diverse suburban community with healthcare and small business employment",
        "proximity_message": "Located 42 miles from our Smithfield office, we provide timely vocational services to Randolph attorneys"
    },
    {
        "name": "Watertown",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "35,329",
        "county": "Middlesex County",
        "distance_miles": 45,
        "major_employers": "athenahealth, Perkins School for the Blind, biotech companies",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "economy": "Growing biotech and healthcare technology sector near Cambridge",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Watertown attorneys with efficient vocational evaluations"
    },
    {
        "name": "Franklin",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "33,261",
        "county": "Norfolk County",
        "distance_miles": 25,
        "major_employers": "Dean College, EMC Corporation, Garelick Farms",
        "court_info": "Norfolk County Superior Court, Wrentham District Court",
        "economy": "Growing suburban community with education, technology, and manufacturing",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person vocational evaluations for Franklin cases"
    },
    {
        "name": "Lexington",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "34,454",
        "county": "Middlesex County",
        "distance_miles": 48,
        "major_employers": "Shire Pharmaceuticals, MIT Lincoln Laboratory, healthcare practices",
        "court_info": "Middlesex County Superior Court, Concord District Court",
        "economy": "Affluent suburban community with pharmaceuticals, defense research, and professional services",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide expert vocational services to Lexington attorneys"
    },
    {
        "name": "Gloucester",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "30,291",
        "county": "Essex County",
        "distance_miles": 75,
        "major_employers": "Addison Gilbert Hospital, fishing industry, tourism businesses",
        "court_info": "Essex County Superior Court, Gloucester District Court",
        "economy": "America's oldest seaport with fishing, healthcare, and tourism industries",
        "proximity_message": "Serving Gloucester attorneys with vocational evaluations through virtual consultations and scheduled court appearances"
    }
]

# Template for Massachusetts vocational expert pages
def generate_ma_vocational_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ma-vocational-expert.html"
    
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
<title>Vocational Expert {city['name']} MA | Earning Capacity & Employability | Chris Skerritt</title>
<meta content="Expert vocational evaluation services in {city['name']}, Massachusetts. Court-qualified vocational expert for personal injury, disability, and employment cases. Call 203-605-2814" name="description"/>
<link href="../../css/styles.css" rel="stylesheet"/>
<link href="../../css/services.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://skerritteconomics.com/locations/vocational-expert/{filename}" rel="canonical"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Structured Data -->
<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Vocational Expert Services in {city['name']}, MA",
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
    "description": "Expert vocational evaluation and earning capacity assessment services for {city['name']}, Massachusetts. Court-qualified vocational expert serving attorneys and individuals in personal injury, disability, and employment matters.",
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
            "name": "What does a vocational expert do in {city['name']}, MA?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "A vocational expert in {city['name']} evaluates an individual's ability to work and earn income despite injuries or disabilities. We assess transferable skills, labor market conditions, and provide expert testimony in {city['court_info']}. Our services include employability assessments, earning capacity evaluations, and job placement analysis for legal cases."
            }}
        }},
        {{
            "@type": "Question",
            "name": "When do I need a vocational expert for my {city['name']} case?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "You need a vocational expert when determining lost earning capacity in personal injury cases, evaluating disability claims, assessing employability after workplace injuries, or analyzing vocational rehabilitation needs. {city['proximity_message']}."
            }}
        }},
        {{
            "@type": "Question",
            "name": "What is the {city['name']} job market like for injured workers?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{city['economy']}. Major employers include {city['major_employers']}. Our vocational assessments consider these local employment opportunities when evaluating earning capacity and job placement options for injured workers."
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
            "name": "Vocational Expert",
            "item": "https://skerritteconomics.com/locations/vocational-expert/"
        }},
        {{
            "@type": "ListItem",
            "position": 4,
            "name": "{city['name']}, MA",
            "item": "https://skerritteconomics.com/locations/vocational-expert/{filename}"
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
<span class="breadcrumb-current">Vocational Expert {city['name']} MA</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Vocational Expert in {city['name']}, Massachusetts</h1>
<div class="meta">
<span>CRC, CLCP, ABVE/F</span>
<span>Court-Qualified Expert</span>
<span>Serving {city['county']}</span>
</div>
<p class="lead">Expert vocational evaluation services for {city['name']} attorneys and insurance professionals. Comprehensive earning capacity assessments, employability evaluations, and labor market analysis. {city['proximity_message']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Vocational Expert Services in {city['name']}</h2>
<p>As a certified rehabilitation counselor serving {city['name']}, I provide comprehensive vocational evaluations for legal cases throughout {city['county']}. With a population of {city['population']}, {city['name']}'s economy presents unique employment opportunities and challenges that require local expertise.</p>
<p>{city['economy']}. Understanding these local employment dynamics is crucial for accurate vocational assessments and earning capacity evaluations.</p>
</div>
<!-- Local Employment Landscape -->
<div class="service-section">
<h2>{city['name']} Employment Market Analysis</h2>
<p>Key employers in {city['name']} include {city['major_employers']}. Our vocational assessments incorporate:</p>
<ul>
<li><strong>Local Labor Market:</strong> Analysis of available positions matching client's restrictions and qualifications</li>
<li><strong>Wage Data:</strong> Current wage rates for specific occupations in the {city['name']} area</li>
<li><strong>Commute Factors:</strong> Reasonable commuting distances to employment opportunities</li>
<li><strong>Industry Trends:</strong> Growth or decline in relevant employment sectors</li>
<li><strong>Transferable Skills:</strong> How client's work history translates to {city['name']}'s job market</li>
</ul>
</div>
<!-- Services for Local Attorneys -->
<div class="service-section">
<h2>Supporting {city['name']} Legal Professionals</h2>
<p>I provide {city['name']} attorneys with credible vocational evidence for cases in {city['court_info']}. My services include:</p>
<ul>
<li><strong>Personal Injury:</strong> Earning capacity loss due to accident-related limitations</li>
<li><strong>Workers' Compensation:</strong> Employability and wage loss assessments</li>
<li><strong>Disability Claims:</strong> Functional capacity and work capability evaluations</li>
<li><strong>Employment Litigation:</strong> Wrongful termination and discrimination impact analysis</li>
<li><strong>Family Law:</strong> Earning capacity evaluations for support determinations</li>
<li><strong>Expert Testimony:</strong> Clear, defensible opinions in depositions and trial</li>
</ul>
</div>
<!-- Court Experience -->
<div class="service-section">
<h2>Court Experience in {city['county']}</h2>
<p>Our firm has extensive experience providing expert testimony in Massachusetts courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Massachusetts Department of Industrial Accidents</li>
<li>U.S. District Court for the District of Massachusetts</li>
<li>Social Security disability hearings</li>
</ul>
<p>We understand the specific requirements and expectations of {city['name']} area courts and provide reports that meet these standards.</p>
</div>
<!-- Vocational Assessment Process -->
<div class="service-section">
<h2>Our {city['name']} Vocational Assessment Process</h2>
<p>{city['proximity_message']}, offering {location_flexibility}. My comprehensive process includes:</p>
<ul>
<li><strong>Clinical Interview:</strong> In-person or virtual meeting to understand work history and limitations</li>
<li><strong>Records Review:</strong> Medical records, employment files, and educational documents</li>
<li><strong>Vocational Testing:</strong> Standardized assessments of interests, aptitudes, and abilities</li>
<li><strong>Transferable Skills Analysis:</strong> Identifying skills applicable to other occupations</li>
<li><strong>Labor Market Survey:</strong> Researching actual job openings in {city['name']} area</li>
<li><strong>Earning Capacity Analysis:</strong> Calculating pre- and post-injury earning potential</li>
<li><strong>Written Report:</strong> Comprehensive documentation of findings and opinions</li>
</ul>
</div>
<!-- Common Referral Sources -->
<div class="service-section">
<h2>Common {city['name']} Vocational Expert Referrals</h2>
<h3>Personal Injury Cases:</h3>
<ul>
<li>Motor vehicle accidents affecting work capacity</li>
<li>Premises liability injuries limiting employment</li>
<li>Product liability cases with permanent restrictions</li>
<li>Medical malpractice resulting in disability</li>
</ul>
<h3>Workers' Compensation:</h3>
<ul>
<li>Permanent partial disability evaluations</li>
<li>Suitable alternative employment assessments</li>
<li>Vocational rehabilitation planning</li>
<li>Loss of earning capacity calculations</li>
</ul>
<h3>Disability Claims:</h3>
<ul>
<li>Social Security disability evaluations</li>
<li>Long-term disability insurance claims</li>
<li>Veterans disability assessments</li>
<li>ADA reasonable accommodation analysis</li>
</ul>
</div>
<!-- Local Economic Factors -->
<div class="service-section">
<h2>Understanding {city['name']}'s Vocational Landscape</h2>
<p>Accurate vocational assessments require deep knowledge of local conditions:</p>
<ul>
<li><strong>Major Employers:</strong> {city['major_employers']}</li>
<li><strong>Economic Base:</strong> {city['economy']}</li>
<li><strong>Transportation:</strong> Access to public transit and commuting patterns</li>
<li><strong>Education/Training:</strong> Local vocational and educational resources</li>
<li><strong>Demographics:</strong> Population of {city['population']} with diverse workforce needs</li>
</ul>
<p>This local expertise ensures vocational opinions reflect realistic employment opportunities in {city['name']}.</p>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Vocational Expert</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What does a vocational expert do in {city['name']}, MA?</summary>
<p>A vocational expert in {city['name']} evaluates an individual's ability to work and earn income despite injuries or disabilities. We assess transferable skills, labor market conditions, and provide expert testimony in {city['court_info']}. Our services include employability assessments, earning capacity evaluations, and job placement analysis for legal cases.</p>
</details>
<details class="faq-item">
<summary>When do I need a vocational expert for my {city['name']} case?</summary>
<p>You need a vocational expert when determining lost earning capacity in personal injury cases, evaluating disability claims, assessing employability after workplace injuries, or analyzing vocational rehabilitation needs. {city['proximity_message']}.</p>
</details>
<details class="faq-item">
<summary>What is the {city['name']} job market like for injured workers?</summary>
<p>{city['economy']}. Major employers include {city['major_employers']}. Our vocational assessments consider these local employment opportunities when evaluating earning capacity and job placement options for injured workers.</p>
</details>
<details class="faq-item">
<summary>How much does a vocational evaluation cost?</summary>
<p>Vocational evaluation fees vary based on case complexity and scope of analysis required. Most comprehensive evaluations range from $2,500 to $5,000. We provide detailed fee schedules during the initial consultation.</p>
</details>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need a Vocational Expert in {city['name']}?</h2>
<p>Free consultation for {city['name']} attorneys and insurance professionals. Get credible vocational evidence from a court-qualified expert.</p>
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
<p>Expert vocational evaluation services for {city['name']} legal professionals.</p>
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
    filepath = f"/Users/chrisskerritt/SEC/locations/vocational-expert/{filename}"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

# Generate all Massachusetts city pages
for city in ma_cities:
    generate_ma_vocational_page(city)

print(f"\nGenerated {len(ma_cities)} Massachusetts vocational expert pages!")
print("\nPages created for:")
for city in ma_cities:
    print(f"- {city['name']}, MA ({city['distance_miles']} miles from Smithfield)")