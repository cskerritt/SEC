#!/usr/bin/env python3
import os

# Connecticut cities with detailed information and distances from Smithfield, RI
ct_cities = [
    {
        "name": "Bridgeport",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "148,654",
        "county": "Fairfield County",
        "distance_miles": 100,
        "major_employers": "Bridgeport Hospital, St. Vincent's Medical Center, People's United Bank, University of Bridgeport",
        "court_info": "Fairfield County Superior Court, U.S. District Court for Connecticut",
        "economy": "Connecticut's largest city with healthcare, financial services, and education sectors, along with ongoing waterfront redevelopment",
        "proximity_message": "Serving Bridgeport attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony when required"
    },
    {
        "name": "New Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "134,023",
        "county": "New Haven County",
        "distance_miles": 85,
        "major_employers": "Yale University, Yale New Haven Hospital, Knights of Columbus headquarters",
        "court_info": "New Haven County Superior Court, U.S. District Court for Connecticut",
        "economy": "Major academic and medical center anchored by Yale University, with biotechnology, healthcare, and professional services",
        "proximity_message": "Serving New Haven attorneys with expert forensic economic services through virtual consultations and in-person meetings as needed"
    },
    {
        "name": "Stamford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "135,470",
        "county": "Fairfield County",
        "distance_miles": 120,
        "major_employers": "Charter Communications, Pitney Bowes, WWE headquarters, numerous financial firms",
        "court_info": "Stamford Superior Court, Stamford-Norwalk Judicial District",
        "economy": "Major corporate center with headquarters of Fortune 500 companies, strong financial services and media sectors",
        "proximity_message": "Serving Stamford attorneys with comprehensive forensic economic services through virtual evaluations and in-person testimony at trial"
    },
    {
        "name": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "121,054",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_employers": "The Hartford, Aetna, Hartford Hospital, State of Connecticut",
        "court_info": "Hartford Superior Court, Connecticut Supreme Court, U.S. District Court for Connecticut",
        "economy": "State capital and insurance capital of America, with major insurance companies, healthcare, and government employment",
        "proximity_message": "Serving Hartford attorneys with expert forensic economic services through flexible virtual consultations and in-person meetings"
    },
    {
        "name": "Waterbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "114,403",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "Saint Mary's Hospital, Waterbury Hospital, Webster Bank, City of Waterbury",
        "court_info": "Waterbury Superior Court, Waterbury Judicial District",
        "economy": "Former brass manufacturing center now focused on healthcare, financial services, and retail",
        "proximity_message": "Serving Waterbury attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Norwalk",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "91,184",
        "county": "Fairfield County",
        "distance_miles": 110,
        "major_employers": "Norwalk Hospital, Xerox, FactSet, Booking Holdings",
        "court_info": "Stamford-Norwalk Judicial District Court",
        "economy": "Corporate headquarters location with technology, financial services, and healthcare sectors",
        "proximity_message": "Serving Norwalk attorneys with expert forensic economic services through virtual evaluations and in-person testimony as needed"
    },
    {
        "name": "Danbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "86,518",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "Danbury Hospital, Boehringer Ingelheim, Praxair, Western Connecticut State University",
        "court_info": "Danbury Superior Court, Danbury Judicial District",
        "economy": "Healthcare, pharmaceuticals, education, and corporate headquarters with proximity to New York",
        "proximity_message": "Serving Danbury attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "New Britain",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "74,135",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Hospital of Central Connecticut, Stanley Black & Decker, Central Connecticut State University",
        "court_info": "New Britain Superior Court, New Britain Judicial District",
        "economy": "Hardware City with manufacturing heritage, now diversified with healthcare, education, and tools manufacturing",
        "proximity_message": "Serving New Britain attorneys with expert forensic economic services through flexible consultation options"
    },
    {
        "name": "West Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "55,584",
        "county": "New Haven County",
        "distance_miles": 85,
        "major_employers": "VA Connecticut Healthcare System, University of New Haven, Yale New Haven Health",
        "court_info": "New Haven County Superior Court",
        "economy": "Healthcare, higher education, and veterans services with growing biotechnology sector",
        "proximity_message": "Serving West Haven attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Bristol",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "60,640",
        "county": "Hartford County",
        "distance_miles": 60,
        "major_employers": "ESPN headquarters, Bristol Hospital, Barnes Group",
        "court_info": "Bristol Superior Court, New Britain Judicial District",
        "economy": "Home to ESPN with strong media, healthcare, and manufacturing sectors",
        "proximity_message": "Serving Bristol attorneys with expert forensic economic services through flexible virtual and in-person consultations"
    },
    {
        "name": "Meriden",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,512",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "MidState Medical Center, Meriden Board of Education, Nufern",
        "court_info": "Meriden Superior Court, New Haven Judicial District",
        "economy": "Healthcare, education, and specialized manufacturing including fiber optics",
        "proximity_message": "Serving Meriden attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Milford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "50,558",
        "county": "New Haven County",
        "distance_miles": 90,
        "major_employers": "Milford Hospital, Subway headquarters, Schick",
        "court_info": "Milford Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate headquarters, healthcare, and retail with coastal economy elements",
        "proximity_message": "Serving Milford attorneys with expert forensic economic services through virtual evaluations and in-person testimony"
    },
    {
        "name": "Stratford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "52,355",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "Sikorsky Aircraft, Town of Stratford, aerospace suppliers",
        "court_info": "Bridgeport Superior Court, Fairfield Judicial District",
        "economy": "Major aerospace manufacturing center with Sikorsky helicopters and related suppliers",
        "proximity_message": "Serving Stratford attorneys with comprehensive forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "East Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "51,045",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_employers": "Pratt & Whitney, Goodwin University, aerospace manufacturers",
        "court_info": "Hartford Superior Court",
        "economy": "Aerospace manufacturing hub anchored by Pratt & Whitney jet engines",
        "proximity_message": "Serving East Hartford attorneys with expert forensic economic services through flexible consultation arrangements"
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
        "economy": "Healthcare, higher education, and state facilities with historic downtown",
        "proximity_message": "Serving Middletown attorneys with comprehensive forensic economic services through virtual and in-person consultations"
    },
    {
        "name": "Manchester",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "59,713",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Manchester Memorial Hospital, retail centers, Allied Printing",
        "court_info": "Manchester Superior Court, Hartford Judicial District",
        "economy": "Healthcare, retail, and printing with growing professional services",
        "proximity_message": "Serving Manchester attorneys with expert forensic economic services through flexible meeting options"
    },
    {
        "name": "Enfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "42,269",
        "county": "Hartford County",
        "distance_miles": 75,
        "major_employers": "Mass Mutual, LEGO North America, Brooks Brothers distribution",
        "court_info": "Enfield Superior Court, Hartford Judicial District",
        "economy": "Distribution centers, financial services, and retail near Massachusetts border",
        "proximity_message": "Serving Enfield attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Shelton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "40,869",
        "county": "Fairfield County",
        "distance_miles": 90,
        "major_employers": "PerkinElmer, Hubbell, Edgewell Personal Care",
        "court_info": "Derby Superior Court, Ansonia-Milford Judicial District",
        "economy": "Corporate headquarters and manufacturing with life sciences focus",
        "proximity_message": "Serving Shelton attorneys with expert forensic economic services through virtual evaluations and in-person testimony"
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
        "economy": "Manufacturing, healthcare, and clean energy technology",
        "proximity_message": "Serving Torrington attorneys with comprehensive forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Trumbull",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "36,827",
        "county": "Fairfield County",
        "distance_miles": 95,
        "major_employers": "St. Vincent's Medical Center (nearby), Aquarion Water, corporate offices",
        "court_info": "Bridgeport Superior Court",
        "economy": "Suburban community with corporate offices and professional services",
        "proximity_message": "Serving Trumbull attorneys with expert forensic economic services through virtual consultations and in-person testimony"
    },
    {
        "name": "Glastonbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "35,159",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Rate Reduction Company, local businesses, professional services",
        "court_info": "Hartford Superior Court",
        "economy": "Affluent suburban community with professional services and local businesses",
        "proximity_message": "Serving Glastonbury attorneys with comprehensive forensic economic services through flexible consultation options"
    },
    {
        "name": "Naugatuck",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "31,519",
        "county": "New Haven County",
        "distance_miles": 75,
        "major_employers": "H&R Block manufacturing, Peter Paul Electronics, local manufacturers",
        "court_info": "Waterbury Superior Court",
        "economy": "Manufacturing heritage with rubber and chemical production",
        "proximity_message": "Serving Naugatuck attorneys with expert forensic economic services through virtual consultations and in-person meetings"
    },
    {
        "name": "Newington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "30,536",
        "county": "Hartford County",
        "distance_miles": 65,
        "major_employers": "Connecticut State Police headquarters, retail centers",
        "court_info": "Hartford Superior Court",
        "economy": "Government services, retail, and professional services",
        "proximity_message": "Serving Newington attorneys with comprehensive forensic economic services through flexible meeting arrangements"
    },
    {
        "name": "Wallingford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "44,396",
        "county": "New Haven County",
        "distance_miles": 70,
        "major_employers": "Amphenol, Ulbrich Stainless Steels, Bristol-Myers Squibb",
        "court_info": "Meriden Superior Court",
        "economy": "Manufacturing, pharmaceuticals, and technology companies",
        "proximity_message": "Serving Wallingford attorneys with expert forensic economic services through virtual and in-person consultations"
    },
    {
        "name": "Wethersfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "27,298",
        "county": "Hartford County",
        "distance_miles": 70,
        "major_employers": "State of Connecticut Department of Motor Vehicles, local businesses",
        "court_info": "Hartford Superior Court",
        "economy": "Government services and historic community with local businesses",
        "proximity_message": "Serving Wethersfield attorneys with comprehensive forensic economic services through flexible consultation options"
    },
    {
        "name": "Greenwich",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "63,518",
        "county": "Fairfield County",
        "distance_miles": 130,
        "major_employers": "Greenwich Hospital, hedge funds, financial services firms",
        "court_info": "Stamford Superior Court",
        "economy": "Wealthy community with hedge funds, private equity, and financial services",
        "proximity_message": "Serving Greenwich attorneys with expert forensic economic services through virtual evaluations and in-person testimony at trial"
    }
]

# Template for Connecticut forensic economics pages
def generate_ct_page(city):
    filename = f"{city['name'].lower().replace(' ', '-')}-ct-forensic-economist.html"
    
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
<title>Forensic Economist {city['name']} CT | Economic Damage Expert | Chris Skerritt</title>
<meta content="Expert forensic economist serving {city['name']}, Connecticut attorneys. Economic damage calculations, lost earnings analysis, expert testimony. Free consultation 203-605-2814" name="description"/>
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
    "name": "Forensic Economics Services in {city['name']}, CT",
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
    "description": "Expert forensic economist providing economic damage analysis, lost earnings calculations, and expert testimony for attorneys in {city['name']}, Connecticut.",
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
            "name": "What types of economic damages do you calculate for {city['name']} attorneys?",
            "acceptedAnswer": {{
                "@type": "Answer",
                "text": "For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with Connecticut law and are tailored to local wage data and economic conditions in {city['county']}."
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
                "text": "Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout Connecticut's court system."
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
            "name": "{city['name']}, CT",
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
<span class="breadcrumb-current">Forensic Economist {city['name']} CT</span>
</li>
</ol>
</div>
</nav>
<!-- Service Hero -->
<section class="service-hero">
<div class="container">
<h1>Forensic Economist in {city['name']}, Connecticut</h1>
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
<p>As a leading forensic economist serving {city['name']}, we provide comprehensive economic damage analysis for attorneys throughout {city['county']}. With a population of {city['population']}, {city['name']} is home to major employers including {city['major_employers']}, creating a unique economic landscape that requires specialized knowledge for accurate damage calculations.</p>
<p>{city['economy']}. Our forensic economic analyses incorporate this local economic context, ensuring that damage calculations reflect the actual earning opportunities and economic conditions in the {city['name']} area.</p>
</div>
<!-- Services for Local Attorneys -->
<div class="service-section">
<h2>Economic Damage Analysis for {city['name']} Attorneys</h2>
<p>We provide {city['name']} law firms with reliable economic analysis for cases in {city['court_info']}. Our comprehensive services include:</p>
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
<p>Our firm has extensive experience providing expert testimony in Connecticut courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>Depositions at {city['name']} law offices</li>
<li>Mediation and arbitration proceedings</li>
<li>Settlement conferences and negotiations</li>
</ul>
<p>Our reports are designed to meet Connecticut's evidentiary standards, and we work closely with {city['name']} attorneys to ensure all economic damage calculations are clearly presented and defensible.</p>
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
<p>For {city['name']} attorneys, we calculate comprehensive economic damages including lost earnings, lost earning capacity, household services value, fringe benefits, medical costs, and business losses. Our analyses comply with Connecticut law and are tailored to local wage data and economic conditions in {city['county']}.</p>
</details>
<details class="faq-item">
<summary>How quickly can you provide economic damage reports in {city['name']}?</summary>
<p>{city['proximity_message']}. Preliminary damage assessments are typically available within 3-5 business days, with comprehensive reports completed within 2-3 weeks depending on case complexity.</p>
</details>
<details class="faq-item">
<summary>Do you testify in {city['county']} courts?</summary>
<p>Yes, our firm regularly provides expert testimony in {city['court_info']}. We have extensive experience presenting economic damage calculations to judges and juries throughout Connecticut's court system.</p>
</details>
<details class="faq-item">
<summary>What makes your {city['name']} economic damage calculations reliable?</summary>
<p>Our calculations use local {city['county']} wage data, employment statistics, and economic conditions specific to the {city['name']} area. We employ accepted forensic economic methodologies while incorporating deep knowledge of the local economy, major employers, and labor market conditions.</p>
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

# Generate all Connecticut city pages
for city in ct_cities:
    generate_ct_page(city)

print(f"\nGenerated {len(ct_cities)} Connecticut forensic economics pages!")
print("\nPages created for:")
for city in ct_cities:
    print(f"- {city['name']}, CT ({city['distance_miles']} miles from Smithfield)")