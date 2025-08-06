#!/usr/bin/env python3
"""
Fix the locations page and contact form with professional Bootstrap 5 layout
"""

import os
import shutil

def update_locations_page():
    """Update the locations page with Bootstrap 5 layout"""
    
    locations_content = '''---
layout: default
title: Forensic Economics & Business Valuation Services | All U.S. Locations
meta_description: Find expert forensic economists and business valuation analysts across the United States. Skerritt Economics provides comprehensive economic damage analysis, vocational assessments, and life care planning services throughout all 50 states and Washington DC.
---

<!-- Hero Section with Gradient -->
<section class="hero-section bg-gradient-hero text-white py-5">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-10 mx-auto text-center">
        <h1 class="display-4 mb-4 animate__animated animate__fadeInDown">
          Expert Economic Analysis Nationwide
        </h1>
        <p class="lead mb-4 animate__animated animate__fadeInUp animate__delay-1s">
          Find forensic economists and business valuation experts across all 50 states. 
          Court-tested methodologies with consistent results nationwide.
        </p>
        <div class="hero-search animate__animated animate__fadeInUp animate__delay-2s">
          <div class="input-group input-group-lg mx-auto" style="max-width: 600px;">
            <input type="text" class="form-control" id="locationSearch" placeholder="Search by state or city name..." aria-label="Search locations">
            <button class="btn btn-light" type="button" id="searchBtn">
              <i class="fas fa-search"></i> Search
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Services Overview -->
<section class="py-5">
  <div class="container">
    <h2 class="text-center mb-5">Comprehensive Economic Analysis Services</h2>
    <div class="row g-4">
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm border-0 hover-lift">
          <div class="card-body text-center">
            <div class="mb-3">
              <i class="fas fa-chart-line fa-3x text-primary"></i>
            </div>
            <h4 class="card-title">Forensic Economics</h4>
            <p class="card-text">Economic damage calculations for personal injury, wrongful death, and employment litigation.</p>
            <a href="/services/forensic-economics/" class="btn btn-sm btn-outline-primary">Learn More →</a>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm border-0 hover-lift">
          <div class="card-body text-center">
            <div class="mb-3">
              <i class="fas fa-building fa-3x text-primary"></i>
            </div>
            <h4 class="card-title">Business Valuation</h4>
            <p class="card-text">Expert valuations for litigation support, divorce proceedings, and shareholder disputes.</p>
            <a href="/services/business-valuation/" class="btn btn-sm btn-outline-primary">Learn More →</a>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm border-0 hover-lift">
          <div class="card-body text-center">
            <div class="mb-3">
              <i class="fas fa-briefcase fa-3x text-primary"></i>
            </div>
            <h4 class="card-title">Vocational Assessment</h4>
            <p class="card-text">Comprehensive earning capacity evaluations and vocational rehabilitation planning.</p>
            <a href="/services/vocational-expert/" class="btn btn-sm btn-outline-primary">Learn More →</a>
          </div>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm border-0 hover-lift">
          <div class="card-body text-center">
            <div class="mb-3">
              <i class="fas fa-heartbeat fa-3x text-primary"></i>
            </div>
            <h4 class="card-title">Life Care Planning</h4>
            <p class="card-text">Certified life care planning with detailed future medical care cost projections.</p>
            <a href="/services/life-care-planning/" class="btn btn-sm btn-outline-primary">Learn More →</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- States Section -->
<section class="py-5 bg-light">
  <div class="container">
    <h2 class="text-center mb-5">Select Your State</h2>
    
    <!-- New England States (Featured) -->
    <h3 class="h4 text-primary mb-4">New England (Headquarters Region)</h3>
    <div class="row g-4 mb-5">
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 border-primary">
          <div class="card-header bg-primary text-white">
            <h4 class="mb-0">Massachusetts</h4>
            <small>41 Cities</small>
          </div>
          <div class="card-body">
            <p class="small">Boston, Worcester, Springfield, Cambridge, Lowell, and 36 more cities</p>
            <div class="mb-3">
              <span class="badge bg-success me-1">Forensic Economics</span>
              <span class="badge bg-success me-1">Business Valuation</span>
              <span class="badge bg-success me-1">Vocational Expert</span>
              <span class="badge bg-success">Life Care Planning</span>
            </div>
            <a href="/locations/massachusetts/" class="btn btn-primary btn-sm stretched-link">View All MA Locations →</a>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100 border-warning">
          <div class="card-header bg-warning text-dark">
            <h4 class="mb-0">Rhode Island</h4>
            <small>8 Cities</small>
            <span class="badge bg-danger float-end">HQ</span>
          </div>
          <div class="card-body">
            <p class="small">Providence, Warwick, Cranston, Pawtucket, East Providence, and 3 more</p>
            <div class="mb-3">
              <span class="badge bg-success me-1">All Services</span>
            </div>
            <a href="/locations/rhode-island/" class="btn btn-warning btn-sm stretched-link">View All RI Locations →</a>
          </div>
        </div>
      </div>
      
      <div class="col-md-6 col-lg-4">
        <div class="card h-100">
          <div class="card-header bg-secondary text-white">
            <h4 class="mb-0">Connecticut</h4>
            <small>23 Cities</small>
          </div>
          <div class="card-body">
            <p class="small">Bridgeport, Hartford, Stamford, New Haven, Waterbury, and 18 more</p>
            <div class="mb-3">
              <span class="badge bg-success me-1">All Services</span>
            </div>
            <a href="/locations/connecticut/" class="btn btn-secondary btn-sm stretched-link">View All CT Locations →</a>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Other States in Accordion -->
    <h3 class="h4 text-primary mb-4">All Other States</h3>
    <div class="accordion" id="statesAccordion">
      
      <!-- Mid-Atlantic -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingMidAtlantic">
          <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseMidAtlantic" aria-expanded="true" aria-controls="collapseMidAtlantic">
            <strong>Mid-Atlantic States</strong>
          </button>
        </h2>
        <div id="collapseMidAtlantic" class="accordion-collapse collapse show" aria-labelledby="headingMidAtlantic" data-bs-parent="#statesAccordion">
          <div class="accordion-body">
            <div class="row g-3">
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">New York</h5>
                    <p class="card-text small">New York City, Buffalo, Rochester, Albany</p>
                    <a href="/locations/new-york/" class="btn btn-sm btn-outline-primary">View NY →</a>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">New Jersey</h5>
                    <p class="card-text small">Newark, Jersey City, Paterson, Elizabeth</p>
                    <a href="/locations/new-jersey/" class="btn btn-sm btn-outline-primary">View NJ →</a>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">Pennsylvania</h5>
                    <p class="card-text small">Philadelphia, Pittsburgh, Allentown, Erie</p>
                    <a href="/locations/pennsylvania/" class="btn btn-sm btn-outline-primary">View PA →</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Southeast -->
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingSoutheast">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseSoutheast" aria-expanded="false" aria-controls="collapseSoutheast">
            <strong>Southeast States</strong>
          </button>
        </h2>
        <div id="collapseSoutheast" class="accordion-collapse collapse" aria-labelledby="headingSoutheast" data-bs-parent="#statesAccordion">
          <div class="accordion-body">
            <div class="row g-3">
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">Florida</h5>
                    <p class="card-text small">Miami, Tampa, Orlando, Jacksonville</p>
                    <a href="/locations/florida/" class="btn btn-sm btn-outline-primary">View FL →</a>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">Georgia</h5>
                    <p class="card-text small">Atlanta, Augusta, Columbus, Savannah</p>
                    <a href="/locations/georgia/" class="btn btn-sm btn-outline-primary">View GA →</a>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card">
                  <div class="card-body">
                    <h5 class="card-title">North Carolina</h5>
                    <p class="card-text small">Charlotte, Raleigh, Greensboro, Durham</p>
                    <a href="/locations/north-carolina/" class="btn btn-sm btn-outline-primary">View NC →</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Continue with other regions... -->
    </div>
  </div>
</section>

<!-- Quick Access Cities -->
<section class="py-5">
  <div class="container">
    <h2 class="text-center mb-5">Major Metropolitan Areas</h2>
    <div class="row">
      <div class="col-md-3 mb-4">
        <h5 class="text-primary">Northeast</h5>
        <ul class="list-unstyled">
          <li><a href="/locations/cities/boston-ma-forensic-economist.html">Boston, MA</a></li>
          <li><a href="/locations/cities/new-york-ny-forensic-economist.html">New York, NY</a></li>
          <li><a href="/locations/cities/philadelphia-pa-forensic-economist.html">Philadelphia, PA</a></li>
          <li><a href="/locations/cities/providence-ri-forensic-economist.html">Providence, RI</a></li>
        </ul>
      </div>
      <div class="col-md-3 mb-4">
        <h5 class="text-primary">Southeast</h5>
        <ul class="list-unstyled">
          <li><a href="/locations/cities/atlanta-ga-forensic-economist.html">Atlanta, GA</a></li>
          <li><a href="/locations/cities/miami-fl-forensic-economist.html">Miami, FL</a></li>
          <li><a href="/locations/cities/charlotte-nc-forensic-economist.html">Charlotte, NC</a></li>
          <li><a href="/locations/cities/washington-dc-forensic-economist.html">Washington, DC</a></li>
        </ul>
      </div>
      <div class="col-md-3 mb-4">
        <h5 class="text-primary">Midwest</h5>
        <ul class="list-unstyled">
          <li><a href="/locations/cities/chicago-il-forensic-economist.html">Chicago, IL</a></li>
          <li><a href="/locations/cities/detroit-mi-forensic-economist.html">Detroit, MI</a></li>
          <li><a href="/locations/cities/columbus-oh-forensic-economist.html">Columbus, OH</a></li>
          <li><a href="/locations/cities/minneapolis-mn-forensic-economist.html">Minneapolis, MN</a></li>
        </ul>
      </div>
      <div class="col-md-3 mb-4">
        <h5 class="text-primary">West</h5>
        <ul class="list-unstyled">
          <li><a href="/locations/cities/los-angeles-ca-forensic-economist.html">Los Angeles, CA</a></li>
          <li><a href="/locations/cities/san-francisco-ca-forensic-economist.html">San Francisco, CA</a></li>
          <li><a href="/locations/cities/seattle-wa-forensic-economist.html">Seattle, WA</a></li>
          <li><a href="/locations/cities/denver-co-forensic-economist.html">Denver, CO</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose Section -->
<section class="py-5 bg-light">
  <div class="container">
    <h2 class="text-center mb-5">Why Choose Skerritt Economics</h2>
    <div class="row g-4">
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-map-marked-alt fa-3x text-primary"></i>
          </div>
          <h5>Nationwide Coverage</h5>
          <p>Complete coverage across all 50 states with deep understanding of local economies and courts</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-bolt fa-3x text-primary"></i>
          </div>
          <h5>Rapid Response</h5>
          <p>24-hour initial case evaluation and preliminary damage estimates regardless of location</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-graduation-cap fa-3x text-primary"></i>
          </div>
          <h5>Expert Credentials</h5>
          <p>Multiple professional certifications including CRC, MBA, CLCP, and ABVE/F</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-balance-scale fa-3x text-primary"></i>
          </div>
          <h5>Court Experience</h5>
          <p>Qualified expert witness in federal and state courts throughout the United States</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="cta-section py-5 bg-primary text-white">
  <div class="container text-center">
    <h2 class="mb-4">Need Expert Economic Analysis?</h2>
    <p class="lead mb-4">Contact us today for a free consultation on your case, regardless of location</p>
    <div class="d-flex gap-3 justify-content-center flex-wrap">
      <a href="/contact/" class="btn btn-light btn-lg">Schedule Consultation</a>
      <a href="tel:203-605-2814" class="btn btn-outline-light btn-lg">
        <i class="fas fa-phone"></i> (203) 605-2814
      </a>
    </div>
  </div>
</section>

<!-- JavaScript for Search Functionality -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('locationSearch');
  const searchBtn = document.getElementById('searchBtn');
  
  // Simple search functionality
  function performSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    if (searchTerm.length < 2) return;
    
    // Scroll to states section
    const statesSection = document.querySelector('.accordion');
    if (statesSection) {
      statesSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    // Expand all accordions and highlight matches
    const accordionButtons = document.querySelectorAll('.accordion-button');
    accordionButtons.forEach(btn => {
      const collapse = document.querySelector(btn.getAttribute('data-bs-target'));
      if (collapse && collapse.textContent.toLowerCase().includes(searchTerm)) {
        btn.classList.remove('collapsed');
        collapse.classList.add('show');
      }
    });
  }
  
  searchBtn.addEventListener('click', performSearch);
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      performSearch();
    }
  });
});
</script>
'''
    
    # Write the updated locations page
    with open('locations/index.html', 'w', encoding='utf-8') as f:
        f.write(locations_content)
    
    print("✅ Updated locations/index.html with Bootstrap 5 layout")

def update_contact_page():
    """Update the contact page with improved Bootstrap 5 form layout"""
    
    contact_content = '''---
layout: default
title: Contact Forensic Economist | Free Consultation
meta_description: Contact forensic economist Chris Skerritt. Expert economic analysis for attorneys nationwide. 1 business day response. Free consultation 203-605-2814
---

<!-- Hero Section -->
<section class="hero-section bg-gradient-hero text-white py-5">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-lg-10 mx-auto text-center">
        <h1 class="display-4 mb-4 animate__animated animate__fadeInDown">
          Schedule Your Free Consultation
        </h1>
        <p class="lead mb-4 animate__animated animate__fadeInUp animate__delay-1s">
          Get expert economic analysis for your case. Free consultation with 1 business day response.
        </p>
        <div class="row justify-content-center animate__animated animate__fadeInUp animate__delay-2s">
          <div class="col-auto">
            <div class="d-flex align-items-center text-white">
              <i class="fas fa-check-circle me-2"></i> No Cost Consultation
            </div>
          </div>
          <div class="col-auto">
            <div class="d-flex align-items-center text-white">
              <i class="fas fa-check-circle me-2"></i> 1 Business Day Response
            </div>
          </div>
          <div class="col-auto">
            <div class="d-flex align-items-center text-white">
              <i class="fas fa-check-circle me-2"></i> No Obligation
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Contact Form Section -->
<section class="py-5">
  <div class="container">
    <div class="row g-5">
      <!-- Contact Form -->
      <div class="col-lg-8">
        <div class="card shadow-sm">
          <div class="card-body p-4 p-lg-5">
            <h2 class="mb-4">Request Your Free Case Assessment</h2>
            <p class="text-muted mb-4">Tell us about your case and we'll respond within 1 business day with a preliminary assessment.</p>
            
            <form action="https://formspree.io/f/mnnvgzgd" method="POST" id="contactForm" class="needs-validation" novalidate>
              <!-- Hidden fields -->
              <input type="hidden" name="_subject" value="New Case Consultation Request">
              <input type="hidden" name="_next" value="https://skerritteconomics.com/contact/thank-you/">
              <input type="hidden" name="_cc" value="chris@skerritteconomics.com">
              
              <div class="row g-3">
                <!-- Name and Email -->
                <div class="col-md-6">
                  <label for="name" class="form-label">Full Name *</label>
                  <input type="text" class="form-control" id="name" name="name" required>
                  <div class="invalid-feedback">Please provide your name.</div>
                </div>
                <div class="col-md-6">
                  <label for="email" class="form-label">Email Address *</label>
                  <input type="email" class="form-control" id="email" name="email" required>
                  <div class="invalid-feedback">Please provide a valid email.</div>
                </div>
                
                <!-- Phone and Firm -->
                <div class="col-md-6">
                  <label for="phone" class="form-label">Phone Number</label>
                  <input type="tel" class="form-control" id="phone" name="phone">
                </div>
                <div class="col-md-6">
                  <label for="firm" class="form-label">Law Firm / Organization</label>
                  <input type="text" class="form-control" id="firm" name="firm">
                </div>
                
                <!-- Case Type and Jurisdiction -->
                <div class="col-md-6">
                  <label for="case-type" class="form-label">Case Type *</label>
                  <select class="form-select" id="case-type" name="case-type" required>
                    <option value="">Select Case Type</option>
                    <option value="personal-injury">Personal Injury</option>
                    <option value="wrongful-death">Wrongful Death</option>
                    <option value="medical-malpractice">Medical Malpractice</option>
                    <option value="employment">Employment Litigation</option>
                    <option value="commercial-disputes">Commercial/Shareholder Disputes</option>
                    <option value="business-valuation">Business Valuation</option>
                    <option value="other">Other</option>
                  </select>
                  <div class="invalid-feedback">Please select a case type.</div>
                </div>
                <div class="col-md-6">
                  <label for="jurisdiction" class="form-label">Jurisdiction</label>
                  <select class="form-select" id="jurisdiction" name="jurisdiction">
                    <option value="">Select Jurisdiction</option>
                    <optgroup label="New England">
                      <option value="connecticut">Connecticut</option>
                      <option value="maine">Maine</option>
                      <option value="massachusetts">Massachusetts</option>
                      <option value="new-hampshire">New Hampshire</option>
                      <option value="rhode-island">Rhode Island</option>
                      <option value="vermont">Vermont</option>
                    </optgroup>
                    <optgroup label="Other States">
                      <option value="alabama">Alabama</option>
                      <option value="alaska">Alaska</option>
                      <option value="arizona">Arizona</option>
                      <option value="arkansas">Arkansas</option>
                      <option value="california">California</option>
                      <option value="colorado">Colorado</option>
                      <option value="delaware">Delaware</option>
                      <option value="florida">Florida</option>
                      <option value="georgia">Georgia</option>
                      <option value="hawaii">Hawaii</option>
                      <option value="idaho">Idaho</option>
                      <option value="illinois">Illinois</option>
                      <option value="indiana">Indiana</option>
                      <option value="iowa">Iowa</option>
                      <option value="kansas">Kansas</option>
                      <option value="kentucky">Kentucky</option>
                      <option value="louisiana">Louisiana</option>
                      <option value="maryland">Maryland</option>
                      <option value="michigan">Michigan</option>
                      <option value="minnesota">Minnesota</option>
                      <option value="mississippi">Mississippi</option>
                      <option value="missouri">Missouri</option>
                      <option value="montana">Montana</option>
                      <option value="nebraska">Nebraska</option>
                      <option value="nevada">Nevada</option>
                      <option value="new-jersey">New Jersey</option>
                      <option value="new-mexico">New Mexico</option>
                      <option value="new-york">New York</option>
                      <option value="north-carolina">North Carolina</option>
                      <option value="north-dakota">North Dakota</option>
                      <option value="ohio">Ohio</option>
                      <option value="oklahoma">Oklahoma</option>
                      <option value="oregon">Oregon</option>
                      <option value="pennsylvania">Pennsylvania</option>
                      <option value="south-carolina">South Carolina</option>
                      <option value="south-dakota">South Dakota</option>
                      <option value="tennessee">Tennessee</option>
                      <option value="texas">Texas</option>
                      <option value="utah">Utah</option>
                      <option value="virginia">Virginia</option>
                      <option value="washington">Washington</option>
                      <option value="west-virginia">West Virginia</option>
                      <option value="wisconsin">Wisconsin</option>
                      <option value="wyoming">Wyoming</option>
                    </optgroup>
                    <optgroup label="Federal">
                      <option value="washington-dc">Washington D.C.</option>
                      <option value="federal">Federal Court</option>
                    </optgroup>
                  </select>
                </div>
                
                <!-- Timeline -->
                <div class="col-12">
                  <label for="timeline" class="form-label">Timeline for Analysis</label>
                  <select class="form-select" id="timeline" name="timeline">
                    <option value="">Select Timeline</option>
                    <option value="immediate">Immediate (Rush)</option>
                    <option value="1-2-weeks">1-2 Weeks</option>
                    <option value="3-4-weeks">3-4 Weeks</option>
                    <option value="flexible">Flexible</option>
                  </select>
                </div>
                
                <!-- Message -->
                <div class="col-12">
                  <label for="message" class="form-label">Case Details *</label>
                  <textarea class="form-control" id="message" name="message" rows="5" 
                    placeholder="Briefly describe your case and the economic analysis needed." required></textarea>
                  <div class="invalid-feedback">Please provide case details.</div>
                </div>
              </div>
              
              <!-- What Happens Next -->
              <div class="alert alert-info mt-4">
                <h5 class="alert-heading"><i class="fas fa-info-circle"></i> What happens next?</h5>
                <ul class="mb-0">
                  <li>We'll review your case details within 1 business day</li>
                  <li>You'll receive a preliminary assessment via email or phone</li>
                  <li>We'll discuss timeline, scope, and next steps</li>
                  <li>No commitment required - consultation is completely free</li>
                </ul>
              </div>
              
              <!-- Submit Button -->
              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary btn-lg">
                  Get Free Case Assessment <i class="fas fa-arrow-right ms-2"></i>
                </button>
              </div>
              
              <p class="text-center text-muted small mt-3">
                <i class="fas fa-lock"></i> Your information is secure and confidential. We never share client details.
              </p>
            </form>
          </div>
        </div>
      </div>
      
      <!-- Contact Information Sidebar -->
      <div class="col-lg-4">
        <!-- Contact Card -->
        <div class="card shadow-sm mb-4">
          <div class="card-body">
            <h3 class="h4 mb-4">Direct Contact</h3>
            
            <div class="mb-4">
              <h5 class="h6 text-primary mb-1">Christopher Skerritt</h5>
              <p class="small text-muted mb-0">M.Ed, MBA, CRC, CLCP</p>
              <p class="small text-muted">Principal Economic Consultant</p>
            </div>
            
            <div class="d-flex align-items-start mb-3">
              <i class="fas fa-phone text-primary me-3 mt-1"></i>
              <div>
                <h6 class="mb-1">Phone</h6>
                <a href="tel:203-605-2814" class="text-decoration-none">(203) 605-2814</a>
                <p class="small text-muted mb-0">Available 8 AM - 6 PM ET</p>
              </div>
            </div>
            
            <div class="d-flex align-items-start mb-3">
              <i class="fas fa-envelope text-primary me-3 mt-1"></i>
              <div>
                <h6 class="mb-1">Email</h6>
                <a href="mailto:chris@skerritteconomics.com" class="text-decoration-none">chris@skerritteconomics.com</a>
                <p class="small text-muted mb-0">Response within 1 business day</p>
              </div>
            </div>
            
            <div class="d-flex align-items-start">
              <i class="fas fa-map-marker-alt text-primary me-3 mt-1"></i>
              <div>
                <h6 class="mb-1">Office</h6>
                <address class="small mb-0">
                  400 Putnam Pike Ste J<br>
                  Smithfield, RI 02917<br>
                  <em>Serving all 50 states</em>
                </address>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Response Times Card -->
        <div class="card shadow-sm mb-4">
          <div class="card-body">
            <h4 class="h5 mb-3">Response Times</h4>
            <ul class="list-unstyled mb-0">
              <li class="mb-2">
                <i class="fas fa-clock text-primary me-2"></i>
                <strong>Initial Response:</strong> 1 business day
              </li>
              <li class="mb-2">
                <i class="fas fa-chart-line text-primary me-2"></i>
                <strong>Preliminary Assessment:</strong> 3-5 days
              </li>
              <li class="mb-2">
                <i class="fas fa-file-alt text-primary me-2"></i>
                <strong>Full Report:</strong> 2-3 weeks
              </li>
              <li>
                <i class="fas fa-gavel text-primary me-2"></i>
                <strong>Expert Testimony:</strong> Available
              </li>
            </ul>
          </div>
        </div>
        
        <!-- Credentials Card -->
        <div class="card shadow-sm">
          <div class="card-body">
            <h4 class="h5 mb-3">Professional Credentials</h4>
            <div class="row g-2">
              <div class="col-6">
                <div class="text-center p-2 bg-light rounded">
                  <i class="fas fa-certificate text-primary mb-1"></i>
                  <p class="small mb-0">CRC</p>
                </div>
              </div>
              <div class="col-6">
                <div class="text-center p-2 bg-light rounded">
                  <i class="fas fa-certificate text-primary mb-1"></i>
                  <p class="small mb-0">CLCP</p>
                </div>
              </div>
              <div class="col-6">
                <div class="text-center p-2 bg-light rounded">
                  <i class="fas fa-graduation-cap text-primary mb-1"></i>
                  <p class="small mb-0">M.Ed</p>
                </div>
              </div>
              <div class="col-6">
                <div class="text-center p-2 bg-light rounded">
                  <i class="fas fa-graduation-cap text-primary mb-1"></i>
                  <p class="small mb-0">MBA</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose Section -->
<section class="py-5 bg-light">
  <div class="container">
    <h2 class="text-center mb-5">Why Choose Skerritt Economics?</h2>
    <div class="row g-4">
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-bolt fa-3x text-primary"></i>
          </div>
          <h5>Rapid Response</h5>
          <p>1 business day response guarantee with preliminary assessments in 3-5 days</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-chart-line fa-3x text-primary"></i>
          </div>
          <h5>Court-Tested</h5>
          <p>Extensive experience in state and federal courts nationwide</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-comments fa-3x text-primary"></i>
          </div>
          <h5>Clear Reports</h5>
          <p>Reports designed for judges and juries to understand</p>
        </div>
      </div>
      <div class="col-md-6 col-lg-3">
        <div class="text-center">
          <div class="mb-3">
            <i class="fas fa-calculator fa-3x text-primary"></i>
          </div>
          <h5>Comprehensive</h5>
          <p>Full economic damages including lost earnings and life care costs</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ Section -->
<section class="py-5">
  <div class="container">
    <h2 class="text-center mb-5">Frequently Asked Questions</h2>
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <div class="accordion" id="faqAccordion">
          <div class="accordion-item">
            <h3 class="accordion-header" id="faq1">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1" aria-expanded="true" aria-controls="collapse1">
                How quickly can I schedule a free consultation?
              </button>
            </h3>
            <div id="collapse1" class="accordion-collapse collapse show" aria-labelledby="faq1" data-bs-parent="#faqAccordion">
              <div class="accordion-body">
                We guarantee a response within 1 business day of your initial contact. Most free consultations are scheduled within 2-3 business days, though we can accommodate urgent matters when needed.
              </div>
            </div>
          </div>
          
          <div class="accordion-item">
            <h3 class="accordion-header" id="faq2">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2" aria-expanded="false" aria-controls="collapse2">
                What information should I prepare before contacting you?
              </button>
            </h3>
            <div id="collapse2" class="accordion-collapse collapse" aria-labelledby="faq2" data-bs-parent="#faqAccordion">
              <div class="accordion-body">
                For your free consultation, helpful information includes: case type and jurisdiction, relevant dates (injury, termination, or incident), basic demographic information about the plaintiff, preliminary medical prognosis or employment history, and any specific economic questions you need addressed. However, we can begin discussions with minimal information.
              </div>
            </div>
          </div>
          
          <div class="accordion-item">
            <h3 class="accordion-header" id="faq3">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3" aria-expanded="false" aria-controls="collapse3">
                Do you provide services outside of Rhode Island?
              </button>
            </h3>
            <div id="collapse3" class="accordion-collapse collapse" aria-labelledby="faq3" data-bs-parent="#faqAccordion">
              <div class="accordion-body">
                Yes! While we're based in Smithfield, Rhode Island, we serve attorneys throughout all 50 states. We regularly provide deposition and trial testimony in state and federal courts nationwide.
              </div>
            </div>
          </div>
          
          <div class="accordion-item">
            <h3 class="accordion-header" id="faq4">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4" aria-expanded="false" aria-controls="collapse4">
                Can you work with tight deadlines?
              </button>
            </h3>
            <div id="collapse4" class="accordion-collapse collapse" aria-labelledby="faq4" data-bs-parent="#faqAccordion">
              <div class="accordion-body">
                Absolutely. We understand litigation deadlines and maintain capacity for urgent cases. Rush services are available for preliminary reports, rebuttal analyses, and court testimony. When you contact us, please indicate your timeline so we can prioritize accordingly.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA -->
<section class="py-5 bg-primary text-white">
  <div class="container text-center">
    <h2 class="mb-4">Ready to Discuss Your Case?</h2>
    <p class="lead mb-4">Schedule your free consultation today. We'll respond within 1 business day.</p>
    <div class="d-flex gap-3 justify-content-center flex-wrap">
      <a href="#contactForm" class="btn btn-light btn-lg">Request Consultation</a>
      <a href="tel:203-605-2814" class="btn btn-outline-light btn-lg">
        <i class="fas fa-phone"></i> Call (203) 605-2814
      </a>
    </div>
  </div>
</section>

<!-- Form Validation Script -->
<script>
// Bootstrap form validation
(function() {
  'use strict'
  
  // Fetch all forms with validation
  var forms = document.querySelectorAll('.needs-validation')
  
  // Loop and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function(form) {
      form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        
        form.classList.add('was-validated')
      }, false)
    })
})()

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});
</script>
'''
    
    # Write the updated contact page
    with open('contact/index.html', 'w', encoding='utf-8') as f:
        f.write(contact_content)
    
    print("✅ Updated contact/index.html with professional Bootstrap 5 form layout")

def main():
    # Create backups first
    if os.path.exists('locations/index.html'):
        shutil.copy2('locations/index.html', 'locations/index.html.pre-ui-backup')
    
    if os.path.exists('contact/index.html'):
        shutil.copy2('contact/index.html', 'contact/index.html.pre-ui-backup')
    
    # Update both pages
    update_locations_page()
    update_contact_page()
    
    print("\n✅ Both pages have been updated with professional Bootstrap 5 layouts!")
    print("\nThe pages now feature:")
    print("  • Blue gradient hero sections with white text")
    print("  • Professional Bootstrap 5 components")
    print("  • Improved form layout with validation")
    print("  • Responsive design for all devices")
    print("  • Font Awesome icons")
    print("  • Smooth animations")
    
    print("\nReview the updated pages at:")
    print("  • http://localhost:8888/locations/")
    print("  • http://localhost:8888/contact/")

if __name__ == "__main__":
    main()