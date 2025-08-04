#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_navigation_in_file(filepath):
    """Update navigation in a single HTML file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already updated
    if 'Enhanced Navigation with All Services' in content or 'navigation-enhanced.css' in content:
        print(f"  Already updated: {filepath}")
        return False
    
    # Add navigation-enhanced.css if not present
    if 'navigation-enhanced.css' not in content:
        # Find the styles.css line and add after it
        content = re.sub(
            r'(<link[^>]*href="[^"]*styles\.css"[^>]*>)',
            r'\1\n<link href="../../css/navigation-enhanced.css" rel="stylesheet"/>',
            content
        )
    
    # Replace the old navigation with the new one
    nav_start = content.find('<!-- Navigation -->')
    nav_end = content.find('</nav>', nav_start) + 6
    
    if nav_start == -1:
        print(f"  No navigation found: {filepath}")
        return False
    
    # Check if there's a mobile overlay after nav
    if '<div class="mobile-nav-overlay"></div>' not in content[nav_end:nav_end+100]:
        overlay_html = '\n<!-- Mobile Navigation Overlay -->\n<div class="mobile-nav-overlay"></div>'
    else:
        overlay_html = ''
    
    new_navigation = '''<!-- Enhanced Navigation with All Services -->
<nav class="main-nav" role="navigation" aria-label="Main navigation">
<div class="container">
<div class="nav-wrapper">
<!-- Logo -->
<a href="../../index.html" class="logo" aria-label="Skerritt Economics & Consulting Home">
<strong>Skerritt Economics</strong>
<span>&amp; Consulting</span>
</a>

<!-- Mobile Menu Toggle -->
<button class="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="nav-menu">
<span></span>
<span></span>
<span></span>
</button>

<!-- Navigation Menu with ALL Services -->
<ul class="nav-menu" id="nav-menu">
<li>
<a href="../../index.html">Home</a>
</li>

<!-- Complete Services Dropdown -->
<li class="has-dropdown{active_services}">
<a href="../../services/" aria-haspopup="true" aria-expanded="false">Services</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../../services/forensic-economics/">
Forensic Economics
<span class="service-badge">Popular</span>
</a>
</li>
<li role="menuitem">
<a href="../../services/business-valuation/">Business Valuation</a>
</li>
<li role="menuitem">
<a href="../../services/life-care-planning/">
Life Care Planning
<span class="service-badge new">New</span>
</a>
</li>
<li role="menuitem">
<a href="../../services/vocational-expert/">Vocational Expert</a>
</li>
<li role="menuitem">
<a href="../../services/business-consulting/">Business Consulting</a>
</li>
<li role="menuitem" class="dropdown-divider">
<a href="../../services/" class="view-all-link">View All Services →</a>
</li>
</ul>
</li>

<!-- Practice Areas Dropdown -->
<li class="has-dropdown{active_practice}">
<a href="../../practice-areas/" aria-haspopup="true" aria-expanded="false">Practice Areas</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../../practice-areas/personal-injury/">Personal Injury &amp; Wrongful Death</a>
</li>
<li role="menuitem">
<a href="../../practice-areas/medical-malpractice/">Medical Malpractice</a>
</li>
<li role="menuitem">
<a href="../../practice-areas/employment/">Employment Litigation</a>
</li>
<li role="menuitem">
<a href="../../practice-areas/commercial-disputes/">Commercial Disputes</a>
</li>
<li role="menuitem">
<a href="../../practice-areas/family-law/">Family Law &amp; Divorce</a>
</li>
<li role="menuitem">
<a href="../../practice-areas/product-liability/">Product Liability</a>
</li>
</ul>
</li>

<!-- Locations Dropdown -->
<li class="has-dropdown">
<a href="../../locations/" aria-haspopup="true" aria-expanded="false">Locations</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../../locations/cities/">Browse by City</a>
</li>
<li role="menuitem">
<a href="../../locations/states/">Browse by State</a>
</li>
<li role="menuitem" class="dropdown-divider">
<a href="../../locations/rhode-island/">Rhode Island</a>
</li>
<li role="menuitem">
<a href="../../locations/massachusetts/">Massachusetts</a>
</li>
<li role="menuitem">
<a href="../../locations/connecticut/">Connecticut</a>
</li>
</ul>
</li>

<li>
<a href="../../case-studies/">Case Studies</a>
</li>

<li>
<a href="../../about/">About</a>
</li>

<li>
<a href="../../blog/">Blog</a>
</li>

<li>
<a href="../../contact/" class="nav-cta">Contact</a>
</li>
</ul>
</div>
</div>
</nav>''' + overlay_html
    
    # Determine if this is a service or practice area page
    if '/services/' in str(filepath):
        new_navigation = new_navigation.replace('{active_services}', ' active')
        new_navigation = new_navigation.replace('{active_practice}', '')
    elif '/practice-areas/' in str(filepath):
        new_navigation = new_navigation.replace('{active_services}', '')
        new_navigation = new_navigation.replace('{active_practice}', ' active')
    else:
        new_navigation = new_navigation.replace('{active_services}', '')
        new_navigation = new_navigation.replace('{active_practice}', '')
    
    # Replace the navigation
    content = content[:nav_start] + new_navigation + content[nav_end:]
    
    # Add navigation JavaScript at the end of body if not present
    if 'navigation-enhanced.js' not in content:
        # Find </body> tag
        body_end = content.rfind('</body>')
        if body_end != -1:
            js_include = '''
<!-- Enhanced Navigation JavaScript -->
<script src="../../js/navigation-enhanced.js"></script>
'''
            content = content[:body_end] + js_include + content[body_end:]
    
    # Write the updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated: {filepath}")
    return True

def main():
    base_dir = Path('/Users/chrisskerritt/SEC')
    
    # Service pages
    service_pages = [
        'services/forensic-economics/index.html',
        'services/business-valuation/index.html',
        'services/life-care-planning/index.html',
        'services/vocational-expert/index.html',
        'services/business-consulting/index.html'
    ]
    
    # Practice area pages
    practice_pages = [
        'practice-areas/personal-injury/index.html',
        'practice-areas/medical-malpractice/index.html',
        'practice-areas/employment/index.html',
        'practice-areas/commercial-disputes/index.html'
    ]
    
    print("Updating Service Pages:")
    for page in service_pages:
        filepath = base_dir / page
        if filepath.exists():
            update_navigation_in_file(filepath)
        else:
            print(f"  Not found: {filepath}")
    
    print("\nUpdating Practice Area Pages:")
    for page in practice_pages:
        filepath = base_dir / page
        if filepath.exists():
            update_navigation_in_file(filepath)
        else:
            print(f"  Not found: {filepath}")
    
    print("\nDone!")

if __name__ == '__main__':
    main()