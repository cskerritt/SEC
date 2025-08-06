#!/usr/bin/env python3
"""
Migration script to update all city pages with modern UI design
"""

import os
import re
import glob
from bs4 import BeautifulSoup
import json

def create_modern_header():
    """Create modern header HTML"""
    return '''
<!-- Modern Header -->
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
</div>
'''

def create_modern_footer():
    """Create modern footer HTML"""
    return '''
<!-- Modern Footer -->
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
</footer>
'''

def update_css_links(soup):
    """Update CSS links to include modern UI"""
    head = soup.find('head')
    if not head:
        return
    
    # Remove old CSS files
    old_css = ['styles.css', 'city-pages.css', 'override.css']
    for link in head.find_all('link', rel='stylesheet'):
        href = link.get('href', '')
        if any(css in href for css in old_css):
            link.decompose()
    
    # Add modern UI CSS
    modern_css = soup.new_tag('link', rel='stylesheet', href='/css/modern-ui.css')
    font_awesome = soup.new_tag('link', rel='stylesheet', 
                                href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css')
    
    head.append(modern_css)
    head.append(font_awesome)

def transform_hero_section(soup):
    """Transform hero section to modern design"""
    hero = soup.find('section', class_='hero-section')
    if not hero:
        return
    
    # Get existing content
    h1 = hero.find('h1')
    subtitle = hero.find('p', class_='hero-subtitle')
    
    if h1 and subtitle:
        hero_title = h1.get_text(strip=True)
        hero_subtitle = subtitle.get_text(strip=True)
        
        # Create new modern hero
        new_hero = f'''
<section class="hero-modern">
  <div class="hero-background">
    <div style="background: linear-gradient(45deg, #1e3a8a, #2563eb); height: 100%; width: 100%;"></div>
    <div class="hero-overlay"></div>
  </div>
  
  <div class="hero-content container">
    <h1 class="hero-title">
      {hero_title.split(' - ')[0]}
      <span class="accent">{' - '.join(hero_title.split(' - ')[1:]) if ' - ' in hero_title else 'Expert Services'}</span>
    </h1>
    <p class="hero-subtitle">{hero_subtitle}</p>
    <div class="hero-actions">
      <a href="/contact/" class="btn btn-accent btn-lg">Schedule Consultation</a>
      <a href="/services/" class="btn btn-outline btn-lg">View Services</a>
    </div>
  </div>
</section>
'''
        
        # Replace old hero with new
        new_hero_soup = BeautifulSoup(new_hero, 'html.parser')
        hero.replace_with(new_hero_soup)

def transform_services_section(soup):
    """Transform services section to modern design"""
    services = soup.find('section', class_='services-section')
    if not services:
        return
    
    # Add modern classes
    services['class'] = 'services-section'
    
    # Update service cards
    for card in services.find_all(class_='service-card'):
        # Add modern card classes
        if 'service-card' not in card.get('class', []):
            card['class'] = card.get('class', []) + ['service-card']
        
        # Add icon if missing
        h3 = card.find('h3')
        if h3 and not card.find(class_='card-icon'):
            icon_div = soup.new_tag('div', class_='card-icon')
            icon = soup.new_tag('i', class_='fas fa-chart-line')
            icon_div.append(icon)
            card.insert(0, icon_div)
            
            # Update h3 class
            h3['class'] = 'card-title'
        
        # Update paragraph classes
        for p in card.find_all('p'):
            if 'card-description' not in p.get('class', []):
                p['class'] = 'card-description'

def transform_contact_section(soup):
    """Transform contact/CTA sections to modern design"""
    cta_sections = soup.find_all('section', class_=['contact-section', 'cta-section'])
    
    for cta in cta_sections:
        # Add gradient background
        cta['style'] = 'background: var(--gradient-primary); color: var(--primary-foreground);'
        
        # Update headings
        for h2 in cta.find_all('h2'):
            h2['style'] = 'font-size: var(--text-4xl); color: var(--primary-foreground); margin-bottom: var(--spacing-4);'
        
        # Update buttons
        for btn in cta.find_all('a', class_='btn'):
            if 'btn-primary' in btn.get('class', []):
                btn['class'] = ['btn', 'btn-accent', 'btn-lg']
            elif 'btn-secondary' in btn.get('class', []):
                btn['class'] = ['btn', 'btn-outline', 'btn-lg']

def add_mobile_menu_script(soup):
    """Add mobile menu toggle script"""
    script = '''
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
'''
    
    body = soup.find('body')
    if body:
        script_tag = BeautifulSoup(script, 'html.parser')
        body.append(script_tag)

def process_city_page(filepath):
    """Process a single city page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Update CSS links
        update_css_links(soup)
        
        # Replace old header with modern header
        old_header = soup.find('header')
        if old_header:
            old_header.decompose()
        
        old_nav = soup.find('nav', class_='navbar')
        if old_nav:
            old_nav.decompose()
            
        # Add modern header after body tag
        body = soup.find('body')
        if body:
            header_html = BeautifulSoup(create_modern_header(), 'html.parser')
            body.insert(0, header_html)
        
        # Transform sections
        transform_hero_section(soup)
        transform_services_section(soup)
        transform_contact_section(soup)
        
        # Replace old footer with modern footer
        old_footer = soup.find('footer')
        if old_footer:
            old_footer.decompose()
        
        # Add modern footer before closing body tag
        if body:
            footer_html = BeautifulSoup(create_modern_footer(), 'html.parser')
            body.append(footer_html)
        
        # Add mobile menu script
        add_mobile_menu_script(soup)
        
        # Save updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        
        return True, f"Updated: {os.path.basename(filepath)}"
        
    except Exception as e:
        return False, f"Error processing {filepath}: {str(e)}"

def main():
    """Main migration function"""
    print("Starting City Pages Modern UI Migration")
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
    print(f"To run full migration, modify this script to process all pages.")
    
    # Uncomment below to process all pages
    # print("\nProcessing all pages...")
    # for i, page in enumerate(city_pages):
    #     success, message = process_city_page(page)
    #     if i % 100 == 0:
    #         print(f"Progress: {i}/{len(city_pages)} pages processed")

if __name__ == "__main__":
    main()