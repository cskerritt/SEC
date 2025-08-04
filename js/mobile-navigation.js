/**
 * Mobile Navigation Enhancement
 * Handles dropdown toggles and menu interactions
 */

document.addEventListener('DOMContentLoaded', function() {
  // Get elements
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const overlay = document.querySelector('.mobile-nav-overlay');
  const dropdownParents = document.querySelectorAll('.nav-menu .has-dropdown');
  
  // Mobile menu toggle
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      const isOpen = navMenu.classList.contains('active');
      
      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
    });
  }
  
  // Close menu when clicking overlay
  if (overlay) {
    overlay.addEventListener('click', closeMenu);
  }
  
  // Handle dropdown toggles on mobile
  dropdownParents.forEach(parent => {
    const link = parent.querySelector(':scope > a');
    
    if (link) {
      link.addEventListener('click', function(e) {
        // Only prevent default on mobile if has dropdown
        if (window.innerWidth <= 768 && parent.classList.contains('has-dropdown')) {
          e.preventDefault();
          e.stopPropagation();
          
          // Toggle this dropdown
          const isOpen = parent.classList.contains('active');
          
          // Close all other dropdowns
          dropdownParents.forEach(other => {
            if (other !== parent) {
              other.classList.remove('active');
            }
          });
          
          // Toggle current dropdown
          if (isOpen) {
            parent.classList.remove('active');
          } else {
            parent.classList.add('active');
          }
        }
      });
    }
  });
  
  // Handle window resize
  let resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      if (window.innerWidth > 768) {
        closeMenu();
        // Remove active class from all dropdowns on desktop
        dropdownParents.forEach(parent => {
          parent.classList.remove('active');
        });
      }
    }, 250);
  });
  
  // Close menu when clicking outside
  document.addEventListener('click', function(e) {
    if (window.innerWidth <= 768 && navMenu && navMenu.classList.contains('active')) {
      if (!navMenu.contains(e.target) && !mobileToggle.contains(e.target)) {
        closeMenu();
      }
    }
  });
  
  // Helper functions
  function openMenu() {
    if (navMenu) navMenu.classList.add('active');
    if (mobileToggle) mobileToggle.classList.add('active');
    if (overlay) overlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
  }
  
  function closeMenu() {
    if (navMenu) navMenu.classList.remove('active');
    if (mobileToggle) mobileToggle.classList.remove('active');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = ''; // Re-enable scrolling
    
    // Close all dropdowns
    dropdownParents.forEach(parent => {
      parent.classList.remove('active');
    });
  }
  
  // Handle escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && navMenu && navMenu.classList.contains('active')) {
      closeMenu();
    }
  });
  
  // Ensure dropdowns work on desktop with keyboard navigation
  if (window.innerWidth > 768) {
    dropdownParents.forEach(parent => {
      const link = parent.querySelector(':scope > a');
      
      if (link) {
        // Add aria attributes for accessibility
        link.setAttribute('aria-haspopup', 'true');
        link.setAttribute('aria-expanded', 'false');
        
        parent.addEventListener('mouseenter', function() {
          link.setAttribute('aria-expanded', 'true');
        });
        
        parent.addEventListener('mouseleave', function() {
          link.setAttribute('aria-expanded', 'false');
        });
        
        // Keyboard navigation
        link.addEventListener('focus', function() {
          parent.classList.add('focus-within');
        });
        
        link.addEventListener('blur', function() {
          setTimeout(() => {
            if (!parent.contains(document.activeElement)) {
              parent.classList.remove('focus-within');
            }
          }, 100);
        });
      }
    });
  }
});