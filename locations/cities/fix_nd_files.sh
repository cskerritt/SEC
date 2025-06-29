#!/bin/bash

# Function to fix a single file
fix_file() {
    local file=$1
    local city_name=$2
    local geo_lat=$3
    local geo_lon=$4
    local industries=$5
    
    echo "Fixing $file..."
    
    # Replace geo coordinates
    sed -i.bak "s/39.8283;-98.5795/${geo_lat};${geo_lon}/g" "$file"
    sed -i.bak "s/39.8283, -98.5795/${geo_lat}, ${geo_lon}/g" "$file"
    
    # Replace NYC references
    sed -i.bak "s/Manhattan, Brooklyn, Queens, Bronx, and Staten Island/North Dakota/g" "$file"
    sed -i.bak "s/NYC litigation/North Dakota litigation/g" "$file"
    sed -i.bak "s/five boroughs/region/g" "$file"
    sed -i.bak "s/NYC Markets/North Dakota Markets/g" "$file"
    sed -i.bak "s/New York Case/North Dakota Case/g" "$file"
    sed -i.bak "s/New York's federal and state court systems/North Dakota's federal and state court systems/g" "$file"
    sed -i.bak "s/New York litigation/North Dakota litigation/g" "$file"
    sed -i.bak "s/New York federal court/North Dakota federal court/g" "$file"
    sed -i.bak "s/New York state court/North Dakota state court/g" "$file"
    
    # Clean up backup files
    rm "${file}.bak"
}

# Fix Grafton
fix_file "grafton-nd-forensic-economist.html" "Grafton" "48.4211" "-97.4103"

# Fix Grand Forks
fix_file "grand-forks-nd-forensic-economist.html" "Grand Forks" "47.9254" "-97.0329"

# Fix Jamestown
fix_file "jamestown-nd-forensic-economist.html" "Jamestown" "46.9102" "-98.7084"

# Fix Mandan
fix_file "mandan-nd-forensic-economist.html" "Mandan" "46.8267" "-100.8897"

# Fix Valley City
fix_file "valley-city-nd-forensic-economist.html" "Valley City" "46.9230" "-98.0032"

# Fix Wahpeton
fix_file "wahpeton-nd-forensic-economist.html" "Wahpeton" "46.2652" "-96.6059"

# Fix Watford City
fix_file "watford-city-nd-forensic-economist.html" "Watford City" "47.8019" "-103.2829"

# Fix West Fargo
fix_file "west-fargo-nd-forensic-economist.html" "West Fargo" "46.8750" "-96.9001"

echo "All files fixed!"