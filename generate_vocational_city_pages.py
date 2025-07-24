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
        "major_employers": "Massachusetts General Hospital, Brigham and Women's Hospital, Boston University, financial services",
        "court_info": "Suffolk County Superior Court, John Adams Courthouse",
        "economy": "Healthcare, education, biotechnology, and financial services dominate Boston's diverse economy",
        "distance": "approximately 50 miles from our Smithfield office"
    },
    {
        "name": "Worcester",
        "state": "Massachusetts", 
        "state_abbr": "MA",
        "population": "206,518",
        "major_employers": "UMass Medical School, Saint Vincent Hospital, Worcester Polytechnic Institute",
        "court_info": "Worcester County Superior Court, Worcester Trial Court",
        "economy": "Healthcare, education, manufacturing, and biotechnology sectors",
        "distance": "approximately 35 miles from our Smithfield office"
    },
    {
        "name": "Springfield",
        "state": "Massachusetts",
        "state_abbr": "MA", 
        "population": "155,929",
        "major_employers": "Baystate Health, MassMutual, Smith & Wesson",
        "court_info": "Hampden County Superior Court, Springfield",
        "economy": "Healthcare, insurance, manufacturing, and education",
        "distance": "approximately 60 miles from our Smithfield office"
    },
    {
        "name": "Cambridge",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "118,403",
        "major_employers": "MIT, Harvard University, biotechnology companies",
        "court_info": "Middlesex County Superior Court, Cambridge",
        "economy": "Education, research, biotechnology, and technology sectors",
        "distance": "approximately 45 miles from our Smithfield office"
    },
    {
        "name": "Lowell", 
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "115,554",
        "major_employers": "Lowell General Hospital, UMass Lowell, technology companies",
        "court_info": "Middlesex County Superior Court, Lowell",
        "economy": "Healthcare, education, technology, and advanced manufacturing",
        "distance": "approximately 55 miles from our Smithfield office"
    },
    # Connecticut
    {
        "name": "Bridgeport",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "148,654",
        "major_employers": "Bridgeport Hospital, St. Vincent's Medical Center, Sikorsky Aircraft",
        "court_info": "Fairfield County Superior Court, Bridgeport",
        "economy": "Healthcare, aerospace manufacturing, and maritime industries",
        "distance": "approximately 100 miles from our Smithfield office"
    },
    {
        "name": "Stamford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "135,470",
        "major_employers": "Financial services, Charter Communications, Pitney Bowes",
        "court_info": "Stamford Superior Court",
        "economy": "Corporate headquarters, financial services, and professional services",
        "distance": "approximately 120 miles from our Smithfield office"
    },
    {
        "name": "New Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "134,023",
        "major_employers": "Yale University, Yale New Haven Hospital",
        "court_info": "New Haven County Superior Court",
        "economy": "Education, healthcare, biotechnology, and professional services",
        "distance": "approximately 85 miles from our Smithfield office"
    },
    {
        "name": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "121,054",
        "major_employers": "Hartford Hospital, insurance companies (The Hartford, Aetna)",
        "court_info": "Hartford Superior Court, Connecticut Supreme Court",
        "economy": "Insurance industry capital, healthcare, government services",
        "distance": "approximately 70 miles from our Smithfield office"
    },
    # New Hampshire
    {
        "name": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "115,644",
        "major_employers": "Elliot Hospital, Southern New Hampshire University, BAE Systems",
        "court_info": "Hillsborough County Superior Court, Manchester",
        "economy": "Healthcare, education, technology, and advanced manufacturing",
        "distance": "approximately 80 miles from our Smithfield office"
    },
    # Maine
    {
        "name": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "68,408",
        "major_employers": "Maine Medical Center, financial services, tourism industry",
        "court_info": "Cumberland County Superior Court, Portland",
        "economy": "Healthcare, tourism, maritime industries, and food/beverage",
        "distance": "approximately 160 miles from our Smithfield office"
    },
    # Vermont
    {
        "name": "Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "44,743",
        "major_employers": "University of Vermont Medical Center, University of Vermont, GlobalFoundries",
        "court_info": "Chittenden County Superior Court, Burlington",
        "economy": "Healthcare, education, technology, and tourism",
        "distance": "approximately 280 miles from our Smithfield office"
    }
]

# Template for city pages
def generate_city_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-{city['state_abbr'].lower()}-vocational-expert.html"
    
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Vocational Expert {city['name']} {city['state_abbr']} | Chris Skerritt | Earning Capacity Evaluations</title>
<meta content="Expert vocational evaluations in {city['name']}, {city['state']}. CRC-certified vocational expert providing earning capacity assessments for personal injury & disability cases. Free consultation 203-605-2814" name="description"/>
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
    "name": "Vocational Expert Services in {city['name']}, {city['state_abbr']}",
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
    "description": "Expert vocational evaluations and earning capacity assessments for attorneys in {city['name']}, {city['state']}. CRC-certified vocational expert with extensive experience in personal injury, workers' compensation, and disability cases.",
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
            "name": "What does a vocational expert do in {city['name']} personal injury cases?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "A vocational expert in {city['name']} evaluates an injured person's ability to work and earn income after an accident or injury. We assess transferable skills, labor market conditions, and provide earning capacity evaluations that help {city['state']} attorneys quantify economic damages in personal injury, workers' compensation, and disability cases."
            }}
        }},
        {{
            "@type": "Question",
            "name": "How much does a vocational expert cost in {city['name']}, {city['state_abbr']}?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Vocational expert fees in {city['name']} typically range from $2,500 to $5,000 depending on case complexity. This includes the vocational assessment, earning capacity evaluation, written report, and deposition testimony if needed. We provide detailed fee estimates during the free initial consultation."
            }}
        }},
        {{
            "@type": "Question",
            "name": "When should {city['name']} attorneys hire a vocational expert?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "{city['name']} attorneys should engage a vocational expert when clients have permanent work restrictions, cannot return to previous employment, or face reduced earning capacity. Early involvement allows for proper vocational testing, labor market analysis, and coordination with medical experts to strengthen your case."
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
            "name": "{city['name']}, {city['state_abbr']}",
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
<span class="breadcrumb-current">Vocational Expert {city['name']} {city['state_abbr']}</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Vocational Expert in {city['name']}, {city['state']}</h1>
<div class="meta">
<span>CRC Certified</span>
<span>Court-Qualified Expert</span>
<span>Serving {city['name']} Area</span>
</div>
<p class="lead">Expert vocational evaluations and earning capacity assessments for {city['name']} attorneys. As CRC-certified vocational experts based in Rhode Island, we provide comprehensive vocational assessments for personal injury, workers' compensation, and disability cases throughout {city['name']} and {city['state']}.</p>
</div>
</section>
<!-- Local Service Content -->
<section class="service-content">
<div class="container">
<div class="service-sections">
<!-- City Overview -->
<div class="service-section">
<h2>Vocational Expert Services in {city['name']}</h2>
<p>Serving {city['name']}'s legal community with expert vocational evaluations, we understand the unique employment landscape of this {city['state']} city. With a population of {city['population']}, {city['name']} features major employers including {city['major_employers']}. Our vocational assessments reflect deep knowledge of the local labor market and employment opportunities specific to {city['name']}.</p>
<p>{city['economy']}. Located {city['distance']}, we provide timely and responsive vocational expert services to {city['name']} attorneys handling personal injury, workers' compensation, and disability cases.</p>
</div>
<!-- Services for City Attorneys -->
<div class="service-section">
<h2>Vocational Evaluations for {city['name']} Attorneys</h2>
<p>{city['name']} law firms rely on comprehensive vocational assessments to support their cases in {city['court_info']}. Our services include:</p>
<ul>
<li><strong>Earning Capacity Evaluations:</strong> Detailed analysis of pre-injury and post-injury earning potential specific to the {city['name']} job market</li>
<li><strong>Transferable Skills Analysis:</strong> Assessment of skills that transfer to available positions in the {city['name']} metropolitan area</li>
<li><strong>Labor Market Surveys:</strong> Real-time analysis of job availability in {city['name']} and surrounding areas</li>
<li><strong>Vocational Testing:</strong> Comprehensive aptitude and interest testing to identify suitable alternative occupations</li>
<li><strong>Job Placement Feasibility:</strong> Realistic assessment of employment options given {city['name']}'s current economic conditions</li>
<li><strong>Expert Testimony:</strong> Clear, persuasive testimony in {city['state']} courts explaining vocational findings</li>
</ul>
</div>
<!-- Employment Landscape -->
<div class="service-section">
<h2>Understanding {city['name']}'s Employment Market</h2>
<p>Effective vocational assessments require deep understanding of local employment conditions. {city['name']}'s economy is characterized by its diverse employment sectors and major employers including {city['major_employers']}.</p>
<p>This economic diversity provides various reemployment opportunities, but also requires careful analysis of transferable skills and physical capabilities when assessing injured workers' vocational potential in the {city['name']} area.</p>
</div>
<!-- Common Case Types -->
<div class="service-section">
<h2>Common {city['name']} Vocational Expert Cases</h2>
<h3>Personal Injury Cases:</h3>
<ul>
<li>Motor vehicle accidents on local highways and city streets</li>
<li>Slip and fall injuries at retail establishments and commercial properties</li>
<li>Construction and workplace accidents</li>
<li>Product liability injuries affecting work capacity</li>
</ul>
<h3>Workers' Compensation:</h3>
<ul>
<li>Healthcare worker injuries at area hospitals and medical facilities</li>
<li>Manufacturing and industrial workplace injuries</li>
<li>Office worker repetitive stress injuries</li>
<li>Service industry workplace accidents</li>
</ul>
<h3>Disability Evaluations:</h3>
<ul>
<li>Social Security disability assessments</li>
<li>Long-term disability insurance claims</li>
<li>Veterans disability evaluations</li>
<li>ADA accommodation assessments</li>
</ul>
</div>
<!-- Why Attorneys Choose Us -->
<div class="service-section">
<h2>Why {city['name']} Attorneys Choose Skerritt Economics</h2>
<ul>
<li><strong>Regional Expertise:</strong> Extensive knowledge of {city['state']}'s employment landscape and labor market conditions</li>
<li><strong>Court Experience:</strong> Our firm has extensive experience testifying in {city['state']} courts</li>
<li><strong>Comprehensive Approach:</strong> Integration with economic loss calculations for complete damage assessments</li>
<li><strong>Timely Service:</strong> Located {city['distance']}, providing responsive service to {city['name']} attorneys</li>
<li><strong>Professional Credentials:</strong> CRC certified with extensive vocational evaluation experience</li>
</ul>
</div>
<!-- FAQ Section -->
<div class="service-section">
<h2>Frequently Asked Questions - {city['name']} Vocational Expert</h2>
<div class="faq-grid">
<details class="faq-item">
<summary>What does a vocational expert do in {city['name']} personal injury cases?</summary>
<p>A vocational expert in {city['name']} evaluates an injured person's ability to work and earn income after an accident or injury. We assess transferable skills, labor market conditions, and provide earning capacity evaluations that help {city['state']} attorneys quantify economic damages in personal injury, workers' compensation, and disability cases.</p>
</details>
<details class="faq-item">
<summary>How much does a vocational expert cost in {city['name']}, {city['state_abbr']}?</summary>
<p>Vocational expert fees in {city['name']} typically range from $2,500 to $5,000 depending on case complexity. This includes the vocational assessment, earning capacity evaluation, written report, and deposition testimony if needed. We provide detailed fee estimates during the free initial consultation.</p>
</details>
<details class="faq-item">
<summary>When should {city['name']} attorneys hire a vocational expert?</summary>
<p>{city['name']} attorneys should engage a vocational expert when clients have permanent work restrictions, cannot return to previous employment, or face reduced earning capacity. Early involvement allows for proper vocational testing, labor market analysis, and coordination with medical experts to strengthen your case.</p>
</details>
<details class="faq-item">
<summary>What information do you need for a {city['name']} vocational assessment?</summary>
<p>For {city['name']} cases, we typically need medical records, work history, education records, and information about the client's physical and mental capabilities. Understanding their previous employment in {city['name']}'s job market and any specialized skills helps create accurate vocational assessments.</p>
</details>
</div>
</div>
<!-- Related Services -->
<div class="service-section">
<h2>Related Services for {city['name']} Attorneys</h2>
<div class="related-pages-grid">
<div class="related-page-card">
<h4><a href="../../services/forensic-economics/">Forensic Economics</a></h4>
<p>Complete economic loss calculations to complement vocational assessments.</p>
</div>
<div class="related-page-card">
<h4><a href="../../services/life-care-planning/">Life Care Planning</a></h4>
<p>Future medical cost projections for catastrophic injury cases.</p>
</div>
<div class="related-page-card">
<h4><a href="../../practice-areas/personal-injury/">Personal Injury Economics</a></h4>
<p>Comprehensive damage calculations for {city['name']} injury cases.</p>
</div>
<div class="related-page-card">
<h4><a href="../../practice-areas/employment/">Employment Litigation Support</a></h4>
<p>Economic analysis for wrongful termination and discrimination cases.</p>
</div>
</div>
</div>
<!-- Contact CTA -->
<div class="service-cta">
<h2>Need a Vocational Expert in {city['name']}?</h2>
<p>Free consultation for {city['name']} attorneys. Get expert vocational evaluations for your personal injury, workers' compensation, or disability cases.</p>
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
<p>Expert vocational evaluations for {city['name']} attorneys.</p>
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

# Generate all city pages
for city in cities:
    generate_city_page(city)

print(f"\nGenerated {len(cities)} vocational expert city pages!")