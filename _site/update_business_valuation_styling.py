#!/usr/bin/env python3
"""
Script to update business valuation analyst pages with custom CSS styling
and hero section structure to match forensic economist pages.
"""

import os
import re
import sys

# The custom CSS styling to add
CUSTOM_CSS = '''    <style>
        .hero-section {
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
            color: white;
            padding: 120px 0 80px;
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
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
            opacity: 0.3;
        }
        
        .hero-content {
            position: relative;
            z-index: 2;
        }
        
        .hero-content h1 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }
        
        .hero-content p {
            font-size: 1.25rem;
            opacity: 0.95;
            max-width: 600px;
            line-height: 1.6;
        }
        
        .location-badges {
            display: flex;
            gap: 15px;
            margin-top: 30px;
            flex-wrap: wrap;
        }
        
        .badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 14px;
            font-weight: 500;
            backdrop-filter: blur(10px);
        }
        
        .content-section {
            padding: 80px 0;
        }
        
        .intro-text {
            font-size: 1.125rem;
            color: #4b5563;
            line-height: 1.8;
            margin-bottom: 40px;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            margin: 60px 0;
        }
        
        .feature-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-left: 4px solid #1e40af;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        }
        
        .feature-card h3 {
            color: #1e40af;
            margin-bottom: 15px;
            font-size: 1.25rem;
        }
        
        .feature-card p {
            color: #6b7280;
            line-height: 1.6;
        }
        
        .courts-section {
            background: #f8fafc;
            padding: 60px 0;
        }
        
        .courts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .court-item {
            background: white;
            padding: 20px;
            border-radius: 8px;
            border-left: 3px solid #10b981;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        }
        
        .industries-section {
            padding: 80px 0;
        }
        
        .industry-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 30px;
        }
        
        .industry-tag {
            background: #e0f2fe;
            color: #0f172a;
            padding: 10px 18px;
            border-radius: 25px;
            font-weight: 500;
            font-size: 14px;
            border: 1px solid #0ea5e9;
            transition: all 0.3s ease;
        }
        
        .industry-tag:hover {
            background: #0ea5e9;
            color: white;
        }
        
        .tools-showcase {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
            padding: 80px 0;
        }
        
        .tools-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .tool-card {
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 3px 15px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .tool-card:hover {
            transform: translateY(-3px);
        }
        
        .tool-card h4 {
            color: #1e40af;
            margin-bottom: 10px;
        }
        
        .tool-card p {
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 20px;
        }
        
        .tool-btn {
            background: #1e40af;
            color: white;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 500;
            transition: background 0.3s ease;
        }
        
        .tool-btn:hover {
            background: #1e3a8a;
            color: white;
            text-decoration: none;
        }
        
        .cta-section {
            background: #1e40af;
            color: white;
            padding: 80px 0;
            text-align: center;
        }
        
        .cta-section h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        
        .cta-section p {
            font-size: 1.125rem;
            opacity: 0.9;
            margin-bottom: 30px;
        }
        
        .cta-btn {
            background: #10b981;
            color: white;
            padding: 15px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 1.125rem;
            transition: all 0.3s ease;
        }
        
        .cta-btn:hover {
            background: #059669;
            color: white;
            text-decoration: none;
            transform: translateY(-2px);
        }
        
        .sidebar {
            position: sticky;
            top: 100px;
        }
        
        .contact-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
            text-align: center;
        }
        
        .contact-card h3 {
            color: #1e40af;
            margin-bottom: 15px;
        }
        
        .contact-info {
            margin: 20px 0;
        }
        
        .contact-info p {
            margin: 8px 0;
        }
        
        .credentials-card {
            background: #f8fafc;
            padding: 25px;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
        }
        
        .credentials-card h4 {
            color: #1e40af;
            margin-bottom: 15px;
        }
        
        .credentials-list {
            list-style: none;
            padding: 0;
        }
        
        .credentials-list li {
            padding: 8px 0;
            border-bottom: 1px solid #e2e8f0;
            position: relative;
            padding-left: 20px;
        }
        
        .credentials-list li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: bold;
        }
        
        .content-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 60px;
            align-items: start;
        }
        
        .seo-content {
            margin: 60px 0;
        }
        
        .seo-content h2 {
            color: #1e40af;
            margin-bottom: 20px;
        }
        
        .seo-content h3 {
            color: #374151;
            margin: 30px 0 15px 0;
        }
        
        .service-areas-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        
        .area-item {
            background: #f1f5f9;
            padding: 10px 15px;
            border-radius: 6px;
            border-left: 3px solid #0ea5e9;
            font-size: 14px;
        }
        
        @media (max-width: 968px) {
            .content-grid {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            
            .hero-content h1 {
                font-size: 2.5rem;
            }
            
            .sidebar {
                position: relative;
                top: auto;
            }
        }
    </style>'''

def update_business_valuation_file(file_path):
    """Update a single business valuation file with custom CSS and hero structure."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the file already has the custom styling
        if '.hero-section {' in content:
            print(f"✓ {file_path} already has custom styling")
            return True
        
        # Add custom CSS before </head>
        content = content.replace('</head>', f'{CUSTOM_CSS}\n</head>')
        
        # Replace location-hero with hero-section
        content = content.replace('class="location-hero"', 'class="hero-section"')
        
        # Update hero structure - look for the current hero-stats and hero-cta patterns
        # and replace with location-badges structure
        
        # Look for existing hero-stats pattern and replace with badges
        hero_stats_pattern = r'<div class="hero-stats">.*?</div>\s*<div class="hero-cta">.*?</div>'
        hero_replacement = '''<div class="location-badges">
                    <span class="badge">Certified Appraiser</span>
                    <span class="badge">Business Valuation Expert</span>
                    <span class="badge">Litigation Support</span>
                    <span class="badge">Fast Turnaround</span>
                </div>'''
        
        content = re.sub(hero_stats_pattern, hero_replacement, content, flags=re.DOTALL)
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function to update all business valuation files."""
    
    # List of files to update (first 150)
    files = [
        "/Users/chrisskerritt/SEC/locations/cities/blue-springs-mo-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/fall-river-ma-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/san-francisco-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/smyrna-tn-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/johnston-ri-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/livingston-mt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/meridian-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/savannah-ga-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/caldwell-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/sioux-falls-sd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/lexington-ky-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/joliet-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/nashua-nh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/clayton-de-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/norwalk-ct-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/pine-bluff-ar-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/spearfish-sd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/portland-or-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/kahului-hi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/dodge-city-ks-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/greensboro-nc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/logan-ut-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/federal-way-wa-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/durham-nc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/longmont-co-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/greenbelt-md-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/provo-ut-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/bridgeport-ct-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/berlin-nh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/hagerstown-md-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/lake-oswego-or-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/des-moines-ia-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/el-paso-tx-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/lees-summit-mo-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/easton-pa-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/worcester-ma-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/eugene-or-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/bellevue-ne-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/kenosha-wi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/erie-pa-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/north-charleston-sc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/soldotna-ak-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/missoula-mt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/rochester-mn-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/orono-me-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/west-des-moines-ia-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/champaign-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/riverton-wy-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/medford-or-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/kuna-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/elko-nv-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/pittsburgh-pa-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/shawnee-ok-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/mesa-az-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/sheridan-wy-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/beulah-nd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/hutchinson-ks-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/council-bluffs-ia-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/biddeford-me-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/bartlett-tn-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/wichita-ks-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/irving-tx-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/clovis-nm-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/harrington-de-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/eau-claire-wi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/south-burlington-vt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/charles-town-wv-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/minnetonka-mn-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/florence-ky-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/baltimore-md-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/jamestown-nd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/naperville-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/decatur-al-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/loveland-co-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/santa-ana-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/north-las-vegas-nv-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/kaneohe-hi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/boulder-city-nv-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/grafton-nd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/aiken-sc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/stockton-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/flagstaff-az-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/bentonville-ar-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/elyria-oh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/athens-ga-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/cleveland-oh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/westminster-md-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/miles-city-mt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/central-falls-ri-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/rochester-nh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/columbus-ne-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/manhattan-ks-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/waukegan-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/huron-sd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/ridgeland-ms-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/olive-branch-ms-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/west-jordan-ut-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/alexandria-va-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/wilkes-barre-pa-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/mount-pleasant-sc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/sioux-city-ia-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/north-providence-ri-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/terre-haute-in-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/phoenix-az-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/san-diego-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/milford-de-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/schenectady-ny-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/presque-isle-me-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/decatur-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/hialeah-fl-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/madison-al-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/coral-springs-fl-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/keene-nh-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/high-point-nc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/slidell-la-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/newark-de-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/little-rock-ar-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/charlotte-nc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/lewiston-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/mount-vernon-ny-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/essex-vt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/chapel-hill-nc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/georgetown-ky-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/laurel-mt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/topeka-ks-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/boise-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/marrero-la-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/yankton-sd-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/waipahu-hi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/saint-joseph-mo-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/new-rochelle-ny-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/greenville-ms-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/irvine-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/barre-vt-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/north-platte-ne-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/ankeny-ia-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/schaumburg-il-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/miramar-fl-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/myrtle-beach-sc-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/fond-du-lac-wi-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/san-jose-ca-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/idaho-falls-id-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/greenwich-ct-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/springfield-or-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/minneapolis-mn-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/grand-island-ne-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/smyrna-de-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/norfolk-ne-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/conway-ar-business-valuation-analyst.html",
        "/Users/chrisskerritt/SEC/locations/cities/west-haven-ct-business-valuation-analyst.html"
    ]
    
    print(f"Updating {len(files)} business valuation analyst pages...")
    
    success_count = 0
    error_count = 0
    
    for file_path in files:
        if update_business_valuation_file(file_path):
            success_count += 1
        else:
            error_count += 1
    
    print(f"\n=== Update Summary ===")
    print(f"✓ Successfully updated: {success_count} files")
    print(f"✗ Errors: {error_count} files")
    print(f"Total processed: {len(files)} files")

if __name__ == "__main__":
    main()