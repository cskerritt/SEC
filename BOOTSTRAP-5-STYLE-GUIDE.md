# Bootstrap 5 Style Guide for Skerritt Economics
## Comprehensive Design System Reference

---

## 🎨 Core Design Principles

1. **Consistency**: Every page uses the same components and patterns
2. **Accessibility**: WCAG AAA compliant contrast ratios
3. **Mobile-First**: Responsive design that works on all devices
4. **Performance**: CDN-hosted resources, minimal custom CSS
5. **Professional**: Clean, modern design appropriate for legal/business clients

---

## 🎨 Color Palette

### Primary Colors
```css
/* Brand Colors - Use these consistently */
--primary-blue: #032b5b;      /* Deep Blue - Headers, CTAs */
--secondary-blue: #1e40af;    /* Lighter Blue - Gradients */
--accent-gold: #d4a11e;       /* Gold - Highlights, badges */
--text-white: #ffffff;        /* White - Text on dark backgrounds */
--text-dark: #212529;         /* Dark - Regular text */
--text-muted: #6c757d;        /* Gray - Secondary text */
```

### Bootstrap Color Classes
```html
<!-- Backgrounds -->
<div class="bg-primary">...</div>          <!-- Bootstrap primary (override with our blue) -->
<div class="bg-gradient-primary">...</div>  <!-- Blue gradient background -->
<div class="bg-light">...</div>            <!-- Light gray background -->
<div class="bg-white">...</div>            <!-- White background -->

<!-- Text Colors -->
<p class="text-primary">...</p>             <!-- Blue text -->
<p class="text-white">...</p>               <!-- White text -->
<p class="text-muted">...</p>               <!-- Gray text -->
<p class="text-dark">...</p>                <!-- Dark text -->
```

### Custom Gradient
```css
/* Hero Section Gradient - Use this for all hero sections */
.bg-gradient-primary {
    background: linear-gradient(135deg, #032b5b 0%, #1e40af 100%) !important;
}
```

---

## 📐 Layout Structure

### Standard Page Template
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="../../css/modern-ui.css">
</head>
<body>
    <!-- Hero Section -->
    <section class="hero-section bg-gradient-primary text-white py-5">
        <div class="container">
            <div class="row align-items-center min-vh-50">
                <div class="col-lg-8 mx-auto text-center">
                    <h1 class="display-4 fw-bold mb-4">Page Title</h1>
                    <p class="lead mb-4">Page description</p>
                    <div class="d-flex gap-3 justify-content-center flex-wrap">
                        <a href="#" class="btn btn-light btn-lg">Primary CTA</a>
                        <a href="#" class="btn btn-outline-light btn-lg">Secondary CTA</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Content Sections -->
    <section class="py-5">
        <div class="container">
            <!-- Content here -->
        </div>
    </section>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## 🧩 Component Library

### 1. Hero Sections
```html
<!-- Standard Hero -->
<section class="hero-section bg-gradient-primary text-white py-5">
    <div class="container">
        <div class="row align-items-center min-vh-50">
            <div class="col-lg-8 mx-auto text-center">
                <h1 class="display-4 fw-bold mb-4">Expert Economic Analysis</h1>
                <p class="lead mb-5">Trusted by attorneys nationwide</p>
                <div class="d-flex gap-3 justify-content-center flex-wrap">
                    <a href="/contact/" class="btn btn-light btn-lg px-4">Get Consultation</a>
                    <a href="#services" class="btn btn-outline-light btn-lg px-4">Our Services</a>
                </div>
            </div>
        </div>
    </div>
</section>
```

### 2. Service Cards
```html
<!-- Service Card Grid -->
<div class="row g-4">
    <div class="col-md-6 col-lg-3">
        <div class="card h-100 shadow-sm hover-shadow transition">
            <div class="card-body text-center">
                <div class="feature-icon bg-primary bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                    <i class="fas fa-chart-line text-white fa-2x"></i>
                </div>
                <h3 class="h5">Service Title</h3>
                <p class="text-muted">Service description goes here</p>
                <a href="#" class="btn btn-sm btn-outline-primary">Learn More →</a>
            </div>
        </div>
    </div>
</div>
```

### 3. Buttons
```html
<!-- Primary Buttons -->
<button class="btn btn-primary btn-lg">Large Primary</button>
<button class="btn btn-primary">Regular Primary</button>
<button class="btn btn-primary btn-sm">Small Primary</button>

<!-- Light Buttons (for dark backgrounds) -->
<button class="btn btn-light btn-lg">Light Button</button>
<button class="btn btn-outline-light btn-lg">Outline Light</button>

<!-- Secondary Buttons -->
<button class="btn btn-outline-primary">Outline Primary</button>
<button class="btn btn-secondary">Secondary</button>
```

### 4. Forms
```html
<!-- Professional Form Layout -->
<form class="needs-validation" novalidate>
    <div class="row g-3">
        <div class="col-md-6">
            <label for="name" class="form-label">Full Name <span class="text-danger">*</span></label>
            <input type="text" class="form-control form-control-lg" id="name" required>
            <div class="invalid-feedback">Please enter your name.</div>
        </div>
        <div class="col-md-6">
            <label for="email" class="form-label">Email <span class="text-danger">*</span></label>
            <input type="email" class="form-control form-control-lg" id="email" required>
            <div class="invalid-feedback">Please enter a valid email.</div>
        </div>
        <div class="col-12">
            <label for="message" class="form-label">Message</label>
            <textarea class="form-control form-control-lg" id="message" rows="4"></textarea>
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary btn-lg">Submit</button>
        </div>
    </div>
</form>
```

### 5. Feature Sections
```html
<!-- Icon Feature Grid -->
<section class="py-5 bg-light">
    <div class="container">
        <h2 class="text-center mb-5">Why Choose Us</h2>
        <div class="row g-4">
            <div class="col-md-6 col-lg-3">
                <div class="text-center">
                    <div class="feature-icon bg-primary bg-gradient rounded-circle p-3 d-inline-flex mb-3">
                        <i class="fas fa-check text-white fa-2x"></i>
                    </div>
                    <h3 class="h5">Feature Title</h3>
                    <p class="text-muted">Feature description</p>
                </div>
            </div>
        </div>
    </div>
</section>
```

### 6. Accordions
```html
<!-- FAQ Accordion -->
<div class="accordion" id="faqAccordion">
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
                Question goes here?
            </button>
        </h2>
        <div id="faq1" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion">
            <div class="accordion-body">
                Answer goes here...
            </div>
        </div>
    </div>
</div>
```

### 7. CTA Sections
```html
<!-- Call to Action -->
<section class="py-5 bg-gradient-primary text-white">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-8">
                <h2 class="mb-3">Ready to Get Started?</h2>
                <p class="lead mb-4 mb-lg-0">Contact us today for a free consultation</p>
            </div>
            <div class="col-lg-4 text-lg-end">
                <a href="/contact/" class="btn btn-light btn-lg me-2">Get Started</a>
                <a href="tel:203-605-2814" class="btn btn-outline-light btn-lg">Call Now</a>
            </div>
        </div>
    </div>
</section>
```

---

## 📱 Responsive Utilities

### Breakpoints
```scss
// Bootstrap 5 Breakpoints
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```

### Responsive Classes
```html
<!-- Responsive Display -->
<div class="d-none d-md-block">Hidden on mobile</div>
<div class="d-block d-md-none">Mobile only</div>

<!-- Responsive Columns -->
<div class="col-12 col-md-6 col-lg-4">Responsive column</div>

<!-- Responsive Spacing -->
<div class="py-3 py-md-4 py-lg-5">Responsive padding</div>

<!-- Responsive Text -->
<h1 class="fs-3 fs-md-2 fs-lg-1">Responsive heading</h1>
```

---

## 🎯 Icon Usage

### Font Awesome Icons
```html
<!-- Service Icons -->
<i class="fas fa-chart-line"></i>      <!-- Forensic Economics -->
<i class="fas fa-building"></i>        <!-- Business Valuation -->
<i class="fas fa-user-tie"></i>        <!-- Vocational Expert -->
<i class="fas fa-heart"></i>           <!-- Life Care Planning -->

<!-- UI Icons -->
<i class="fas fa-check"></i>           <!-- Checkmark -->
<i class="fas fa-phone"></i>           <!-- Phone -->
<i class="fas fa-envelope"></i>        <!-- Email -->
<i class="fas fa-map-marker-alt"></i>  <!-- Location -->
<i class="fas fa-search"></i>          <!-- Search -->
<i class="fas fa-bars"></i>            <!-- Menu -->
<i class="fas fa-times"></i>           <!-- Close -->
<i class="fas fa-arrow-right"></i>     <!-- Arrow -->
```

---

## 🚀 Custom CSS Classes

### Add to every page that needs custom styling:
```css
/* Custom hover effects */
.hover-shadow {
    transition: all 0.3s ease;
}
.hover-shadow:hover {
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    transform: translateY(-5px);
}

/* Ensure blue gradient */
.bg-gradient-primary {
    background: linear-gradient(135deg, #032b5b 0%, #1e40af 100%) !important;
}

/* Feature icons */
.feature-icon {
    width: 80px;
    height: 80px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

/* Minimum height for hero sections */
.min-vh-50 {
    min-height: 50vh;
}
```

---

## 📋 Implementation Checklist

When updating any page, ensure:

- [ ] Uses `layout: modern-default` in front matter
- [ ] Includes Bootstrap 5.3.2 CSS from CDN
- [ ] Includes Font Awesome 6.5.1 from CDN
- [ ] Has blue gradient hero section with white text
- [ ] Uses Bootstrap grid system (container, row, col)
- [ ] Buttons use Bootstrap button classes
- [ ] Forms use Bootstrap form classes
- [ ] All text on colored backgrounds has proper contrast
- [ ] Responsive classes used for mobile compatibility
- [ ] Custom CSS is minimal and follows the guide
- [ ] Icons use Font Awesome classes
- [ ] Spacing uses Bootstrap utilities (py-5, mb-4, etc.)
- [ ] Cards use Bootstrap card component
- [ ] CTAs are prominent and use proper button styling

---

## 🔧 Common Patterns

### 1. Page with Hero + Services + CTA
```
[Hero Section - Blue Gradient]
[Services Grid - White/Light Background]
[Features Section - Light Background]
[CTA Section - Blue Gradient]
```

### 2. Form Page Layout
```
[Hero Section - Blue Gradient]
[Two Column: Form | Sidebar Info]
[FAQ Section - White Background]
[CTA Section - Blue Gradient]
```

### 3. Location/Directory Page
```
[Hero Section - Blue Gradient]
[Search Bar - White Background]
[States Grid/Accordion - Light Background]
[CTA Section - Blue Gradient]
```

---

## ⚠️ Important Notes

1. **Always use relative paths** for internal links
2. **CDN resources** should be loaded from official CDNs
3. **Test on mobile** - use browser dev tools
4. **Validate forms** - use Bootstrap validation
5. **Keep it simple** - don't over-customize
6. **Follow the pattern** - consistency is key

---

This style guide ensures every page on the Skerritt Economics website maintains a consistent, professional appearance using Bootstrap 5 components and our brand colors.