#!/usr/bin/env python3
import os

# Rhode Island cities with detailed information
ri_cities = [
    {
        "name": "Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "190,934",
        "county": "Providence County",
        "distance_miles": 10,
        "major_employers": "Brown University, Lifespan health system, Citizens Bank, state government offices",
        "court_info": "Rhode Island Superior Court (Licht Judicial Complex), U.S. District Court, Workers' Compensation Court",
        "economy": "As the state capital and largest city, Providence has a diverse economy including healthcare, education, financial services, and government",
        "proximity_message": "Located just 10 miles from our Smithfield office, we provide prompt, in-person forensic economic evaluations and can quickly respond to urgent case needs"
    },
    {
        "name": "Warwick",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,823",
        "county": "Kent County",
        "distance_miles": 15,
        "major_employers": "T.F. Green Airport, Kent Hospital, retail centers, Citizens Bank operations center",
        "court_info": "Kent County Courthouse",
        "economy": "Rhode Island's second-largest city with a strong service sector, healthcare, and airport-related businesses",
        "proximity_message": "Located just 15 miles from our Smithfield office, we provide timely, in-person forensic economic services to Warwick attorneys"
    },
    {
        "name": "Cranston",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,934",
        "county": "Providence County",
        "distance_miles": 12,
        "major_employers": "Manufacturing companies, retail centers, healthcare facilities",
        "court_info": "Cases typically heard in Providence County Superior Court",
        "economy": "Mix of residential, commercial, and light industrial with strong healthcare and retail sectors",
        "proximity_message": "Just 12 miles from our Smithfield office, we offer immediate response and in-person consultations for Cranston legal professionals"
    },
    {
        "name": "Pawtucket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "75,604",
        "county": "Providence County",
        "distance_miles": 8,
        "major_employers": "Hasbro (headquarters), Memorial Hospital, manufacturing companies",
        "court_info": "Cases heard in Providence County Superior Court",
        "economy": "Historic manufacturing center transitioning to mixed economy with healthcare, retail, and creative industries",
        "proximity_message": "Only 8 miles from our Smithfield office, we provide immediate, cost-effective forensic economic services with quick turnaround times"
    },
    {
        "name": "East Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "47,139",
        "county": "Providence County",
        "distance_miles": 12,
        "major_employers": "Healthcare facilities, retail centers, waterfront businesses",
        "court_info": "Providence County Superior Court jurisdiction",
        "economy": "Suburban community with growing healthcare sector and revitalized waterfront district",
        "proximity_message": "Just 12 miles from our Smithfield office, we offer convenient in-person meetings and rapid case response"
    },
    {
        "name": "Woonsocket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "43,240",
        "county": "Providence County",
        "distance_miles": 10,
        "major_employers": "Landmark Medical Center, CVS Health operations, manufacturing",
        "court_info": "Providence County Superior Court, Woonsocket District Court",
        "economy": "Former mill city with healthcare, retail, and light manufacturing base",
        "proximity_message": "Located just 10 miles from our Smithfield office, we provide quick, in-person forensic economic evaluations for Woonsocket attorneys"
    },
    {
        "name": "Newport",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "25,163",
        "county": "Newport County",
        "distance_miles": 30,
        "major_employers": "Naval Station Newport, Newport Hospital, tourism industry, hospitality",
        "court_info": "Newport County Superior Court",
        "economy": "Tourism, military presence, healthcare, and marine industries drive the local economy",
        "proximity_message": "Located 30 miles from our Smithfield office, we regularly serve Newport attorneys with both in-person meetings and efficient remote consultations"
    },
    {
        "name": "Westerly",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "23,359",
        "county": "Washington County",
        "distance_miles": 45,
        "major_employers": "Westerly Hospital, Electric Boat, tourism and hospitality",
        "court_info": "Washington County Superior Court (Wakefield)",
        "economy": "Coastal community with tourism, healthcare, and defense contractor employment",
        "proximity_message": "Serving Westerly attorneys with flexible consultation options, including in-person meetings at your office or ours, and comprehensive virtual evaluations"
    }
]

# Template for Rhode Island forensic economics pages
def generate_ri_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ri-forensic-economist.html"
    
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
<title>Forensic Economist {city['name']} RI | Economic Damage Expert | Chris Skerritt</title>
<meta content="Expert forensic economist serving {city['name']}, Rhode Island attorneys. Economic damage calculations, lost earnings analysis, expert testimony. Free consultation 203-605-2814" name="description"/>
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
    "name": "Forensic Economics Services in {city['name']}, RI",
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
    "description": "Expert forensic economist providing economic damage analysis, lost earnings calculations, and expert testimony for attorneys in {city['name']}, Rhode Island.",
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
            "name": "What types of economic damages do you calculate for {city['name']} attorneys?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "For {city['name']} attorneys, I calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. My analyses comply with Rhode Island law and are tailored to local wage data and economic conditions in {city['county']}."
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
                "text": "Yes, I regularly provide expert testimony in {city['court_info']}. I have extensive experience presenting economic damage calculations to judges and juries throughout Rhode Island's court system."
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
            "name": "{city['name']}, RI",
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
<span class="breadcrumb-current">Forensic Economist {city['name']} RI</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Forensic Economist in {city['name']}, Rhode Island</h1>
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
<p>As a leading forensic economist serving {city['name']}, I provide comprehensive economic damage analysis for attorneys throughout {city['county']}. With a population of {city['population']}, {city['name']} is home to major employers including {city['major_employers']}, creating a unique economic landscape that requires specialized knowledge for accurate damage calculations.</p>
<p>{city['economy']}. My forensic economic analyses incorporate this local economic context, ensuring that damage calculations reflect the actual earning opportunities and economic conditions in the {city['name']} area.</p>
</div>
<!-- Services for Local Attorneys -->
<div class="service-section">
<h2>Economic Damage Analysis for {city['name']} Attorneys</h2>
<p>I provide {city['name']} law firms with reliable economic analysis for cases in {city['court_info']}. My comprehensive services include:</p>
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
<p>Our firm has extensive experience providing expert testimony in Rhode Island courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences and negotiations</li>
</ul>
<p>Our reports are designed to meet Rhode Island's evidentiary standards, and we work closely with {city['name']} attorneys to ensure all economic damage calculations are clearly presented and defensible.</p>
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
<p>For {city['name']} attorneys, I calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. My analyses comply with Rhode Island law and are tailored to local wage data and economic conditions in {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How quickly can you provide economic damage reports in {city['name']}?</summary>
<p>{city['proximity_message']}. Preliminary damage assessments are typically available within 3-5 business days, with comprehensive reports completed within 2-3 weeks depending on case complexity.</p>
</details>
<details class="faq-item">
<summary>Do you testify in {city['county']} courts?</summary>
<p>Yes, I regularly provide expert testimony in {city['court_info']}. I have extensive experience presenting economic damage calculations to judges and juries throughout Rhode Island's court system.</p>
</details>
<details class="faq-item">
<summary>What makes your {city['name']} economic damage calculations reliable?</summary>
<p>My calculations use local {city['county']} wage data, employment statistics, and economic conditions specific to the {city['name']} area. I employ accepted forensic economic methodologies while incorporating deep knowledge of the local economy, major employers, and labor market conditions.</p>
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

# Generate all Rhode Island city pages
for city in ri_cities:
    generate_ri_page(city)

print(f"\nGenerated {len(ri_cities)} Rhode Island forensic economics pages!")
print("\nPages created for:")
for city in ri_cities:
    print(f"- {city['name']}, RI ({city['distance_miles']} miles from Smithfield)")