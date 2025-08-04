/**
 * Force Navigation Fixed Position
 * This script ensures the navigation is always fixed position
 * Runs after all CSS has loaded to override any conflicting styles
 */

document.addEventListener('DOMContentLoaded', function() {
  // Wait for all styles to load
  window.addEventListener('load', function() {
    // Add a final override after a slight delay to ensure it's absolutely last
    setTimeout(function() {
      const nav = document.querySelector('.main-nav');
      if (nav) {
        // Force fixed position via inline styles (highest specificity)
        nav.style.position = 'fixed';
        nav.style.top = '0';
        nav.style.left = '0';
        nav.style.right = '0';
        nav.style.width = '100%';
        nav.style.zIndex = '99999';
        
        // Ensure body has padding
        document.body.style.paddingTop = '70px';
        
        // Also create a style element to ensure it persists
        const style = document.createElement('style');
        style.innerHTML = `
          .main-nav {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100% !important;
            z-index: 99999 !important;
          }
          body {
            padding-top: 70px !important;
          }
          @media (max-width: 768px) {
            .main-nav {
              height: 60px !important;
            }
            body {
              padding-top: 60px !important;
            }
          }
        `;
        document.head.appendChild(style);
        
        console.log('Navigation forced to fixed position');
      }
    }, 500); // Half second delay to ensure all CSS is loaded
  });
});