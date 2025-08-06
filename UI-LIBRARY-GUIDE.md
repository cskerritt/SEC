# UI Library Implementation Guide

## Overview

This guide documents the comprehensive UI library implementation for the Skerritt Economics website, ensuring consistent, professional, and accessible UI across all pages.

## Libraries Implemented

### 1. **Bootstrap 5.3.2**
- **Purpose**: Core UI framework providing responsive grid, components, and utilities
- **Size**: ~25KB CSS (minified + gzipped)
- **Customization**: Custom SCSS theme matching your brand colors

### 2. **Alpine.js 3.13.3**
- **Purpose**: Lightweight reactive framework for interactive components
- **Size**: ~15KB (minified + gzipped)
- **Usage**: Dropdowns, toggles, modals, and dynamic UI elements

### 3. **Animate.css 4.1.1**
- **Purpose**: Professional animation library
- **Size**: ~4KB (core animations only)
- **Usage**: Hero animations, scroll reveals, transitions

### 4. **Font Awesome 6.5.1**
- **Purpose**: Comprehensive icon library
- **Size**: ~10KB (subset of used icons)
- **Usage**: Service icons, UI elements, social media

## Installation

### 1. Include UI Library Setup in Layout

Add to your `_layouts/default.html` in the `<head>` section:

```liquid
{% include ui-library-setup.html %}
```

### 2. Compile Bootstrap SCSS

Install Bootstrap via npm:
```bash
npm install bootstrap@5.3.2
```

Compile the custom theme:
```bash
sass css/ui-library-bootstrap.scss css/ui-library-bootstrap.css --style=compressed
```

Or use Jekyll's built-in Sass processor by renaming to `ui-library-bootstrap.scss` and placing in `_sass/`.

## Component Library

### Hero Section
```liquid
{% include components/hero-section.html 
   title="Expert Forensic Economics" 
   accent_text="For Legal Success"
   subtitle="Court-qualified expert witness services for attorneys nationwide"
   cta_text="Schedule Consultation" 
   cta_url="/contact/"
   secondary_text="View Services"
   secondary_url="/services/"
   features=page.hero_features
   scroll_hint=true %}
```

### Service Cards
```liquid
{% include components/service-card.html 
   icon="fa-calculator" 
   title="Economic Damage Analysis"
   description="Comprehensive calculations for lost earnings and benefits"
   link="/services/forensic-economics/"
   badges=page.service_badges
   features=page.service_features %}
```

### Contact Card (Sidebar)
```liquid
{% include components/contact-card.html %}
```

### Testimonial Cards
```liquid
{% include components/testimonial-card.html 
   quote="Outstanding expert witness services that helped us win our case."
   author="John Smith"
   title="Managing Partner, Smith & Associates"
   rating=5 %}
```

### CTA Sections
```liquid
{% include components/cta-section.html 
   title="Ready to Strengthen Your Case?" 
   description="Get expert economic analysis from court-qualified professionals"
   cta_text="Schedule Free Consultation" 
   cta_url="/contact/"
   style="gradient" %}
```

## Bootstrap Classes Reference

### Layout
- **Container**: `container`, `container-fluid`, `container-{breakpoint}`
- **Grid**: `row`, `col`, `col-{breakpoint}-{size}`
- **Spacing**: `p-{0-5}`, `m-{0-5}`, `px-{size}`, `py-{size}`

### Typography
- **Headings**: `display-{1-6}`, `h{1-6}`
- **Text**: `lead`, `fs-{1-6}`, `fw-{light|normal|bold}`
- **Alignment**: `text-{start|center|end}`

### Components
- **Buttons**: `btn`, `btn-{primary|secondary|accent|outline-*}`
- **Cards**: `card`, `card-body`, `card-header`, `card-footer`
- **Badges**: `badge`, `badge-{primary|secondary|accent}`
- **Alerts**: `alert`, `alert-{primary|success|warning|danger}`

### Utilities
- **Display**: `d-{none|block|flex}`, `d-{breakpoint}-{value}`
- **Position**: `position-{static|relative|absolute|fixed|sticky}`
- **Shadow**: `shadow-{none|sm|lg}`
- **Border**: `border`, `rounded`, `rounded-{size}`

## Alpine.js Components

### Toggle Component
```html
<div x-data="{ open: false }">
  <button @click="open = !open" class="btn btn-primary">
    Toggle Content
  </button>
  <div x-show="open" x-transition>
    <!-- Hidden content -->
  </div>
</div>
```

### Dropdown Component
```html
<div x-data="{ dropdown: false }" @click.outside="dropdown = false">
  <button @click="dropdown = !dropdown" class="btn btn-secondary">
    Options <i class="fas fa-chevron-down"></i>
  </button>
  <div x-show="dropdown" x-transition class="dropdown-menu show">
    <!-- Dropdown items -->
  </div>
</div>
```

### Tab Component
```html
<div x-data="{ activeTab: 'tab1' }">
  <ul class="nav nav-tabs">
    <li class="nav-item">
      <a @click="activeTab = 'tab1'" 
         :class="{ 'active': activeTab === 'tab1' }" 
         class="nav-link" href="#">Tab 1</a>
    </li>
  </ul>
  <div x-show="activeTab === 'tab1'" x-transition>
    <!-- Tab content -->
  </div>
</div>
```

## Responsive Design

### Breakpoints
- **xs**: <576px (default)
- **sm**: ≥576px
- **md**: ≥768px
- **lg**: ≥1024px
- **xl**: ≥1280px
- **xxl**: ≥1536px

### Mobile-First Classes
```html
<!-- Stack on mobile, side-by-side on tablet+ -->
<div class="row">
  <div class="col-12 col-md-6">Content 1</div>
  <div class="col-12 col-md-6">Content 2</div>
</div>

<!-- Hide on mobile, show on desktop -->
<div class="d-none d-lg-block">Desktop only</div>

<!-- Different spacing on different screens -->
<div class="p-3 p-md-4 p-lg-5">Responsive padding</div>
```

## Accessibility Features

### Built-in Accessibility
1. **ARIA Labels**: All interactive elements have proper ARIA labels
2. **Focus States**: Enhanced focus indicators for keyboard navigation
3. **Skip Links**: Include skip navigation links
4. **Semantic HTML**: Proper heading hierarchy and landmarks
5. **Color Contrast**: All text meets WCAG AAA standards

### Accessible Components
```html
<!-- Accessible button with loading state -->
<button class="btn btn-primary" 
        aria-label="Submit contact form"
        data-loading-text="<i class='fas fa-spinner fa-spin'></i> Sending...">
  Send Message
</button>

<!-- Accessible modal trigger -->
<button class="btn btn-secondary" 
        data-bs-toggle="modal" 
        data-bs-target="#myModal"
        aria-label="Open contact modal">
  Contact Us
</button>
```

## Performance Optimization

### 1. Load Only What You Need
```html
<!-- Load only required Bootstrap components -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap-grid.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap-utilities.min.css" rel="stylesheet">
```

### 2. Lazy Load Components
```html
<!-- Lazy load Alpine.js components -->
<div x-data="{ loaded: false }" 
     x-intersect="loaded = true">
  <div x-show="loaded" x-transition>
    <!-- Heavy content -->
  </div>
</div>
```

### 3. Preload Critical Resources
```html
<link rel="preload" href="/css/ui-library-bootstrap.css" as="style">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
```

## Migration Guide for Existing Pages

### 1. Service Pages
Replace existing markup with Bootstrap components:

**Before:**
```html
<div class="service-card">
  <h3>Service Title</h3>
  <p>Description</p>
</div>
```

**After:**
```liquid
{% include components/service-card.html 
   title="Service Title"
   description="Description"
   icon="fa-chart-line" %}
```

### 2. City Pages
Update the 3,155 city pages using the batch update script:

```python
# Script to update city pages with new UI library
import os
import re

def update_city_page(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add Bootstrap classes
    content = re.sub(r'class="button"', 'class="btn btn-primary"', content)
    content = re.sub(r'class="card"', 'class="card shadow-sm hover-lift"', content)
    
    # Add UI library include if not present
    if 'ui-library-setup.html' not in content:
        content = content.replace('</head>', '{% include ui-library-setup.html %}\n</head>')
    
    with open(filepath, 'w') as f:
        f.write(content)

# Run on all city pages
for filename in os.listdir('locations/cities/'):
    if filename.endswith('.html'):
        update_city_page(f'locations/cities/{filename}')
```

### 3. Form Elements
Update forms to use Bootstrap styling:

**Before:**
```html
<form>
  <input type="text" name="name" placeholder="Your Name">
  <button type="submit">Submit</button>
</form>
```

**After:**
```html
<form class="needs-validation" novalidate>
  <div class="mb-3">
    <label for="name" class="form-label">Your Name</label>
    <input type="text" class="form-control" id="name" required>
    <div class="invalid-feedback">Please provide your name.</div>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## Testing Checklist

### Browser Testing
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Responsive Testing
- [ ] Mobile (320px - 576px)
- [ ] Tablet (768px - 1024px)
- [ ] Desktop (1024px+)
- [ ] Large screens (1920px+)

### Accessibility Testing
- [ ] Keyboard navigation
- [ ] Screen reader compatibility
- [ ] Color contrast (WCAG AAA)
- [ ] Focus indicators
- [ ] ARIA labels

### Performance Testing
- [ ] Page load time < 3s
- [ ] First Contentful Paint < 1.5s
- [ ] Cumulative Layout Shift < 0.1
- [ ] JavaScript bundle size < 100KB

## Troubleshooting

### Common Issues

1. **Bootstrap not loading**: Check CDN links and fallback to local files
2. **Alpine.js not working**: Ensure `defer` attribute is present
3. **Animations janky**: Use `will-change` CSS property sparingly
4. **Mobile menu not closing**: Add `@click.outside` directive

### Debug Mode
Add to any page for debugging:
```html
<script>
// Enable Bootstrap tooltips everywhere
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl, {
    trigger: 'hover focus',
    placement: 'auto',
    html: true
  })
})

// Log Alpine.js component states
document.addEventListener('alpine:init', () => {
  Alpine.magic('log', () => {
    return (...args) => console.log(...args)
  })
})
</script>
```

## Resources

- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Alpine.js Documentation](https://alpinejs.dev/)
- [Animate.css Documentation](https://animate.style/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

## Next Steps

1. Compile Bootstrap SCSS with your custom variables
2. Test components on a few pages first
3. Run the migration script on city pages
4. Update Jekyll templates to use new components
5. Monitor performance metrics
6. Gather user feedback

Remember: Consistency is key. Use these components everywhere for a professional, cohesive experience.