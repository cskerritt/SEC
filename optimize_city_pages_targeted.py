#!/usr/bin/env python3
"""
Targeted City Page SEO Optimization
Only processes files with title > 60 chars or description > 160 chars
"""

import os
import re
from pathlib import Path
import concurrent.futures
from collections import defaultdict

def check_seo_issues(filepath):
    """Quick check if file has SEO issues"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # Read only first 1000 chars for efficiency
            head = f.read(1000)
        
        # Extract title
        title_match = re.search(r'<title>([^<]+)</title>', head)
        if title_match and len(title_match.group(1)) > 60:
            return True
        
        # Extract description
        desc_match = re.search(r'<meta\s+(?:name="description"\s+content|content="[^"]*"\s+name="description")="([^"]+)"', head)
        if desc_match and len(desc_match.group(1)) > 160:
            return True
        
        return False
    except:
        return False

def create_optimized_content(city, state_abbr, service_type):
    """Create optimized title and description"""
    # Service type shortcuts
    service_map = {
        'forensic-economist': 'Forensic Economist',
        'business-valuation': 'Business Valuation', 
        'life-care-planner': 'Life Care Planner',
        'vocational-expert': 'Vocational Expert'
    }
    
    service = service_map.get(service_type, 'Expert')
    
    # Title: City ST Service (aim for < 60 chars)
    title = f"{city} {state_abbr.upper()} {service}"
    if len(title) > 60:
        # Use abbreviations
        title = title.replace('Forensic Economist', 'Forensic Econ')
        title = title.replace('Business Valuation', 'Biz Valuation')
        title = title.replace('Vocational Expert', 'Voc Expert')
    
    # Description: Keep under 160 chars
    desc = f"Expert {service.lower()} services in {city}, {state_abbr.upper()}. Court-qualified expert witness. Free consultation."
    
    return title, desc

def process_city_file(filepath):
    """Process a single city file"""
    try:
        # Parse filename
        filename = os.path.basename(filepath)
        match = re.match(r'(.+?)-([a-z]{2})-(.+?)\.html', filename)
        if not match:
            return None
        
        city = match.group(1).replace('-', ' ').title()
        state_abbr = match.group(2)
        service_type = match.group(3)
        
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes_made = False
        
        # Check and replace title
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match:
            original_title = title_match.group(1)
            if len(original_title) > 60:
                opt_title, _ = create_optimized_content(city, state_abbr, service_type)
                content = content.replace(f'<title>{original_title}</title>', 
                                        f'<title>{opt_title}</title>')
                changes_made = True
        
        # Check and replace description
        desc_pattern = r'<meta\s+name="description"\s+content="([^"]+)"'
        desc_match = re.search(desc_pattern, content)
        if not desc_match:
            desc_pattern = r'<meta\s+content="([^"]+)"\s+name="description"'
            desc_match = re.search(desc_pattern, content)
        
        if desc_match:
            original_desc = desc_match.group(1)
            if len(original_desc) > 160:
                _, opt_desc = create_optimized_content(city, state_abbr, service_type)
                new_meta = desc_match.group(0).replace(original_desc, opt_desc)
                content = content.replace(desc_match.group(0), new_meta)
                changes_made = True
        
        if changes_made:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return filepath
        
        return None
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def main():
    """Main function with parallel processing"""
    base_path = Path('/Users/chrisskerritt/SEC')
    cities_path = base_path / 'locations' / 'cities'
    
    print("Phase 3 SEO Optimization - City Pages (Targeted)")
    print("=" * 60)
    print("Scanning for files with SEO issues...")
    
    # First pass: identify files with issues
    city_files = list(cities_path.glob('*.html'))
    files_with_issues = []
    
    # Use parallel processing for scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_seo_issues, f): f for f in city_files}
        
        for future in concurrent.futures.as_completed(futures):
            filepath = futures[future]
            try:
                if future.result():
                    files_with_issues.append(filepath)
            except:
                pass
    
    print(f"Found {len(files_with_issues)} files with SEO issues out of {len(city_files)} total files")
    
    if not files_with_issues:
        print("No files need optimization!")
        return
    
    print(f"\nProcessing {len(files_with_issues)} files...")
    
    # Process files with issues
    processed_files = []
    batch_size = 100
    
    for i in range(0, len(files_with_issues), batch_size):
        batch = files_with_issues[i:i+batch_size]
        print(f"\nBatch {i//batch_size + 1}: Processing files {i+1}-{min(i+batch_size, len(files_with_issues))}")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(process_city_file, f) for f in batch]
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    processed_files.append(result)
        
        print(f"Progress: {len(processed_files)} files optimized")
    
    print("\n" + "=" * 60)
    print(f"Phase 3 SEO Optimization Complete!")
    print(f"Files optimized: {len(processed_files)}")
    
    # Group by state for summary
    if processed_files:
        state_counts = defaultdict(int)
        for f in processed_files:
            match = re.search(r'-([a-z]{2})-', str(f))
            if match:
                state_counts[match.group(1).upper()] += 1
        
        print("\nFiles optimized by state:")
        for state, count in sorted(state_counts.items()):
            print(f"  {state}: {count} files")

if __name__ == '__main__':
    main()