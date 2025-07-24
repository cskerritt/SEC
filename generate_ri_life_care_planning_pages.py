#!/usr/bin/env python3
import os

# Rhode Island cities with life care planning focus - excluding Providence which already exists
ri_cities = [
    {
        "name": "Warwick",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,823",
        "county": "Kent County",
        "distance_miles": 10,
        "medical_facilities": "Kent Hospital, Warwick Mall Medical Center, numerous medical practices",
        "court_info": "Kent County Superior Court, Warwick Municipal Court",
        "healthcare_landscape": "Major healthcare hub with Kent Hospital and extensive outpatient facilities. Strong rehabilitation services network.",
        "proximity_message": "Located just 10 miles from our Smithfield office, providing immediate response for Warwick life care planning assessments"
    },
    {
        "name": "Cranston",
        "state": "Rhode Island", 
        "state_abbr": "RI",
        "population": "82,934",
        "county": "Providence County",
        "distance_miles": 8,
        "medical_facilities": "Various medical offices, proximity to Providence hospitals, rehabilitation centers",
        "court_info": "Providence County Superior Court, Cranston Municipal Court",
        "healthcare_landscape": "Access to Providence's major medical centers while maintaining local healthcare facilities and rehabilitation services.",
        "proximity_message": "Just 8 miles from our Smithfield office, allowing for quick on-site assessments and court appearances in Cranston"
    },
    {
        "name": "Pawtucket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "75,604",
        "county": "Providence County",
        "distance_miles": 7,
        "medical_facilities": "Memorial Hospital of Rhode Island, Blackstone Valley Community Health Care",
        "court_info": "Providence County Superior Court, Pawtucket Municipal Court",
        "healthcare_landscape": "Memorial Hospital anchors local healthcare with specialized rehabilitation and skilled nursing facilities.",
        "proximity_message": "Only 7 miles from our office, enabling frequent in-person meetings and rapid response for Pawtucket cases"
    },
    {
        "name": "East Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "47,139",
        "county": "Providence County", 
        "distance_miles": 10,
        "medical_facilities": "Emma Pendleton Bradley Hospital, East Bay Community Action Program health centers",
        "court_info": "Providence County Superior Court, East Providence Municipal Court",
        "healthcare_landscape": "Specialized mental health facilities and community health centers with access to Providence medical resources.",
        "proximity_message": "A short 10-mile drive from Smithfield allows for convenient scheduling of evaluations and meetings"
    },
    {
        "name": "Woonsocket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "43,240",
        "county": "Providence County",
        "distance_miles": 12,
        "medical_facilities": "Landmark Medical Center, Thundermist Health Center, various specialists",
        "court_info": "Providence County Superior Court, Woonsocket District Court",
        "healthcare_landscape": "Landmark Medical Center provides comprehensive care with strong rehabilitation and home health networks.",
        "proximity_message": "Located 12 miles from our office, we regularly serve Woonsocket with both virtual and in-person evaluations"
    },
    {
        "name": "Newport",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "25,163",
        "county": "Newport County",
        "distance_miles": 35,
        "medical_facilities": "Newport Hospital, Naval Health Clinic New England, specialized rehabilitation centers",
        "court_info": "Newport County Superior Court, Newport Municipal Court",
        "healthcare_landscape": "Newport Hospital serves as regional medical center with specialized services for military and civilian populations.",
        "proximity_message": "Serving Newport with comprehensive life care planning services, offering both in-person and virtual consultation options"
    },
    {
        "name": "Central Falls",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "22,583",
        "county": "Providence County",
        "distance_miles": 9,
        "medical_facilities": "Blackstone Valley Community Health Care, proximity to Pawtucket medical facilities",
        "court_info": "Providence County Superior Court, Central Falls Municipal Court",
        "healthcare_landscape": "Community health centers provide primary care with access to regional hospitals for specialized services.",
        "proximity_message": "Just 9 miles away, providing quick access for Central Falls life care planning evaluations and court testimony"
    },
    {
        "name": "Westerly",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "23,359",
        "county": "Washington County",
        "distance_miles": 50,
        "medical_facilities": "Westerly Hospital, The Westerly Center for Healthy Aging, coastal rehabilitation facilities",
        "court_info": "Washington County Superior Court, Fourth Division District Court",
        "healthcare_landscape": "Westerly Hospital provides full-service care with specialized geriatric and rehabilitation programs.",
        "proximity_message": "Providing expert life care planning services to Westerly through flexible scheduling and virtual consultation options"
    }
]

# Template for Rhode Island life care planning pages
def generate_ri_life_care_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ri-life-care-planning.html"
    
    # Determine the proximity/service message based on distance
    if city['distance_miles'] <= 20:
        location_flexibility = "immediate response times and flexible meeting locations"
    elif city['distance_miles'] <= 40:
        location_flexibility = "both in-person and virtual consultation options"
    else:
        location_flexibility = "comprehensive service through virtual consultations and in-person testimony"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Life Care Planning {city['name']} RI | Future Medical Costs | Chris Skerritt CLCP</title>
<meta content="Certified Life Care Planner in {city['name']}, Rhode Island. Expert assessment of future medical needs and costs for catastrophic injuries. Call 203-605-2814" name="description"/>
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
    "name": "Life Care Planning Services in {city['name']}, RI",
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
    "description": "Certified Life Care Planning services for catastrophic injury cases in {city['name']}, Rhode Island. Expert assessment of future medical needs, costs, and care requirements for personal injury litigation.",
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
            "name": "What is a Life Care Plan and why do I need one in {city['name']}, RI?",
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
            "name": "{city['name']}, RI",
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
<span class="breadcrumb-current">Life Care Planning {city['name']} RI</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Life Care Planning in {city['name']}, Rhode Island</h1>
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
<summary>What is a Life Care Plan and why do I need one in {city['name']}, RI?</summary>
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

# Generate all Rhode Island city pages
for city in ri_cities:
    generate_ri_life_care_page(city)

print(f"\nGenerated {len(ri_cities)} Rhode Island life care planning pages!")
print("\nPages created for:")
for city in ri_cities:
    print(f"- {city['name']}, RI ({city['distance_miles']} miles from Smithfield)")