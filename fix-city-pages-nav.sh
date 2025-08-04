#!/bin/bash

echo "Adding navigation fixes to all city pages..."

# Add the CSS and JS fixes to all city HTML files
for file in locations/cities/*.html; do
  if [ -f "$file" ]; then
    # Check if already has the fix
    if grep -q "force-navigation-fixed.js" "$file"; then
      continue
    fi
    
    # Add our fix CSS and JS before </head>
    sed -i.bak '/<\/head>/i\
<link href="../../css/ultimate-consistency-fix.css" rel="stylesheet"/>\
<script src="../../js/force-navigation-fixed.js" defer></script>' "$file"
    
    echo "Fixed: $file"
  fi
done

echo "Navigation fixes added to city pages"

# Clean up backup files
rm -f locations/cities/*.bak