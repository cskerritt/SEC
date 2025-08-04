/**
 * Main JavaScript File - Consolidated for Jekyll/GitHub Pages
 * Handles all interactive functionality with no external dependencies
 */

(function() {
    'use strict';

    // ==========================================================================
    // Mobile Navigation
    // ==========================================================================
    function initMobileNavigation() {
        const mobileToggle = document.querySelector('.mobile-menu-toggle');
        const navMenu = document.querySelector('.nav-menu');
        
        if (!mobileToggle || !navMenu) return;
        
        mobileToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger menu
            const spans = this.querySelectorAll('span');
            if (navMenu.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translateY(7px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translateY(-7px)';
            } else {
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.main-nav')) {
                navMenu.classList.remove('active');
                const spans = mobileToggle.querySelectorAll('span');
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });
        
        // Close menu when pressing Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                const spans = mobileToggle.querySelectorAll('span');
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
            }
        });
    }

    // ==========================================================================
    // Smooth Scrolling
    // ==========================================================================
    function initSmoothScrolling() {
        const links = document.querySelectorAll('a[href^="#"]');
        
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                
                const target = document.querySelector(href);
                if (!target) return;
                
                e.preventDefault();
                const headerHeight = document.querySelector('.main-nav').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            });
        });
    }

    // ==========================================================================
    // Sticky Header
    // ==========================================================================
    function initStickyHeader() {
        const header = document.querySelector('.main-nav');
        if (!header) return;
        
        let lastScroll = 0;
        const headerHeight = header.offsetHeight;
        
        window.addEventListener('scroll', function() {
            const currentScroll = window.pageYOffset;
            
            // Add shadow when scrolling
            if (currentScroll > 0) {
                header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
            } else {
                header.style.boxShadow = '';
            }
            
            // Hide/show header on scroll (optional)
            if (currentScroll > lastScroll && currentScroll > headerHeight) {
                // Scrolling down
                // header.style.transform = 'translateY(-100%)';
            } else {
                // Scrolling up
                header.style.transform = 'translateY(0)';
            }
            
            lastScroll = currentScroll;
        });
    }

    // ==========================================================================
    // Lazy Loading Images
    // ==========================================================================
    function initLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        img.classList.add('loaded');
                        observer.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px'
            });
            
            images.forEach(img => imageObserver.observe(img));
        } else {
            // Fallback for older browsers
            images.forEach(img => {
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                img.classList.add('loaded');
            });
        }
    }

    // ==========================================================================
    // Form Validation
    // ==========================================================================
    function initFormValidation() {
        const forms = document.querySelectorAll('form[data-validate]');
        
        forms.forEach(form => {
            form.addEventListener('submit', function(e) {
                let isValid = true;
                const requiredFields = form.querySelectorAll('[required]');
                
                requiredFields.forEach(field => {
                    if (!field.value.trim()) {
                        isValid = false;
                        field.classList.add('error');
                        
                        // Show error message
                        let errorMsg = field.nextElementSibling;
                        if (!errorMsg || !errorMsg.classList.contains('error-message')) {
                            errorMsg = document.createElement('span');
                            errorMsg.classList.add('error-message');
                            errorMsg.textContent = 'This field is required';
                            field.parentNode.insertBefore(errorMsg, field.nextSibling);
                        }
                    } else {
                        field.classList.remove('error');
                        const errorMsg = field.nextElementSibling;
                        if (errorMsg && errorMsg.classList.contains('error-message')) {
                            errorMsg.remove();
                        }
                    }
                });
                
                // Email validation
                const emailFields = form.querySelectorAll('input[type="email"]');
                emailFields.forEach(field => {
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (field.value && !emailPattern.test(field.value)) {
                        isValid = false;
                        field.classList.add('error');
                        
                        let errorMsg = field.nextElementSibling;
                        if (!errorMsg || !errorMsg.classList.contains('error-message')) {
                            errorMsg = document.createElement('span');
                            errorMsg.classList.add('error-message');
                            errorMsg.textContent = 'Please enter a valid email address';
                            field.parentNode.insertBefore(errorMsg, field.nextSibling);
                        }
                    }
                });
                
                if (!isValid) {
                    e.preventDefault();
                    
                    // Scroll to first error
                    const firstError = form.querySelector('.error');
                    if (firstError) {
                        firstError.focus();
                        firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            });
            
            // Clear error on input
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                input.addEventListener('input', function() {
                    this.classList.remove('error');
                    const errorMsg = this.nextElementSibling;
                    if (errorMsg && errorMsg.classList.contains('error-message')) {
                        errorMsg.remove();
                    }
                });
            });
        });
    }

    // ==========================================================================
    // Accessibility Enhancements
    // ==========================================================================
    function initAccessibility() {
        // Skip to content link
        const skipLink = document.querySelector('.skip-link');
        if (skipLink) {
            skipLink.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.tabIndex = -1;
                    target.focus();
                }
            });
        }
        
        // Dropdown keyboard navigation
        const dropdowns = document.querySelectorAll('.has-dropdown');
        dropdowns.forEach(dropdown => {
            const link = dropdown.querySelector('.nav-link');
            const menu = dropdown.querySelector('.dropdown');
            
            if (link && menu) {
                link.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        menu.style.visibility = menu.style.visibility === 'visible' ? 'hidden' : 'visible';
                        menu.style.opacity = menu.style.opacity === '1' ? '0' : '1';
                    }
                });
            }
        });
        
        // Escape key closes dropdowns
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const openDropdowns = document.querySelectorAll('.dropdown[style*="visible"]');
                openDropdowns.forEach(dropdown => {
                    dropdown.style.visibility = 'hidden';
                    dropdown.style.opacity = '0';
                });
            }
        });
    }

    // ==========================================================================
    // Analytics Events
    // ==========================================================================
    function initAnalytics() {
        // Track outbound links
        const outboundLinks = document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])');
        outboundLinks.forEach(link => {
            link.addEventListener('click', function() {
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'click', {
                        'event_category': 'outbound',
                        'event_label': this.href
                    });
                }
            });
        });
        
        // Track form submissions
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', function() {
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'submit', {
                        'event_category': 'form',
                        'event_label': this.id || 'unnamed-form'
                    });
                }
            });
        });
    }

    // ==========================================================================
    // Initialize Everything
    // ==========================================================================
    function init() {
        initMobileNavigation();
        initSmoothScrolling();
        initStickyHeader();
        initLazyLoading();
        initFormValidation();
        initAccessibility();
        initAnalytics();
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Expose some functions globally if needed
    window.siteUtils = {
        scrollToTop: function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },
        toggleMobileMenu: function() {
            const navMenu = document.querySelector('.nav-menu');
            if (navMenu) {
                navMenu.classList.toggle('active');
            }
        }
    };
})();