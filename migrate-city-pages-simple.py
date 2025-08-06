#!/usr/bin/env python3
"""
Simple migration script to update city pages with modern UI design
Uses regex instead of BeautifulSoup to avoid dependencies
"""

import os
import re
import glob
import json

def update_css_in_head(html_content):
    """Update CSS links in the head section"""
    # Remove old CSS files
    html_content = re.sub(r'<link[^>]*href="[^"]*(?:styles\.css|city-pages\.css|override\.css)[^"]*"[^>]*>', '', html_content)
    
    # Add modern UI CSS before closing head tag
    modern_css = '''
    <link rel="stylesheet" href="/css/modern-ui.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>'''
    
    html_content = re.sub(r'</head>', modern_css, html_content, count=1)
    return html_content

def create_modern_header():
    """Create modern header HTML"""
    return '''<!-- Modern Header -->
<header class="header-modern">
  <div class="container">
    <div class="header-container">
      <a href="/" class="header-logo">
        Skerritt Economics
      </a>
      
      <nav class="header-nav">
        <a href="/services/">Services</a>
        <a href="/about/">About</a>
        <a href="/locations/">Locations</a>
        <a href="/contact/">Contact</a>
        <a href="/contact/" class="btn btn-professional btn-sm">
          Get Started
        </a>
      </nav>
      
      <button class="mobile-menu-toggle" aria-label="Toggle mobile menu">
        <i class="fas fa-bars"></i>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Menu -->
<div class="mobile-menu" id="mobile-menu">
  <nav class="mobile-menu-nav">
    <a href="/services/">Services</a>
    <a href="/about/">About</a>
    <a href="/locations/">Locations</a>
    <a href="/contact/">Contact</a>
    <a href="/contact/" class="btn btn-professional btn-sm" style="margin-top: 1rem;">
      Get Started
    </a>
  </nav>
</div>'''

def update_header(html_content):
    """Replace old header with modern header"""
    # Remove old header/nav
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<nav[^>]*class="navbar[^"]*"[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL)
    
    # Add modern header after body tag
    modern_header = create_modern_header()
    html_content = re.sub(r'(<body[^>]*>)', r'\1\n' + modern_header, html_content, count=1)
    
    return html_content

def transform_hero_section(html_content):
    """Transform hero section to modern design"""
    # Find hero section
    hero_match = re.search(r'<section[^>]*class="hero-section"[^>]*>(.*?)</section>', html_content, re.DOTALL)
    if not hero_match:
        return html_content
    
    # Extract title and subtitle
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', hero_match.group(1))
    subtitle_match = re.search(r'<p[^>]*class="hero-subtitle"[^>]*>(.*?)</p>', hero_match.group(1))
    
    if title_match and subtitle_match:
        title = title_match.group(1).strip()
        subtitle = subtitle_match.group(1).strip()
        
        # Split title for accent
        title_parts = title.split(' - ', 1)
        main_title = title_parts[0]
        accent_title = title_parts[1] if len(title_parts) > 1 else 'Expert Services'
        
        # Create new modern hero
        modern_hero = f'''<section class="hero-modern">
  <div class="hero-background">
    <div style="background: linear-gradient(45deg, #1e3a8a, #2563eb); height: 100%; width: 100%;"></div>
    <div class="hero-overlay"></div>
  </div>
  
  <div class="hero-content container">
    <h1 class="hero-title">
      {main_title}
      <span class="accent">{accent_title}</span>
    </h1>
    <p class="hero-subtitle">{subtitle}</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn btn-accent btn-lg">Schedule Consultation</a>
      <a href="/services/" class="btn btn-outline btn-lg">View Services</a>
    </div>
  </div>
</section>'''
        
        # Replace old hero with new
        html_content = html_content.replace(hero_match.group(0), modern_hero)
    
    return html_content

def update_service_cards(html_content):
    """Update service cards with modern styling"""
    # Add card-icon div after service-card opening
    def add_icon(match):
        card_content = match.group(0)
        # Add icon div after opening tag
        icon_html = '''
        <div class="card-icon">
          <i class="fas fa-chart-line"></i>
        </div>'''
        card_content = re.sub(r'(<div[^>]*class="service-card"[^>]*>)', r'\1' + icon_html, card_content, count=1)
        # Update h3 class
        card_content = re.sub(r'<h3>', '<h3 class="card-title">', card_content)
        # Update p class
        card_content = re.sub(r'<p>', '<p class="card-description">', card_content)
        return card_content
    
    html_content = re.sub(r'<div[^>]*class="service-card"[^>]*>.*?</div>\s*</div>', add_icon, html_content, flags=re.DOTALL)
    
    # Update services section class
    html_content = re.sub(r'class="services-section"', 'class="services-section"', html_content)
    
    return html_content

def create_modern_footer():
    """Create modern footer HTML"""
    return '''<!-- Modern Footer -->
<footer class="footer-modern">
  <div class="container">
    <div class="footer-content">
      <div class="footer-section">
        <h3>About Skerritt Economics</h3>
        <p style="color: var(--muted-foreground); line-height: var(--leading-relaxed);">
          Leading forensic economics firm providing expert testimony and economic analysis for legal professionals nationwide.
        </p>
      </div>
      
      <div class="footer-section">
        <h3>Services</h3>
        <ul>
          <li><a href="/services/forensic-economics/">Forensic Economics</a></li>
          <li><a href="/services/business-valuation/">Business Valuation</a></li>
          <li><a href="/services/life-care-planning/">Life Care Planning</a></li>
          <li><a href="/services/vocational-expert/">Vocational Expert</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>Quick Links</h3>
        <ul>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/team/">Our Team</a></li>
          <li><a href="/testimonials/">Testimonials</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h3>Contact</h3>
        <ul>
          <li><a href="tel:+12036052814">+1 (203) 605-2814</a></li>
          <li><a href="mailto:chris@skerritteconomics.com">chris@skerritteconomics.com</a></li>
          <li>400 Putnam Pike Ste J<br>Smithfield, RI 02917</li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2024 Skerritt Economics & Consulting. All rights reserved.</p>
    </div>
  </div>
</footer>'''

def update_footer(html_content):
    """Replace old footer with modern footer"""
    # Remove old footer
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL)
    
    # Add modern footer before closing body tag
    modern_footer = create_modern_footer()
    
    # Add mobile menu script
    mobile_script = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  
  if (mobileMenuToggle && mobileMenu) {
    mobileMenuToggle.addEventListener('click', function() {
      mobileMenu.classList.toggle('active');
      const isOpen = mobileMenu.classList.contains('active');
      mobileMenuToggle.innerHTML = isOpen ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
    });
  }
});
</script>
</body>'''
    
    html_content = re.sub(r'</body>', modern_footer + '\n' + mobile_script, html_content, count=1)
    
    return html_content

def update_cta_sections(html_content):
    """Update CTA sections with modern styling"""
    # Update CTA section styling
    html_content = re.sub(
        r'<section[^>]*class="(?:contact-section|cta-section)"[^>]*>',
        '<section class="section" style="background: var(--gradient-primary); color: var(--primary-foreground);">',
        html_content
    )
    
    # Update CTA buttons
    html_content = re.sub(r'class="btn btn-primary"', 'class="btn btn-accent btn-lg"', html_content)
    html_content = re.sub(r'class="btn btn-secondary"', 'class="btn btn-outline btn-lg"', html_content)
    
    return html_content

def process_city_page(filepath):
    """Process a single city page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Apply transformations
        html_content = update_css_in_head(html_content)
        html_content = update_header(html_content)
        html_content = transform_hero_section(html_content)
        html_content = update_service_cards(html_content)
        html_content = update_cta_sections(html_content)
        html_content = update_footer(html_content)
        
        # Save updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return True, f"Updated: {os.path.basename(filepath)}"
        
    except Exception as e:
        return False, f"Error processing {filepath}: {str(e)}"

def main():
    """Main migration function"""
    print("Starting City Pages Modern UI Migration (Simple Version)")
    print("=" * 50)
    
    # Find all city pages
    city_pages_dir = '/Users/chrisskerritt/SEC/locations/cities'
    city_pages = glob.glob(os.path.join(city_pages_dir, '*.html'))
    
    print(f"Found {len(city_pages)} city pages to migrate")
    
    # Process a sample first
    sample_pages = city_pages[:5]  # Process first 5 pages as sample
    
    print("\nProcessing sample pages first...")
    results = []
    
    for page in sample_pages:
        success, message = process_city_page(page)
        results.append({
            'file': os.path.basename(page),
            'success': success,
            'message': message
        })
        print(f"{'✓' if success else '✗'} {message}")
    
    # Save sample results
    with open('modern-ui-migration-sample.json', 'w') as f:
        json.dump({
            'total_pages': len(city_pages),
            'sample_processed': len(sample_pages),
            'results': results
        }, f, indent=2)
    
    print(f"\nSample migration complete. Check the updated pages before running full migration.")
    print(f"Sample pages updated:")
    for page in sample_pages:
        print(f"  - {os.path.basename(page)}")
    
    # Uncomment below to process all pages
    # print("\nProcessing all pages...")
    # for i, page in enumerate(city_pages):
    #     success, message = process_city_page(page)
    #     if i % 100 == 0:
    #         print(f"Progress: {i}/{len(city_pages)} pages processed")

if __name__ == "__main__":
    main()