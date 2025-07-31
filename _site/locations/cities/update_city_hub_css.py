#!/usr/bin/env python3

import os
import re

def update_css_in_hub_files():
    """Update CSS reference in city hub files"""
    
    # List of city hub files (without service suffix)
    hub_files = [
        "los-angeles-ca.html", "chicago-il.html", "houston-tx.html", 
        "phoenix-az.html", "philadelphia-pa.html", "san-antonio-tx.html",
        "san-diego-ca.html", "dallas-tx.html", "san-jose-ca.html",
        "austin-tx.html", "jacksonville-fl.html", "san-francisco-ca.html",
        "columbus-oh.html", "fort-worth-tx.html", "indianapolis-in.html",
        "charlotte-nc.html", "seattle-wa.html", "denver-co.html",
        "washington-dc.html", "boston-ma.html", "el-paso-tx.html",
        "nashville-tn.html", "detroit-mi.html", "oklahoma-city-ok.html",
        "portland-or.html", "las-vegas-nv.html", "memphis-tn.html",
        "louisville-ky.html", "baltimore-md.html", "milwaukee-wi.html",
        "albuquerque-nm.html", "tucson-az.html", "fresno-ca.html",
        "sacramento-ca.html", "mesa-az.html", "kansas-city-mo.html",
        "atlanta-ga.html", "omaha-ne.html", "colorado-springs-co.html",
        "raleigh-nc.html", "long-beach-ca.html", "virginia-beach-va.html",
        "miami-fl.html", "oakland-ca.html", "minneapolis-mn.html",
        "tulsa-ok.html", "bakersfield-ca.html", "wichita-ks.html",
        "arlington-tx.html", "aurora-co.html", "new-york-ny.html"
    ]
    
    updated_count = 0
    
    for filename in hub_files:
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                
                # Replace city-pages.css with city-pages-enhanced.css
                updated_content = content.replace(
                    '<link rel="stylesheet" href="../../css/city-pages.css">',
                    '<link rel="stylesheet" href="../../css/city-pages-enhanced.css">'
                )
                
                # Only write if changes were made
                if content != updated_content:
                    with open(filename, 'w') as f:
                        f.write(updated_content)
                    updated_count += 1
                    print(f"Updated: {filename}")
            except Exception as e:
                print(f"Error updating {filename}: {e}")
    
    print(f"\nTotal hub files updated: {updated_count}")

if __name__ == "__main__":
    update_css_in_hub_files()