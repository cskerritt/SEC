#!/usr/bin/env python3
"""
Update main pages (Services, Practice Areas, About, Case Studies) with complete navigation
"""

import os
import re

def update_navigation_in_file(filepath):
    """Update navigation in a single HTML file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has enhanced navigation
    if 'navigation-enhanced.css' in content and 'navigation-enhanced.js' in content:
        print(f"✓ {filepath} already has enhanced navigation")
        return False
    
    # Add navigation-enhanced.css after styles.css
    if 'navigation-enhanced.css' not in content:
        content = content.replace(
            '<link href="../css/styles.css" rel="stylesheet"/>',
            '<link href="../css/styles.css" rel="stylesheet"/>\n<link href="../css/navigation-enhanced.css" rel="stylesheet"/>'
        )
    
    # Find and replace the navigation section
    nav_pattern = r'<!-- Navigation -->.*?</nav>'
    header_pattern = r'<header[^>]*>.*?</header>'
    body_nav_pattern = r'<body>\s*<nav[^>]*>.*?</nav>'
    
    new_navigation = '''<!-- Enhanced Navigation with All Services -->
<nav class="main-nav" role="navigation" aria-label="Main navigation">
<div class="container">
<div class="nav-wrapper">
<!-- Logo -->
<a href="../index.html" class="logo" aria-label="Skerritt Economics & Consulting Home">
<strong>Skerritt Economics</strong>
<span>& Consulting</span>
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
<a href="../index.html">Home</a>
</li>

<!-- Complete Services Dropdown -->
<li class="has-dropdown">
<a href="../services/" aria-haspopup="true" aria-expanded="false">Services</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../services/forensic-economics/">
Forensic Economics
<span class="service-badge">Popular</span>
</a>
</li>
<li role="menuitem">
<a href="../services/business-valuation/">Business Valuation</a>
</li>
<li role="menuitem">
<a href="../services/life-care-planning/">
Life Care Planning
<span class="service-badge new">New</span>
</a>
</li>
<li role="menuitem">
<a href="../services/vocational-expert/">Vocational Expert</a>
</li>
<li role="menuitem">
<a href="../services/business-consulting/">Business Consulting</a>
</li>
<li role="menuitem" class="dropdown-divider">
<a href="../services/" class="view-all-link">View All Services →</a>
</li>
</ul>
</li>

<!-- Practice Areas Dropdown -->
<li class="has-dropdown">
<a href="../practice-areas/" aria-haspopup="true" aria-expanded="false">Practice Areas</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../practice-areas/personal-injury/">Personal Injury & Wrongful Death</a>
</li>
<li role="menuitem">
<a href="../practice-areas/medical-malpractice/">Medical Malpractice</a>
</li>
<li role="menuitem">
<a href="../practice-areas/employment/">Employment Litigation</a>
</li>
<li role="menuitem">
<a href="../practice-areas/commercial-disputes/">Commercial Disputes</a>
</li>
<li role="menuitem">
<a href="../practice-areas/family-law/">Family Law & Divorce</a>
</li>
<li role="menuitem">
<a href="../practice-areas/product-liability/">Product Liability</a>
</li>
</ul>
</li>

<!-- Locations Dropdown -->
<li class="has-dropdown">
<a href="../locations/" aria-haspopup="true" aria-expanded="false">Locations</a>
<ul class="dropdown" role="menu">
<li role="menuitem">
<a href="../locations/cities/">Browse by City</a>
</li>
<li role="menuitem">
<a href="../locations/states/">Browse by State</a>
</li>
<li role="menuitem" class="dropdown-divider">
<a href="../locations/rhode-island/">Rhode Island</a>
</li>
<li role="menuitem">
<a href="../locations/massachusetts/">Massachusetts</a>
</li>
<li role="menuitem">
<a href="../locations/connecticut/">Connecticut</a>
</li>
</ul>
</li>

<li>
<a href="../case-studies/">Case Studies</a>
</li>

<li>
<a href="../about/">About</a>
</li>

<li>
<a href="../blog/">Blog</a>
</li>

<li>
<a href="../contact/" class="nav-cta">Contact</a>
</li>
</ul>
</div>
</div>
</nav>
<!-- Mobile Navigation Overlay -->
<div class="mobile-nav-overlay"></div>'''
    
    # Try different patterns to find and replace navigation
    replaced = False
    
    # Pattern 1: Look for existing nav with class main-nav
    if '<nav class="main-nav"' in content:
        # Find the start and end of the nav element
        nav_start = content.find('<nav class="main-nav"')
        if nav_start != -1:
            nav_end = content.find('</nav>', nav_start) + 6
            # Also include mobile overlay if it exists
            overlay_end = content.find('<div class="mobile-nav-overlay"></div>', nav_end)
            if overlay_end != -1:
                nav_end = overlay_end + len('<div class="mobile-nav-overlay"></div>')
            
            content = content[:nav_start] + new_navigation + content[nav_end:]
            replaced = True
    
    # Pattern 2: Look for simple nav without class
    if not replaced and '<nav>' in content:
        nav_start = content.find('<nav>')
        if nav_start != -1:
            nav_end = content.find('</nav>', nav_start) + 6
            content = content[:nav_start] + new_navigation + content[nav_end:]
            replaced = True
    
    # Pattern 3: Look for header with nav inside
    if not replaced:
        header_match = re.search(r'<header[^>]*>.*?</header>', content, re.DOTALL)
        if header_match:
            content = content.replace(header_match.group(0), new_navigation)
            replaced = True
    
    # Add navigation JS before closing body tag
    if 'navigation-enhanced.js' not in content:
        js_addition = '''
<!-- Enhanced Navigation JavaScript -->
<script src="../js/navigation-enhanced.js"></script>'''
        content = content.replace('</body>', js_addition + '\n</body>')
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {filepath}")
    return True

# List of main pages to update
main_pages = [
    'services/index.html',
    'practice-areas/index.html', 
    'about/index.html',
    'case-studies/index.html'
]

# Update each page
updated_count = 0
for page in main_pages:
    filepath = f'/Users/chrisskerritt/SEC/{page}'
    if os.path.exists(filepath):
        if update_navigation_in_file(filepath):
            updated_count += 1
    else:
        print(f"❌ File not found: {filepath}")

print(f"\n✅ Updated {updated_count} files with complete navigation")