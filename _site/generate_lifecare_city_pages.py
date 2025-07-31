#!/usr/bin/env python3
import os

# City data with population and local details
cities = [
    # Massachusetts
    {
        "name": "Boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "675,647",
        "major_medical": "Massachusetts General Hospital, Brigham and Women's Hospital, Boston Children's Hospital, Dana-Farber Cancer Institute",
        "court_info": "Suffolk County Superior Court, John Adams Courthouse",
        "healthcare_landscape": "Boston is home to world-renowned medical facilities and teaching hospitals, making it a center for complex medical care and catastrophic injury treatment",
        "distance": "approximately 50 miles from our Smithfield office"
    },
    {
        "name": "Worcester",
        "state": "Massachusetts", 
        "state_abbr": "MA",
        "population": "206,518",
        "major_medical": "UMass Medical School, Saint Vincent Hospital, Worcester Recovery Center",
        "court_info": "Worcester County Superior Court, Worcester Trial Court",
        "healthcare_landscape": "Worcester offers comprehensive medical services with specialties in rehabilitation and long-term care",
        "distance": "approximately 35 miles from our Smithfield office"
    },
    {
        "name": "Springfield",
        "state": "Massachusetts",
        "state_abbr": "MA", 
        "population": "155,929",
        "major_medical": "Baystate Medical Center, Shriners Hospital for Children",
        "court_info": "Hampden County Superior Court, Springfield",
        "healthcare_landscape": "Springfield provides specialized pediatric care and comprehensive rehabilitation services",
        "distance": "approximately 60 miles from our Smithfield office"
    },
    {
        "name": "Cambridge",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "118,403",
        "major_medical": "Mount Auburn Hospital, Cambridge Health Alliance",
        "court_info": "Middlesex County Superior Court, Cambridge",
        "healthcare_landscape": "Cambridge benefits from proximity to Boston's medical facilities while maintaining strong community hospitals",
        "distance": "approximately 45 miles from our Smithfield office"
    },
    {
        "name": "Lowell", 
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "115,554",
        "major_medical": "Lowell General Hospital, Saints Medical Center",
        "court_info": "Middlesex County Superior Court, Lowell",
        "healthcare_landscape": "Lowell provides comprehensive medical services with growing rehabilitation and home health programs",
        "distance": "approximately 55 miles from our Smithfield office"
    },
    # Connecticut
    {
        "name": "Bridgeport",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "148,654",
        "major_medical": "Bridgeport Hospital, St. Vincent's Medical Center",
        "court_info": "Fairfield County Superior Court, Bridgeport",
        "healthcare_landscape": "Bridgeport offers comprehensive medical services with strong trauma and rehabilitation programs",
        "distance": "approximately 100 miles from our Smithfield office"
    },
    {
        "name": "Stamford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "135,470",
        "major_medical": "Stamford Hospital, specialized outpatient centers",
        "court_info": "Stamford Superior Court",
        "healthcare_landscape": "Stamford provides advanced medical care with access to New York metropolitan area specialists",
        "distance": "approximately 120 miles from our Smithfield office"
    },
    {
        "name": "New Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "134,023",
        "major_medical": "Yale New Haven Hospital, Yale Medicine",
        "court_info": "New Haven County Superior Court",
        "healthcare_landscape": "New Haven is home to one of the nation's leading academic medical centers with comprehensive specialty care",
        "distance": "approximately 85 miles from our Smithfield office"
    },
    {
        "name": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "121,054",
        "major_medical": "Hartford Hospital, Connecticut Children's Medical Center",
        "court_info": "Hartford Superior Court, Connecticut Supreme Court",
        "healthcare_landscape": "Hartford offers extensive medical services including specialized pediatric and rehabilitation care",
        "distance": "approximately 70 miles from our Smithfield office"
    },
    # Rhode Island
    {
        "name": "Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "190,934",
        "major_medical": "Rhode Island Hospital, Hasbro Children's Hospital, Miriam Hospital",
        "court_info": "Rhode Island Superior Court, Providence County",
        "healthcare_landscape": "Providence serves as Rhode Island's medical hub with comprehensive trauma, pediatric, and rehabilitation services",
        "distance": "just 10 miles from our Smithfield office"
    },
    # New Hampshire
    {
        "name": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "115,644",
        "major_medical": "Elliot Hospital, Catholic Medical Center, Manchester VA Medical Center",
        "court_info": "Hillsborough County Superior Court, Manchester",
        "healthcare_landscape": "Manchester provides comprehensive medical services for southern New Hampshire including specialized veteran care",
        "distance": "approximately 80 miles from our Smithfield office"
    },
    # Maine
    {
        "name": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "68,408",
        "major_medical": "Maine Medical Center, Barbara Bush Children's Hospital",
        "court_info": "Cumberland County Superior Court, Portland",
        "healthcare_landscape": "Portland is Maine's medical hub with the state's only Level I trauma center and comprehensive specialty services",
        "distance": "approximately 160 miles from our Smithfield office"
    },
    # Vermont
    {
        "name": "Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "44,743",
        "major_medical": "University of Vermont Medical Center",
        "court_info": "Chittenden County Superior Court, Burlington",
        "healthcare_landscape": "Burlington serves as Vermont's primary medical center with comprehensive specialty and trauma care",
        "distance": "approximately 280 miles from our Smithfield office"
    }
]

# Template for city pages
def generate_city_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-{city['state_abbr'].lower()}-life-care-planning.html"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Life Care Planning {city['name']} {city['state_abbr']} | Chris Skerritt CLCP | Future Medical Cost Expert</title>
<meta content="Expert life care planning in {city['name']}, {city['state']}. CLCP-certified life care planner providing future medical cost projections for catastrophic injury cases. Free consultation 203-605-2814" name="description"/>
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
    "description": "Expert life care planning services and future medical cost projections for attorneys in {city['name']}, {city['state']}. CLCP-certified life care planner with extensive experience in catastrophic injury, medical malpractice, and personal injury cases.",
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
            "name": "What does a life care planner do in {city['name']} catastrophic injury cases?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "A life care planner in {city['name']} develops comprehensive plans outlining all future medical care, equipment, medications, and services needed for catastrophically injured individuals. We work with medical professionals to project lifetime care costs, helping {city['state']} attorneys accurately value damages in personal injury and medical malpractice cases."
            }}
        }},
        {{
            "@type": "Question",
            "name": "How much does life care planning cost in {city['name']}, {city['state_abbr']}?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Life care planning fees in {city['name']} typically range from $3,500 to $8,000 depending on injury complexity and the scope of future care needs. This includes medical record review, care plan development, cost projections, and expert testimony if needed. We provide detailed fee estimates during the free initial consultation."
            }}
        }},
        {{
            "@type": "Question",
            "name": "When should {city['name']} attorneys hire a life care planner?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{city['name']} attorneys should engage a life care planner when clients have suffered catastrophic injuries requiring long-term or lifetime medical care. Early involvement allows for comprehensive assessment of future needs and coordination with treating physicians to develop accurate, defensible care plans."
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
<span>CLCP Certified</span>
<span>Court-Qualified Expert</span>
<span>Serving {city['name']} Area</span>
</div>
<p class="lead">Expert life care planning and future medical cost projections for {city['name']} attorneys. As CLCP-certified life care planners based in Rhode Island, we provide comprehensive life care plans for catastrophic injury, medical malpractice, and personal injury cases throughout {city['name']} and {city['state']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Life Care Planning Services in {city['name']}</h2>
<p>Serving {city['name']}'s legal community with expert life care planning services, we understand the unique healthcare landscape of this {city['state']} city. With a population of {city['population']}, {city['name']} features major medical facilities including {city['major_medical']}. Our life care plans reflect deep knowledge of local healthcare resources, costs, and long-term care options specific to {city['name']}.</p>
<p>{city['healthcare_landscape']}. Located {city['distance']}, we provide timely and responsive life care planning services to {city['name']} attorneys handling catastrophic injury, medical malpractice, and personal injury cases.</p>
</div>
<!-- Services for City Attorneys -->
<div class="service-section">
<h2>Life Care Planning for {city['name']} Attorneys</h2>
<p>{city['name']} law firms rely on comprehensive life care plans to support their cases in {city['court_info']}. Our services include:</p>
<ul>
<li><strong>Comprehensive Life Care Plans:</strong> Detailed assessment of all future medical, surgical, therapeutic, and support needs</li>
<li><strong>Future Medical Cost Projections:</strong> Accurate costing using local {city['name']} healthcare provider rates and medical inflation factors</li>
<li><strong>Medical Equipment & Supplies:</strong> Itemized lists of assistive devices, medical equipment, and consumable supplies with replacement schedules</li>
<li><strong>Home Modifications:</strong> Assessment of necessary home modifications for accessibility and medical care</li>
<li><strong>Care Coordination:</strong> Evaluation of case management and care coordination needs</li>
<li><strong>Expert Testimony:</strong> Clear, persuasive testimony in {city['state']} courts explaining life care plan components and costs</li>
</ul>
</div>
<!-- Healthcare Landscape -->
<div class="service-section">
<h2>Understanding {city['name']}'s Healthcare Resources</h2>
<p>Effective life care planning requires deep understanding of local healthcare resources and costs. {city['name']}'s medical landscape includes:</p>
<h3>Major Medical Facilities:</h3>
<p>{city['major_medical']} provide comprehensive medical services essential for catastrophic injury care. Understanding these facilities' specialties, costs, and capabilities is crucial for developing accurate life care plans.</p>
<p>This medical infrastructure provides various treatment options, but also requires careful analysis of costs, accessibility, and long-term care availability when developing life care plans for injured individuals in the {city['name']} area.</p>
</div>
<!-- Common Case Types -->
<div class="service-section">
<h2>Common {city['name']} Life Care Planning Cases</h2>
<h3>Catastrophic Injury Cases:</h3>
<ul>
<li>Traumatic brain injuries from motor vehicle accidents</li>
<li>Spinal cord injuries resulting in paralysis</li>
<li>Severe burn injuries requiring ongoing treatment</li>
<li>Amputations requiring prosthetics and lifetime care</li>
</ul>
<h3>Medical Malpractice:</h3>
<ul>
<li>Birth injuries including cerebral palsy and brain damage</li>
<li>Surgical errors resulting in permanent disability</li>
<li>Delayed diagnosis leading to advanced disease</li>
<li>Medication errors causing permanent harm</li>
</ul>
<h3>Long-Term Care Needs:</h3>
<ul>
<li>24-hour attendant care requirements</li>
<li>Skilled nursing and rehabilitation services</li>
<li>Ongoing therapeutic interventions</li>
<li>Specialized medical equipment and technology</li>
</ul>
</div>
<!-- Why Attorneys Choose Us -->
<div class="service-section">
<h2>Why {city['name']} Attorneys Choose Skerritt Economics</h2>
<ul>
<li><strong>CLCP Certification:</strong> Certified Life Care Planner with specialized training in catastrophic injury care planning</li>
<li><strong>Local Knowledge:</strong> Extensive familiarity with {city['state']}'s healthcare systems, costs, and resources</li>
<li><strong>Court Experience:</strong> Our firm has extensive experience testifying in {city['state']} courts about life care plans</li>
<li><strong>Comprehensive Approach:</strong> Integration with economic loss calculations for complete damage assessments</li>
<li><strong>Medical Collaboration:</strong> Strong relationships with healthcare providers for accurate care assessments</li>
<li><strong>Timely Service:</strong> Located {city['distance']}, providing responsive service to {city['name']} attorneys</li>
</ul>
</div>
<!-- Cost Considerations -->
<div class="service-section">
<h2>Life Care Planning Cost Factors in {city['name']}</h2>
<p>Life care plan costs in {city['name']} vary based on several factors:</p>
<ul>
<li><strong>Local Healthcare Costs:</strong> {city['name']}'s medical costs compared to national averages</li>
<li><strong>Specialty Care Availability:</strong> Access to specialized providers and associated travel costs</li>
<li><strong>Home Health Services:</strong> Local rates for nursing, therapy, and attendant care</li>
<li><strong>Medical Equipment:</strong> Regional pricing for durable medical equipment and supplies</li>
<li><strong>Housing Costs:</strong> Impact on home modification expenses and accessible housing options</li>
</ul>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Life Care Planning</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What does a life care planner do in {city['name']} catastrophic injury cases?</summary>
<p>A life care planner in {city['name']} develops comprehensive plans outlining all future medical care, equipment, medications, and services needed for catastrophically injured individuals. We work with medical professionals to project lifetime care costs, helping {city['state']} attorneys accurately value damages in personal injury and medical malpractice cases.</p>
</details>
<details class="faq-item">
<summary>How much does life care planning cost in {city['name']}, {city['state_abbr']}?</summary>
<p>Life care planning fees in {city['name']} typically range from $3,500 to $8,000 depending on injury complexity and the scope of future care needs. This includes medical record review, care plan development, cost projections, and expert testimony if needed. We provide detailed fee estimates during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When should {city['name']} attorneys hire a life care planner?</summary>
<p>{city['name']} attorneys should engage a life care planner when clients have suffered catastrophic injuries requiring long-term or lifetime medical care. Early involvement allows for comprehensive assessment of future needs and coordination with treating physicians to develop accurate, defensible care plans.</p>
</details>
<details class="faq-item">
<summary>What injuries typically require life care planning in {city['name']}?</summary>
<p>Common injuries requiring life care planning include traumatic brain injuries, spinal cord injuries, severe burns, amputations, birth injuries like cerebral palsy, and any condition resulting in permanent disability. These cases require detailed planning for medical care, equipment, medications, therapy, and support services throughout the individual's life.</p>
</details>
</div>
</div>
<!-- Related Services -->
<div class="service-section">
<h2>Related Services for {city['name']} Attorneys</h2>
<div class="related-pages-grid">
<div class="related-page-card">
<h4><a href="../../services/forensic-economics/">Forensic Economics</a></h4>
<p>Economic loss calculations to complement life care plans.</p>
</div>
<div class="related-page-card">
<h4><a href="../../services/vocational-expert/">Vocational Expert</a></h4>
<p>Earning capacity assessments for injured individuals.</p>
</div>
<div class="related-page-card">
<h4><a href="../../practice-areas/medical-malpractice/">Medical Malpractice Economics</a></h4>
<p>Comprehensive damage calculations for medical negligence cases.</p>
</div>
<div class="related-page-card">
<h4><a href="../../practice-areas/personal-injury/">Personal Injury Economics</a></h4>
<p>Complete economic analysis for catastrophic injury cases.</p>
</div>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need a Life Care Planner in {city['name']}?</h2>
<p>Free consultation for {city['name']} attorneys. Get expert life care planning for your catastrophic injury, medical malpractice, or personal injury cases.</p>
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
<p>Expert life care planning for {city['name']} attorneys.</p>
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

# Generate all city pages
for city in cities:
    generate_city_page(city)

print(f"\nGenerated {len(cities)} life care planning city pages!")