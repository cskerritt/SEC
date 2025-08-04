const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1920, height: 1080 });
  
  await page.goto('http://localhost:4000/about/', { waitUntil: 'networkidle' });
  
  // Check text positioning issues
  const textIssues = await page.evaluate(() => {
    const results = {};
    
    // Check Professional Summary section
    const profSummary = document.querySelector('.about-section');
    if (profSummary) {
      const summaryStyles = window.getComputedStyle(profSummary);
      results.summaryPadding = summaryStyles.padding;
      results.summaryMargin = summaryStyles.margin;
      results.summaryMaxWidth = summaryStyles.maxWidth;
      
      const firstParagraph = profSummary.querySelector('p');
      if (firstParagraph) {
        const pStyles = window.getComputedStyle(firstParagraph);
        results.paragraphMargin = pStyles.margin;
        results.paragraphPadding = pStyles.padding;
        results.paragraphLineHeight = pStyles.lineHeight;
        results.paragraphFontSize = pStyles.fontSize;
        results.paragraphColor = pStyles.color;
        
        // Check if text is cut off
        const rect = firstParagraph.getBoundingClientRect();
        results.paragraphPosition = {
          left: rect.left,
          top: rect.top,
          width: rect.width
        };
      }
    }
    
    // Check container
    const container = document.querySelector('.about-content .container');
    if (container) {
      const containerStyles = window.getComputedStyle(container);
      results.containerPadding = containerStyles.padding;
      results.containerMaxWidth = containerStyles.maxWidth;
      results.containerMargin = containerStyles.margin;
    }
    
    // Check for any overflow issues
    const aboutContent = document.querySelector('.about-content');
    if (aboutContent) {
      results.contentOverflow = window.getComputedStyle(aboutContent).overflow;
      results.contentPadding = window.getComputedStyle(aboutContent).padding;
    }
    
    return results;
  });
  
  console.log('📄 ABOUT PAGE TEXT POSITIONING ANALYSIS\n');
  console.log('=' .repeat(60));
  
  console.log('\nProfessional Summary Section:');
  console.log('  Padding:', textIssues.summaryPadding);
  console.log('  Margin:', textIssues.summaryMargin);
  console.log('  Max Width:', textIssues.summaryMaxWidth);
  
  console.log('\nParagraph Styles:');
  console.log('  Margin:', textIssues.paragraphMargin);
  console.log('  Padding:', textIssues.paragraphPadding);
  console.log('  Line Height:', textIssues.paragraphLineHeight);
  console.log('  Font Size:', textIssues.paragraphFontSize);
  console.log('  Color:', textIssues.paragraphColor);
  
  console.log('\nParagraph Position:');
  console.log('  Left:', textIssues.paragraphPosition?.left);
  console.log('  Top:', textIssues.paragraphPosition?.top);
  console.log('  Width:', textIssues.paragraphPosition?.width);
  
  console.log('\nContainer:');
  console.log('  Padding:', textIssues.containerPadding);
  console.log('  Max Width:', textIssues.containerMaxWidth);
  console.log('  Margin:', textIssues.containerMargin);
  
  console.log('\nContent Area:');
  console.log('  Overflow:', textIssues.contentOverflow);
  console.log('  Padding:', textIssues.contentPadding);
  
  await browser.close();
})();