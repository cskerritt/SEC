#!/usr/bin/env python3
import os
import glob

# CSS and JS to add
fix_code = '''<link href="../../css/ultimate-consistency-fix.css" rel="stylesheet"/>
<script src="../../js/force-navigation-fixed.js" defer></script>
</head>'''

def fix_city_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already fixed
    if 'force-navigation-fixed.js' in content:
        return False
    
    # Add fixes before </head>
    content = content.replace('</head>', fix_code)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Fix all city pages
city_pages = glob.glob('locations/cities/*.html')
fixed_count = 0

print(f"Found {len(city_pages)} city pages to fix")

for page in city_pages:
    if fix_city_page(page):
        fixed_count += 1
        if fixed_count % 100 == 0:
            print(f"Fixed {fixed_count} pages...")

print(f"\nFixed {fixed_count} city pages")
print("All city pages now have navigation fixes!")