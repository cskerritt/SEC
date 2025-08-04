#!/bin/bash

echo "Finding all HTML files in _site directory..."
files=$(find _site -name "*.html" -type f 2>/dev/null)
total=$(echo "$files" | wc -l | tr -d ' ')

echo "Found $total HTML files to test"
echo ""
echo "Testing navigation on ALL pages..."
echo "================================================================================"

# Create a Node.js script to test a single page
cat > test-single-page.js << 'EOF'
const { chromium } = require('playwright');

(async () => {
  const url = process.argv[2];
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 5000 });
    await page.waitForTimeout(600);
    
    const result = await page.evaluate(() => {
      const nav = document.querySelector('.main-nav');
      if (!nav) return 'NO_NAV';
      
      const computedStyles = window.getComputedStyle(nav);
      const inlineStyles = nav.style;
      const finalPosition = inlineStyles.position || computedStyles.position;
      
      return finalPosition === 'fixed' ? 'FIXED' : finalPosition.toUpperCase();
    });
    
    console.log(result);
  } catch (error) {
    console.log('ERROR');
  }
  
  await browser.close();
})();
EOF

fixed=0
not_fixed=0
no_nav=0
errors=0
counter=0

# Test each file
while IFS= read -r file; do
  counter=$((counter + 1))
  
  # Convert file path to URL
  url_path=${file#_site/}
  url="http://localhost:4000/$url_path"
  
  # Test the page
  result=$(node test-single-page.js "$url" 2>/dev/null)
  
  case "$result" in
    "FIXED")
      fixed=$((fixed + 1))
      ;;
    "NO_NAV")
      no_nav=$((no_nav + 1))
      echo "❌ No navigation: $url_path"
      ;;
    "ERROR")
      errors=$((errors + 1))
      ;;
    *)
      not_fixed=$((not_fixed + 1))
      echo "❌ Not fixed ($result): $url_path"
      ;;
  esac
  
  # Show progress
  if [ $((counter % 100)) -eq 0 ]; then
    echo "Progress: $counter/$total pages tested..."
  fi
done <<< "$files"

echo ""
echo "================================================================================"
echo "FINAL RESULTS"
echo "================================================================================"
echo "Total pages tested: $total"
echo "Pages with FIXED navigation: $fixed"
echo "Pages with NON-FIXED navigation: $not_fixed"
echo "Pages with NO navigation: $no_nav"
echo "Pages with errors: $errors"
echo ""

success_rate=$(echo "scale=1; $fixed * 100 / $total" | bc)
echo "Success rate: ${success_rate}%"

if [ $not_fixed -eq 0 ] && [ $no_nav -eq 0 ]; then
  echo ""
  echo "✅ SUCCESS: All pages have fixed navigation!"
else
  echo ""
  echo "❌ ISSUES FOUND: $((not_fixed + no_nav)) pages need fixes"
fi

# Clean up
rm -f test-single-page.js