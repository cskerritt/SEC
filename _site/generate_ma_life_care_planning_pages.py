#!/usr/bin/env python3
import os

# Massachusetts cities with life care planning focus - excluding Boston, Worcester, Springfield, Cambridge, Lowell which already exist
ma_cities = [
    {
        "name": "Brockton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "105,643",
        "county": "Plymouth County",
        "distance_miles": 40,
        "medical_facilities": "Good Samaritan Medical Center, Brockton Hospital, Signature Healthcare",
        "court_info": "Plymouth County Superior Court (Brockton), Brockton District Court",
        "healthcare_landscape": "Regional medical center with comprehensive acute care, rehabilitation services, and multiple specialty clinics.",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Brockton attorneys with both in-person and virtual consultations"
    },
    {
        "name": "Quincy",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,636",
        "county": "Norfolk County",
        "distance_miles": 45,
        "medical_facilities": "Quincy Medical Center (closed - nearest is South Shore Hospital), various specialty practices",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "healthcare_landscape": "Following Quincy Medical Center closure, residents rely on nearby hospitals with strong outpatient and rehabilitation networks.",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Quincy attorneys with timely life care planning evaluations and flexible consultation options"
    },
    {
        "name": "Lynn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,253",
        "county": "Essex County",
        "distance_miles": 65,
        "medical_facilities": "Lynn Community Health Center, Union Hospital (part of Lahey Health)",
        "court_info": "Essex County Superior Court (Salem), Lynn District Court",
        "healthcare_landscape": "Community health centers and hospital services with access to Boston-area specialty care.",
        "proximity_message": "Serving Lynn attorneys with comprehensive life care planning services through virtual consultations and in-person meetings when required"
    },
    {
        "name": "New Bedford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "101,079",
        "county": "Bristol County",
        "distance_miles": 35,
        "medical_facilities": "St. Luke's Hospital, Southcoast Health System, specialized rehabilitation centers",
        "court_info": "Bristol County Superior Court (New Bedford), New Bedford District Court",
        "healthcare_landscape": "Major healthcare system serving southeastern Massachusetts with comprehensive medical and rehabilitation services.",
        "proximity_message": "Located 35 miles from our Smithfield office, we provide prompt life care planning services to New Bedford attorneys with flexible meeting arrangements"
    },
    {
        "name": "Fall River",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "94,000",
        "county": "Bristol County",
        "distance_miles": 25,
        "medical_facilities": "Saint Anne's Hospital, Charlton Memorial Hospital, rehabilitation facilities",
        "court_info": "Bristol County Superior Court (Fall River), Fall River District Court",
        "healthcare_landscape": "Dual hospital system providing comprehensive care with strong rehabilitation and home health networks.",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person life care planning evaluations and court testimony for Fall River cases"
    },
    {
        "name": "Newton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "88,923",
        "county": "Middlesex County",
        "distance_miles": 45,
        "medical_facilities": "Newton-Wellesley Hospital, numerous specialty medical practices",
        "court_info": "Middlesex County Superior Court, Newton District Court",
        "healthcare_landscape": "Premier suburban hospital with extensive specialty services and access to Boston teaching hospitals.",
        "proximity_message": "Located 45 miles from our Smithfield office, we provide expert life care planning services to Newton attorneys with flexible scheduling options"
    },
    {
        "name": "Lawrence",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "89,143",
        "county": "Essex County",
        "distance_miles": 60,
        "medical_facilities": "Lawrence General Hospital, Greater Lawrence Family Health Center",
        "court_info": "Essex County Superior Court (Lawrence), Lawrence District Court",
        "healthcare_landscape": "Community hospital with bilingual services and strong primary care network serving diverse population.",
        "proximity_message": "Serving Lawrence attorneys with comprehensive life care planning evaluations through both virtual consultations and in-person meetings"
    },
    {
        "name": "Somerville",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "81,360",
        "county": "Middlesex County",
        "distance_miles": 48,
        "medical_facilities": "Cambridge Health Alliance facilities, proximity to Boston medical centers",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "healthcare_landscape": "Access to Cambridge Health Alliance and major Boston teaching hospitals for comprehensive care.",
        "proximity_message": "Located 48 miles from our Smithfield office, we serve Somerville attorneys with timely life care planning assessments and court testimony"
    },
    {
        "name": "Framingham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "72,362",
        "county": "Middlesex County",
        "distance_miles": 40,
        "medical_facilities": "MetroWest Medical Center, extensive outpatient facilities",
        "court_info": "Middlesex County Superior Court, Framingham District Court",
        "healthcare_landscape": "Major regional medical center with comprehensive services including trauma care and rehabilitation.",
        "proximity_message": "Located 40 miles from our Smithfield office, we regularly serve Framingham attorneys with convenient consultation options"
    },
    {
        "name": "Haverhill",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "67,787",
        "county": "Essex County",
        "distance_miles": 70,
        "medical_facilities": "Holy Family Hospital (Haverhill campus), Whittier Rehabilitation Hospital",
        "court_info": "Essex County Superior Court, Haverhill District Court",
        "healthcare_landscape": "Hospital services with specialized rehabilitation facility providing comprehensive post-acute care.",
        "proximity_message": "Serving Haverhill attorneys with expert life care planning services through virtual consultations and in-person meetings at trial"
    },
    {
        "name": "Waltham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "65,218",
        "county": "Middlesex County",
        "distance_miles": 42,
        "medical_facilities": "Various medical offices, proximity to Newton-Wellesley and Boston hospitals",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "healthcare_landscape": "Strong outpatient services with easy access to major medical centers in Newton and Boston.",
        "proximity_message": "Located 42 miles from our Smithfield office, we provide timely life care planning evaluations to Waltham attorneys"
    },
    {
        "name": "Malden",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "66,263",
        "county": "Middlesex County",
        "distance_miles": 50,
        "medical_facilities": "Hallmark Health Medical Center, Cambridge Health Alliance facilities",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "healthcare_landscape": "Community hospital services with access to larger healthcare systems for specialty care.",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Malden attorneys with flexible life care planning assessment options"
    },
    {
        "name": "Medford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,659",
        "county": "Middlesex County",
        "distance_miles": 48,
        "medical_facilities": "Lawrence Memorial Hospital, proximity to Boston medical centers",
        "court_info": "Middlesex County Superior Court, Somerville District Court",
        "healthcare_landscape": "Community hospital with rehabilitation services and access to Boston teaching hospitals.",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide comprehensive life care planning services to Medford attorneys"
    },
    {
        "name": "Taunton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "59,408",
        "county": "Bristol County",
        "distance_miles": 25,
        "medical_facilities": "Morton Hospital, Taunton State Hospital, various rehabilitation centers",
        "court_info": "Bristol County Superior Court (Taunton), Taunton District Court",
        "healthcare_landscape": "Regional hospital with psychiatric facilities and comprehensive outpatient services.",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person life care planning evaluations for Taunton cases"
    },
    {
        "name": "Weymouth",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "57,213",
        "county": "Norfolk County",
        "distance_miles": 45,
        "medical_facilities": "South Shore Hospital (nearby), various medical practices",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "healthcare_landscape": "Access to major regional hospital with comprehensive medical and rehabilitation services.",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Weymouth attorneys with timely life care planning assessments"
    },
    {
        "name": "Revere",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "62,186",
        "county": "Suffolk County",
        "distance_miles": 55,
        "medical_facilities": "Various healthcare centers, proximity to Boston hospitals",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "healthcare_landscape": "Community health centers with easy access to Boston's major medical facilities.",
        "proximity_message": "Serving Revere attorneys with comprehensive life care planning evaluations through flexible consultation arrangements"
    },
    {
        "name": "Peabody",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "54,481",
        "county": "Essex County",
        "distance_miles": 60,
        "medical_facilities": "Lahey Hospital & Medical Center (nearby), various specialty practices",
        "court_info": "Essex County Superior Court, Peabody District Court",
        "healthcare_landscape": "Access to major medical center with comprehensive specialty and rehabilitation services.",
        "proximity_message": "Serving Peabody attorneys with expert life care planning services through both virtual and in-person consultations"
    },
    {
        "name": "Methuen",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "53,059",
        "county": "Essex County",
        "distance_miles": 65,
        "medical_facilities": "Holy Family Hospital, various medical offices",
        "court_info": "Essex County Superior Court, Lawrence District Court",
        "healthcare_landscape": "Hospital services with rehabilitation facilities and comprehensive outpatient care.",
        "proximity_message": "Providing life care planning evaluations to Methuen attorneys through virtual consultations and in-person meetings when needed"
    },
    {
        "name": "Everett",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "49,075",
        "county": "Middlesex County",
        "distance_miles": 52,
        "medical_facilities": "Cambridge Health Alliance Everett Hospital, Whidden Memorial Hospital",
        "court_info": "Middlesex County Superior Court, Malden District Court",
        "healthcare_landscape": "Community hospital with emergency services and access to larger healthcare systems.",
        "proximity_message": "Located 52 miles from our Smithfield office, we serve Everett attorneys with comprehensive life care planning assessments"
    },
    {
        "name": "Salem",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "44,480",
        "county": "Essex County",
        "distance_miles": 65,
        "medical_facilities": "North Shore Medical Center (Salem Hospital), Spaulding Rehabilitation",
        "court_info": "Essex County Superior Court (Salem), Salem District Court",
        "healthcare_landscape": "Major regional hospital with specialized rehabilitation services and comprehensive care.",
        "proximity_message": "Serving Salem attorneys with expert life care planning evaluations through flexible scheduling and consultation options"
    },
    {
        "name": "Chicopee",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "55,560",
        "county": "Hampden County",
        "distance_miles": 65,
        "medical_facilities": "Baystate Medical practices, Holyoke Medical Center (nearby)",
        "court_info": "Hampden County Superior Court, Chicopee District Court",
        "healthcare_landscape": "Access to regional medical centers with comprehensive specialty and rehabilitation services.",
        "proximity_message": "Providing comprehensive life care planning services to Chicopee attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Westfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,094",
        "county": "Hampden County",
        "distance_miles": 70,
        "medical_facilities": "Noble Hospital (part of Baystate Health), rehabilitation centers",
        "court_info": "Hampden County Superior Court, Westfield District Court",
        "healthcare_landscape": "Community hospital with access to Baystate Health system for comprehensive care.",
        "proximity_message": "Serving Westfield attorneys with life care planning evaluations through virtual consultations and in-person meetings at trial"
    },
    {
        "name": "Beverly",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "42,670",
        "county": "Essex County",
        "distance_miles": 65,
        "medical_facilities": "Beverly Hospital (part of Lahey Health), various specialty practices",
        "court_info": "Essex County Superior Court, Salem District Court",
        "healthcare_landscape": "Community hospital with comprehensive services and access to Lahey Health network.",
        "proximity_message": "Providing expert life care planning services to Beverly attorneys through flexible consultation arrangements"
    },
    {
        "name": "Holyoke",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "38,238",
        "county": "Hampden County",
        "distance_miles": 70,
        "medical_facilities": "Holyoke Medical Center, Holyoke Health Center",
        "court_info": "Hampden County Superior Court, Holyoke District Court",
        "healthcare_landscape": "Regional medical center serving diverse population with bilingual services.",
        "proximity_message": "Serving Holyoke attorneys with comprehensive life care planning evaluations through virtual and in-person options"
    },
    {
        "name": "Marlborough",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,793",
        "county": "Middlesex County",
        "distance_miles": 38,
        "medical_facilities": "UMass Memorial - Marlborough Hospital, various medical offices",
        "court_info": "Middlesex County Superior Court, Marlborough District Court",
        "healthcare_landscape": "Community hospital with rehabilitation services and specialty care access.",
        "proximity_message": "Located 38 miles from our Smithfield office, we regularly serve Marlborough attorneys with convenient consultations"
    },
    {
        "name": "Fitchburg",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "41,946",
        "county": "Worcester County",
        "distance_miles": 50,
        "medical_facilities": "HealthAlliance-Clinton Hospital (Burbank Campus), rehabilitation centers",
        "court_info": "Worcester County Superior Court, Fitchburg District Court",
        "healthcare_landscape": "Regional hospital with comprehensive services including rehabilitation and specialty care.",
        "proximity_message": "Located 50 miles from our Smithfield office, we serve Fitchburg attorneys with timely life care planning assessments"
    },
    {
        "name": "Woburn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "40,876",
        "county": "Middlesex County",
        "distance_miles": 48,
        "medical_facilities": "Various medical practices, proximity to Winchester Hospital",
        "court_info": "Middlesex County Superior Court, Woburn District Court",
        "healthcare_landscape": "Strong outpatient services with access to nearby hospitals for acute care.",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide efficient life care planning services to Woburn attorneys"
    },
    {
        "name": "Chelsea",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "40,787",
        "county": "Suffolk County",
        "distance_miles": 52,
        "medical_facilities": "Massachusetts General Hospital Chelsea HealthCare Center",
        "court_info": "Suffolk County Superior Court, Chelsea District Court",
        "healthcare_landscape": "Community health center affiliated with MGH providing comprehensive primary and specialty care.",
        "proximity_message": "Located 52 miles from our Smithfield office, we serve Chelsea attorneys with comprehensive life care planning evaluations"
    },
    {
        "name": "Leominster",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,782",
        "county": "Worcester County",
        "distance_miles": 45,
        "medical_facilities": "HealthAlliance-Clinton Hospital (Leominster Campus)",
        "court_info": "Worcester County Superior Court, Leominster District Court",
        "healthcare_landscape": "Hospital campus with emergency services and comprehensive outpatient care.",
        "proximity_message": "Located 45 miles from our Smithfield office, we regularly serve Leominster attorneys with flexible consultations"
    },
    {
        "name": "Pittsfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "43,927",
        "county": "Berkshire County",
        "distance_miles": 115,
        "medical_facilities": "Berkshire Medical Center, specialized rehabilitation facilities",
        "court_info": "Berkshire County Superior Court, Pittsfield District Court",
        "healthcare_landscape": "Regional medical center serving all of Berkshire County with comprehensive services.",
        "proximity_message": "Serving Pittsfield attorneys with life care planning evaluations through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Attleboro",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "46,461",
        "county": "Bristol County",
        "distance_miles": 15,
        "medical_facilities": "Sturdy Memorial Hospital, various rehabilitation centers",
        "court_info": "Bristol County Superior Court, Attleboro District Court",
        "healthcare_landscape": "Community hospital with comprehensive services and strong rehabilitation programs.",
        "proximity_message": "Located just 15 miles from our Smithfield office, we offer immediate availability for Attleboro life care planning evaluations"
    },
    {
        "name": "Barnstable",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "48,916",
        "county": "Barnstable County",
        "distance_miles": 75,
        "medical_facilities": "Cape Cod Hospital, Cape Cod Healthcare rehabilitation services",
        "court_info": "Barnstable County Superior Court, Barnstable District Court",
        "healthcare_landscape": "Major Cape Cod medical center with comprehensive services including specialized rehabilitation.",
        "proximity_message": "Serving Cape Cod attorneys with comprehensive life care planning services through virtual consultations and scheduled visits"
    },
    {
        "name": "Northampton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "29,571",
        "county": "Hampshire County",
        "distance_miles": 75,
        "medical_facilities": "Cooley Dickinson Hospital, specialized mental health facilities",
        "court_info": "Hampshire County Superior Court, Northampton District Court",
        "healthcare_landscape": "Regional hospital with psychiatric services and comprehensive medical care.",
        "proximity_message": "Serving Northampton attorneys with life care planning evaluations through virtual consultations and in-person meetings"
    },
    {
        "name": "Randolph",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "34,984",
        "county": "Norfolk County",
        "distance_miles": 42,
        "medical_facilities": "Various medical practices, proximity to South Shore and Boston hospitals",
        "court_info": "Norfolk County Superior Court, Quincy District Court",
        "healthcare_landscape": "Access to multiple regional hospitals with comprehensive medical services.",
        "proximity_message": "Located 42 miles from our Smithfield office, we provide timely life care planning services to Randolph attorneys"
    },
    {
        "name": "Watertown",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "35,329",
        "county": "Middlesex County",
        "distance_miles": 45,
        "medical_facilities": "Various specialty practices, proximity to Mount Auburn Hospital",
        "court_info": "Middlesex County Superior Court, Waltham District Court",
        "healthcare_landscape": "Access to teaching hospital with comprehensive specialty services.",
        "proximity_message": "Located 45 miles from our Smithfield office, we serve Watertown attorneys with efficient life care planning evaluations"
    },
    {
        "name": "Franklin",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "33,261",
        "county": "Norfolk County",
        "distance_miles": 25,
        "medical_facilities": "Various medical offices, proximity to Milford Regional Medical Center",
        "court_info": "Norfolk County Superior Court, Wrentham District Court",
        "healthcare_landscape": "Access to regional medical center with comprehensive services.",
        "proximity_message": "Located just 25 miles from our Smithfield office, we offer convenient in-person life care planning evaluations for Franklin cases"
    },
    {
        "name": "Lexington",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "34,454",
        "county": "Middlesex County",
        "distance_miles": 48,
        "medical_facilities": "Various specialty practices, proximity to Lahey Hospital",
        "court_info": "Middlesex County Superior Court, Concord District Court",
        "healthcare_landscape": "Affluent community with access to premier medical facilities and specialists.",
        "proximity_message": "Located 48 miles from our Smithfield office, we provide expert life care planning services to Lexington attorneys"
    },
    {
        "name": "Gloucester",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "30,291",
        "county": "Essex County",
        "distance_miles": 75,
        "medical_facilities": "Addison Gilbert Hospital (part of Lahey Health), rehabilitation services",
        "court_info": "Essex County Superior Court, Gloucester District Court",
        "healthcare_landscape": "Community hospital with emergency services and access to Lahey Health network.",
        "proximity_message": "Serving Gloucester attorneys with life care planning evaluations through virtual consultations and scheduled court appearances"
    }
]

# Template for Massachusetts life care planning pages
def generate_ma_life_care_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ma-life-care-planning.html"
    
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
<title>Life Care Planning {city['name']} MA | Future Medical Costs | Chris Skerritt CLCP</title>
<meta content="Certified Life Care Planner in {city['name']}, Massachusetts. Expert assessment of future medical needs and costs for catastrophic injuries. Call 203-605-2814" name="description"/>
<link href="../../css/styles.css" rel="stylesheet"/>
<link href="../../css/services.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://skerritteconomics.com/locations/life-care-planning/{filename}" rel="canonical"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<!-- Structured Data -->
<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Life Care Planning Services in {city['name']}, MA",
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
    "description": "Certified Life Care Planning services for catastrophic injury cases in {city['name']}, Massachusetts. Expert assessment of future medical needs, costs, and care requirements for personal injury litigation.",
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
            "name": "What is a Life Care Plan and why do I need one in {city['name']}, MA?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "A Life Care Plan is a comprehensive assessment of all future medical needs and associated costs for someone with a catastrophic injury or chronic condition. In {city['name']}, life care plans are essential for personal injury cases, medical malpractice claims, and workers' compensation matters to ensure adequate compensation for lifetime care needs. Our plans consider local healthcare resources including {city['medical_facilities']}."
            }}
        }},
        {{
            "@type": "Question",
            "name": "What medical facilities in {city['name']} are considered in life care planning?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{city['healthcare_landscape']} Key facilities include {city['medical_facilities']}. Our life care plans incorporate costs from these local providers while ensuring access to specialized care when needed."
            }}
        }},
        {{
            "@type": "Question",
            "name": "How much does a Life Care Plan cost for a {city['name']} case?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Life Care Planning fees typically range from $3,500 to $8,000 depending on case complexity and the severity of injuries. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation."
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
            "name": "Life Care Planning",
            "item": "https://skerritteconomics.com/locations/life-care-planning/"
        }},
        {{
            "@type": "ListItem",
            "position": 4,
            "name": "{city['name']}, MA",
            "item": "https://skerritteconomics.com/locations/life-care-planning/{filename}"
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
<span class="breadcrumb-current">Life Care Planning {city['name']} MA</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Life Care Planning in {city['name']}, Massachusetts</h1>
<div class="meta">
<span>Certified Life Care Planner (CLCP)</span>
<span>Court-Qualified Expert</span>
<span>Serving {city['county']}</span>
</div>
<p class="lead">Expert life care planning services for {city['name']} attorneys handling catastrophic injury cases. Comprehensive assessment of future medical needs, treatment costs, and care requirements. {city['proximity_message']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Life Care Planning Services in {city['name']}</h2>
<p>As a Certified Life Care Planner serving {city['name']}, I provide comprehensive assessments of future medical care needs for individuals with catastrophic injuries or chronic conditions. With a population of {city['population']}, {city['name']} offers various medical resources that must be carefully evaluated when planning long-term care.</p>
<p>{city['healthcare_landscape']} Understanding these local healthcare resources is crucial for developing realistic and cost-effective life care plans.</p>
</div>
<!-- Local Healthcare Resources -->
<div class="service-section">
<h2>{city['name']} Healthcare Resources for Life Care Planning</h2>
<p>Key medical facilities in {city['name']} include {city['medical_facilities']}. Our life care plans incorporate:</p>
<ul>
<li><strong>Acute Care:</strong> Hospital services and emergency care availability</li>
<li><strong>Rehabilitation Services:</strong> Physical, occupational, and speech therapy resources</li>
<li><strong>Skilled Nursing:</strong> Long-term care and skilled nursing facilities</li>
<li><strong>Home Health Services:</strong> In-home nursing and therapy providers</li>
<li><strong>Medical Equipment:</strong> DME suppliers and adaptive equipment vendors</li>
<li><strong>Specialist Care:</strong> Access to specialized physicians and treatment centers</li>
</ul>
</div>
<!-- Services for Local Attorneys -->
<div class="service-section">
<h2>Supporting {city['name']} Legal Professionals</h2>
<p>I provide {city['name']} attorneys with comprehensive life care plans for cases in {city['court_info']}. My services include:</p>
<ul>
<li><strong>Catastrophic Injuries:</strong> Spinal cord injuries, traumatic brain injuries, amputations</li>
<li><strong>Birth Injuries:</strong> Cerebral palsy, hypoxic injuries, developmental disabilities</li>
<li><strong>Medical Complications:</strong> Surgical errors, medication injuries, chronic conditions</li>
<li><strong>Burn Injuries:</strong> Severe burns requiring ongoing treatment and reconstruction</li>
<li><strong>Future Medical Costs:</strong> Detailed projections of all medical expenses</li>
<li><strong>Expert Testimony:</strong> Clear presentation of care needs and associated costs</li>
</ul>
</div>
<!-- Life Care Planning Process -->
<div class="service-section">
<h2>Our {city['name']} Life Care Planning Process</h2>
<p>{city['proximity_message']}, offering {location_flexibility}. My comprehensive process includes:</p>
<ul>
<li><strong>Medical Records Review:</strong> Thorough analysis of all medical documentation</li>
<li><strong>Client Assessment:</strong> In-person or virtual evaluation of current condition and needs</li>
<li><strong>Physician Consultation:</strong> Collaboration with treating physicians and specialists</li>
<li><strong>Facility Research:</strong> Cost analysis of {city['name']} area healthcare providers</li>
<li><strong>Future Needs Projection:</strong> Evidence-based assessment of lifetime care requirements</li>
<li><strong>Cost Development:</strong> Detailed pricing using local and regional cost data</li>
<li><strong>Plan Documentation:</strong> Comprehensive report meeting legal standards</li>
</ul>
</div>
<!-- Common Case Types -->
<div class="service-section">
<h2>Common {city['name']} Life Care Planning Cases</h2>
<h3>Personal Injury:</h3>
<ul>
<li>Motor vehicle accidents with severe injuries</li>
<li>Premises liability with permanent disabilities</li>
<li>Product liability causing chronic conditions</li>
<li>Construction accidents with multiple trauma</li>
</ul>
<h3>Medical Malpractice:</h3>
<ul>
<li>Surgical errors requiring revision surgeries</li>
<li>Diagnostic failures leading to progressive conditions</li>
<li>Birth injuries requiring lifetime care</li>
<li>Medication errors with permanent effects</li>
</ul>
<h3>Workers' Compensation:</h3>
<ul>
<li>Industrial accidents with permanent impairment</li>
<li>Repetitive trauma requiring ongoing treatment</li>
<li>Occupational diseases needing long-term care</li>
<li>Multiple injury claims with complex needs</li>
</ul>
</div>
<!-- Cost Components -->
<div class="service-section">
<h2>Life Care Plan Components for {city['name']} Cases</h2>
<p>Comprehensive life care plans address all aspects of future care:</p>
<ul>
<li><strong>Medical Care:</strong> Physician visits, surgeries, hospitalizations</li>
<li><strong>Rehabilitation:</strong> PT, OT, speech therapy, cognitive rehabilitation</li>
<li><strong>Diagnostic Testing:</strong> Imaging, laboratory work, specialized assessments</li>
<li><strong>Medications:</strong> Prescription drugs, medical supplies, supplements</li>
<li><strong>Durable Medical Equipment:</strong> Wheelchairs, prosthetics, adaptive devices</li>
<li><strong>Home Modifications:</strong> Accessibility improvements, safety equipment</li>
<li><strong>Attendant Care:</strong> Nursing care, personal care assistants</li>
<li><strong>Transportation:</strong> Medical transportation, vehicle modifications</li>
</ul>
</div>
<!-- Local Factors -->
<div class="service-section">
<h2>Understanding {city['name']}'s Healthcare Landscape</h2>
<p>Accurate life care plans require knowledge of local healthcare conditions:</p>
<ul>
<li><strong>Medical Facilities:</strong> {city['medical_facilities']}</li>
<li><strong>Healthcare Access:</strong> {city['healthcare_landscape']}</li>
<li><strong>Specialist Availability:</strong> Access to specialized care and wait times</li>
<li><strong>Cost Variations:</strong> Local pricing compared to regional averages</li>
<li><strong>Demographics:</strong> Population of {city['population']} affecting service availability</li>
</ul>
<p>This local expertise ensures life care plans reflect realistic care options and costs in {city['name']}.</p>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Life Care Planning</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What is a Life Care Plan and why do I need one in {city['name']}, MA?</summary>
<p>A Life Care Plan is a comprehensive assessment of all future medical needs and associated costs for someone with a catastrophic injury or chronic condition. In {city['name']}, life care plans are essential for personal injury cases, medical malpractice claims, and workers' compensation matters to ensure adequate compensation for lifetime care needs. Our plans consider local healthcare resources including {city['medical_facilities']}.</p>
</details>
<details class="faq-item">
<summary>What medical facilities in {city['name']} are considered in life care planning?</summary>
<p>{city['healthcare_landscape']} Key facilities include {city['medical_facilities']}. Our life care plans incorporate costs from these local providers while ensuring access to specialized care when needed.</p>
</details>
<details class="faq-item">
<summary>How much does a Life Care Plan cost for a {city['name']} case?</summary>
<p>Life Care Planning fees typically range from $3,500 to $8,000 depending on case complexity and the severity of injuries. {city['proximity_message']}. We provide detailed fee quotes during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>How long does it take to complete a Life Care Plan?</summary>
<p>Most life care plans are completed within 4-6 weeks, depending on the complexity of injuries and availability of medical records. Expedited service is available for urgent cases.</p>
</details>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need Life Care Planning in {city['name']}?</h2>
<p>Free consultation for {city['name']} attorneys handling catastrophic injury cases. Get a comprehensive life care plan from a Certified Life Care Planner.</p>
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
<p>Certified Life Care Planning services for {city['name']} catastrophic injury cases.</p>
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
    filepath = f"/Users/chrisskerritt/SEC/locations/life-care-planning/{filename}"
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Created: {filename}")

# Generate all Massachusetts city pages
for city in ma_cities:
    generate_ma_life_care_page(city)

print(f"\nGenerated {len(ma_cities)} Massachusetts life care planning pages!")
print("\nPages created for:")
for city in ma_cities:
    print(f"- {city['name']}, MA ({city['distance_miles']} miles from Smithfield)")