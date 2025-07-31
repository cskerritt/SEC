#!/usr/bin/env python3
import os

# Connecticut cities with vocational expert focus - excluding Bridgeport, New Haven, Stamford, Hartford which already exist
ct_cities = [
    {
        "name": "Waterbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "114,403",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "Waterbury Hospital, Saint Mary's Hospital, Webster Bank, Post University",
        "court_info": "Waterbury Superior Court, Waterbury Judicial District",
        "economy": "Regional center with healthcare systems, banks, and diverse manufacturing and retail businesses",
        "proximity_message": "Serving Waterbury businesses with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Norwalk",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "91,184",
        "county": "Fairfield County",
        "distance_miles": 110,
        "major_employers": "Norwalk Hospital, Xerox, FactSet Research Systems, Diageo North America",
        "court_info": "Stamford-Norwalk Judicial District Court",
        "economy": "Corporate headquarters location with technology firms, healthcare providers, and professional services",
        "proximity_message": "Serving Norwalk attorneys with expert vocational services through virtual evaluations and in-person meetings as needed"
    },
    {
        "name": "Danbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "86,518",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "Danbury Hospital, Western Connecticut State University, Praxair, Ethan Allen",
        "court_info": "Danbury Superior Court, Danbury Judicial District",
        "economy": "Healthcare and pharmaceutical hub with hospital systems, biotech companies, and diverse businesses",
        "proximity_message": "Serving Danbury attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "New Britain",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "74,135",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Hospital of Central Connecticut, Central Connecticut State University, Stanley Black & Decker",
        "court_info": "New Britain Superior Court, New Britain Judicial District",
        "economy": "Hardware City with manufacturing heritage, healthcare facilities, and educational institutions",
        "proximity_message": "Serving New Britain attorneys with expert vocational services through flexible consultation options"
    },
    {
        "name": "West Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "55,584",
        "county": "New Haven County",
        "distance_miles": 85,
        "major_employers": "Yale New Haven Health, University of New Haven, VA Connecticut Healthcare",
        "court_info": "New Haven County Superior Court",
        "economy": "Healthcare and education center with VA facilities, university presence, and growing biotech sector",
        "proximity_message": "Serving West Haven attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Bristol",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "60,640",
        "county": "Hartford County",
        "distance_miles": 60,
        "major_employers": "ESPN, Bristol Hospital, Barnes Group, UTC Aerospace Systems",
        "court_info": "Bristol Superior Court, New Britain Judicial District",
        "economy": "Home to ESPN with strong media presence, healthcare services, and manufacturing companies",
        "proximity_message": "Serving Bristol attorneys with expert vocational services through flexible virtual and in-person consultations"
    },
    {
        "name": "Meriden",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,512",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "MidState Medical Center, Anthem Blue Cross, Hunter's Ambulance",
        "court_info": "Meriden Superior Court, New Haven Judicial District",
        "economy": "Healthcare and manufacturing center with medical facilities and specialized manufacturing",
        "proximity_message": "Serving Meriden attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Milford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "50,558",
        "county": "New Haven County",
        "distance_miles": 90,
        "major_employers": "Subway headquarters, Schick, Doctor's Associates, various healthcare facilities",
        "court_info": "Milford Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate headquarters location with healthcare providers, retail centers, and coastal businesses",
        "proximity_message": "Serving Milford attorneys with expert vocational services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Stratford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "52,355",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "Sikorsky Aircraft, Stratford Health Department, Town of Stratford",
        "court_info": "Bridgeport Superior Court, Fairfield Judicial District",
        "economy": "Aerospace manufacturing center with Sikorsky and related suppliers, plus healthcare and retail",
        "proximity_message": "Serving Stratford attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "East Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "51,045",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_employers": "Pratt & Whitney, Goodwin University, Rentschler Field",
        "court_info": "Hartford Superior Court",
        "economy": "Aerospace manufacturing hub with Pratt & Whitney and related technology companies",
        "proximity_message": "Serving East Hartford attorneys with expert vocational services through flexible consultation arrangements"
    },
    {
        "name": "Middletown",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "47,717",
        "county": "Middlesex County",
        "distance_miles": 65,
        "major_employers": "Middlesex Hospital, Wesleyan University, Connecticut Valley Hospital",
        "court_info": "Middlesex Superior Court, Middletown Judicial District",
        "economy": "Healthcare, education, and insurance center with hospital systems and university presence",
        "proximity_message": "Serving Middletown attorneys with comprehensive vocational services through virtual and in-person consultations"
    },
    {
        "name": "Manchester",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,713",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Manchester Memorial Hospital, Allied Printing, Journal Inquirer",
        "court_info": "Manchester Superior Court, Hartford Judicial District",
        "economy": "Healthcare and retail hub with hospital systems, shopping centers, and printing industry",
        "proximity_message": "Serving Manchester attorneys with expert vocational services through flexible meeting options"
    },
    {
        "name": "Enfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "42,269",
        "county": "Hartford County",
        "distance_miles": 75,
        "major_employers": "Mass Mutual, LEGO Systems, Brooks Brothers Distribution",
        "court_info": "Enfield Superior Court, Hartford Judicial District",
        "economy": "Distribution and logistics center with financial services and retail near Massachusetts border",
        "proximity_message": "Serving Enfield attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Shelton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "40,869",
        "county": "Fairfield County",
        "distance_miles": 90,
        "major_employers": "PerkinElmer, Pitney Bowes, Edgewell Personal Care, Hubbell Incorporated",
        "court_info": "Derby Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate and life sciences hub with headquarters facilities and specialized manufacturing",
        "proximity_message": "Serving Shelton attorneys with expert vocational services through virtual evaluations and in-person meetings"
    },
    {
        "name": "Torrington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,515",
        "county": "Litchfield County",
        "distance_miles": 85,
        "major_employers": "Charlotte Hungerford Hospital, Dymax Corporation, FuelCell Energy",
        "court_info": "Torrington Superior Court, Litchfield Judicial District",
        "economy": "Healthcare and manufacturing center with hospital systems and clean energy technology companies",
        "proximity_message": "Serving Torrington attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Trumbull",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "36,827",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "St. Vincent's Medical Center, Aquarion Water Company, various corporate offices",
        "court_info": "Bridgeport Superior Court",
        "economy": "Suburban business community with corporate offices, medical practices, and professional services",
        "proximity_message": "Serving Trumbull attorneys with expert vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Glastonbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,159",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "various professional services, medical practices, local businesses",
        "court_info": "Hartford Superior Court",
        "economy": "Affluent community with professional service firms, medical practices, and technology companies",
        "proximity_message": "Serving Glastonbury attorneys with comprehensive vocational services through flexible consultation options"
    },
    {
        "name": "Naugatuck",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "31,519",
        "county": "New Haven County",
        "distance_miles": 75,
        "major_employers": "Peter Paul Electronics, H&R Block, various manufacturers",
        "court_info": "Waterbury Superior Court",
        "economy": "Manufacturing center with rubber and chemical production plus healthcare services",
        "proximity_message": "Serving Naugatuck attorneys with expert vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Newington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "30,536",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Connecticut Department of Motor Vehicles, various state agencies, retail centers",
        "court_info": "Hartford Superior Court",
        "economy": "Government and retail center with state facilities and shopping districts",
        "proximity_message": "Serving Newington attorneys with comprehensive vocational services through flexible meeting arrangements"
    },
    {
        "name": "Wallingford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "44,396",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "Gaylord Hospital, Bristol-Myers Squibb, Anthem Blue Cross",
        "court_info": "Meriden Superior Court",
        "economy": "Manufacturing and pharmaceutical center with technology companies and healthcare providers",
        "proximity_message": "Serving Wallingford attorneys with expert vocational services through virtual and in-person consultations"
    },
    {
        "name": "Wethersfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "27,298",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_employers": "Connecticut Department of Corrections, various state offices, local businesses",
        "court_info": "Hartford Superior Court",
        "economy": "Historic community with government services and established local businesses",
        "proximity_message": "Serving Wethersfield attorneys with comprehensive vocational services through flexible consultation options"
    },
    {
        "name": "Greenwich",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "63,518",
        "county": "Fairfield County",
        "distance_miles": 130,
        "major_employers": "Greenwich Hospital, numerous hedge funds, private equity firms",
        "court_info": "Stamford Superior Court",
        "economy": "Wealthy community with concentration of hedge funds, private equity, and financial services",
        "proximity_message": "Serving Greenwich attorneys with expert vocational services through virtual evaluations and in-person meetings at trial"
    }
]

# Template for Connecticut vocational expert pages
def generate_ct_vocational_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ct-vocational-expert.html"
    
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
<title>Vocational Expert {city['name']} CT | Earning Capacity & Employability | Chris Skerritt</title>
<meta content="Expert vocational evaluation services in {city['name']}, Connecticut. Court-qualified vocational expert for personal injury, disability, and employment cases. Call 203-605-2814" name="description"/>
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
    "name": "Vocational Expert Services in {city['name']}, CT",
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
    "description": "Expert vocational evaluation and earning capacity assessment services for {city['name']}, Connecticut. Court-qualified vocational expert serving attorneys and individuals in personal injury, disability, and employment matters.",
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
            "name": "What does a vocational expert do in {city['name']}, CT?",
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
            "name": "{city['name']}, CT",
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
<span class="breadcrumb-current">Vocational Expert {city['name']} CT</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Vocational Expert in {city['name']}, Connecticut</h1>
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
<p>Our firm has extensive experience providing expert testimony in Connecticut courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Connecticut Workers' Compensation Commission</li>
<li>U.S. District Court for the District of Connecticut</li>
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
<summary>What does a vocational expert do in {city['name']}, CT?</summary>
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

# Generate all Connecticut city pages
for city in ct_cities:
    generate_ct_vocational_page(city)

print(f"\nGenerated {len(ct_cities)} Connecticut vocational expert pages!")
print("\nPages created for:")
for city in ct_cities:
    print(f"- {city['name']}, CT ({city['distance_miles']} miles from Smithfield)")