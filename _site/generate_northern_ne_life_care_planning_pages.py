#!/usr/bin/env python3
import os

# Northern New England cities with life care planning focus - excluding Manchester NH, Portland ME, Burlington VT which already exist
northern_ne_cities = [
    # New Hampshire cities (excluding Manchester which already exists)
    {
        "name": "Nashua",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "91,322",
        "county": "Hillsborough County",
        "distance_miles": 85,
        "medical_facilities": "Southern New Hampshire Medical Center, St. Joseph Hospital, rehabilitation centers",
        "court_info": "Hillsborough County Superior Court South, Nashua District Court",
        "healthcare_landscape": "Two major hospitals providing comprehensive care with specialized rehabilitation services.",
        "proximity_message": "Serving Nashua attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Concord",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "43,976",
        "county": "Merrimack County",
        "distance_miles": 110,
        "medical_facilities": "Concord Hospital, Capital Region Mental Health Center, rehabilitation facilities",
        "court_info": "Merrimack County Superior Court, Concord District Court, New Hampshire Supreme Court",
        "healthcare_landscape": "Capital city with major regional hospital and comprehensive mental health services.",
        "proximity_message": "Providing life care planning evaluations to Concord attorneys through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Derry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "34,317",
        "county": "Rockingham County",
        "distance_miles": 90,
        "medical_facilities": "Parkland Medical Center, various medical practices, rehabilitation services",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "healthcare_landscape": "Community hospital with emergency services and outpatient rehabilitation programs.",
        "proximity_message": "Serving Derry attorneys with expert life care planning services through flexible consultation arrangements"
    },
    {
        "name": "Rochester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,492",
        "county": "Strafford County",
        "distance_miles": 110,
        "medical_facilities": "Frisbie Memorial Hospital, Skyhaven Nursing & Rehabilitation Center",
        "court_info": "Strafford County Superior Court, Rochester District Court",
        "healthcare_landscape": "Regional hospital with skilled nursing and rehabilitation facilities.",
        "proximity_message": "Providing comprehensive life care planning services to Rochester attorneys through virtual and in-person options"
    },
    {
        "name": "Salem",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "30,089",
        "county": "Rockingham County",
        "distance_miles": 75,
        "medical_facilities": "Access to Lawrence General Hospital, local medical centers",
        "court_info": "Rockingham County Superior Court, Salem District Court",
        "healthcare_landscape": "Border town with access to both New Hampshire and Massachusetts healthcare systems.",
        "proximity_message": "Serving Salem attorneys with life care planning evaluations through convenient virtual and in-person consultations"
    },
    {
        "name": "Dover",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,741",
        "county": "Strafford County",
        "distance_miles": 115,
        "medical_facilities": "Wentworth-Douglass Hospital, rehabilitation and skilled nursing facilities",
        "court_info": "Strafford County Superior Court, Dover District Court",
        "healthcare_landscape": "Major seacoast hospital with comprehensive medical and rehabilitation services.",
        "proximity_message": "Providing expert life care planning services to Dover attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Merrimack",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "26,632",
        "county": "Hillsborough County",
        "distance_miles": 85,
        "medical_facilities": "Access to Southern NH Medical Center, local medical offices",
        "court_info": "Hillsborough County Superior Court South, Merrimack District Court",
        "healthcare_landscape": "Suburban community with access to regional medical centers.",
        "proximity_message": "Serving Merrimack attorneys with comprehensive life care planning assessments through flexible meeting options"
    },
    {
        "name": "Londonderry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "25,826",
        "county": "Rockingham County",
        "distance_miles": 80,
        "medical_facilities": "Local medical practices, access to Derry and Manchester hospitals",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "healthcare_landscape": "Growing community with local healthcare and access to regional hospitals.",
        "proximity_message": "Providing life care planning evaluations to Londonderry attorneys through virtual and in-person consultations"
    },
    {
        "name": "Keene",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,047",
        "county": "Cheshire County",
        "distance_miles": 95,
        "medical_facilities": "Cheshire Medical Center, rehabilitation services, mental health facilities",
        "court_info": "Cheshire County Superior Court, Keene District Court",
        "healthcare_landscape": "Regional medical center serving southwestern New Hampshire.",
        "proximity_message": "Serving Keene attorneys with expert life care planning services through virtual consultations and scheduled visits"
    },
    {
        "name": "Bedford",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,322",
        "county": "Hillsborough County",
        "distance_miles": 90,
        "medical_facilities": "Access to Elliot Hospital, Catholic Medical Center, specialty practices",
        "court_info": "Hillsborough County Superior Court South, Manchester District Court",
        "healthcare_landscape": "Affluent community with access to Manchester's major medical facilities.",
        "proximity_message": "Providing life care planning assessments to Bedford attorneys through convenient consultation arrangements"
    },
    {
        "name": "Portsmouth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "21,956",
        "county": "Rockingham County",
        "distance_miles": 120,
        "medical_facilities": "Portsmouth Regional Hospital, rehabilitation centers, specialty clinics",
        "court_info": "Rockingham County Superior Court, Portsmouth District Court",
        "healthcare_landscape": "Seacoast regional hospital with comprehensive services and ocean-based rehabilitation.",
        "proximity_message": "Serving Portsmouth attorneys with life care planning evaluations through virtual consultations and in-person testimony"
    },
    {
        "name": "Goffstown",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "18,577",
        "county": "Hillsborough County",
        "distance_miles": 95,
        "medical_facilities": "Access to Manchester hospitals, local rehabilitation services",
        "court_info": "Hillsborough County Superior Court South, Goffstown District Court",
        "healthcare_landscape": "Small town with access to Manchester's healthcare resources.",
        "proximity_message": "Providing life care planning services to Goffstown attorneys through flexible virtual and in-person options"
    },
    {
        "name": "Laconia",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "16,871",
        "county": "Belknap County",
        "distance_miles": 135,
        "medical_facilities": "Lakes Region General Hospital, rehabilitation and nursing facilities",
        "court_info": "Belknap County Superior Court, Laconia District Court",
        "healthcare_landscape": "Lakes Region medical center with seasonal population variations affecting services.",
        "proximity_message": "Serving Laconia attorneys with life care planning assessments through virtual consultations and court appearances"
    },
    {
        "name": "Hooksett",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "14,871",
        "county": "Merrimack County",
        "distance_miles": 95,
        "medical_facilities": "Access to Manchester and Concord hospitals, local medical offices",
        "court_info": "Merrimack County Superior Court, Hooksett District Court",
        "healthcare_landscape": "Central location between Manchester and Concord medical facilities.",
        "proximity_message": "Providing life care planning evaluations to Hooksett attorneys through convenient consultation options"
    },
    # Maine cities (excluding Portland which already exists)
    {
        "name": "Lewiston",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "37,121",
        "county": "Androscoggin County",
        "distance_miles": 165,
        "medical_facilities": "Central Maine Medical Center, St. Mary's Regional Medical Center",
        "court_info": "Androscoggin County Superior Court, Lewiston District Court",
        "healthcare_landscape": "Twin hospitals providing comprehensive care with Level II trauma center.",
        "proximity_message": "Serving Lewiston attorneys with life care planning evaluations through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Bangor",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "31,753",
        "county": "Penobscot County",
        "distance_miles": 250,
        "medical_facilities": "Northern Light Eastern Maine Medical Center, St. Joseph Hospital",
        "court_info": "Penobscot County Superior Court, Bangor District Court",
        "healthcare_landscape": "Major regional medical center serving northern and eastern Maine with Level II trauma center.",
        "proximity_message": "Providing comprehensive life care planning services to Bangor attorneys through virtual evaluations and scheduled court appearances"
    },
    {
        "name": "South Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "26,498",
        "county": "Cumberland County",
        "distance_miles": 155,
        "medical_facilities": "Access to Maine Medical Center, rehabilitation facilities",
        "court_info": "Cumberland County Superior Court, South Portland District Court",
        "healthcare_landscape": "Proximity to Maine's largest medical center with comprehensive specialty services.",
        "proximity_message": "Serving South Portland attorneys with life care planning assessments through virtual consultations and in-person meetings"
    },
    {
        "name": "Auburn",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "24,061",
        "county": "Androscoggin County",
        "distance_miles": 165,
        "medical_facilities": "Access to Central Maine Medical Center, various medical practices",
        "court_info": "Androscoggin County Superior Court, Auburn District Court",
        "healthcare_landscape": "Twin city with Lewiston sharing major medical resources.",
        "proximity_message": "Providing life care planning evaluations to Auburn attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Biddeford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "22,552",
        "county": "York County",
        "distance_miles": 140,
        "medical_facilities": "Southern Maine Health Care, rehabilitation centers",
        "court_info": "York County Superior Court, Biddeford District Court",
        "healthcare_landscape": "Coastal hospital with comprehensive services and university health programs.",
        "proximity_message": "Serving Biddeford attorneys with expert life care planning services through virtual and in-person consultations"
    },
    {
        "name": "Sanford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "21,982",
        "county": "York County",
        "distance_miles": 120,
        "medical_facilities": "Southern Maine Health Care - Sanford Medical Center",
        "court_info": "York County Superior Court, Springvale District Court",
        "healthcare_landscape": "Regional medical center with emergency and rehabilitation services.",
        "proximity_message": "Providing life care planning assessments to Sanford attorneys through flexible consultation arrangements"
    },
    {
        "name": "Augusta",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "18,899",
        "county": "Kennebec County",
        "distance_miles": 180,
        "medical_facilities": "MaineGeneral Medical Center, state psychiatric facilities",
        "court_info": "Kennebec County Superior Court, Augusta District Court, Maine Supreme Judicial Court",
        "healthcare_landscape": "State capital with major hospital and specialized psychiatric services.",
        "proximity_message": "Serving Augusta attorneys with life care planning evaluations through virtual consultations and scheduled court appearances"
    },
    {
        "name": "Saco",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,381",
        "county": "York County",
        "distance_miles": 140,
        "medical_facilities": "Access to Southern Maine Health Care, local medical practices",
        "court_info": "York County Superior Court, Biddeford District Court",
        "healthcare_landscape": "Coastal community sharing healthcare resources with Biddeford.",
        "proximity_message": "Providing life care planning services to Saco attorneys through virtual consultations and in-person options"
    },
    {
        "name": "Westbrook",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,400",
        "county": "Cumberland County",
        "distance_miles": 155,
        "medical_facilities": "Spring Harbor Hospital, access to Maine Medical Center",
        "court_info": "Cumberland County Superior Court, Westbrook District Court",
        "healthcare_landscape": "Psychiatric hospital and proximity to Portland's medical facilities.",
        "proximity_message": "Serving Westbrook attorneys with life care planning assessments through virtual and in-person consultations"
    },
    {
        "name": "Waterville",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "15,722",
        "county": "Kennebec County",
        "distance_miles": 180,
        "medical_facilities": "MaineGeneral Medical Center - Thayer Unit, rehabilitation services",
        "court_info": "Kennebec County Superior Court, Waterville District Court",
        "healthcare_landscape": "Hospital campus with rehabilitation services and specialty clinics.",
        "proximity_message": "Providing life care planning evaluations to Waterville attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Brunswick",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "21,756",
        "county": "Cumberland County",
        "distance_miles": 165,
        "medical_facilities": "Mid Coast Hospital, Parkview Adventist Medical Center",
        "court_info": "Cumberland County Superior Court, West Bath District Court",
        "healthcare_landscape": "Regional hospital with comprehensive services and military healthcare access.",
        "proximity_message": "Serving Brunswick attorneys with expert life care planning services through virtual consultations and scheduled visits"
    },
    # Vermont cities (excluding Burlington which already exists)
    {
        "name": "Essex Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "10,761",
        "county": "Chittenden County",
        "distance_miles": 270,
        "medical_facilities": "Access to University of Vermont Medical Center, local practices",
        "court_info": "Chittenden County Superior Court, Vermont District Court",
        "healthcare_landscape": "Suburban community with access to Vermont's largest medical center.",
        "proximity_message": "Providing life care planning evaluations to Essex Junction attorneys through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Rutland",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,807",
        "county": "Rutland County",
        "distance_miles": 200,
        "medical_facilities": "Rutland Regional Medical Center, rehabilitation facilities",
        "court_info": "Rutland County Superior Court, Rutland District Court",
        "healthcare_landscape": "Regional medical center serving central Vermont with comprehensive services.",
        "proximity_message": "Serving Rutland attorneys with life care planning assessments through virtual consultations and scheduled court appearances"
    },
    {
        "name": "St. Albans",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "6,918",
        "county": "Franklin County",
        "distance_miles": 300,
        "medical_facilities": "Northwestern Medical Center, rehabilitation services",
        "court_info": "Franklin County Superior Court, St. Albans District Court",
        "healthcare_landscape": "Community hospital serving northwestern Vermont near Canadian border.",
        "proximity_message": "Providing life care planning services to St. Albans attorneys through comprehensive virtual evaluations and court testimony"
    }
]

# Template for Northern New England life care planning pages
def generate_northern_ne_life_care_page(city):
    filename = f"{city['name'].lower().replace(' ', '-').replace('.', '')}-{city['state_abbr'].lower()}-life-care-planning.html"
    
    # Determine the proximity/service message based on distance
    if city['distance_miles'] <= 50:
        location_flexibility = "immediate response times and flexible meeting locations"
    elif city['distance_miles'] <= 100:
        location_flexibility = "both in-person and virtual consultation options"
    else:
        location_flexibility = "comprehensive service through virtual consultations and in-person testimony"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Life Care Planning {city['name']} {city['state_abbr']} | Future Medical Costs | Chris Skerritt CLCP</title>
<meta content="Certified Life Care Planner in {city['name']}, {city['state']}. Expert assessment of future medical needs and costs for catastrophic injuries. Call 203-605-2814" name="description"/>
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
    "name": "Life Care Planning Services in {city['name']}, {city['state_abbr']}",
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
    "description": "Certified Life Care Planning services for catastrophic injury cases in {city['name']}, {city['state']}. Expert assessment of future medical needs, costs, and care requirements for personal injury litigation.",
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
            "name": "What is a Life Care Plan and why do I need one in {city['name']}, {city['state_abbr']}?",
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
            "name": "{city['name']}, {city['state_abbr']}",
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
<span class="breadcrumb-current">Life Care Planning {city['name']} {city['state_abbr']}</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Life Care Planning in {city['name']}, {city['state']}</h1>
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
<summary>What is a Life Care Plan and why do I need one in {city['name']}, {city['state_abbr']}?</summary>
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

# Generate all Northern New England city pages
for city in northern_ne_cities:
    generate_northern_ne_life_care_page(city)

print(f"\nGenerated {len(northern_ne_cities)} Northern New England life care planning pages!")
print("\nPages created for:")
for city in northern_ne_cities:
    print(f"- {city['name']}, {city['state_abbr']} ({city['distance_miles']} miles from Smithfield)")