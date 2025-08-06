#!/usr/bin/env python3
"""
Fix locations and contact pages to use modern Bootstrap 5 layout
"""

import os
import re
from pathlib import Path

def update_locations_page():
    """Update the locations page with modern Bootstrap 5 layout"""
    
    locations_path = "locations/index.html"
    
    # New content for locations page
    new_content = """---
layout: modern-default
title: Forensic Economics & Business Valuation Services | All U.S. Locations
meta_description: Find expert forensic economists and business valuation analysts across the United States. Skerritt Economics provides comprehensive economic damage analysis, vocational assessments, and life care planning services throughout all 50 states and Washington DC.
---

<main id="main-content" tabindex="-1">
  <!-- Hero Section -->
  <section class="hero-section bg-gradient-primary">
    <div class="container">
      <div class="row align-items-center min-vh-50">
        <div class="col-lg-8 mx-auto text-center text-white">
          <h1 class="display-4 fw-bold mb-4">Expert Economic Services Nationwide</h1>
          <p class="lead mb-5">Find forensic economists, business valuation analysts, and expert witnesses across all 50 states. Trusted by attorneys nationwide for accurate economic damage calculations.</p>
          <div class="d-flex gap-3 justify-content-center flex-wrap">
            <a href="#states-section" class="btn btn-light btn-lg px-4">Find Your State</a>
            <a href="/contact/" class="btn btn-outline-light btn-lg px-4">Get Consultation</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Services Overview -->
  <section class="py-5 bg-light">
    <div class="container">
      <h2 class="text-center mb-5">Comprehensive Economic Analysis Services</h2>
      <p class="lead text-center mb-5 text-muted">Skerritt Economics & Consulting provides expert forensic economics and business valuation services to attorneys, businesses, and government agencies throughout all 50 states and Washington DC.</p>
      
      <div class="row g-4">
        <div class="col-md-6 col-lg-3">
          <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-body text-center">
              <div class="feature-icon bg-primary bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                <i class="fas fa-chart-line text-white fa-2x"></i>
              </div>
              <h3 class="h5">Forensic Economics</h3>
              <p class="text-muted">Economic damage calculations for personal injury, wrongful death, and employment litigation.</p>
              <a href="/services/forensic-economics/" class="btn btn-sm btn-outline-primary">Learn More →</a>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-body text-center">
              <div class="feature-icon bg-success bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                <i class="fas fa-building text-white fa-2x"></i>
              </div>
              <h3 class="h5">Business Valuation</h3>
              <p class="text-muted">Expert business valuations for litigation support, divorce proceedings, and disputes.</p>
              <a href="/services/business-valuation/" class="btn btn-sm btn-outline-success">Learn More →</a>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-body text-center">
              <div class="feature-icon bg-info bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                <i class="fas fa-user-tie text-white fa-2x"></i>
              </div>
              <h3 class="h5">Vocational Assessment</h3>
              <p class="text-muted">Comprehensive earning capacity evaluations and vocational rehabilitation planning.</p>
              <a href="/services/vocational-expert/" class="btn btn-sm btn-outline-info">Learn More →</a>
            </div>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-body text-center">
              <div class="feature-icon bg-warning bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                <i class="fas fa-heart text-white fa-2x"></i>
              </div>
              <h3 class="h5">Life Care Planning</h3>
              <p class="text-muted">Certified life care planning services for catastrophic injury cases.</p>
              <a href="/services/life-care-planning/" class="btn btn-sm btn-outline-warning">Learn More →</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Location Search -->
  <section class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 mx-auto text-center">
          <h2 class="mb-4">Find Services in Your Area</h2>
          <div class="input-group input-group-lg mb-4">
            <span class="input-group-text bg-primary text-white">
              <i class="fas fa-search"></i>
            </span>
            <input type="text" id="locationSearch" class="form-control" placeholder="Search by state or city name..." aria-label="Search for services by state or city name">
            <button class="btn btn-primary" type="button" id="clearSearch" style="display: none;">Clear</button>
          </div>
          <p class="text-muted">Start typing to filter locations below</p>
        </div>
      </div>
    </div>
  </section>

  <!-- States Grid -->
  <section class="py-5 bg-light" id="states-section">
    <div class="container">
      <h2 class="text-center mb-5">Select Your State</h2>
      
      <!-- New England States -->
      <h3 class="h4 mb-4 text-primary">New England</h3>
      <div class="row g-4 mb-5" id="newEnglandStates">
        <!-- Massachusetts -->
        <div class="col-lg-4 col-md-6" data-state="Massachusetts">
          <div class="card h-100 border-primary shadow-sm hover-shadow transition">
            <div class="card-header bg-primary text-white">
              <h4 class="h5 mb-0 d-flex justify-content-between align-items-center">
                <a href="massachusetts.html" class="text-white text-decoration-none">Massachusetts</a>
                <span class="badge bg-light text-primary">41 Cities</span>
              </h4>
            </div>
            <div class="card-body">
              <p class="text-muted small mb-3">Boston, Worcester, Springfield, Cambridge, Lowell, New Bedford, Quincy, Lynn, Fall River, Newton, and 31 more cities</p>
              <div class="d-flex flex-wrap gap-1 mb-3">
                <span class="badge bg-primary bg-opacity-10 text-primary">Forensic Economics</span>
                <span class="badge bg-success bg-opacity-10 text-success">Business Valuation</span>
                <span class="badge bg-info bg-opacity-10 text-info">Vocational Expert</span>
                <span class="badge bg-warning bg-opacity-10 text-warning">Life Care Planning</span>
              </div>
              <a href="massachusetts.html" class="btn btn-primary btn-sm w-100">View All Massachusetts Locations →</a>
            </div>
          </div>
        </div>

        <!-- Connecticut -->
        <div class="col-lg-4 col-md-6" data-state="Connecticut">
          <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-header bg-gradient-primary text-white">
              <h4 class="h5 mb-0 d-flex justify-content-between align-items-center">
                <a href="connecticut.html" class="text-white text-decoration-none">Connecticut</a>
                <span class="badge bg-light text-primary">23 Cities</span>
              </h4>
            </div>
            <div class="card-body">
              <p class="text-muted small mb-3">Bridgeport, Hartford, Stamford, New Haven, Waterbury, Norwalk, Danbury, New Britain, Bristol, Meriden, and 13 more cities</p>
              <div class="d-flex flex-wrap gap-1 mb-3">
                <span class="badge bg-primary bg-opacity-10 text-primary">Forensic Economics</span>
                <span class="badge bg-success bg-opacity-10 text-success">Business Valuation</span>
                <span class="badge bg-info bg-opacity-10 text-info">Vocational Expert</span>
                <span class="badge bg-warning bg-opacity-10 text-warning">Life Care Planning</span>
              </div>
              <a href="connecticut.html" class="btn btn-outline-primary btn-sm w-100">View All Connecticut Locations →</a>
            </div>
          </div>
        </div>

        <!-- Rhode Island -->
        <div class="col-lg-4 col-md-6" data-state="Rhode Island">
          <div class="card h-100 border-success shadow hover-shadow transition">
            <div class="card-header bg-success text-white position-relative">
              <h4 class="h5 mb-0 d-flex justify-content-between align-items-center">
                <a href="rhode-island.html" class="text-white text-decoration-none">Rhode Island</a>
                <div>
                  <span class="badge bg-light text-success">8 Cities</span>
                  <span class="badge bg-warning text-dark ms-1">HQ</span>
                </div>
              </h4>
            </div>
            <div class="card-body">
              <p class="text-muted small mb-3">Providence, Warwick, Cranston, Pawtucket, East Providence, Woonsocket, Newport, and Westerly</p>
              <div class="d-flex flex-wrap gap-1 mb-3">
                <span class="badge bg-primary bg-opacity-10 text-primary">Forensic Economics</span>
                <span class="badge bg-success bg-opacity-10 text-success">Business Valuation</span>
                <span class="badge bg-info bg-opacity-10 text-info">Vocational Expert</span>
                <span class="badge bg-warning bg-opacity-10 text-warning">Life Care Planning</span>
              </div>
              <a href="rhode-island.html" class="btn btn-success btn-sm w-100">View All Rhode Island Locations →</a>
            </div>
          </div>
        </div>

        <!-- Continue with other New England states... -->
      </div>

      <!-- Accordion for Other Regions -->
      <div class="accordion" id="statesAccordion">
        <!-- Mid-Atlantic States -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#midAtlantic" aria-expanded="true" aria-controls="midAtlantic">
              <i class="fas fa-map-marker-alt me-2"></i> Mid-Atlantic States
            </button>
          </h2>
          <div id="midAtlantic" class="accordion-collapse collapse show" data-bs-parent="#statesAccordion">
            <div class="accordion-body">
              <div class="row g-3">
                <div class="col-md-4">
                  <div class="card">
                    <div class="card-body">
                      <h5 class="card-title"><a href="new-york.html">New York</a></h5>
                      <p class="card-text small">New York City, Buffalo, Rochester, Albany, Syracuse</p>
                      <a href="new-york.html" class="btn btn-sm btn-outline-primary">View New York →</a>
                    </div>
                  </div>
                </div>
                <!-- Continue with other Mid-Atlantic states... -->
              </div>
            </div>
          </div>
        </div>

        <!-- Southeast States -->
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#southeast" aria-expanded="false" aria-controls="southeast">
              <i class="fas fa-map-marker-alt me-2"></i> Southeast States
            </button>
          </h2>
          <div id="southeast" class="accordion-collapse collapse" data-bs-parent="#statesAccordion">
            <div class="accordion-body">
              <div class="row g-3">
                <div class="col-md-4">
                  <div class="card">
                    <div class="card-body">
                      <h5 class="card-title"><a href="virginia.html">Virginia</a></h5>
                      <p class="card-text small">Virginia Beach, Norfolk, Richmond, Arlington, Newport News</p>
                      <a href="virginia.html" class="btn btn-sm btn-outline-primary">View Virginia →</a>
                    </div>
                  </div>
                </div>
                <!-- Continue with other Southeast states... -->
              </div>
            </div>
          </div>
        </div>

        <!-- Continue with other regions... -->
      </div>
    </div>
  </section>

  <!-- Major Cities Quick Access -->
  <section class="py-5">
    <div class="container">
      <h2 class="text-center mb-5">Major Metropolitan Areas</h2>
      <div class="row g-4">
        <div class="col-lg-3 col-md-6">
          <div class="card bg-light">
            <div class="card-header bg-primary text-white">
              <h5 class="mb-0">Massachusetts</h5>
            </div>
            <div class="list-group list-group-flush">
              <a href="cities/boston-ma-forensic-economist.html" class="list-group-item list-group-item-action">Boston</a>
              <a href="cities/worcester-ma-forensic-economist.html" class="list-group-item list-group-item-action">Worcester</a>
              <a href="cities/springfield-ma-forensic-economist.html" class="list-group-item list-group-item-action">Springfield</a>
              <a href="cities/cambridge-ma-forensic-economist.html" class="list-group-item list-group-item-action">Cambridge</a>
            </div>
          </div>
        </div>
        <!-- Continue with other major cities... -->
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
            <div class="feature-icon bg-primary bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-check text-white fa-2x"></i>
            </div>
            <h3 class="h5">Nationwide Coverage</h3>
            <p class="text-muted">Complete coverage across all 50 states with deep understanding of local economies and courts</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-success bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-bolt text-white fa-2x"></i>
            </div>
            <h3 class="h5">Rapid Response</h3>
            <p class="text-muted">24-hour initial case evaluation and preliminary damage estimates regardless of location</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-info bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-graduation-cap text-white fa-2x"></i>
            </div>
            <h3 class="h5">Expert Credentials</h3>
            <p class="text-muted">Multiple professional certifications including CRC, MBA, CLCP, and ABVE/F</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-warning bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-balance-scale text-white fa-2x"></i>
            </div>
            <h3 class="h5">Court Experience</h3>
            <p class="text-muted">Qualified expert witness in federal and state courts throughout the United States</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="py-5 bg-gradient-primary text-white">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-8">
          <h2 class="mb-3">Need Expert Economic Analysis?</h2>
          <p class="lead mb-4 mb-lg-0">Contact us today for a free consultation on your case, regardless of location</p>
        </div>
        <div class="col-lg-4 text-lg-end">
          <a href="/contact/" class="btn btn-light btn-lg me-2 mb-2">Schedule Consultation</a>
          <a href="tel:203-605-2814" class="btn btn-outline-light btn-lg mb-2">Call (203) 605-2814</a>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- Location Search JavaScript -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('locationSearch');
  const clearButton = document.getElementById('clearSearch');
  const stateCards = document.querySelectorAll('[data-state]');

  searchInput.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    clearButton.style.display = searchTerm ? 'block' : 'none';
    
    stateCards.forEach(card => {
      const state = card.getAttribute('data-state').toLowerCase();
      const content = card.textContent.toLowerCase();
      
      if (content.includes(searchTerm)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });

  clearButton.addEventListener('click', function() {
    searchInput.value = '';
    clearButton.style.display = 'none';
    stateCards.forEach(card => {
      card.style.display = '';
    });
  });
});
</script>
"""
    
    # Write the updated file
    with open(locations_path, 'w') as f:
        f.write(new_content)
    
    print(f"✅ Updated locations page with modern Bootstrap 5 layout")

def update_contact_page():
    """Enhance the contact page with better Bootstrap 5 styling"""
    
    contact_path = "contact/index.html"
    
    # Read the current file to preserve form structure
    with open(contact_path, 'r') as f:
        current_content = f.read()
    
    # Extract the form action URL
    form_action_match = re.search(r'action="([^"]+)"', current_content)
    form_action = form_action_match.group(1) if form_action_match else "https://formspree.io/f/mnnvgzgd"
    
    # New enhanced content for contact page
    new_content = f"""---
layout: modern-default
title: Contact Forensic Economist | Free Consultation
meta_description: Contact forensic economist Chris Skerritt. Expert economic analysis for New England attorneys. 1 business day response. Free consultation 203-605-2814
---

<main id="main-content" tabindex="-1">
  <!-- Hero Section -->
  <section class="hero-section bg-gradient-primary text-white py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-8 mx-auto text-center">
          <h1 class="display-4 fw-bold mb-4">Schedule Your Free Consultation</h1>
          <p class="lead mb-4">Get expert economic analysis for your case with guaranteed 1 business day response</p>
          <div class="row g-3 justify-content-center">
            <div class="col-auto">
              <div class="d-flex align-items-center">
                <i class="fas fa-check-circle me-2"></i>
                <span>No Cost Consultation</span>
              </div>
            </div>
            <div class="col-auto">
              <div class="d-flex align-items-center">
                <i class="fas fa-clock me-2"></i>
                <span>1 Business Day Response</span>
              </div>
            </div>
            <div class="col-auto">
              <div class="d-flex align-items-center">
                <i class="fas fa-shield-alt me-2"></i>
                <span>No Obligation</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Content -->
  <section class="py-5">
    <div class="container">
      <div class="row g-5">
        <!-- Contact Form Column -->
        <div class="col-lg-8">
          <div class="card shadow-lg border-0">
            <div class="card-header bg-white border-0 pt-4 pb-0">
              <h2 class="h3 mb-3">Request Your Free Consultation</h2>
              <p class="text-muted">Tell us about your case and we'll respond within 1 business day with a preliminary assessment.</p>
            </div>
            <div class="card-body p-4">
              <form action="{form_action}" class="needs-validation" id="contactForm" method="POST" onsubmit="trackFormSubmission('consultation_request')" novalidate>
                <!-- Hidden inputs -->
                <input name="_subject" type="hidden" value="New Case Consultation Request"/>
                <input name="_next" type="hidden" value="https://skerritteconomics.com/contact/thank-you/"/>
                <input name="_cc" type="hidden" value="chris@skerritteconomics.com"/>
                
                <div class="row g-3">
                  <!-- Full Name -->
                  <div class="col-md-6">
                    <label for="name" class="form-label">Full Name <span class="text-danger">*</span></label>
                    <input type="text" class="form-control form-control-lg" id="name" name="name" required>
                    <div class="invalid-feedback">Please enter your full name.</div>
                  </div>
                  
                  <!-- Email -->
                  <div class="col-md-6">
                    <label for="email" class="form-label">Email Address <span class="text-danger">*</span></label>
                    <input type="email" class="form-control form-control-lg" id="email" name="email" required>
                    <div class="invalid-feedback">Please enter a valid email address.</div>
                  </div>
                  
                  <!-- Phone -->
                  <div class="col-md-6">
                    <label for="phone" class="form-label">Phone Number</label>
                    <input type="tel" class="form-control form-control-lg" id="phone" name="phone">
                  </div>
                  
                  <!-- Firm -->
                  <div class="col-md-6">
                    <label for="firm" class="form-label">Law Firm / Organization</label>
                    <input type="text" class="form-control form-control-lg" id="firm" name="firm">
                  </div>
                  
                  <!-- Case Type -->
                  <div class="col-md-6">
                    <label for="case-type" class="form-label">Case Type <span class="text-danger">*</span></label>
                    <select class="form-select form-select-lg" id="case-type" name="case-type" required>
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
                  
                  <!-- Jurisdiction -->
                  <div class="col-md-6">
                    <label for="jurisdiction" class="form-label">Jurisdiction</label>
                    <select class="form-select form-select-lg" id="jurisdiction" name="jurisdiction">
                      <option value="">Select Jurisdiction</option>
                      <optgroup label="New England">
                        <option value="massachusetts">Massachusetts</option>
                        <option value="rhode-island">Rhode Island</option>
                        <option value="connecticut">Connecticut</option>
                        <option value="new-hampshire">New Hampshire</option>
                        <option value="vermont">Vermont</option>
                        <option value="maine">Maine</option>
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
                        <option value="washington-dc">Washington D.C.</option>
                        <option value="federal">Federal Court</option>
                        <option value="other">Other</option>
                      </optgroup>
                    </select>
                  </div>
                  
                  <!-- Timeline -->
                  <div class="col-12">
                    <label for="timeline" class="form-label">Timeline for Analysis</label>
                    <select class="form-select form-select-lg" id="timeline" name="timeline">
                      <option value="">Select Timeline</option>
                      <option value="immediate">Immediate (Rush)</option>
                      <option value="1-2-weeks">1-2 Weeks</option>
                      <option value="3-4-weeks">3-4 Weeks</option>
                      <option value="flexible">Flexible</option>
                    </select>
                  </div>
                  
                  <!-- Message -->
                  <div class="col-12">
                    <label for="message" class="form-label">Case Details <span class="text-danger">*</span></label>
                    <textarea class="form-control form-control-lg" id="message" name="message" rows="6" placeholder="Briefly describe your case and the economic analysis needed." required></textarea>
                    <div class="invalid-feedback">Please provide case details.</div>
                  </div>
                </div>
                
                <!-- What Happens Next -->
                <div class="alert alert-info mt-4" role="alert">
                  <h5 class="alert-heading"><i class="fas fa-info-circle me-2"></i>What happens next?</h5>
                  <ul class="mb-0">
                    <li>We'll review your case details within 1 business day</li>
                    <li>You'll receive a preliminary assessment via email or phone</li>
                    <li>We'll discuss timeline, scope, and next steps</li>
                    <li>No commitment required - consultation is completely free</li>
                  </ul>
                </div>
                
                <!-- Submit Button -->
                <div class="d-grid gap-2 mt-4">
                  <button type="submit" class="btn btn-primary btn-lg">
                    <i class="fas fa-paper-plane me-2"></i>Get Free Case Assessment
                  </button>
                </div>
                
                <!-- Security Note -->
                <p class="text-center text-muted small mt-3 mb-0">
                  <i class="fas fa-lock me-1"></i>Your information is secure and confidential. We never share client details.
                </p>
              </form>
            </div>
          </div>
        </div>
        
        <!-- Contact Information Column -->
        <div class="col-lg-4">
          <!-- Contact Card -->
          <div class="card shadow mb-4">
            <div class="card-body">
              <h3 class="h5 mb-4">Contact Information</h3>
              
              <div class="mb-4">
                <h4 class="h6 text-primary mb-2">Christopher Skerritt</h4>
                <p class="small text-muted mb-1">M.Ed, MBA, CRC, CLCP</p>
                <p class="small text-muted">Principal Economic Consultant</p>
              </div>
              
              <div class="d-flex align-items-start mb-3">
                <i class="fas fa-phone text-primary me-3 mt-1"></i>
                <div>
                  <a href="tel:203-605-2814" class="fw-bold text-decoration-none" onclick="trackPhoneClick()">(203) 605-2814</a>
                  <p class="small text-muted mb-0">Direct Line • 8 AM - 6 PM ET</p>
                </div>
              </div>
              
              <div class="d-flex align-items-start mb-3">
                <i class="fas fa-envelope text-primary me-3 mt-1"></i>
                <div>
                  <a href="mailto:chris@skerritteconomics.com" class="text-decoration-none" onclick="trackEmailClick()">chris@skerritteconomics.com</a>
                  <p class="small text-muted mb-0">Responses within 1 business day</p>
                </div>
              </div>
              
              <div class="d-flex align-items-start">
                <i class="fas fa-map-marker-alt text-primary me-3 mt-1"></i>
                <div>
                  <address class="mb-0">
                    400 Putnam Pike Ste J<br>
                    Smithfield, RI 02917<br>
                    <em class="text-muted small">Serving all of New England</em>
                  </address>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Response Times Card -->
          <div class="card shadow mb-4">
            <div class="card-body">
              <h3 class="h5 mb-4"><i class="fas fa-clock text-primary me-2"></i>Response Times</h3>
              <ul class="list-unstyled mb-0">
                <li class="mb-2">
                  <strong>Initial Response:</strong>
                  <span class="text-muted">Within 1 business day</span>
                </li>
                <li class="mb-2">
                  <strong>Preliminary Assessment:</strong>
                  <span class="text-muted">3-5 business days</span>
                </li>
                <li class="mb-2">
                  <strong>Full Report:</strong>
                  <span class="text-muted">2-3 weeks (varies by complexity)</span>
                </li>
                <li>
                  <strong>Expert Testimony:</strong>
                  <span class="text-muted">Available for deposition and trial</span>
                </li>
              </ul>
            </div>
          </div>
          
          <!-- Credentials Card -->
          <div class="card shadow">
            <div class="card-body">
              <h3 class="h5 mb-4"><i class="fas fa-certificate text-primary me-2"></i>Professional Credentials</h3>
              <div class="row g-2">
                <div class="col-6">
                  <div class="text-center p-3 bg-light rounded">
                    <strong class="text-primary">CRC</strong>
                    <p class="small mb-0 text-muted">Certified Rehabilitation Counselor</p>
                  </div>
                </div>
                <div class="col-6">
                  <div class="text-center p-3 bg-light rounded">
                    <strong class="text-primary">CLCP</strong>
                    <p class="small mb-0 text-muted">Certified Life Care Planner</p>
                  </div>
                </div>
                <div class="col-6">
                  <div class="text-center p-3 bg-light rounded">
                    <strong class="text-primary">M.Ed</strong>
                    <p class="small mb-0 text-muted">Master of Education</p>
                  </div>
                </div>
                <div class="col-6">
                  <div class="text-center p-3 bg-light rounded">
                    <strong class="text-primary">MBA</strong>
                    <p class="small mb-0 text-muted">Master of Business Administration</p>
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
            <div class="feature-icon bg-primary bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-bolt text-white fa-2x"></i>
            </div>
            <h3 class="h5">Rapid Response</h3>
            <p class="text-muted">1 business day response guarantee with preliminary assessments in 3-5 days</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-success bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-chart-line text-white fa-2x"></i>
            </div>
            <h3 class="h5">Court-Tested Expertise</h3>
            <p class="text-muted">Extensive experience in RI, MA, and federal courts</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-info bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-bullseye text-white fa-2x"></i>
            </div>
            <h3 class="h5">Clear Communication</h3>
            <p class="text-muted">Reports designed for judges and juries to understand</p>
          </div>
        </div>
        <div class="col-md-6 col-lg-3">
          <div class="text-center">
            <div class="feature-icon bg-warning bg-gradient rounded-circle p-3 d-inline-flex mb-3">
              <i class="fas fa-briefcase text-white fa-2x"></i>
            </div>
            <h3 class="h5">Comprehensive Analysis</h3>
            <p class="text-muted">Full economic damages including lost earnings, benefits, and life care costs</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="py-5">
    <div class="container">
      <h2 class="text-center mb-5">Frequently Asked Questions</h2>
      <div class="row">
        <div class="col-lg-10 mx-auto">
          <div class="accordion" id="faqAccordion" itemscope itemtype="https://schema.org/FAQPage">
            <div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
              <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="true" aria-controls="faq1" itemprop="name">
                  How quickly can I schedule a free consultation with your forensic economist?
                </button>
              </h2>
              <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div class="accordion-body" itemprop="text">
                  We guarantee a response within 1 business day of your initial contact. Most free consultations are scheduled within 2-3 business days, though we can accommodate urgent matters when needed.
                </div>
              </div>
            </div>
            
            <div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2" aria-expanded="false" aria-controls="faq2" itemprop="name">
                  What information should I prepare before contacting your forensic economics firm?
                </button>
              </h2>
              <div id="faq2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div class="accordion-body" itemprop="text">
                  For your free consultation, helpful information includes: case type and jurisdiction, relevant dates (injury, termination, or incident), basic demographic information about the plaintiff, preliminary medical prognosis or employment history, and any specific economic questions you need addressed. However, we can begin discussions with minimal information.
                </div>
              </div>
            </div>
            
            <div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3" aria-expanded="false" aria-controls="faq3" itemprop="name">
                  Do you provide economic expert services outside of Rhode Island?
                </button>
              </h2>
              <div id="faq3" class="accordion-collapse collapse" data-bs-parent="#faqAccordion" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div class="accordion-body" itemprop="text">
                  Yes, while we're based in Smithfield, Rhode Island, we serve attorneys throughout New England including Massachusetts, Connecticut, New Hampshire, Vermont, and Maine. We regularly provide deposition and trial testimony in state and federal courts across the region.
                </div>
              </div>
            </div>
            
            <div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq4" aria-expanded="false" aria-controls="faq4" itemprop="name">
                  What makes your free consultation different from other economic experts?
                </button>
              </h2>
              <div id="faq4" class="accordion-collapse collapse" data-bs-parent="#faqAccordion" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div class="accordion-body" itemprop="text">
                  Our free consultation includes a preliminary damage assessment, strategic recommendations for strengthening your economic arguments, and identification of key economic issues specific to your jurisdiction. Unlike many experts who simply discuss fees, we provide actionable insights to help you evaluate the economic merits of your case.
                </div>
              </div>
            </div>
            
            <div class="accordion-item" itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq5" aria-expanded="false" aria-controls="faq5" itemprop="name">
                  Can you work with tight deadlines or provide rush economic analysis?
                </button>
              </h2>
              <div id="faq5" class="accordion-collapse collapse" data-bs-parent="#faqAccordion" itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
                <div class="accordion-body" itemprop="text">
                  Absolutely. We understand litigation deadlines and maintain capacity for urgent cases. Rush services are available for preliminary reports, rebuttal analyses, and court testimony. When you contact our forensic economist team, please indicate your timeline so we can prioritize accordingly.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="py-5 bg-gradient-primary text-white">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-8">
          <h2 class="mb-3">Ready to Discuss Your Case?</h2>
          <p class="lead mb-4 mb-lg-0">Schedule your free consultation today. We'll respond within 1 business day.</p>
        </div>
        <div class="col-lg-4 text-lg-end">
          <a href="#contactForm" class="btn btn-light btn-lg me-2 mb-2">Request Free Consultation</a>
          <a href="tel:203-605-2814" class="btn btn-outline-light btn-lg mb-2">Call (203) 605-2814</a>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- Form Validation Script -->
<script>
// Bootstrap form validation
(function() {{
  'use strict';
  window.addEventListener('load', function() {{
    var forms = document.getElementsByClassName('needs-validation');
    Array.prototype.filter.call(forms, function(form) {{
      form.addEventListener('submit', function(event) {{
        if (form.checkValidity() === false) {{
          event.preventDefault();
          event.stopPropagation();
        }}
        form.classList.add('was-validated');
      }}, false);
    }});
  }}, false);
}})();
</script>
"""
    
    # Write the updated file
    with open(contact_path, 'w') as f:
        f.write(new_content)
    
    print(f"✅ Enhanced contact page with professional Bootstrap 5 layout")

def main():
    """Main function to update both pages"""
    print("🚀 Updating locations and contact pages with modern Bootstrap 5 layout...")
    
    # Update both pages
    update_locations_page()
    update_contact_page()
    
    print("\n✅ Both pages have been updated successfully!")
    print("\n📝 Next steps:")
    print("1. Review the updated pages at http://localhost:8888/locations/ and http://localhost:8888/contact/")
    print("2. The pages now use the modern-default layout with Bootstrap 5")
    print("3. Both pages have professional styling with blue gradient headers and improved form layouts")

if __name__ == "__main__":
    main()