#!/usr/bin/env python3
"""
Phase 1 SEO Optimization Script
Optimizes titles and meta descriptions for high-priority pages
"""

import os
import re
from pathlib import Path

def optimize_title(title):
    """Optimize title to be under 60 characters while maintaining SEO value"""
    if len(title) <= 60:
        return title
    
    # Decode HTML entities first
    title = title.replace('&amp;', '&')
    
    # Define optimization patterns - apply in order of preference
    optimizations = [
        # First try: Remove secondary branding
        (r'\s*\|\s*Skerritt Economics$', ''),
        # Second try: Shorten expert phrases
        (r'\s*\|\s*Rhode Island Expert\s*\|\s*Skerritt', ' | RI | Skerritt'),
        (r'Forensic Economist & Business Valuation Expert', 'Forensic Economist & Valuation'),
        # Third try: Use state abbreviations
        (r'Rhode Island', 'RI'),
        (r'Connecticut', 'CT'),
        (r'Massachusetts', 'MA'),
        (r'New Hampshire', 'NH'),
        (r'New Jersey', 'NJ'),
        (r'New York', 'NY'),
        (r'North Carolina', 'NC'),
        (r'Pennsylvania', 'PA'),
        (r'California', 'CA'),
        (r'Illinois', 'IL'),
        (r'Michigan', 'MI'),
        (r'Florida', 'FL'),
        (r'Georgia', 'GA'),
        (r'Texas', 'TX'),
        (r'Ohio', 'OH'),
        # Fourth try: Shorten service names
        (r'Forensic Economics', 'Forensic Econ'),
        (r'Business Valuation', 'Biz Valuation'),
        (r'Life Care Planning', 'Life Care Plan'),
        (r'Vocational Expert', 'Voc Expert'),
        (r'Employment & Earning Capacity Analysis', 'Employment Analysis'),
        (r'Future Medical Cost Analysis', 'Medical Cost Analysis'),
        # Last resort: Remove 'Expert' if still too long
        (r' Expert', ''),
    ]
    
    optimized = title
    for pattern, replacement in optimizations:
        new_optimized = re.sub(pattern, replacement, optimized)
        # Only apply if it actually reduces length
        if len(new_optimized) < len(optimized):
            optimized = new_optimized
            if len(optimized) <= 60:
                break
    
    # Re-encode ampersands for HTML
    optimized = optimized.replace('&', '&amp;')
    
    return optimized

def optimize_description(description):
    """Optimize meta description to be under 160 characters while maintaining value"""
    if len(description) <= 160:
        return description
    
    # Try to cut at a sentence boundary
    if '. ' in description[:160]:
        cut_point = description[:160].rfind('. ') + 1
        return description[:cut_point].strip()
    
    # Otherwise, cut at word boundary and add ellipsis
    cut_point = description[:157].rfind(' ')
    return description[:cut_point] + '...'

def process_file(filepath):
    """Process a single HTML file to optimize SEO elements"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes_made = False
    
    # Extract and optimize title
    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if title_match:
        original_title = title_match.group(1).strip()
        optimized_title = optimize_title(original_title)
        if original_title != optimized_title:
            content = content.replace(f'<title>{original_title}</title>', 
                                    f'<title>{optimized_title}</title>')
            changes_made = True
            print(f"  Title: {len(original_title)} → {len(optimized_title)} chars")
            print(f"    Old: {original_title}")
            print(f"    New: {optimized_title}")
    
    # Extract and optimize meta description
    desc_match = re.search(r'<meta\s+(?:name="description"|content="[^"]*"\s+name="description")\s+content="([^"]*)"', content)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content="([^"]*)"\s+name="description"', content)
    
    if desc_match:
        original_desc = desc_match.group(1)
        optimized_desc = optimize_description(original_desc)
        if original_desc != optimized_desc:
            # Replace the entire meta tag to maintain structure
            old_tag = desc_match.group(0)
            new_tag = old_tag.replace(original_desc, optimized_desc)
            content = content.replace(old_tag, new_tag)
            changes_made = True
            print(f"  Description: {len(original_desc)} → {len(optimized_desc)} chars")
            print(f"    Old: {original_desc[:80]}...")
            print(f"    New: {optimized_desc[:80]}...")
    
    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to process high-priority files"""
    
    # Define high-priority files
    priority_files = [
        # Main service pages
        'services/index.html',
        'services/forensic-economics/index.html',
        'services/business-valuation/index.html',
        'services/life-care-planning/index.html',
        'services/vocational-expert/index.html',
        
        # Main pages
        'index.html',
        'about/index.html',
        'contact/index.html',
        'testimonials/index.html',
        
        # Top state pages (based on population/market size)
        'locations/california.html',
        'locations/texas.html',
        'locations/florida.html',
        'locations/new-york.html',
        'locations/pennsylvania.html',
        'locations/illinois.html',
        'locations/ohio.html',
        'locations/georgia.html',
        'locations/north-carolina.html',
        'locations/michigan.html',
        
        # Blog category pages
        'blog/index.html',
        'blog/tags/index.html',
    ]
    
    base_path = Path('/Users/chrisskerritt/SEC')
    files_processed = 0
    files_changed = 0
    
    print("Starting Phase 1 SEO Optimization...")
    print("=" * 60)
    
    for relative_path in priority_files:
        filepath = base_path / relative_path
        if filepath.exists():
            print(f"\nProcessing: {relative_path}")
            if process_file(filepath):
                files_changed += 1
            files_processed += 1
        else:
            print(f"\nSkipping (not found): {relative_path}")
    
    print("\n" + "=" * 60)
    print(f"Phase 1 SEO Optimization Complete!")
    print(f"Files processed: {files_processed}")
    print(f"Files changed: {files_changed}")

if __name__ == '__main__':
    main()