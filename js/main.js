// Mobile Navigation Toggle with Overlay
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    // Create mobile navigation overlay
    const mobileNavOverlay = document.createElement('div');
    mobileNavOverlay.className = 'mobile-nav-overlay';
    document.body.appendChild(mobileNavOverlay);
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            mobileNavOverlay.classList.toggle('active');
            this.classList.toggle('active');
            document.body.classList.toggle('menu-open');
        });
    }

    // Close mobile menu or toggle dropdowns when clicking on navigation links
    const navLinks = document.querySelectorAll('.nav-menu a');
    const dropdownParents = document.querySelectorAll('.nav-menu .has-dropdown');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const parentLi = link.parentElement;
            if (parentLi && parentLi.classList.contains('has-dropdown')) {
                if (!parentLi.classList.contains('open')) {
                    e.preventDefault();
                    dropdownParents.forEach(item => {
                        if (item !== parentLi) item.classList.remove('open');
                    });
                    parentLi.classList.add('open');
                } else {
                    if (navMenu) navMenu.classList.remove('active');
                    if (mobileNavOverlay) mobileNavOverlay.classList.remove('active');
                    if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
                    document.body.classList.remove('menu-open');
                }
                return;
            }
            if (navMenu) navMenu.classList.remove('active');
            if (mobileNavOverlay) mobileNavOverlay.classList.remove('active');
            if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
            document.body.classList.remove('menu-open');
        });

        // Keyboard accessibility for dropdowns
        link.addEventListener('keydown', function(e) {
            const parentLi = link.parentElement;
            if ((e.key === 'Enter' || e.key === ' ') && parentLi && parentLi.classList.contains('has-dropdown')) {
                e.preventDefault();
                dropdownParents.forEach(item => {
                    if (item !== parentLi) item.classList.remove('open');
                });
                parentLi.classList.toggle('open');
            }
        });
    });

    // Close mobile menu when clicking on overlay
    mobileNavOverlay.addEventListener('click', function() {
        if (navMenu) navMenu.classList.remove('active');
        if (mobileNavOverlay) mobileNavOverlay.classList.remove('active');
        if (mobileMenuToggle) mobileMenuToggle.classList.remove('active');
        document.body.classList.remove('menu-open');
    });

    // Close mobile menu when clicking outside navigation area
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.nav-wrapper') && !event.target.closest('.nav-menu')) {
            navMenu.classList.remove('active');
            mobileNavOverlay.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    });

    // Close any open dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        dropdownParents.forEach(item => {
            if (!item.contains(e.target)) {
                item.classList.remove('open');
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add scroll effect to navigation with debouncing
    let lastScrollTop = 0;
    const nav = document.querySelector('.main-nav');
    let ticking = false;
    
    function updateNavOnScroll() {
        if (!nav) return;
        
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // Scrolling down
            nav.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            nav.style.transform = 'translateY(0)';
        }
        
        // Add shadow when scrolled
        if (scrollTop > 10) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
        
        lastScrollTop = scrollTop;
        ticking = false;
    }
    
    // Add smooth fade-in animation for elements
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    const elementsToAnimate = document.querySelectorAll('.service-card, .benefit-card, .testimonial, .case-study, .publication-card, .location-card');
    
    // Don't hide any elements - let CSS handle initial state
    elementsToAnimate.forEach(el => {
        observer.observe(el);
    });
    
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(updateNavOnScroll);
            ticking = true;
        }
    });
    
    // Lazy load images for better performance
    const lazyImages = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    }
    
    // Enhanced form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.classList.add('loading');
                submitBtn.disabled = true;
                
                // Add loading spinner to button
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="loading-dots"><span></span><span></span><span></span></span> Processing...';
                
                // Restore button after timeout (in case of errors)
                setTimeout(() => {
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }, 10000);
            }
        });
        
        // Real-time validation
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (this.value.trim() === '') {
                    this.classList.add('error');
                    this.classList.remove('success');
                } else {
                    this.classList.remove('error');
                    this.classList.add('success');
                }
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('error') && this.value.trim() !== '') {
                    this.classList.remove('error');
                    this.classList.add('success');
                }
            });
        });
    });
    
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.btn, button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
    
    // Enhanced FAQ interaction with mobile optimization
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const summary = item.querySelector('summary');
        if (summary) {
            summary.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Close other FAQ items on mobile for better UX
                if (window.innerWidth <= 768) {
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item && otherItem.hasAttribute('open')) {
                            otherItem.removeAttribute('open');
                        }
                    });
                }
                
                // Toggle current item
                if (item.hasAttribute('open')) {
                    item.removeAttribute('open');
                } else {
                    item.setAttribute('open', '');
                }
            });
        }
    });

    // Mobile Table of Contents Generator
    function generateMobileTOC() {
        const headings = document.querySelectorAll('h2, h3, h4');
        if (headings.length < 3) return; // Only show TOC if there are enough headings

        const tocContainer = document.createElement('div');
        tocContainer.className = 'mobile-toc collapsed';
        
        const tocHeader = document.createElement('div');
        tocHeader.className = 'mobile-toc-header';
        tocHeader.textContent = 'Table of Contents';
        
        const tocContent = document.createElement('div');
        tocContent.className = 'mobile-toc-content';
        
        const tocList = document.createElement('ul');
        
        headings.forEach((heading, index) => {
            // Create ID if it doesn't exist
            if (!heading.id) {
                heading.id = 'heading-' + index;
            }
            
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = '#' + heading.id;
            link.textContent = heading.textContent;
            link.className = heading.tagName.toLowerCase() === 'h2' ? 'toc-h2' : 
                             heading.tagName.toLowerCase() === 'h3' ? 'toc-h3' : 'toc-h4';
            
            listItem.appendChild(link);
            tocList.appendChild(listItem);
        });
        
        tocContent.appendChild(tocList);
        tocContainer.appendChild(tocHeader);
        tocContainer.appendChild(tocContent);
        
        // Insert TOC after first paragraph or at beginning of main content
        const mainContent = document.querySelector('main') || document.querySelector('.container');
        const firstP = mainContent?.querySelector('p');
        if (firstP) {
            firstP.parentNode.insertBefore(tocContainer, firstP.nextSibling);
        } else if (mainContent) {
            mainContent.insertBefore(tocContainer, mainContent.firstChild);
        }
        
        // Toggle functionality
        tocHeader.addEventListener('click', function() {
            tocContainer.classList.toggle('collapsed');
        });
        
        // Highlight active section
        const updateActiveTOC = () => {
            const scrollPosition = window.scrollY + 100;
            let activeHeading = null;
            
            headings.forEach(heading => {
                if (heading.offsetTop <= scrollPosition) {
                    activeHeading = heading;
                }
            });
            
            // Remove all active classes
            tocList.querySelectorAll('a').forEach(link => link.classList.remove('active'));
            
            // Add active class to current section
            if (activeHeading) {
                const activeLink = tocList.querySelector(`a[href="#${activeHeading.id}"]`);
                if (activeLink) activeLink.classList.add('active');
            }
        };
        
        window.addEventListener('scroll', updateActiveTOC);
        updateActiveTOC();
    }

    // Back to Top Button
    function createBackToTopButton() {
        const backToTopBtn = document.createElement('button');
        backToTopBtn.className = 'back-to-top';
        backToTopBtn.innerHTML = '↑';
        backToTopBtn.setAttribute('aria-label', 'Back to top');
        backToTopBtn.setAttribute('title', 'Back to top');
        
        document.body.appendChild(backToTopBtn);
        
        // Show/hide based on scroll position
        const toggleBackToTop = () => {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        };
        
        // Smooth scroll to top
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        window.addEventListener('scroll', toggleBackToTop);
        toggleBackToTop();
    }

    // Accordion Functionality
    function initializeAccordions() {
        const accordions = document.querySelectorAll('.accordion');
        accordions.forEach(accordion => {
            const header = accordion.querySelector('.accordion-header');
            if (header) {
                header.addEventListener('click', function() {
                    accordion.classList.toggle('open');
                    
                    // Close other accordions in the same group (optional)
                    const group = accordion.closest('.accordion-group');
                    if (group) {
                        const siblings = group.querySelectorAll('.accordion');
                        siblings.forEach(sibling => {
                            if (sibling !== accordion) {
                                sibling.classList.remove('open');
                            }
                        });
                    }
                });
            }
        });
    }

    // Mobile Form Enhancements
    function enhanceMobileForms() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            // Convert regular form groups to mobile-optimized ones
            const formGroups = form.querySelectorAll('.form-group');
            formGroups.forEach(group => {
                if (window.innerWidth <= 768) {
                    group.classList.add('mobile-form-group');
                }
            });
            
            // Enhanced input focus for mobile
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                input.addEventListener('focus', function() {
                    // Scroll input into view on mobile
                    if (window.innerWidth <= 768) {
                        setTimeout(() => {
                            this.scrollIntoView({
                                behavior: 'smooth',
                                block: 'center'
                            });
                        }, 300);
                    }
                });
            });
        });
    }

    // Touch Target Enhancement
    function enhanceTouchTargets() {
        const clickableElements = document.querySelectorAll('a, button, .clickable, .btn');
        clickableElements.forEach(element => {
            element.classList.add('touch-target');
        });
    }

    // Viewport Meta Tag Optimization
    function optimizeViewport() {
        let viewportMeta = document.querySelector('meta[name="viewport"]');
        if (viewportMeta) {
            // Enhance existing viewport meta tag
            viewportMeta.setAttribute('content', 'width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover');
        } else {
            // Create viewport meta tag if it doesn't exist
            viewportMeta = document.createElement('meta');
            viewportMeta.name = 'viewport';
            viewportMeta.content = 'width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover';
            document.head.appendChild(viewportMeta);
        }
    }

    // Initialize all mobile features
    if (window.innerWidth <= 768) {
        generateMobileTOC();
    }
    createBackToTopButton();
    initializeAccordions();
    enhanceMobileForms();
    enhanceTouchTargets();
    optimizeViewport();

    // Responsive handler for window resize
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            // Re-initialize mobile features if switching to mobile view
            if (window.innerWidth <= 768) {
                enhanceMobileForms();
                if (!document.querySelector('.mobile-toc')) {
                    generateMobileTOC();
                }
            }
        }, 250);
    });

    // Improved swipe gesture for mobile navigation
    let touchStartX = 0;
    let touchEndX = 0;
    
    document.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
    });
    
    document.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });
    
    function handleSwipe() {
        const swipeThreshold = 50;
        const swipeDistance = touchEndX - touchStartX;
        
        // Swipe right to open menu (only if menu is closed)
        if (swipeDistance > swipeThreshold && !navMenu.classList.contains('active')) {
            if (touchStartX < 50) { // Only if swipe starts from left edge
                navMenu.classList.add('active');
                mobileNavOverlay.classList.add('active');
                mobileMenuToggle.classList.add('active');
                document.body.classList.add('menu-open');
            }
        }
        
        // Swipe left to close menu (only if menu is open)
        if (swipeDistance < -swipeThreshold && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            mobileNavOverlay.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    }

    // Icon and Visual Enhancement Interactions
    function initializeIconEnhancements() {
        // Animate service icons on hover
        const serviceCards = document.querySelectorAll('.service-card');
        serviceCards.forEach(card => {
            const icon = card.querySelector('.service-icon');
            if (icon) {
                card.addEventListener('mouseenter', () => {
                    icon.classList.add('icon-pulse');
                });
                card.addEventListener('mouseleave', () => {
                    icon.classList.remove('icon-pulse');
                });
            }
        });

        // Animate benefit icons on scroll into view
        const benefitIcons = document.querySelectorAll('.benefit-icon');
        const iconObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('icon-bounce');
                        setTimeout(() => {
                            entry.target.classList.remove('icon-bounce');
                        }, 1000);
                    }, index * 200); // Stagger the animations
                    iconObserver.unobserve(entry.target);
                }
            });
        });

        benefitIcons.forEach(icon => iconObserver.observe(icon));

        // Practice chip hover effects
        const practiceChips = document.querySelectorAll('.practice-chip');
        practiceChips.forEach(chip => {
            const icon = chip.querySelector('.icon');
            if (icon) {
                chip.addEventListener('mouseenter', () => {
                    icon.style.transform = 'scale(1.2) rotate(5deg)';
                });
                chip.addEventListener('mouseleave', () => {
                    icon.style.transform = 'scale(1) rotate(0deg)';
                });
            }
        });

        // Floating Action Button (FAB) animations
        const fab = document.querySelector('.fab');
        if (fab) {
            // Add hover effects
            fab.addEventListener('mouseenter', () => {
                fab.style.transform = 'scale(1.1) translateY(-4px)';
            });
            fab.addEventListener('mouseleave', () => {
                fab.style.transform = 'scale(1) translateY(0)';
            });

            // Add click feedback
            fab.addEventListener('click', () => {
                fab.style.transform = 'scale(0.95) translateY(2px)';
                setTimeout(() => {
                    fab.style.transform = 'scale(1.1) translateY(-4px)';
                }, 150);
            });

            // Stop pulsing on interaction
            fab.addEventListener('mouseenter', () => {
                fab.classList.remove('fab-pulse');
            });
        }

        // Contact icon interactions
        const contactIcons = document.querySelectorAll('.contact-icon');
        contactIcons.forEach(icon => {
            const parentLink = icon.closest('a') || icon.nextElementSibling;
            if (parentLink) {
                parentLink.addEventListener('mouseenter', () => {
                    icon.style.transform = 'scale(1.2)';
                    icon.style.background = 'rgba(255,255,255,0.4)';
                });
                parentLink.addEventListener('mouseleave', () => {
                    icon.style.transform = 'scale(1)';
                    icon.style.background = 'rgba(255,255,255,0.2)';
                });
            }
        });

        // Enhanced button icon interactions
        const buttonsWithIcons = document.querySelectorAll('.btn-with-icon');
        buttonsWithIcons.forEach(button => {
            const icon = button.querySelector('.btn-icon');
            if (icon) {
                button.addEventListener('mouseenter', () => {
                    icon.style.transform = 'translateX(4px) scale(1.1)';
                });
                button.addEventListener('mouseleave', () => {
                    icon.style.transform = 'translateX(0) scale(1)';
                });
            }
        });
    }

    // Initialize visual enhancements
    initializeIconEnhancements();
    
    // Failsafe: Ensure all main content is visible after page load
    window.addEventListener('load', function() {
        // Make sure hero and above-the-fold content is visible
        const criticalElements = document.querySelectorAll('.hero, .hero h1, .hero p, .hero .btn, .trust-indicators, .services-grid, .main-nav');
        criticalElements.forEach(el => {
            if (el) {
                el.style.opacity = '1';
                el.style.visibility = 'visible';
                el.style.transform = 'none';
            }
        });
        
        // Log any elements that might still be hidden (excluding intentionally hidden elements)
        const allElements = document.querySelectorAll('*');
        const hiddenElements = [];
        const intentionallyHidden = ['dropdown', 'mobile-nav-overlay', 'mobile-menu-toggle'];
        
        allElements.forEach(el => {
            // Skip elements that should be hidden
            const shouldSkip = intentionallyHidden.some(className => 
                el.classList.contains(className) || 
                el.closest(`.${className}`)
            );
            
            if (!shouldSkip) {
                const style = window.getComputedStyle(el);
                if (style.opacity === '0' || style.visibility === 'hidden' || style.display === 'none') {
                    const rect = el.getBoundingClientRect();
                    if (rect.width > 0 && rect.height > 0 && rect.top < window.innerHeight) {
                        hiddenElements.push({
                            element: el,
                            className: el.className,
                            id: el.id,
                            tagName: el.tagName.toLowerCase()
                        });
                    }
                }
            }
        });
        
        if (hiddenElements.length > 0) {
            console.warn('Hidden elements found:', hiddenElements);
        }
    });

    // Progressive loading states for images only
    function addProgressiveLoading() {
        const images = document.querySelectorAll('img[data-src]');
        images.forEach(img => {
            // Only handle lazy-loaded images with data-src
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                });
            });
            imageObserver.observe(img);
        });
    }

    // Initialize progressive loading
    addProgressiveLoading();

    // Enhanced visual feedback for form interactions
    function enhanceFormVisuals() {
        const inputs = document.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            // Add visual feedback on focus
            input.addEventListener('focus', () => {
                input.style.transform = 'scale(1.02)';
                input.style.boxShadow = '0 4px 12px rgba(30, 58, 138, 0.15)';
            });

            input.addEventListener('blur', () => {
                input.style.transform = 'scale(1)';
                input.style.boxShadow = '';
            });

            // Add success state for valid inputs
            input.addEventListener('input', () => {
                if (input.checkValidity()) {
                    input.classList.remove('error');
                    input.classList.add('success');
                } else {
                    input.classList.remove('success');
                    if (input.value.length > 0) {
                        input.classList.add('error');
                    }
                }
            });
        });
    }

    enhanceFormVisuals();
});