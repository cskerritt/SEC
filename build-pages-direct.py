#!/usr/bin/env python3
"""
Direct page builder to bypass Jekyll issues
"""

import os
import shutil
from pathlib import Path

def process_page_with_layout(page_path, layout_path, output_path):
    """Process a page with its layout"""
    
    # Read the page content
    with open(page_path, 'r') as f:
        page_content = f.read()
    
    # Skip the front matter
    if page_content.startswith('---'):
        parts = page_content.split('---', 2)
        if len(parts) >= 3:
            page_content = parts[2].strip()
    
    # Read the layout
    with open(layout_path, 'r') as f:
        layout_content = f.read()
    
    # Replace {{ content }} with page content
    final_html = layout_content.replace('{{ content }}', page_content)
    
    # Basic variable replacements
    final_html = final_html.replace('{{ site.title }}', 'Skerritt Economics & Consulting')
    final_html = final_html.replace('{{ site.description }}', 'Expert forensic economics and business valuation services')
    final_html = final_html.replace("{{ '/css/modern-ui.css' | relative_url }}", "/css/modern-ui.css")
    final_html = final_html.replace("{{ '/favicon-32x32.png' | relative_url }}", "/favicon-32x32.png")
    final_html = final_html.replace("{{ '/favicon-16x16.png' | relative_url }}", "/favicon-16x16.png")
    
    # Handle page variables
    final_html = final_html.replace('{% if page.title %}{{ page.title }} - {% endif %}', '')
    final_html = final_html.replace('{% if page.description %}{{ page.description }}{% else %}{{ site.description }}{% endif %}', 
                                   'Expert forensic economics and business valuation services')
    
    # Remove remaining Liquid tags
    import re
    final_html = re.sub(r'{%.*?%}', '', final_html)
    final_html = re.sub(r'{{.*?}}', '', final_html)
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the output
    with open(output_path, 'w') as f:
        f.write(final_html)
    
    print(f"✅ Built: {output_path}")

def main():
    """Build the locations and contact pages"""
    
    print("🔨 Building pages directly...")
    
    # Build locations page
    process_page_with_layout(
        'locations/index.html',
        '_layouts/modern-default.html',
        '_site/locations/index.html'
    )
    
    # Build contact page
    process_page_with_layout(
        'contact/index.html',
        '_layouts/modern-default.html',
        '_site/contact/index.html'
    )
    
    print("\n✅ Pages built successfully!")
    print("\nYou can now view them at:")
    print("- http://localhost:8888/locations/")
    print("- http://localhost:8888/contact/")

if __name__ == "__main__":
    main()