#!/usr/bin/env python3
import os

# Connecticut cities with life care planning focus - excluding Bridgeport, New Haven, Stamford, Hartford which already exist
ct_cities = [
    {
        "name": "Waterbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "114,403",
        "county": "New Haven County",
        "distance_miles": 70,
        "medical_facilities": "Waterbury Hospital, Saint Mary's Hospital, various rehabilitation centers",
        "court_info": "Waterbury Superior Court, Waterbury Judicial District",
        "healthcare_landscape": "Two major hospitals providing comprehensive care with specialized rehabilitation and outpatient services.",
        "proximity_message": "Serving Waterbury with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Norwalk",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "91,184",
        "county": "Fairfield County",
        "distance_miles": 110,
        "medical_facilities": "Norwalk Hospital, numerous specialty practices, rehabilitation facilities",
        "court_info": "Stamford-Norwalk Judicial District Court",
        "healthcare_landscape": "Major community hospital with comprehensive services and proximity to specialized care in Stamford and New York.",
        "proximity_message": "Serving Norwalk attorneys with expert life care planning services through virtual evaluations and in-person meetings as needed"
    },
    {
        "name": "Danbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "86,518",
        "county": "Fairfield County",
        "distance_miles": 95,
        "medical_facilities": "Danbury Hospital, Western Connecticut Health Network facilities",
        "court_info": "Danbury Superior Court, Danbury Judicial District",
        "healthcare_landscape": "Regional medical center with Level II trauma center and comprehensive specialty services.",
        "proximity_message": "Serving Danbury attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "New Britain",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "74,135",
        "county": "Hartford County",
        "distance_miles": 65,
        "medical_facilities": "Hospital of Central Connecticut, various rehabilitation centers",
        "court_info": "New Britain Superior Court, New Britain Judicial District",
        "healthcare_landscape": "Major hospital with two campuses providing acute care and extensive rehabilitation services.",
        "proximity_message": "Serving New Britain attorneys with expert life care planning services through flexible consultation options"
    },
    {
        "name": "West Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "55,584",
        "county": "New Haven County",
        "distance_miles": 85,
        "medical_facilities": "VA Connecticut Healthcare System, proximity to Yale New Haven Health",
        "court_info": "New Haven County Superior Court",
        "healthcare_landscape": "Major VA medical center with specialized services and access to Yale's healthcare network.",
        "proximity_message": "Serving West Haven attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Bristol",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "60,640",
        "county": "Hartford County",
        "distance_miles": 60,
        "medical_facilities": "Bristol Hospital, Inpatient Rehabilitation Unit, outpatient centers",
        "court_info": "Bristol Superior Court, New Britain Judicial District",
        "healthcare_landscape": "Community hospital with specialized inpatient rehabilitation unit and comprehensive outpatient services.",
        "proximity_message": "Serving Bristol attorneys with expert life care planning services through flexible virtual and in-person consultations"
    },
    {
        "name": "Meriden",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,512",
        "county": "New Haven County",
        "distance_miles": 70,
        "medical_facilities": "MidState Medical Center, Gaylord Specialty Healthcare nearby",
        "court_info": "Meriden Superior Court, New Haven Judicial District",
        "healthcare_landscape": "Regional medical center with proximity to Gaylord, a nationally recognized rehabilitation hospital.",
        "proximity_message": "Serving Meriden attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Milford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "50,558",
        "county": "New Haven County",
        "distance_miles": 90,
        "medical_facilities": "Milford Hospital (part of Bridgeport Hospital), Golden Hill Rehab Pavilion",
        "court_info": "Milford Superior Court, Ansonia-Milford Judicial District",
        "healthcare_landscape": "Community hospital integrated with larger health system, specialized rehabilitation facilities.",
        "proximity_message": "Serving Milford attorneys with expert life care planning services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Stratford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "52,355",
        "county": "Fairfield County",
        "distance_miles": 95,
        "medical_facilities": "Access to Bridgeport Hospital, St. Vincent's Medical Center, rehabilitation centers",
        "court_info": "Bridgeport Superior Court, Fairfield Judicial District",
        "healthcare_landscape": "Proximity to two major medical centers with comprehensive acute and rehabilitation services.",
        "proximity_message": "Serving Stratford attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "East Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "51,045",
        "county": "Hartford County",
        "distance_miles": 70,
        "medical_facilities": "Access to Hartford Hospital, Connecticut Children's Medical Center",
        "court_info": "Hartford Superior Court",
        "healthcare_landscape": "Suburban community with access to Hartford's major medical centers including pediatric specialty care.",
        "proximity_message": "Serving East Hartford attorneys with expert life care planning services through flexible consultation arrangements"
    },
    {
        "name": "Middletown",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "47,717",
        "county": "Middlesex County",
        "distance_miles": 65,
        "medical_facilities": "Middlesex Hospital, Connecticut Valley Hospital, rehabilitation services",
        "court_info": "Middlesex Superior Court, Middletown Judicial District",
        "healthcare_landscape": "Regional medical center with psychiatric hospital and comprehensive rehabilitation programs.",
        "proximity_message": "Serving Middletown attorneys with comprehensive life care planning services through virtual and in-person consultations"
    },
    {
        "name": "Manchester",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,713",
        "county": "Hartford County",
        "distance_miles": 65,
        "medical_facilities": "Manchester Memorial Hospital (ECHN), Eastern Rehabilitation Network",
        "court_info": "Manchester Superior Court, Hartford Judicial District",
        "healthcare_landscape": "Community hospital with strong rehabilitation network and outpatient services.",
        "proximity_message": "Serving Manchester attorneys with expert life care planning services through flexible meeting options"
    },
    {
        "name": "Enfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "42,269",
        "county": "Hartford County",
        "distance_miles": 75,
        "medical_facilities": "Access to Bay State Medical Center, Johnson Memorial Hospital",
        "court_info": "Enfield Superior Court, Hartford Judicial District",
        "healthcare_landscape": "Border community with access to both Connecticut and Massachusetts healthcare systems.",
        "proximity_message": "Serving Enfield attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Shelton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "40,869",
        "county": "Fairfield County",
        "distance_miles": 90,
        "medical_facilities": "Griffin Hospital (nearby), access to Yale New Haven Health network",
        "court_info": "Derby Superior Court, Ansonia-Milford Judicial District",
        "healthcare_landscape": "Access to innovative community hospital and major healthcare networks.",
        "proximity_message": "Serving Shelton attorneys with expert life care planning services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Torrington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,515",
        "county": "Litchfield County",
        "distance_miles": 85,
        "medical_facilities": "Charlotte Hungerford Hospital, Geer Nursing & Rehabilitation",
        "court_info": "Torrington Superior Court, Litchfield Judicial District",
        "healthcare_landscape": "Regional medical center serving northwest Connecticut with rehabilitation facilities.",
        "proximity_message": "Serving Torrington attorneys with comprehensive life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Trumbull",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "36,827",
        "county": "Fairfield County",
        "distance_miles": 95,
        "medical_facilities": "St. Vincent's Medical Center (nearby), various specialty practices",
        "court_info": "Bridgeport Superior Court",
        "healthcare_landscape": "Suburban community with access to major medical centers and specialty care.",
        "proximity_message": "Serving Trumbull attorneys with expert life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Glastonbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,159",
        "county": "Hartford County",
        "distance_miles": 65,
        "medical_facilities": "Access to Hartford Healthcare network, numerous medical practices",
        "court_info": "Hartford Superior Court",
        "healthcare_landscape": "Affluent community with excellent access to Hartford's medical facilities and specialists.",
        "proximity_message": "Serving Glastonbury attorneys with comprehensive life care planning services through flexible consultation options"
    },
    {
        "name": "Naugatuck",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "31,519",
        "county": "New Haven County",
        "distance_miles": 75,
        "medical_facilities": "Access to Waterbury and Yale New Haven hospitals, local medical offices",
        "court_info": "Waterbury Superior Court",
        "healthcare_landscape": "Access to multiple hospital systems with comprehensive medical services.",
        "proximity_message": "Serving Naugatuck attorneys with expert life care planning services through virtual consultations and in-person meetings"
    },
    {
        "name": "Newington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "30,536",
        "county": "Hartford County",
        "distance_miles": 65,
        "medical_facilities": "Connecticut Children's Medical Center, Cedar Mountain Rehabilitation",
        "court_info": "Hartford Superior Court",
        "healthcare_landscape": "Home to state's premier children's hospital and specialized rehabilitation facilities.",
        "proximity_message": "Serving Newington attorneys with comprehensive life care planning services through flexible meeting arrangements"
    },
    {
        "name": "Wallingford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "44,396",
        "county": "New Haven County",
        "distance_miles": 70,
        "medical_facilities": "Gaylord Specialty Healthcare, MidState Medical Center, Masonicare",
        "court_info": "Meriden Superior Court",
        "healthcare_landscape": "Home to premier rehabilitation hospital with spinal cord and brain injury programs.",
        "proximity_message": "Serving Wallingford attorneys with expert life care planning services through virtual and in-person consultations"
    },
    {
        "name": "Wethersfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "27,298",
        "county": "Hartford County",
        "distance_miles": 70,
        "medical_facilities": "Access to Hartford Hospital network, numerous medical offices",
        "court_info": "Hartford Superior Court",
        "healthcare_landscape": "Historic community with excellent access to Hartford's medical facilities.",
        "proximity_message": "Serving Wethersfield attorneys with comprehensive life care planning services through flexible consultation options"
    },
    {
        "name": "Greenwich",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "63,518",
        "county": "Fairfield County",
        "distance_miles": 130,
        "medical_facilities": "Greenwich Hospital, proximity to New York medical centers",
        "court_info": "Stamford Superior Court",
        "healthcare_landscape": "Affluent community with premier hospital and access to New York City specialists.",
        "proximity_message": "Serving Greenwich attorneys with expert life care planning services through virtual evaluations and in-person meetings at trial"
    }
]

# Template for Connecticut life care planning pages
def generate_ct_life_care_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ct-life-care-planning.html"
    
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
<title>Life Care Planning {city['name']} CT | Future Medical Costs | Chris Skerritt CLCP</title>
<meta content="Certified Life Care Planner in {city['name']}, Connecticut. Expert assessment of future medical needs and costs for catastrophic injuries. Call 203-605-2814" name="description"/>
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
    "name": "Life Care Planning Services in {city['name']}, CT",
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
    "description": "Certified Life Care Planning services for catastrophic injury cases in {city['name']}, Connecticut. Expert assessment of future medical needs, costs, and care requirements for personal injury litigation.",
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
            "name": "What is a Life Care Plan and why do I need one in {city['name']}, CT?",
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
            "name": "{city['name']}, CT",
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
<span class="breadcrumb-current">Life Care Planning {city['name']} CT</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Life Care Planning in {city['name']}, Connecticut</h1>
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
<summary>What is a Life Care Plan and why do I need one in {city['name']}, CT?</summary>
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

# Generate all Connecticut city pages
for city in ct_cities:
    generate_ct_life_care_page(city)

print(f"\nGenerated {len(ct_cities)} Connecticut life care planning pages!")
print("\nPages created for:")
for city in ct_cities:
    print(f"- {city['name']}, CT ({city['distance_miles']} miles from Smithfield)")