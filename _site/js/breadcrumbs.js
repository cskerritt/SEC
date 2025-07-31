/**
 * Dynamic Breadcrumb Navigation
 * Automatically generates breadcrumbs based on URL structure
 */

(function() {
    'use strict';
    
    // Configuration
    const config = {
        homeLabel: 'Home',
        separator: '›',
        excludePaths: ['index.html', 'index.htm'],
        // Custom labels for specific paths
        pathLabels: {
            'services': 'Services',
            'practice-areas': 'Practice Areas',
            'case-studies': 'Case Studies',
            'locations': 'Locations',
            'business-valuation': 'Business Valuation',
            'forensic-economics': 'Forensic Economics',
            'vocational-expert': 'Vocational Expert',
            'life-care-planning': 'Life Care Planning',
            'personal-injury': 'Personal Injury',
            'medical-malpractice': 'Medical Malpractice',
            'employment': 'Employment Litigation',
            'commercial-disputes': 'Commercial Disputes',
            'about': 'About',
            'contact': 'Contact',
            'blog': 'Blog',
            'resources': 'Resources'
        }
    };
    
    function generateBreadcrumbs() {
        // Don't show breadcrumbs on homepage
        if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
            return;
        }
        
        // Find breadcrumb container
        const breadcrumbContainer = document.querySelector('.breadcrumb-placeholder');
        if (!breadcrumbContainer) {
            return;
        }
        
        // Parse URL path
        const pathParts = window.location.pathname.split('/').filter(part => 
            part && !config.excludePaths.includes(part)
        );
        
        // Create breadcrumb HTML
        let breadcrumbHTML = `
            <nav class="breadcrumb" aria-label="Breadcrumb">
                <div class="breadcrumb-container">
                    <ol class="breadcrumb-list">
                        <li class="breadcrumb-item">
                            <a class="breadcrumb-link" href="/">
                                <span class="breadcrumb-icon">🏠</span>
                                ${config.homeLabel}
                            </a>
                        </li>
        `;
        
        // Generate breadcrumb items
        let currentPath = '';
        pathParts.forEach((part, index) => {
            currentPath += '/' + part;
            const isLast = index === pathParts.length - 1;
            
            // Get label for this part
            let label = config.pathLabels[part] || part
                .replace(/-/g, ' ')
                .replace('.html', '')
                .replace(/\b\w/g, l => l.toUpperCase());
            
            // For state pages, format properly
            if (currentPath.includes('/locations/') && !currentPath.includes('/cities/')) {
                label = label.replace(/\b\w/g, l => l.toUpperCase());
            }
            
            if (isLast) {
                // Current page (no link)
                breadcrumbHTML += `
                    <li class="breadcrumb-item">
                        <span class="breadcrumb-current">${label}</span>
                    </li>
                `;
            } else {
                // Parent pages (with links)
                breadcrumbHTML += `
                    <li class="breadcrumb-item">
                        <a class="breadcrumb-link" href="${currentPath}/">${label}</a>
                    </li>
                `;
            }
        });
        
        breadcrumbHTML += `
                    </ol>
                </div>
            </nav>
        `;
        
        // Insert breadcrumbs
        breadcrumbContainer.innerHTML = breadcrumbHTML;
        
        // Generate structured data
        generateBreadcrumbSchema(pathParts);
    }
    
    function generateBreadcrumbSchema(pathParts) {
        const items = [{
            "@type": "ListItem",
            "position": 1,
            "name": config.homeLabel,
            "item": window.location.origin + "/"
        }];
        
        let currentPath = window.location.origin;
        pathParts.forEach((part, index) => {
            currentPath += '/' + part;
            const label = config.pathLabels[part] || part
                .replace(/-/g, ' ')
                .replace('.html', '')
                .replace(/\b\w/g, l => l.toUpperCase());
            
            items.push({
                "@type": "ListItem",
                "position": index + 2,
                "name": label,
                "item": currentPath + (index < pathParts.length - 1 ? '/' : '')
            });
        });
        
        const schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": items
        };
        
        // Add to page
        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(schema);
        document.head.appendChild(script);
    }
    
    // Initialize breadcrumbs when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', generateBreadcrumbs);
    } else {
        generateBreadcrumbs();
    }
})();