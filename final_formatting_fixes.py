#!/usr/bin/env python3

import os
import re
import glob

def get_custom_css():
    """Return the complete custom CSS styling block"""
    return '''<style>
/* Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #ffffff;
    font-size: 16px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation Styles */
.main-nav {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    transition: all 0.3s ease;
}

.nav-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2c5aa0;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    line-height: 1.2;
}

.logo span {
    font-size: 0.8rem;
    font-weight: 400;
    color: #666;
}

.nav-menu {
    display: flex;
    list-style: none;
    align-items: center;
    gap: 2rem;
}

.nav-menu li {
    position: relative;
}

.nav-menu a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    padding: 0.5rem 0;
    transition: color 0.3s ease;
}

.nav-menu a:hover {
    color: #2c5aa0;
}

.nav-cta {
    background: #2c5aa0;
    color: white !important;
    padding: 0.75rem 1.5rem !important;
    border-radius: 5px;
    transition: background 0.3s ease;
}

.nav-cta:hover {
    background: #1e3f73;
    color: white !important;
}

.mobile-menu-toggle {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0.5rem;
}

.mobile-menu-toggle span {
    width: 25px;
    height: 3px;
    background: #333;
    margin: 3px 0;
    transition: 0.3s;
}

/* Dropdown Styles */
.has-dropdown {
    position: relative;
}

.dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    background: white;
    min-width: 200px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s ease;
    z-index: 1001;
}

.has-dropdown:hover .dropdown {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.dropdown li {
    border-bottom: 1px solid #f0f0f0;
}

.dropdown li:last-child {
    border-bottom: none;
}

.dropdown a {
    display: block;
    padding: 1rem;
    color: #333;
    border-radius: 5px;
}

.dropdown a:hover {
    background: #f8f9fa;
    color: #2c5aa0;
}

/* Hero Section */
.hero-section {
    background: linear-gradient(135deg, #2c5aa0 0%, #1e3f73 100%);
    color: white;
    padding: 150px 0 100px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:rgba(255,255,255,0.1)"/><stop offset="100%" style="stop-color:rgba(255,255,255,0)"/></radialGradient></defs><circle cx="200" cy="200" r="300" fill="url(%23a)"/><circle cx="800" cy="400" r="200" fill="url(%23a)"/><circle cx="400" cy="800" r="250" fill="url(%23a)"/></svg>') no-repeat center center;
    background-size: cover;
    opacity: 0.3;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
    margin: 0 auto;
}

.hero-content h1 {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.lead {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.95;
    line-height: 1.6;
}

.location-badges {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
    flex-wrap: wrap;
}

.location-badge {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.5rem 1rem;
    border-radius: 25px;
    font-size: 0.9rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.location-badge::before {
    content: '📍';
    font-size: 1rem;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-bottom: 3rem;
    flex-wrap: wrap;
}

.stat {
    text-align: center;
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.9rem;
    opacity: 0.9;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.hero-cta {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

/* Button Styles */
.btn {
    display: inline-block;
    padding: 1rem 2rem;
    border-radius: 5px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    border: 2px solid transparent;
    cursor: pointer;
    font-size: 1rem;
    text-align: center;
    min-width: 160px;
}

.btn-primary {
    background: #ff6b35;
    color: white;
    border-color: #ff6b35;
}

.btn-primary:hover {
    background: #e55a2b;
    border-color: #e55a2b;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(255, 107, 53, 0.3);
}

.btn-secondary {
    background: transparent;
    color: white;
    border-color: rgba(255, 255, 255, 0.5);
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: white;
    color: white;
}

.btn-block {
    width: 100%;
    display: block;
}

/* Services Section */
.services-overview {
    padding: 100px 0;
    background: #f8f9fa;
}

.services-overview h2 {
    text-align: center;
    font-size: 2.5rem;
    color: #2c5aa0;
    margin-bottom: 1rem;
}

.services-overview > .container > p {
    text-align: center;
    font-size: 1.1rem;
    color: #666;
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.service-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: center;
}

.service-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.service-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.service-card h3 {
    color: #2c5aa0;
    margin-bottom: 1rem;
    font-size: 1.3rem;
}

.service-card p {
    color: #666;
    line-height: 1.6;
}

/* Industry Expertise */
.industry-expertise {
    padding: 100px 0;
    background: white;
}

.industry-expertise h2 {
    text-align: center;
    font-size: 2.5rem;
    color: #2c5aa0;
    margin-bottom: 1rem;
}

.industry-expertise > .container > p {
    text-align: center;
    font-size: 1.1rem;
    color: #666;
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.industries-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 3rem;
}

.industry-item {
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 5px;
    text-align: center;
    border-left: 4px solid #2c5aa0;
}

.valuation-methods {
    margin-top: 4rem;
}

.valuation-methods h3 {
    text-align: center;
    font-size: 2rem;
    color: #2c5aa0;
    margin-bottom: 2rem;
}

.methods-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.method {
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
}

.method h4 {
    color: #2c5aa0;
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.method p {
    color: #666;
    line-height: 1.6;
}

/* Why Choose Section */
.why-choose {
    padding: 100px 0;
    background: #f8f9fa;
}

.content-split {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 4rem;
    align-items: start;
}

.content-text h2 {
    font-size: 2.5rem;
    color: #2c5aa0;
    margin-bottom: 2rem;
}

.credential {
    margin-bottom: 2rem;
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}

.credential h4 {
    color: #2c5aa0;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.credential ul {
    list-style: none;
}

.credential li {
    margin-bottom: 0.5rem;
    color: #666;
    position: relative;
    padding-left: 1.5rem;
}

.credential li::before {
    content: '✓';
    position: absolute;
    left: 0;
    color: #ff6b35;
    font-weight: bold;
}

.credential strong {
    color: #333;
}

/* Contact Card */
.contact-card {
    background: white;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    position: sticky;
    top: 120px;
}

.contact-card h3 {
    color: #2c5aa0;
    margin-bottom: 1rem;
    font-size: 1.3rem;
}

.contact-card p {
    color: #666;
    margin-bottom: 1.5rem;
}

.contact-methods {
    margin-bottom: 1.5rem;
}

.contact-method {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem;
    margin-bottom: 0.5rem;
    border-radius: 5px;
    text-decoration: none;
    color: #333;
    transition: background 0.3s ease;
}

.contact-method:hover {
    background: #f8f9fa;
}

.method-icon {
    font-size: 1.2rem;
}

.method-text {
    font-weight: 500;
}

.response-time {
    text-align: center;
    margin-top: 1rem;
    color: #28a745;
    font-weight: 500;
}

/* Service Areas */
.service-areas {
    padding: 100px 0;
    background: white;
}

.service-areas h2 {
    text-align: center;
    font-size: 2.5rem;
    color: #2c5aa0;
    margin-bottom: 1rem;
}

.service-areas > .container > p {
    text-align: center;
    font-size: 1.1rem;
    color: #666;
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.coverage-stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
}

.coverage-stat {
    text-align: center;
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 10px;
    min-width: 150px;
}

.coverage-stat .stat-number {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: #2c5aa0;
    margin-bottom: 0.5rem;
}

.coverage-stat .stat-label {
    font-size: 0.9rem;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Contact CTA */
.contact-cta {
    padding: 100px 0;
    background: linear-gradient(135deg, #2c5aa0 0%, #1e3f73 100%);
    color: white;
    text-align: center;
}

.cta-content h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.cta-content p {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    opacity: 0.95;
}

.cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

/* Footer */
.main-footer {
    background: #1a1a1a;
    color: #ccc;
    padding: 50px 0 30px;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
}

.footer-section h3,
.footer-section h4 {
    color: white;
    margin-bottom: 1rem;
}

.footer-section p,
.footer-section li {
    margin-bottom: 0.5rem;
    line-height: 1.6;
}

.footer-section ul {
    list-style: none;
}

.footer-section a {
    color: #ccc;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-section a:hover {
    color: #ff6b35;
}

.contact-info p {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.footer-bottom {
    border-top: 1px solid #333;
    padding-top: 2rem;
    text-align: center;
}

.footer-bottom p {
    margin-bottom: 0.5rem;
    color: #999;
}

/* Responsive Design */
@media (max-width: 768px) {
    .mobile-menu-toggle {
        display: flex;
    }
    
    .nav-menu {
        display: none;
    }
    
    .hero-content h1 {
        font-size: 2.5rem;
    }
    
    .hero-stats {
        gap: 2rem;
    }
    
    .stat-number {
        font-size: 2rem;
    }
    
    .content-split {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .contact-card {
        position: static;
    }
    
    .coverage-stats {
        gap: 1rem;
    }
    
    .cta-content h2 {
        font-size: 2rem;
    }
    
    .hero-cta,
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .btn {
        min-width: 200px;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }
    
    .hero-content h1 {
        font-size: 2rem;
    }
    
    .lead {
        font-size: 1.1rem;
    }
    
    .hero-stats {
        flex-direction: column;
        gap: 1rem;
    }
    
    .location-badges {
        flex-direction: column;
        align-items: center;
    }
    
    .services-grid,
    .methods-grid {
        grid-template-columns: 1fr;
    }
    
    .industries-grid {
        grid-template-columns: 1fr;
    }
}
</style>'''

def get_location_badges_html(city, state):
    """Generate location badges HTML"""
    return f'''                <div class="location-badges">
                    <div class="location-badge">{city}, {state}</div>
                    <div class="location-badge">Licensed Professional</div>
                    <div class="location-badge">Remote Capable</div>
                </div>'''

def process_files():
    """Process all business valuation analyst pages 601-750"""
    base_dir = "/Users/chrisskerritt/SEC/locations/cities"
    pattern = os.path.join(base_dir, "*business-valuation-analyst*.html")
    all_files = sorted(glob.glob(pattern))
    
    # Get files 601-750 (0-based indexing, so 600-749)
    target_files = all_files[600:750]
    
    print(f"Processing {len(target_files)} files (pages 601-750)...")
    
    processed_count = 0
    
    for file_path in target_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract city and state from filename
            filename = os.path.basename(file_path)
            # Remove .html and -business-valuation-analyst
            base_name = filename.replace('-business-valuation-analyst.html', '')
            parts = base_name.split('-')
            if len(parts) >= 2:
                state = parts[-1].upper()
                city = ' '.join(parts[:-1]).title()
            else:
                city = base_name.title()
                state = "US"
            
            # Apply fixes
            modified = False
            
            # 1. Add custom CSS styling if not present
            if '<style>' not in content:
                # Insert CSS after the Google Fonts link
                fonts_pattern = r'(<link href="https://fonts\.googleapis\.com/css2[^>]*>)\s*'
                css_block = get_custom_css()
                replacement = f'\\1\n    {css_block}\n'
                
                if re.search(fonts_pattern, content):
                    content = re.sub(fonts_pattern, replacement, content)
                    modified = True
                else:
                    # If no Google Fonts, add after head tag
                    head_pattern = r'(<head[^>]*>)'
                    replacement = f'\\1\n    {css_block}'
                    content = re.sub(head_pattern, replacement, content)
                    modified = True
            
            # 2. Update hero section class
            if 'class="location-hero"' in content:
                content = content.replace('class="location-hero"', 'class="hero-section"')
                modified = True
            
            # 3. Add location badges if not present
            if 'location-badges' not in content:
                # Find the lead paragraph and add badges after it
                lead_pattern = r'(<p class="lead"[^>]*>.*?</p>)'
                badges_html = get_location_badges_html(city, state)
                replacement = f'\\1\n{badges_html}'
                
                if re.search(lead_pattern, content, re.DOTALL):
                    content = re.sub(lead_pattern, replacement, content, flags=re.DOTALL)
                    modified = True
            
            # Write back if modified
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                processed_count += 1
                print(f"✓ Processed: {filename}")
            else:
                print(f"- Skipped: {filename} (no changes needed)")
                
        except Exception as e:
            print(f"✗ Error processing {file_path}: {str(e)}")
    
    print(f"\nCompleted! Processed {processed_count} files out of {len(target_files)} total files.")
    return processed_count

if __name__ == "__main__":
    process_files()