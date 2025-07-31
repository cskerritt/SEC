// Mobile Select Fix for Table of Contents and other select elements
document.addEventListener('DOMContentLoaded', function() {
    // Function to fix select element styling
    function fixSelectStyling() {
        const selectElements = document.querySelectorAll('select');
        
        selectElements.forEach(select => {
            // Ensure text color is dark
            select.style.color = '#1f2937';
            select.style.backgroundColor = 'white';
            
            // Add aria-label if it's a TOC select
            if (select.parentElement && (
                select.parentElement.classList.contains('mobile-toc') ||
                select.parentElement.classList.contains('toc-dropdown') ||
                select.textContent.includes('Table of Contents')
            )) {
                select.setAttribute('aria-label', 'Table of Contents Navigation');
            }
        });
    }
    
    // Run the fix initially
    fixSelectStyling();
    
    // Watch for dynamically added select elements
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.addedNodes.length) {
                mutation.addedNodes.forEach(node => {
                    if (node.nodeName === 'SELECT' || (node.querySelector && node.querySelector('select'))) {
                        fixSelectStyling();
                    }
                });
            }
        });
    });
    
    // Start observing the document body for changes
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    // Additional fix for mobile TOC if it exists
    const mobileTOC = document.querySelector('.mobile-toc');
    if (mobileTOC) {
        // Check if there's a select element inside
        const tocSelect = mobileTOC.querySelector('select');
        if (tocSelect) {
            tocSelect.style.color = '#1f2937';
            tocSelect.style.backgroundColor = 'white';
            tocSelect.style.border = '1px solid #e5e7eb';
        }
    }
});