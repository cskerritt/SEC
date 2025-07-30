#!/usr/bin/env python3
"""
Review and update all city pages to ensure objective and neutral language
"""

import os
import re

def neutralize_content(content):
    """Replace potentially promotional language with neutral alternatives"""
    
    replacements = [
        # Promotional adjectives to neutral
        (r'\bcompelling\s+testimony\b', 'testimony'),
        (r'\bcompelling\s+courtroom\s+testimony\b', 'courtroom testimony'),
        (r'\bclear,\s+compelling\s+testimony\b', 'clear testimony'),
        (r'\bcompetitive\s+expert\s+witness\s+fees\b', 'expert witness fees'),
        (r'\bcompetitive\s+professional\s+fees\b', 'professional fees'),
        (r'\bextensive\s+testimony\s+experience\b', 'testimony experience'),
        (r'\bdeep\s+understanding\b', 'understanding'),
        (r'\bdeep\s+knowledge\b', 'knowledge'),
        (r'\brigorous\s+economic\s+methodology\b', 'economic methodology'),
        (r'\bwell-documented\s+expert\s+reports\b', 'expert reports'),
        (r'\brapid\s+response\b', 'timely response'),
        (r'\bdefensible\s+(methodologies|valuations|damage calculations|life care plans)\b', r'\1'),
        
        # Headers and phrases
        (r'Why Choose Our', 'About Our'),
        (r'Why\s+([A-Za-z\s]+)\s+Law Firms Choose', r'\1 Law Firms Work With'),
        (r'Why\s+([A-Za-z\s]+)\s+Attorneys Choose', r'\1 Attorneys Work With'),
        (r'Get Started Today', 'Contact Information'),
        (r'Schedule.*?Consultation', 'Request Consultation'),
        
        # Remove superlatives
        (r'\bbest\b', 'effective'),
        (r'\bsuperior\b', 'professional'),
        (r'\bleading\b', 'experienced'),
        (r'\bexceptional\b', 'professional'),
        (r'\boutstanding\b', 'professional'),
        (r'\bpremier\b', 'professional'),
        (r'\btop\b', 'experienced'),
        (r'\bunmatched\b', 'comprehensive'),
        
        # Soften claims
        (r'expertise with', 'experience with'),
        (r'expert testimony that clearly explains', 'expert testimony explaining'),
        (r'meet.*?court requirements and withstand scrutiny', 'meet court requirements'),
        (r'combines? (rigorous|proven|extensive)', 'uses'),
        (r'comprehensive economic damage analysis', 'economic damage analysis'),
        (r'comprehensive (future medical|employability|business)', r'\1'),
        
        # Professional descriptors
        (r'court-qualified expert witnesses?', 'expert witnesses'),
        (r'credentialed (valuation |)professionals?', r'\1professionals'),
        (r'certified (life care planners?|rehabilitation counselors?)', r'\1'),
        
        # Remove emphasis words
        (r'\bvery\s+', ''),
        (r'\bhighly\s+', ''),
        (r'\bextremely\s+', ''),
        (r'\btruly\s+', ''),
        (r'\babsolutely\s+', ''),
    ]
    
    # Apply replacements
    updated_content = content
    for pattern, replacement in replacements:
        updated_content = re.sub(pattern, replacement, updated_content, flags=re.IGNORECASE)
    
    return updated_content

def process_file(filepath):
    """Process a single file to neutralize language"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Neutralize content
        updated_content = neutralize_content(content)
        
        # Only write if changes were made
        if content != updated_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview-system.html']

print(f"Reviewing {len(html_files)} files for neutral language...")

updated_count = 0
for filename in html_files:
    if process_file(filename):
        updated_count += 1
        if updated_count <= 10:  # Show first 10 updates
            print(f"Updated: {filename}")

print(f"\nTotal files updated: {updated_count}")
print("\nKey changes made:")
print("- Replaced promotional adjectives with neutral terms")
print("- Softened absolute claims")
print("- Removed superlatives")
print("- Updated 'Why Choose' sections to 'About Our' or 'Work With'")
print("- Simplified professional descriptors")