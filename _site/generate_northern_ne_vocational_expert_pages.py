#!/usr/bin/env python3
import os

# Northern New England cities with vocational expert focus - excluding Manchester NH, Portland ME, Burlington VT which already exist
northern_ne_cities = [
    # New Hampshire cities (excluding Manchester which already exists)
    {
        "name": "Nashua",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "91,322",
        "county": "Hillsborough County",
        "distance_miles": 85,
        "major_employers": "BAE Systems, Fidelity Investments, Saint Joseph Hospital, Oracle",
        "court_info": "Hillsborough County Superior Court South, Nashua District Court",
        "economy": "Technology and defense contracting hub with financial services and healthcare sectors",
        "proximity_message": "Serving Nashua attorneys with comprehensive vocational services through virtual consultations and in-person meetings"
    },
    {
        "name": "Concord",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "43,976",
        "county": "Merrimack County",
        "distance_miles": 110,
        "major_employers": "Concord Hospital, State of New Hampshire, Lincoln Financial Group",
        "court_info": "Merrimack County Superior Court, Concord District Court, New Hampshire Supreme Court",
        "economy": "State capital with government employment, healthcare, and insurance sectors",
        "proximity_message": "Providing vocational evaluations to Concord attorneys through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Derry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "34,317",
        "county": "Rockingham County",
        "distance_miles": 90,
        "major_employers": "Parkland Medical Center, Pinkerton Academy, various technology firms",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "economy": "Growing community with healthcare, education, and technology companies",
        "proximity_message": "Serving Derry attorneys with expert vocational services through flexible consultation arrangements"
    },
    {
        "name": "Rochester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,492",
        "county": "Strafford County",
        "distance_miles": 110,
        "major_employers": "Frisbie Memorial Hospital, Albany International, City of Rochester",
        "court_info": "Strafford County Superior Court, Rochester District Court",
        "economy": "Manufacturing and healthcare center in the Seacoast region",
        "proximity_message": "Providing comprehensive vocational services to Rochester attorneys through virtual and in-person options"
    },
    {
        "name": "Salem",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "30,089",
        "county": "Rockingham County",
        "distance_miles": 75,
        "major_employers": "various retail businesses, Rockingham Mall, professional services",
        "court_info": "Rockingham County Superior Court, Salem District Court",
        "economy": "Retail and commercial center near Massachusetts border with no sales tax advantage",
        "proximity_message": "Serving Salem attorneys with vocational evaluations through convenient virtual and in-person consultations"
    },
    {
        "name": "Dover",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "32,741",
        "county": "Strafford County",
        "distance_miles": 115,
        "major_employers": "Wentworth-Douglass Hospital, Liberty Mutual, various technology companies",
        "court_info": "Strafford County Superior Court, Dover District Court",
        "economy": "Historic mill city transformed into healthcare and technology center",
        "proximity_message": "Providing expert vocational services to Dover attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Merrimack",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "26,632",
        "county": "Hillsborough County",
        "distance_miles": 85,
        "major_employers": "Fidelity Investments, PC Connection, Anheuser-Busch",
        "court_info": "Hillsborough County Superior Court South, Merrimack District Court",
        "economy": "Corporate center with major employers and distribution facilities",
        "proximity_message": "Serving Merrimack attorneys with comprehensive vocational assessments through flexible meeting options"
    },
    {
        "name": "Londonderry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "25,826",
        "county": "Rockingham County",
        "distance_miles": 80,
        "major_employers": "Stonyfield Farm, Coca-Cola Bottling, various technology companies",
        "court_info": "Rockingham County Superior Court, Derry District Court",
        "economy": "Growing business community with food production and technology sectors",
        "proximity_message": "Providing vocational evaluations to Londonderry attorneys through virtual and in-person consultations"
    },
    {
        "name": "Keene",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,047",
        "county": "Cheshire County",
        "distance_miles": 95,
        "major_employers": "Cheshire Medical Center, Keene State College, C&S Wholesale Grocers",
        "court_info": "Cheshire County Superior Court, Keene District Court",
        "economy": "Regional center with healthcare, education, and distribution",
        "proximity_message": "Serving Keene attorneys with expert vocational services through virtual consultations and scheduled visits"
    },
    {
        "name": "Bedford",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "23,322",
        "county": "Hillsborough County",
        "distance_miles": 90,
        "major_employers": "various professional services, corporate offices, retail businesses",
        "court_info": "Hillsborough County Superior Court South, Manchester District Court",
        "economy": "Affluent suburban community with professional services and corporate presence",
        "proximity_message": "Providing vocational assessments to Bedford attorneys through convenient consultation arrangements"
    },
    {
        "name": "Portsmouth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "21,956",
        "county": "Rockingham County",
        "distance_miles": 120,
        "major_employers": "Portsmouth Naval Shipyard, Portsmouth Regional Hospital, tourism industry",
        "court_info": "Rockingham County Superior Court, Portsmouth District Court",
        "economy": "Historic seaport with naval facility, healthcare, and vibrant tourism sector",
        "proximity_message": "Serving Portsmouth attorneys with vocational evaluations through virtual consultations and in-person testimony"
    },
    {
        "name": "Goffstown",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "18,577",
        "county": "Hillsborough County",
        "distance_miles": 95,
        "major_employers": "various manufacturing companies, local businesses, Saint Anselm College nearby",
        "court_info": "Hillsborough County Superior Court South, Goffstown District Court",
        "economy": "Small town with manufacturing base and proximity to Manchester employment",
        "proximity_message": "Providing vocational services to Goffstown attorneys through flexible virtual and in-person options"
    },
    {
        "name": "Laconia",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "16,871",
        "county": "Belknap County",
        "distance_miles": 135,
        "major_employers": "Lakes Region General Hospital, various tourism businesses, manufacturing",
        "court_info": "Belknap County Superior Court, Laconia District Court",
        "economy": "Lakes Region center with healthcare, tourism, and light manufacturing",
        "proximity_message": "Serving Laconia attorneys with vocational assessments through virtual consultations and court appearances"
    },
    {
        "name": "Hooksett",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "14,871",
        "county": "Merrimack County",
        "distance_miles": 95,
        "major_employers": "various retail outlets, distribution centers, Bass Pro Shops",
        "court_info": "Merrimack County Superior Court, Hooksett District Court",
        "economy": "Retail and distribution hub along Interstate 93 corridor",
        "proximity_message": "Providing vocational evaluations to Hooksett attorneys through convenient consultation options"
    },
    # Maine cities (excluding Portland which already exists)
    {
        "name": "Lewiston",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "37,121",
        "county": "Androscoggin County",
        "distance_miles": 165,
        "major_employers": "Central Maine Medical Center, Bates College, TD Bank",
        "court_info": "Androscoggin County Superior Court, Lewiston District Court",
        "economy": "Former mill city with healthcare, education, and financial services",
        "proximity_message": "Serving Lewiston attorneys with vocational evaluations through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Bangor",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "31,753",
        "county": "Penobscot County",
        "distance_miles": 250,
        "major_employers": "Northern Light Eastern Maine Medical Center, Husson University, Hollywood Casino",
        "court_info": "Penobscot County Superior Court, Bangor District Court",
        "economy": "Regional healthcare and commercial center for northern and eastern Maine",
        "proximity_message": "Providing comprehensive vocational services to Bangor attorneys through virtual evaluations and scheduled court appearances"
    },
    {
        "name": "South Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "26,498",
        "county": "Cumberland County",
        "distance_miles": 155,
        "major_employers": "Maine Mall area retail, Texas Instruments, various marine businesses",
        "court_info": "Cumberland County Superior Court, South Portland District Court",
        "economy": "Retail center and port city with technology and marine industries",
        "proximity_message": "Serving South Portland attorneys with vocational assessments through virtual consultations and in-person meetings"
    },
    {
        "name": "Auburn",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "24,061",
        "county": "Androscoggin County",
        "distance_miles": 165,
        "major_employers": "Central Maine Medical Center facilities, various manufacturers, retail centers",
        "court_info": "Androscoggin County Superior Court, Auburn District Court",
        "economy": "Twin city with Lewiston featuring manufacturing and retail sectors",
        "proximity_message": "Providing vocational evaluations to Auburn attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Biddeford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "22,552",
        "county": "York County",
        "distance_miles": 140,
        "major_employers": "Southern Maine Health Care, University of New England, various mills",
        "court_info": "York County Superior Court, Biddeford District Court",
        "economy": "Former textile center transitioning to healthcare and education",
        "proximity_message": "Serving Biddeford attorneys with expert vocational services through virtual and in-person consultations"
    },
    {
        "name": "Sanford",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "21,982",
        "county": "York County",
        "distance_miles": 120,
        "major_employers": "various manufacturers, Southern Maine Health Care facilities, retail businesses",
        "court_info": "York County Superior Court, Springvale District Court",
        "economy": "Manufacturing center with diverse industrial base",
        "proximity_message": "Providing vocational assessments to Sanford attorneys through flexible consultation arrangements"
    },
    {
        "name": "Augusta",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "18,899",
        "county": "Kennebec County",
        "distance_miles": 180,
        "major_employers": "State of Maine, MaineGeneral Medical Center, various state agencies",
        "court_info": "Kennebec County Superior Court, Augusta District Court, Maine Supreme Judicial Court",
        "economy": "State capital with government employment and healthcare",
        "proximity_message": "Serving Augusta attorneys with vocational evaluations through virtual consultations and scheduled court appearances"
    },
    {
        "name": "Saco",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,381",
        "county": "York County",
        "distance_miles": 140,
        "major_employers": "various manufacturers, retail businesses, tourism-related services",
        "court_info": "York County Superior Court, Biddeford District Court",
        "economy": "Coastal community with manufacturing and seasonal tourism",
        "proximity_message": "Providing vocational services to Saco attorneys through virtual consultations and in-person options"
    },
    {
        "name": "Westbrook",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "20,400",
        "county": "Cumberland County",
        "distance_miles": 155,
        "major_employers": "IDEXX Laboratories, Spring Harbor Hospital, Sappi Fine Paper",
        "court_info": "Cumberland County Superior Court, Westbrook District Court",
        "economy": "Paper mill heritage with biotechnology and healthcare growth",
        "proximity_message": "Serving Westbrook attorneys with vocational assessments through virtual and in-person consultations"
    },
    {
        "name": "Waterville",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "15,722",
        "county": "Kennebec County",
        "distance_miles": 180,
        "major_employers": "MaineGeneral Medical Center, Colby College, Huhtamaki",
        "court_info": "Kennebec County Superior Court, Waterville District Court",
        "economy": "Healthcare and education center with manufacturing presence",
        "proximity_message": "Providing vocational evaluations to Waterville attorneys through virtual consultations and court testimony"
    },
    {
        "name": "Brunswick",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "21,756",
        "county": "Cumberland County",
        "distance_miles": 165,
        "major_employers": "Bath Iron Works employees, Bowdoin College, Mid Coast Hospital",
        "court_info": "Cumberland County Superior Court, West Bath District Court",
        "economy": "Education and healthcare with proximity to naval shipbuilding",
        "proximity_message": "Serving Brunswick attorneys with expert vocational services through virtual consultations and scheduled visits"
    },
    # Vermont cities (excluding Burlington which already exists)
    {
        "name": "Essex Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "10,761",
        "county": "Chittenden County",
        "distance_miles": 270,
        "major_employers": "GlobalFoundries, various technology companies, retail businesses",
        "court_info": "Chittenden County Superior Court, Vermont District Court",
        "economy": "Technology manufacturing center with semiconductor production",
        "proximity_message": "Providing vocational evaluations to Essex Junction attorneys through virtual consultations and in-person testimony at trial"
    },
    {
        "name": "Rutland",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "15,807",
        "county": "Rutland County",
        "distance_miles": 200,
        "major_employers": "Rutland Regional Medical Center, General Electric, Casella Waste Systems",
        "court_info": "Rutland County Superior Court, Rutland District Court",
        "economy": "Regional center with healthcare, manufacturing, and service industries",
        "proximity_message": "Serving Rutland attorneys with vocational assessments through virtual consultations and scheduled court appearances"
    },
    {
        "name": "St. Albans",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "6,918",
        "county": "Franklin County",
        "distance_miles": 300,
        "major_employers": "Northwestern Medical Center, Mylan Technologies, various agricultural businesses",
        "court_info": "Franklin County Superior Court, St. Albans District Court",
        "economy": "Healthcare and manufacturing with strong agricultural sector",
        "proximity_message": "Providing vocational services to St. Albans attorneys through comprehensive virtual evaluations and court testimony"
    }
]

# Template for Northern New England vocational expert pages
def generate_northern_ne_vocational_page(city):
    filename = f"{city['name'].lower().replace(' ', '-').replace('.', '')}-{city['state_abbr'].lower()}-vocational-expert.html"
    
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
<title>Vocational Expert {city['name']} {city['state_abbr']} | Earning Capacity & Employability | Chris Skerritt</title>
<meta content="Expert vocational evaluation services in {city['name']}, {city['state']}. Court-qualified vocational expert for personal injury, disability, and employment cases. Call 203-605-2814" name="description"/>
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
    "description": "Expert vocational evaluation and earning capacity assessment services for {city['name']}, {city['state']}. Court-qualified vocational expert serving attorneys and individuals in personal injury, disability, and employment matters.",
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
            "name": "What does a vocational expert do in {city['name']}, {city['state_abbr']}?",
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
<p>Our firm has extensive experience providing expert testimony in {city['state']} courts, including:</p>
<ul>
<li>{city['court_info']}</li>
<li>U.S. District Court for the District of {city['state']}</li>
<li>Social Security disability hearings</li>
<li>Workers' compensation proceedings</li>
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
<summary>What does a vocational expert do in {city['name']}, {city['state_abbr']}?</summary>
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

# Generate all Northern New England city pages
for city in northern_ne_cities:
    generate_northern_ne_vocational_page(city)

print(f"\nGenerated {len(northern_ne_cities)} Northern New England vocational expert pages!")
print("\nPages created for:")
for city in northern_ne_cities:
    print(f"- {city['name']}, {city['state_abbr']} ({city['distance_miles']} miles from Smithfield)")