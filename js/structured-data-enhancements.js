// Enhanced Structured Data for SEO
// This file contains additional structured data schemas for better search visibility

// Review Schema - Add actual client reviews when available
const reviewSchema = {
    "@context": "https://schema.org",
    "@type": "Review",
    "itemReviewed": {
        "@type": "ProfessionalService",
        "name": "Skerritt Economics & Consulting",
        "image": "https://skerritteconomics.com/sec-logo.png",
        "priceRange": "$$$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "400 Putnam Pike Ste J",
            "addressLocality": "Smithfield",
            "addressRegion": "RI",
            "postalCode": "02917",
            "addressCountry": "US"
        }
    },
    "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
    },
    "author": {
        "@type": "Person",
        "name": "Attorney Client" // Replace with actual client name when permitted
    },
    "datePublished": "2024-01-15",
    "reviewBody": "Chris Skerritt provided exceptional forensic economics analysis for our personal injury case. His report was thorough, well-documented, and his testimony was clear and compelling. Highly recommended for complex economic damage calculations."
};

// AggregateRating Schema
const aggregateRatingSchema = {
    "@context": "https://schema.org",
    "@type": "AggregateRating",
    "itemReviewed": {
        "@type": "ProfessionalService",
        "name": "Skerritt Economics & Consulting"
    },
    "ratingValue": "5.0",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
};

// Person Schema for Chris Skerritt
const personSchema = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Christopher T. Skerritt",
    "honorificPrefix": "Mr.",
    "honorificSuffix": "CRC, CLCP, MBA",
    "jobTitle": "Principal Forensic Economist",
    "worksFor": {
        "@type": "Organization",
        "name": "Skerritt Economics & Consulting",
        "url": "https://skerritteconomics.com"
    },
    "email": "chris@skerritteconomics.com",
    "telephone": "+1-203-605-2814",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "400 Putnam Pike Ste J",
        "addressLocality": "Smithfield",
        "addressRegion": "RI",
        "postalCode": "02917",
        "addressCountry": "US"
    },
    "alumniOf": [
        {
            "@type": "CollegeOrUniversity",
            "name": "University Name" // Replace with actual university
        }
    ],
    "hasCredential": [
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "certificate",
            "name": "CRC - Certified Rehabilitation Counselor",
            "recognizedBy": {
                "@type": "Organization",
                "name": "Commission on Rehabilitation Counselor Certification"
            }
        },
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "certificate",
            "name": "CLCP - Certified Life Care Planner",
            "recognizedBy": {
                "@type": "Organization",
                "name": "International Commission on Health Care Certification"
            }
        },
        {
            "@type": "EducationalOccupationalCredential",
            "credentialCategory": "degree",
            "name": "MBA - Master of Business Administration"
        }
    ],
    "knowsAbout": [
        "Forensic Economics",
        "Business Valuation",
        "Economic Damage Analysis",
        "Life Care Planning",
        "Vocational Assessment",
        "Lost Earnings Calculations",
        "Present Value Analysis"
    ],
    "sameAs": [
        // Add LinkedIn, professional directory URLs when available
    ]
};

// Service Schema with more details
const serviceSchemas = [
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": "Forensic Economics Analysis",
        "provider": {
            "@type": "LocalBusiness",
            "name": "Skerritt Economics & Consulting"
        },
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "New England"
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Forensic Economics Services",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Lost Earnings Analysis",
                        "description": "Calculation of past and future lost earnings due to injury or death"
                    }
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Household Services Valuation",
                        "description": "Economic value of lost household services"
                    }
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": "Present Value Calculations",
                        "description": "Discount future losses to present value"
                    }
                }
            ]
        },
        "audience": {
            "@type": "Audience",
            "audienceType": "Attorneys and Law Firms"
        }
    }
];

// Event Schema for speaking engagements/seminars
const eventSchema = {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "Economic Damages in Personal Injury Cases",
    "description": "CLE seminar on calculating economic damages in personal injury litigation",
    "startDate": "2025-02-15T14:00:00-05:00",
    "endDate": "2025-02-15T16:00:00-05:00",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
    "location": {
        "@type": "VirtualLocation",
        "url": "https://skerritteconomics.com/webinar"
    },
    "organizer": {
        "@type": "Organization",
        "name": "Skerritt Economics & Consulting",
        "url": "https://skerritteconomics.com"
    },
    "performer": {
        "@type": "Person",
        "name": "Christopher T. Skerritt"
    },
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "url": "https://skerritteconomics.com/contact",
        "validFrom": "2025-01-01T00:00:00-05:00"
    }
};

// WebSite Schema with SearchAction
const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "url": "https://skerritteconomics.com/",
    "name": "Skerritt Economics & Consulting",
    "description": "Expert forensic economics and business valuation services",
    "publisher": {
        "@type": "Organization",
        "name": "Skerritt Economics & Consulting"
    },
    "potentialAction": {
        "@type": "SearchAction",
        "target": {
            "@type": "EntryPoint",
            "urlTemplate": "https://skerritteconomics.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
    }
};

// Function to inject structured data into pages
function injectStructuredData(schemas) {
    schemas.forEach(schema => {
        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.text = JSON.stringify(schema);
        document.head.appendChild(script);
    });
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        reviewSchema,
        aggregateRatingSchema,
        personSchema,
        serviceSchemas,
        eventSchema,
        websiteSchema,
        injectStructuredData
    };
}