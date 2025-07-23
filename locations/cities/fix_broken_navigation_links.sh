#!/bin/bash

# Fix broken navigation links containing -xx- state codes
# This script will identify and fix navigation links in the affected pages

echo "Fixing broken navigation links with -xx- state codes..."

# Fix Kansas City, KS pages
for file in kansas-city-ks-ks-*.html; do
    if [ -f "$file" ]; then
        echo "Fixing $file"
        sed -i '' 's/kansas-city-ks-xx-forensic-economist\.html/kansas-city-ks-forensic-economist.html/g' "$file"
        sed -i '' 's/kansas-city-ks-xx-business-valuation-analyst\.html/kansas-city-ks-business-valuation-analyst.html/g' "$file"
        sed -i '' 's/kansas-city-ks-xx-vocational-expert\.html/kansas-city-ks-ks-vocational-expert.html/g' "$file"
        sed -i '' 's/kansas-city-ks-xx-life-care-planner\.html/kansas-city-ks-ks-life-care-planner.html/g' "$file"
    fi
done

# Fix other affected cities
declare -a cities=(
    "charlotte-nc"
    "columbus-ne"
    "florence-sc"
    "evanston-wy"
    "auburn-wa"
    "bellevue-ne"
    "smyrna-tn"
    "lafayette-in"
    "columbus-ms"
    "meridian-id"
    "hartford-vt"
    "norfolk-ne"
    "smyrna-ga"
    "richmond-ky"
    "bristol-ri"
    "laurel-mt"
    "bloomington-mn"
    "lewiston-id"
    "springfield-or"
    "high-point-nc"
    "columbus-ga"
    "wilmington-de"
    "roswell-nm"
    "portsmouth-va"
    "concord-nc"
    "springfield-oh"
    "troy-ny"
    "st-albans-wv"
    "jacksonville-nc"
    "lakewood-oh"
)

for city in "${cities[@]}"; do
    # Extract state code from city name
    state=$(echo "$city" | cut -d'-' -f3)
    
    # Fix vocational expert pages
    ve_file="${city}-${state}-vocational-expert.html"
    if [ -f "$ve_file" ]; then
        echo "Fixing $ve_file"
        sed -i '' "s/${city}-xx-forensic-economist\.html/${city}-forensic-economist.html/g" "$ve_file"
        sed -i '' "s/${city}-xx-business-valuation-analyst\.html/${city}-business-valuation-analyst.html/g" "$ve_file"
        sed -i '' "s/${city}-xx-life-care-planner\.html/${city}-${state}-life-care-planner.html/g" "$ve_file"
    fi
    
    # Fix life care planner pages
    lcp_file="${city}-${state}-life-care-planner.html"
    if [ -f "$lcp_file" ]; then
        echo "Fixing $lcp_file"
        sed -i '' "s/${city}-xx-forensic-economist\.html/${city}-forensic-economist.html/g" "$lcp_file"
        sed -i '' "s/${city}-xx-business-valuation-analyst\.html/${city}-business-valuation-analyst.html/g" "$lcp_file"
        sed -i '' "s/${city}-xx-vocational-expert\.html/${city}-${state}-vocational-expert.html/g" "$lcp_file"
    fi
done

echo "Verifying fixes..."
remaining=$(grep -l "-xx-" *.html | wc -l)
echo "Remaining files with -xx- codes: $remaining"

if [ "$remaining" -eq 0 ]; then
    echo "✓ All broken navigation links have been fixed!"
else
    echo "⚠ Some files still contain -xx- codes. Manual review required."
    grep -l "-xx-" *.html
fi