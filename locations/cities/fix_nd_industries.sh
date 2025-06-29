#!/bin/bash

# Function to replace NYC wage text
replace_wage_text() {
    local file=$1
    local city_description=$2
    
    sed -i.bak "s/The highest wages in the nation, complex career trajectories, substantial benefits packages, and significant cost of living variations across the region all require specialized expertise/${city_description}/g" "$file"
    rm "${file}.bak"
}

# Function to replace industry list
replace_industries() {
    local file=$1
    local industry_content=$2
    
    # Create temporary file with the replacement
    awk -v new_content="$industry_content" '
    /<li><strong>Manhattan Premium Wages:/ {
        skip = 1
        print new_content
    }
    /<li><strong>Staten Island Economy:/ && skip {
        skip = 0
        next
    }
    !skip { print }
    ' "$file" > "${file}.tmp"
    
    mv "${file}.tmp" "$file"
}

# Fix Grafton
replace_wage_text "grafton-nd-forensic-economist.html" "The region's agricultural economy, potato processing industry, and border location create unique employment patterns that require specialized expertise"
replace_industries "grafton-nd-forensic-economist.html" "                            <li><strong>Agricultural Operations:</strong> Potato farming, sugar beet production, and grain operations</li>
                            <li><strong>Food Processing:</strong> Simplot potato processing and agricultural processing</li>
                            <li><strong>Border Economy:</strong> Cross-border trade and transportation with Canada</li>
                            <li><strong>Healthcare Services:</strong> Unity Medical Center and regional healthcare</li>
                            <li><strong>Local Industries:</strong> Retail, education, and government services</li>"

# Fix Jamestown
replace_wage_text "jamestown-nd-forensic-economist.html" "The region's manufacturing base, healthcare sector, and agricultural economy create unique employment patterns that require specialized expertise"
replace_industries "jamestown-nd-forensic-economist.html" "                            <li><strong>Manufacturing:</strong> Cavendish Farms, Goodrich Corporation, and industrial operations</li>
                            <li><strong>Healthcare Sector:</strong> Jamestown Regional Medical Center and healthcare services</li>
                            <li><strong>Education:</strong> University of Jamestown and educational institutions</li>
                            <li><strong>Agricultural Economy:</strong> Farming, ranching, and agribusiness operations</li>
                            <li><strong>Regional Services:</strong> Retail, hospitality, and professional services</li>"

# Fix Mandan
replace_wage_text "mandan-nd-forensic-economist.html" "The region's energy sector, refinery operations, and proximity to the state capital create unique employment patterns that require specialized expertise"
replace_industries "mandan-nd-forensic-economist.html" "                            <li><strong>Energy Industry:</strong> Marathon Petroleum refinery and energy operations</li>
                            <li><strong>Railroad & Transportation:</strong> Historic railroad hub and logistics services</li>
                            <li><strong>Government Employment:</strong> State facilities and correctional services</li>
                            <li><strong>Healthcare Services:</strong> Sanford Health and regional medical facilities</li>
                            <li><strong>Local Economy:</strong> Retail, construction, and professional services</li>"

# Fix Minot (already partially fixed, but needs industry update)
replace_wage_text "minot-nd-forensic-economist.html" "The region's Air Force base, energy sector growth, and regional hub status create unique employment patterns that require specialized expertise"
replace_industries "minot-nd-forensic-economist.html" "                            <li><strong>Minot Air Force Base:</strong> Military employment and defense contractors</li>
                            <li><strong>Energy Sector:</strong> Bakken oil field services and energy infrastructure</li>
                            <li><strong>Healthcare Systems:</strong> Trinity Health and regional medical services</li>
                            <li><strong>Education:</strong> Minot State University and educational institutions</li>
                            <li><strong>Regional Commerce:</strong> Retail hub, transportation, and professional services</li>"

# Fix Valley City
replace_wage_text "valley-city-nd-forensic-economist.html" "The region's manufacturing sector, educational institutions, and agricultural base create unique employment patterns that require specialized expertise"
replace_industries "valley-city-nd-forensic-economist.html" "                            <li><strong>Manufacturing:</strong> John Deere seeding equipment and industrial operations</li>
                            <li><strong>Education:</strong> Valley City State University and educational services</li>
                            <li><strong>Healthcare:</strong> CHI Mercy Health and regional healthcare providers</li>
                            <li><strong>Agricultural Economy:</strong> Farming operations and agribusiness services</li>
                            <li><strong>Local Services:</strong> Retail, hospitality, and government employment</li>"

# Fix Wahpeton
replace_wage_text "wahpeton-nd-forensic-economist.html" "The region's technical education focus, manufacturing base, and agricultural economy create unique employment patterns that require specialized expertise"
replace_industries "wahpeton-nd-forensic-economist.html" "                            <li><strong>Technical Education:</strong> North Dakota State College of Science</li>
                            <li><strong>Manufacturing:</strong> WCCO Belting, Minn-Dak Farmers Cooperative</li>
                            <li><strong>Healthcare Services:</strong> CHI St. Francis Health and medical facilities</li>
                            <li><strong>Agricultural Processing:</strong> Sugar beet processing and agribusiness</li>
                            <li><strong>Regional Economy:</strong> Retail, construction, and professional services</li>"

# Fix Watford City
replace_wage_text "watford-city-nd-forensic-economist.html" "The region's oil boom economy, rapid growth, and Bakken shale development create unique employment patterns that require specialized expertise"
replace_industries "watford-city-nd-forensic-economist.html" "                            <li><strong>Oil & Gas Industry:</strong> Bakken shale operations and oil field services</li>
                            <li><strong>Energy Infrastructure:</strong> Pipeline construction and energy logistics</li>
                            <li><strong>Support Services:</strong> Housing, transportation, and equipment services</li>
                            <li><strong>Healthcare:</strong> McKenzie County Healthcare System</li>
                            <li><strong>Boom Economy:</strong> Construction, retail, and hospitality services</li>"

# Fix West Fargo
replace_wage_text "west-fargo-nd-forensic-economist.html" "The region's rapid growth, diverse economy, and proximity to Fargo create unique employment patterns that require specialized expertise"
replace_industries "west-fargo-nd-forensic-economist.html" "                            <li><strong>Manufacturing:</strong> Case New Holland, Wil-Rich, and industrial operations</li>
                            <li><strong>Technology Sector:</strong> Microsoft campus and technology companies</li>
                            <li><strong>Healthcare Services:</strong> Essentia Health and medical facilities</li>
                            <li><strong>Retail & Commerce:</strong> Regional shopping and commercial services</li>
                            <li><strong>Growth Economy:</strong> Construction, real estate, and professional services</li>"

echo "All ND files industry sections fixed!"