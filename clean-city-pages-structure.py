#!/usr/bin/env python3
"""
Clean up city pages structure to remove duplicates and fix formatting
"""

import os
import re
import glob

def clean_page_structure(html_content):
    """Clean up the page structure"""
    
    # Remove duplicate modern UI CSS links
    html_content = re.sub(r'<link rel="stylesheet" href="/css/modern-ui\.css">\s*<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+\.css">', '', html_content)
    
    # Remove old navigation
    html_content = re.sub(r'<!-- Navigation -->\s*<nav class="main-nav">.*?</nav>', '', html_content, flags=re.DOTALL)
    
    # Remove duplicate mobile menu toggles
    html_content = re.sub(r'<button class="mobile-menu-toggle" aria-label="Toggle menu">.*?</button>', '', html_content, flags=re.DOTALL)
    
    # Remove old inline styles that conflict
    html_content = re.sub(r'<style>\s*\.hero-section\s*{[^}]*experienced:[^}]*}.*?</style>', '', html_content, flags=re.DOTALL)
    
    # Fix the hero section to use modern classes
    old_hero_pattern = r'<section class="hero-section">.*?</section>'
    new_hero = '''<section class="hero-modern">
  <div class="hero-background">
    <div style="background: linear-gradient(45deg, #1e3a8a, #2563eb); height: 100%; width: 100%;"></div>
    <div class="hero-overlay"></div>
  </div>
  
  <div class="hero-content container">'''
    
    # Extract title and subtitle from old hero
    hero_match = re.search(r'<h1>(.*?)</h1>', html_content)
    subtitle_match = re.search(r'<p>([^<]+certified[^<]+)</p>', html_content)
    
    if hero_match and subtitle_match:
        title = hero_match.group(1)
        subtitle = subtitle_match.group(1)
        
        # Split title for accent
        title_parts = title.split(' - ', 1)
        if len(title_parts) == 1:
            title_parts = title.split(' Services', 1)
            if len(title_parts) == 2:
                title_parts[1] = 'Services'
        
        main_title = title_parts[0]
        accent_title = title_parts[1] if len(title_parts) > 1 else 'Expert Services'
        
        new_hero += f'''
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
        html_content = re.sub(old_hero_pattern, new_hero, html_content, flags=re.DOTALL)
    
    # Remove old CSS links that are now handled by modern-ui.css
    old_css_files = [
        'ultimate-consistency-fix.css',
        'force-navigation-fixed.js'
    ]
    for css_file in old_css_files:
        html_content = re.sub(rf'<link[^>]*href="[^"]*{css_file}"[^>]*>', '', html_content)
        html_content = re.sub(rf'<script[^>]*src="[^"]*{css_file}"[^>]*></script>', '', html_content)
    
    # Clean up extra whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    
    return html_content

def process_city_page(filepath):
    """Process a single city page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Clean the page structure
        html_content = clean_page_structure(html_content)
        
        # Save updated file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return True, f"Cleaned: {os.path.basename(filepath)}"
        
    except Exception as e:
        return False, f"Error processing {filepath}: {str(e)}"

def main():
    """Main function"""
    print("Cleaning City Pages Structure")
    print("=" * 50)
    
    # Process the 5 sample pages
    sample_pages = [
        '/Users/chrisskerritt/SEC/locations/cities/phenix-city-al-al-life-care-planner.html',
        '/Users/chrisskerritt/SEC/locations/cities/north-kingstown-ri-ri-vocational-expert.html',
        '/Users/chrisskerritt/SEC/locations/cities/cary-nc-nc-vocational-expert.html',
        '/Users/chrisskerritt/SEC/locations/cities/blue-springs-mo-business-valuation-analyst.html',
        '/Users/chrisskerritt/SEC/locations/cities/sunland-park-nm-nm-vocational-expert.html'
    ]
    
    for page in sample_pages:
        if os.path.exists(page):
            success, message = process_city_page(page)
            print(f"{'✓' if success else '✗'} {message}")
    
    print("\nPages cleaned. Now they should display properly with the modern UI.")

if __name__ == "__main__":
    main()