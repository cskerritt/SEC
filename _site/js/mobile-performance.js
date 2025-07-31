/* Mobile Performance JavaScript - Non-blocking and Optimized */

// Performance monitoring
const perfObserver = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.entryType === 'largest-contentful-paint') {
            console.log('LCP:', entry.startTime);
        }
    }
});

// Only observe on non-mobile to reduce overhead
if (window.innerWidth > 768) {
    perfObserver.observe({ entryTypes: ['largest-contentful-paint'] });
}

// Lazy load images with Intersection Observer
document.addEventListener('DOMContentLoaded', function() {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: '50px 0px',
        threshold: 0.01
    });

    // Observe all lazy images
    document.querySelectorAll('img.lazy').forEach(img => {
        imageObserver.observe(img);
    });
});

// Optimized mobile menu functionality
(function() {
    'use strict';
    
    // Wait for DOM
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileMenu);
    } else {
        initMobileMenu();
    }
    
    function initMobileMenu() {
        const toggle = document.querySelector('.mobile-menu-toggle');
        const menu = document.querySelector('.nav-menu');
        const body = document.body;
        
        if (!toggle || !menu) return;
        
        // Toggle menu
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const isActive = menu.classList.contains('active');
            
            if (isActive) {
                closeMenu();
            } else {
                openMenu();
            }
        });
        
        // Close menu on escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && menu.classList.contains('active')) {
                closeMenu();
            }
        });
        
        // Close menu on outside click
        document.addEventListener('click', function(e) {
            if (menu.classList.contains('active') && 
                !menu.contains(e.target) && 
                !toggle.contains(e.target)) {
                closeMenu();
            }
        });
        
        // Handle window resize
        let resizeTimer;
        window.addEventListener('resize', function() {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function() {
                if (window.innerWidth > 768 && menu.classList.contains('active')) {
                    closeMenu();
                }
            }, 250);
        });
        
        function openMenu() {
            menu.classList.add('active');
            toggle.classList.add('active');
            body.classList.add('menu-open');
            toggle.setAttribute('aria-expanded', 'true');
            
            // Focus first menu item
            const firstLink = menu.querySelector('a');
            if (firstLink) {
                setTimeout(() => firstLink.focus(), 300);
            }
        }
        
        function closeMenu() {
            menu.classList.remove('active');
            toggle.classList.remove('active');
            body.classList.remove('menu-open');
            toggle.setAttribute('aria-expanded', 'false');
            toggle.focus();
        }
    }
})();

// Smooth scroll for anchor links
document.addEventListener('click', function(e) {
    const link = e.target.closest('a[href^="#"]');
    if (!link) return;
    
    const targetId = link.getAttribute('href');
    if (targetId === '#') return;
    
    const target = document.querySelector(targetId);
    if (!target) return;
    
    e.preventDefault();
    
    // Calculate offset for fixed header
    const headerHeight = document.querySelector('.main-nav').offsetHeight || 60;
    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
    
    // Smooth scroll
    window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
    });
});

// Optimize touch interactions
if ('ontouchstart' in window) {
    document.documentElement.classList.add('touch-device');
    
    // Fast click for touch devices
    let touchStartTime;
    let touchStartY;
    
    document.addEventListener('touchstart', function(e) {
        touchStartTime = Date.now();
        touchStartY = e.touches[0].clientY;
    }, { passive: true });
    
    document.addEventListener('touchend', function(e) {
        const touchEndTime = Date.now();
        const touchEndY = e.changedTouches[0].clientY;
        const timeDiff = touchEndTime - touchStartTime;
        const distDiff = Math.abs(touchEndY - touchStartY);
        
        // If it's a tap (not a scroll)
        if (timeDiff < 200 && distDiff < 10) {
            const target = e.target;
            if (target.matches('a, button, input[type="submit"], input[type="button"]')) {
                // Prevent delay
                e.preventDefault();
                target.click();
            }
        }
    }, { passive: false });
}

// Preload critical resources
function preloadResource(url, as) {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = as;
    link.href = url;
    document.head.appendChild(link);
}

// Defer non-critical CSS
function loadDeferredStyles() {
    const links = document.querySelectorAll('link[data-defer]');
    links.forEach(link => {
        link.removeAttribute('data-defer');
        link.media = 'all';
    });
}

// Load deferred styles after page load
if (window.requestIdleCallback) {
    requestIdleCallback(loadDeferredStyles);
} else {
    setTimeout(loadDeferredStyles, 1);
}

// Progressive enhancement for forms
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Add loading states
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.dataset.originalText = submitBtn.textContent;
                submitBtn.textContent = 'Processing...';
            }
        });
        
        // Enhance select elements for mobile
        const selects = form.querySelectorAll('select');
        selects.forEach(select => {
            // Ensure proper mobile styling
            select.addEventListener('change', function() {
                this.classList.add('has-value');
            });
            
            if (select.value) {
                select.classList.add('has-value');
            }
        });
    });
});

// Service Worker Registration (if supported)
if ('serviceWorker' in navigator && window.location.protocol === 'https:') {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js').then(function(registration) {
            console.log('ServiceWorker registration successful');
        }).catch(function(err) {
            console.log('ServiceWorker registration failed: ', err);
        });
    });
}

// Optimize animations for mobile
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

function handleReducedMotionChange() {
    if (prefersReducedMotion.matches) {
        document.documentElement.classList.add('reduce-motion');
    } else {
        document.documentElement.classList.remove('reduce-motion');
    }
}

handleReducedMotionChange();
prefersReducedMotion.addEventListener('change', handleReducedMotionChange);

// Debounce function for scroll/resize events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimize scroll performance
let ticking = false;
function handleScroll() {
    if (!ticking) {
        window.requestAnimationFrame(function() {
            // Add scroll-based optimizations here
            const scrolled = window.pageYOffset > 50;
            document.querySelector('.main-nav').classList.toggle('scrolled', scrolled);
            ticking = false;
        });
        ticking = true;
    }
}

window.addEventListener('scroll', handleScroll, { passive: true });

// Prefetch links on hover (desktop only)
if (window.innerWidth > 768 && 'prefetch' in document.createElement('link')) {
    document.addEventListener('mouseover', function(e) {
        const link = e.target.closest('a');
        if (link && link.href && link.href.startsWith(window.location.origin)) {
            const prefetchLink = document.createElement('link');
            prefetchLink.rel = 'prefetch';
            prefetchLink.href = link.href;
            document.head.appendChild(prefetchLink);
        }
    });
}