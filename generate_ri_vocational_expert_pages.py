#!/usr/bin/env python3
import os

# Rhode Island cities with vocational expert focus - excluding Providence which already exists
ri_cities = [
    {
        "name": "Warwick",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "82,823",
        "county": "Kent County",
        "distance_miles": 10,
        "major_employers": "T.F. Green Airport, Kent Hospital, Citizens Bank, Leviton Manufacturing",
        "court_info": "Kent County Superior Court, Warwick Municipal Court",
        "economy": "Major employment center with airport operations, healthcare facilities, and corporate offices. Growing service sector.",
        "proximity_message": "Located just 10 miles from our Smithfield office, providing immediate response for Warwick vocational assessments"
    },
    {
        "name": "Cranston",
        "state": "Rhode Island", 
        "state_abbr": "RI",
        "population": "82,934",
        "county": "Providence County",
        "distance_miles": 8,
        "major_employers": "Citizens Bank Operations, Cranston Print Works, Stop & Shop Distribution",
        "court_info": "Providence County Superior Court, Cranston Municipal Court",
        "economy": "Mix of retail, light manufacturing, and service industries. Major retail corridors along Route 6.",
        "proximity_message": "Just 8 miles from our Smithfield office, allowing for quick on-site visits and court appearances in Cranston"
    },
    {
        "name": "Pawtucket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "75,604",
        "county": "Providence County",
        "distance_miles": 7,
        "major_employers": "Hasbro, Memorial Hospital, City of Pawtucket, Teknor Apex",
        "court_info": "Providence County Superior Court, Pawtucket Municipal Court",
        "economy": "Former textile manufacturing hub transitioning to healthcare, creative industries, and modern manufacturing.",
        "proximity_message": "Only 7 miles from our office, enabling frequent in-person meetings and rapid response for Pawtucket cases"
    },
    {
        "name": "East Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "47,139",
        "county": "Providence County", 
        "distance_miles": 10,
        "major_employers": "Bradley Hospital, Emma Pendleton Bradley Hospital, Tockwotton Home",
        "court_info": "Providence County Superior Court, East Providence Municipal Court",
        "economy": "Healthcare-focused economy with waterfront development. Mix of healthcare, retail, and professional services.",
        "proximity_message": "A short 10-mile drive from Smithfield allows for convenient scheduling of evaluations and meetings"
    },
    {
        "name": "Woonsocket",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "43,240",
        "county": "Providence County",
        "distance_miles": 12,
        "major_employers": "Landmark Medical Center, CVS Health, Citizens Bank, Woonsocket Call",
        "court_info": "Providence County Superior Court, Woonsocket District Court",
        "economy": "Healthcare and financial services anchor the economy. Historical mill city with growing healthcare sector.",
        "proximity_message": "Located 12 miles from our office, we regularly serve Woonsocket with both virtual and in-person evaluations"
    },
    {
        "name": "Newport",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "25,163",
        "county": "Newport County",
        "distance_miles": 35,
        "major_employers": "Naval Station Newport, Newport Hospital, Salve Regina University",
        "court_info": "Newport County Superior Court, Newport Municipal Court",
        "economy": "Tourism, military, education, and healthcare drive employment. Significant seasonal employment variation.",
        "proximity_message": "Serving Newport with comprehensive vocational services, offering both in-person and virtual consultation options"
    },
    {
        "name": "Central Falls",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "22,583",
        "county": "Providence County",
        "distance_miles": 9,
        "major_employers": "Elizabeth Buffum Chace Center, various manufacturing and retail businesses",
        "court_info": "Providence County Superior Court, Central Falls Municipal Court",
        "economy": "Dense urban area with manufacturing, retail, and service employment. Significant immigrant workforce.",
        "proximity_message": "Just 9 miles away, providing quick access for Central Falls evaluations and court testimony"
    },
    {
        "name": "Westerly",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "23,359",
        "county": "Washington County",
        "distance_miles": 50,
        "major_employers": "Westerly Hospital, Ocean Community Chamber, Watch Hill resorts",
        "court_info": "Washington County Superior Court, Fourth Division District Court",
        "economy": "Tourism-driven coastal economy with healthcare and retail. Seasonal employment patterns.",
        "proximity_message": "Providing expert vocational services to Westerly through flexible scheduling and virtual consultation options"
    }
]

# Template for Rhode Island vocational expert pages
def generate_ri_vocational_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ri-vocational-expert.html"
    
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
<title>Vocational Expert {city['name']} RI | Earning Capacity & Employability | Chris Skerritt</title>
<meta content="Expert vocational evaluation services in {city['name']}, Rhode Island. Court-qualified vocational expert for personal injury, disability, and employment cases. Call 203-605-2814" name="description"/>
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
    "name": "Vocational Expert Services in {city['name']}, RI",
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
    "description": "Expert vocational evaluation and earning capacity assessment services for {city['name']}, Rhode Island. Court-qualified vocational expert serving attorneys and individuals in personal injury, disability, and employment matters.",
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
            "name": "What does a vocational expert do in {city['name']}, RI?",
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
                "text": "{city['economy']} Major employers include {city['major_employers']}. Our vocational assessments consider these local employment opportunities when evaluating earning capacity and job placement options for injured workers."
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
            "name": "{city['name']}, RI",
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
<span class="breadcrumb-current">Vocational Expert {city['name']} RI</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Vocational Expert in {city['name']}, Rhode Island</h1>
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
<p>{city['economy']} Understanding these local employment dynamics is crucial for accurate vocational assessments and earning capacity evaluations.</p>
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
<p>Our firm has extensive experience providing expert testimony in Rhode Island courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Rhode Island Workers' Compensation Court</li>
<li>U.S. District Court for the District of Rhode Island</li>
<li>Social Security disability hearings</li>
</ul>
<p>I understand the specific requirements and expectations of {city['name']} area courts and provide reports that meet these standards.</p>
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
<summary>What does a vocational expert do in {city['name']}, RI?</summary>
<p>A vocational expert in {city['name']} evaluates an individual's ability to work and earn income despite injuries or disabilities. We assess transferable skills, labor market conditions, and provide expert testimony in {city['court_info']}. Our services include employability assessments, earning capacity evaluations, and job placement analysis for legal cases.</p>
</details>
<details class="faq-item">
<summary>When do I need a vocational expert for my {city['name']} case?</summary>
<p>You need a vocational expert when determining lost earning capacity in personal injury cases, evaluating disability claims, assessing employability after workplace injuries, or analyzing vocational rehabilitation needs. {city['proximity_message']}.</p>
</details>
<details class="faq-item">
<summary>What is the {city['name']} job market like for injured workers?</summary>
<p>{city['economy']} Major employers include {city['major_employers']}. Our vocational assessments consider these local employment opportunities when evaluating earning capacity and job placement options for injured workers.</p>
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

# Generate all Rhode Island city pages
for city in ri_cities:
    generate_ri_vocational_page(city)

print(f"\nGenerated {len(ri_cities)} Rhode Island vocational expert pages!")
print("\nPages created for:")
for city in ri_cities:
    print(f"- {city['name']}, RI ({city['distance_miles']} miles from Smithfield)")