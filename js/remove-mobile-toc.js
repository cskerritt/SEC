/* Remove Mobile TOC Script */
(function() {
    'use strict';
    
    // Function to remove all TOC elements
    function removeMobileTOC() {
        // List of selectors to remove
        const tocSelectors = [
            '.mobile-toc',
            '.mobile-toc-header',
            '.mobile-toc-content',
            '.toc',
            '.toc__menu',
            '.toc__title',
            '.sidebar__right',
            '.sidebar',
            'nav.toc',
            'aside.sidebar__right',
            '[class*="toc"]',
            '[class*="table-of-contents"]',
            '[id*="toc"]',
            '.table-of-contents'
        ];
        
        // Remove each element
        tocSelectors.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(element => {
                element.remove();
            });
        });
    }
    
    // Remove on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', removeMobileTOC);
    } else {
        removeMobileTOC();
    }
    
    // Remove on window load (catch any late additions)
    window.addEventListener('load', removeMobileTOC);
    
    // Remove periodically for first 2 seconds (catch any dynamic additions)
    let removeCount = 0;
    const removeInterval = setInterval(() => {
        removeMobileTOC();
        removeCount++;
        if (removeCount > 10) {
            clearInterval(removeInterval);
        }
    }, 200);
    
    // Also prevent the generateMobileTOC function if it exists
    if (window.generateMobileTOC) {
        window.generateMobileTOC = function() { return; };
    }
})();