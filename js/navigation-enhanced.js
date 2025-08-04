/**
 * Enhanced Navigation System
 * A robust, accessible navigation with multi-level dropdowns
 */

class NavigationSystem {
    constructor() {
        this.nav = document.querySelector('.main-nav');
        this.mobileToggle = document.querySelector('.mobile-menu-toggle');
        this.navMenu = document.querySelector('.nav-menu');
        this.dropdowns = document.querySelectorAll('.has-dropdown');
        this.overlay = null;
        this.isOpen = false;
        this.isMobile = window.innerWidth <= 768;
        this.touchStartX = 0;
        this.touchEndX = 0;
        
        this.init();
    }
    
    init() {
        this.createMobileOverlay();
        this.setupEventListeners();
        this.setupKeyboardNavigation();
        this.setupAccessibility();
        this.handleResponsive();
    }
    
    createMobileOverlay() {
        this.overlay = document.createElement('div');
        this.overlay.className = 'mobile-nav-overlay';
        document.body.appendChild(this.overlay);
    }
    
    setupEventListeners() {
        // Mobile toggle
        if (this.mobileToggle) {
            this.mobileToggle.addEventListener('click', () => this.toggleMobileMenu());
        }
        
        // Overlay click
        if (this.overlay) {
            this.overlay.addEventListener('click', () => this.closeMobileMenu());
        }
        
        // Dropdown interactions
        this.dropdowns.forEach(dropdown => {
            const trigger = dropdown.querySelector('> a');
            const menu = dropdown.querySelector('.dropdown');
            
            if (!trigger || !menu) return;
            
            // Desktop hover with intent detection
            if (!this.isMobile) {
                let hoverIntent;
                
                dropdown.addEventListener('mouseenter', () => {
                    clearTimeout(hoverIntent);
                    this.openDropdown(dropdown);
                });
                
                dropdown.addEventListener('mouseleave', () => {
                    hoverIntent = setTimeout(() => {
                        this.closeDropdown(dropdown);
                    }, 300);
                });
            }
            
            // Click handling
            trigger.addEventListener('click', (e) => {
                if (this.isMobile && menu) {
                    e.preventDefault();
                    this.toggleDropdown(dropdown);
                }
            });
            
            // Mobile dropdown toggle button
            if (this.isMobile) {
                const toggleBtn = document.createElement('button');
                toggleBtn.className = 'dropdown-toggle';
                toggleBtn.innerHTML = '<svg width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" stroke="currentColor" fill="none" stroke-width="2"/></svg>';
                toggleBtn.setAttribute('aria-label', 'Toggle submenu');
                
                dropdown.insertBefore(toggleBtn, menu);
                
                toggleBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    this.toggleDropdown(dropdown);
                });
            }
        });
        
        // Click outside to close
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.main-nav')) {
                this.closeAllDropdowns();
                if (this.isOpen) {
                    this.closeMobileMenu();
                }
            }
        });
        
        // Touch gestures for mobile
        document.addEventListener('touchstart', (e) => {
            this.touchStartX = e.changedTouches[0].screenX;
        });
        
        document.addEventListener('touchend', (e) => {
            this.touchEndX = e.changedTouches[0].screenX;
            this.handleSwipe();
        });
        
        // Window resize
        window.addEventListener('resize', () => {
            this.handleResponsive();
        });
        
        // Escape key to close
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllDropdowns();
                if (this.isOpen) {
                    this.closeMobileMenu();
                }
            }
        });
    }
    
    setupKeyboardNavigation() {
        const menuItems = this.navMenu?.querySelectorAll('a');
        
        menuItems?.forEach((item, index) => {
            item.addEventListener('keydown', (e) => {
                switch(e.key) {
                    case 'ArrowRight':
                        e.preventDefault();
                        const nextIndex = (index + 1) % menuItems.length;
                        menuItems[nextIndex].focus();
                        break;
                        
                    case 'ArrowLeft':
                        e.preventDefault();
                        const prevIndex = index === 0 ? menuItems.length - 1 : index - 1;
                        menuItems[prevIndex].focus();
                        break;
                        
                    case 'ArrowDown':
                        const dropdown = item.parentElement.querySelector('.dropdown');
                        if (dropdown) {
                            e.preventDefault();
                            const firstItem = dropdown.querySelector('a');
                            if (firstItem) {
                                this.openDropdown(item.parentElement);
                                firstItem.focus();
                            }
                        }
                        break;
                        
                    case 'Enter':
                    case ' ':
                        if (item.parentElement.classList.contains('has-dropdown')) {
                            e.preventDefault();
                            this.toggleDropdown(item.parentElement);
                        }
                        break;
                }
            });
        });
        
        // Dropdown keyboard navigation
        this.dropdowns.forEach(dropdown => {
            const dropdownItems = dropdown.querySelectorAll('.dropdown a');
            
            dropdownItems.forEach((item, index) => {
                item.addEventListener('keydown', (e) => {
                    switch(e.key) {
                        case 'ArrowDown':
                            e.preventDefault();
                            const nextItem = dropdownItems[index + 1];
                            if (nextItem) {
                                nextItem.focus();
                            }
                            break;
                            
                        case 'ArrowUp':
                            e.preventDefault();
                            if (index === 0) {
                                const trigger = dropdown.querySelector('> a');
                                trigger?.focus();
                                this.closeDropdown(dropdown);
                            } else {
                                dropdownItems[index - 1].focus();
                            }
                            break;
                            
                        case 'Escape':
                            e.preventDefault();
                            const trigger = dropdown.querySelector('> a');
                            trigger?.focus();
                            this.closeDropdown(dropdown);
                            break;
                    }
                });
            });
        });
    }
    
    setupAccessibility() {
        // Add ARIA attributes
        this.dropdowns.forEach(dropdown => {
            const trigger = dropdown.querySelector('> a');
            const menu = dropdown.querySelector('.dropdown');
            
            if (trigger && menu) {
                trigger.setAttribute('aria-haspopup', 'true');
                trigger.setAttribute('aria-expanded', 'false');
                menu.setAttribute('role', 'menu');
                
                menu.querySelectorAll('li').forEach(item => {
                    item.setAttribute('role', 'menuitem');
                });
            }
        });
        
        // Skip navigation link
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.className = 'skip-nav';
        skipLink.textContent = 'Skip to main content';
        document.body.insertBefore(skipLink, document.body.firstChild);
    }
    
    toggleMobileMenu() {
        this.isOpen = !this.isOpen;
        
        if (this.isOpen) {
            this.openMobileMenu();
        } else {
            this.closeMobileMenu();
        }
    }
    
    openMobileMenu() {
        this.isOpen = true;
        this.navMenu?.classList.add('active');
        this.overlay?.classList.add('active');
        this.mobileToggle?.classList.add('active');
        this.mobileToggle?.setAttribute('aria-expanded', 'true');
        document.body.classList.add('menu-open');
        
        // Trap focus
        this.trapFocus(this.navMenu);
    }
    
    closeMobileMenu() {
        this.isOpen = false;
        this.navMenu?.classList.remove('active');
        this.overlay?.classList.remove('active');
        this.mobileToggle?.classList.remove('active');
        this.mobileToggle?.setAttribute('aria-expanded', 'false');
        document.body.classList.remove('menu-open');
        
        // Release focus trap
        this.releaseFocus();
    }
    
    toggleDropdown(dropdown) {
        const isOpen = dropdown.classList.contains('open');
        
        // Close other dropdowns first
        this.closeAllDropdowns();
        
        if (!isOpen) {
            this.openDropdown(dropdown);
        }
    }
    
    openDropdown(dropdown) {
        dropdown.classList.add('open');
        const trigger = dropdown.querySelector('> a');
        trigger?.setAttribute('aria-expanded', 'true');
        
        // Update toggle button
        const toggleBtn = dropdown.querySelector('.dropdown-toggle');
        if (toggleBtn) {
            toggleBtn.classList.add('active');
        }
    }
    
    closeDropdown(dropdown) {
        dropdown.classList.remove('open');
        const trigger = dropdown.querySelector('> a');
        trigger?.setAttribute('aria-expanded', 'false');
        
        // Update toggle button
        const toggleBtn = dropdown.querySelector('.dropdown-toggle');
        if (toggleBtn) {
            toggleBtn.classList.remove('active');
        }
    }
    
    closeAllDropdowns() {
        this.dropdowns.forEach(dropdown => {
            this.closeDropdown(dropdown);
        });
    }
    
    handleSwipe() {
        const swipeThreshold = 50;
        const diff = this.touchEndX - this.touchStartX;
        
        // Swipe right to open
        if (diff > swipeThreshold && !this.isOpen && this.touchStartX < 50) {
            this.openMobileMenu();
        }
        
        // Swipe left to close
        if (diff < -swipeThreshold && this.isOpen) {
            this.closeMobileMenu();
        }
    }
    
    handleResponsive() {
        const wasMobile = this.isMobile;
        this.isMobile = window.innerWidth <= 768;
        
        // Clean up when switching between mobile and desktop
        if (wasMobile !== this.isMobile) {
            this.closeAllDropdowns();
            this.closeMobileMenu();
            
            // Remove/add mobile-specific elements
            document.querySelectorAll('.dropdown-toggle').forEach(btn => {
                btn.style.display = this.isMobile ? 'block' : 'none';
            });
        }
    }
    
    trapFocus(element) {
        if (!element) return;
        
        const focusableElements = element.querySelectorAll(
            'a[href], button, textarea, input[type="text"], input[type="radio"], input[type="checkbox"], select'
        );
        
        const firstFocusable = focusableElements[0];
        const lastFocusable = focusableElements[focusableElements.length - 1];
        
        this.focusTrapHandler = (e) => {
            if (e.key === 'Tab') {
                if (e.shiftKey && document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                } else if (!e.shiftKey && document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        };
        
        document.addEventListener('keydown', this.focusTrapHandler);
        firstFocusable?.focus();
    }
    
    releaseFocus() {
        if (this.focusTrapHandler) {
            document.removeEventListener('keydown', this.focusTrapHandler);
            this.focusTrapHandler = null;
        }
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new NavigationSystem();
    });
} else {
    new NavigationSystem();
}

// Export for use in other scripts
window.NavigationSystem = NavigationSystem;