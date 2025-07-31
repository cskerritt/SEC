/* Mobile Menu Fix JavaScript */
document.addEventListener('DOMContentLoaded', function() {
    'use strict';
    
    // Get elements
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const body = document.body;
    
    // Create overlay if it doesn't exist
    let mobileNavOverlay = document.querySelector('.mobile-nav-overlay');
    if (!mobileNavOverlay) {
        mobileNavOverlay = document.createElement('div');
        mobileNavOverlay.className = 'mobile-nav-overlay';
        body.appendChild(mobileNavOverlay);
    }
    
    // Toggle menu function
    function toggleMenu() {
        const isActive = navMenu.classList.contains('active');
        
        if (isActive) {
            closeMenu();
        } else {
            openMenu();
        }
    }
    
    // Open menu
    function openMenu() {
        navMenu.classList.add('active');
        mobileNavOverlay.classList.add('active');
        mobileMenuToggle.classList.add('active');
        body.classList.add('menu-open');
        mobileMenuToggle.setAttribute('aria-expanded', 'true');
    }
    
    // Close menu
    function closeMenu() {
        navMenu.classList.remove('active');
        mobileNavOverlay.classList.remove('active');
        mobileMenuToggle.classList.remove('active');
        body.classList.remove('menu-open');
        mobileMenuToggle.setAttribute('aria-expanded', 'false');
    }
    
    // Event listeners
    if (mobileMenuToggle && navMenu) {
        // Toggle button click
        mobileMenuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            toggleMenu();
        });
        
        // Overlay click
        mobileNavOverlay.addEventListener('click', closeMenu);
        
        // Handle dropdown menus on mobile
        const dropdowns = document.querySelectorAll('.has-dropdown');
        dropdowns.forEach(dropdown => {
            const link = dropdown.querySelector('> a');
            if (link) {
                link.addEventListener('click', function(e) {
                    if (window.innerWidth <= 768 && dropdown.querySelector('.dropdown')) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                    }
                });
            }
        });
        
        // Close menu when clicking non-dropdown links
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                const parentLi = this.parentElement;
                const hasDropdown = parentLi.classList.contains('has-dropdown');
                const hasSubMenu = parentLi.querySelector('.dropdown');
                
                // If it's not a dropdown parent, close the menu
                if (!hasDropdown || !hasSubMenu) {
                    closeMenu();
                }
            });
        });
        
        // Close menu on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                closeMenu();
            }
        });
        
        // Handle window resize
        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function() {
                if (window.innerWidth > 768) {
                    closeMenu();
                }
            }, 250);
        });
    }
    
    // Fix for iOS bounce and viewport issues
    if (/iPhone|iPad|iPod/.test(navigator.userAgent)) {
        // Prevent bounce on iOS
        document.addEventListener('touchmove', function(e) {
            if (body.classList.contains('menu-open')) {
                e.preventDefault();
            }
        }, { passive: false });
        
        // Allow scrolling within menu
        if (navMenu) {
            navMenu.addEventListener('touchmove', function(e) {
                e.stopPropagation();
            }, { passive: true });
        }
    }
});