/**
 * Lazy Loading for Images
 * Adds native lazy loading support and fallback for older browsers
 */

(function() {
    'use strict';
    
    // Check if native lazy loading is supported
    const supportsLazyLoading = 'loading' in HTMLImageElement.prototype;
    
    if (supportsLazyLoading) {
        // Native lazy loading is supported
        // Add loading="lazy" to all images except those in hero/above-the-fold sections
        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('img:not([loading])');
            
            images.forEach(function(img) {
                // Skip images in hero sections or explicitly marked as eager
                const parent = img.closest('.hero, .hero-section, .above-the-fold, [data-loading="eager"]');
                if (!parent && !img.classList.contains('eager-load')) {
                    img.setAttribute('loading', 'lazy');
                }
            });
        });
    } else {
        // Fallback for browsers that don't support native lazy loading
        // Use Intersection Observer API
        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('img[data-src]');
            
            const imageObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        if (img.dataset.srcset) {
                            img.srcset = img.dataset.srcset;
                        }
                        img.classList.add('loaded');
                        imageObserver.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px',
                threshold: 0.01
            });
            
            images.forEach(function(img) {
                imageObserver.observe(img);
            });
        });
    }
    
    // Add fade-in effect for loaded images
    const style = document.createElement('style');
    style.textContent = `
        img {
            opacity: 1;
            transition: opacity 0.3s ease-in-out;
        }
        
        img:not([src]):not([srcset]) {
            opacity: 0;
        }
        
        img.loaded {
            opacity: 1;
        }
        
        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            img {
                transition: none;
            }
        }
    `;
    document.head.appendChild(style);
})();