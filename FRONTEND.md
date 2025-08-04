# Frontend Development Guidelines

## Project Overview
Skerritt Economics & Consulting website - A Jekyll-based static site for forensic economics and business valuation services.

## Tech Stack
- **Static Site Generator**: Jekyll 4.3.3
- **CSS Framework**: Custom CSS with design system tokens
- **JavaScript**: Vanilla JS for progressive enhancement
- **Build Tools**: Bundle (Ruby), Jekyll build pipeline
- **Deployment**: GitHub Pages

## Architecture

### Directory Structure
```
/
├── _includes/          # Reusable HTML components
├── _layouts/           # Page templates
├── _site/              # Built site (git ignored)
├── css/                # Stylesheets
├── js/                 # JavaScript files
├── images/             # Image assets
├── services/           # Service pages
├── practice-areas/     # Practice area pages
├── locations/          # Location pages
│   └── cities/         # 3,155 city-specific pages
├── blog/               # Blog posts
├── case-studies/       # Case study pages
└── tools/              # Interactive calculators
```

### Page Types
1. **Homepage** - Hero, services overview, trust signals, CTA
2. **Service Pages** - Detailed service descriptions with CTAs
3. **Practice Area Pages** - Legal practice area information
4. **Location Pages** - Geographic service areas
5. **City Pages** - SEO-optimized local landing pages
6. **Blog/Articles** - Educational content
7. **Contact** - Contact form and information

## Design System Implementation

### CSS Architecture
```css
/* Layer Order (from lowest to highest specificity) */
1. css/styles.css                    /* Base styles */
2. css/ui-ux-complete-fix.css        /* UI/UX standardization */
3. css/navigation-*.css              /* Navigation fixes */
4. css/about-*.css                   /* Page-specific fixes */
5. css/service-cta-white-text.css    /* Component overrides */
```

### Component Patterns

#### Hero Sections
```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <h1>{{ heading }}</h1>
      <p class="hero-subtitle">{{ subtitle }}</p>
      <div class="hero-cta">
        <a href="#" class="btn btn-primary">Primary CTA</a>
        <a href="#" class="btn btn-secondary">Secondary CTA</a>
      </div>
    </div>
  </div>
</section>
```

#### Service Cards
```html
<article class="service-card">
  <h3>{{ title }}</h3>
  <p>{{ description }}</p>
  <ul>
    <li>{{ feature }}</li>
  </ul>
  <a href="#" class="learn-more">Learn More →</a>
</article>
```

#### CTA Sections
```html
<section class="cta-section">
  <div class="container">
    <div class="cta-content">
      <h2>{{ heading }}</h2>
      <p>{{ description }}</p>
      <a href="#" class="btn btn-primary btn-large">{{ cta_text }}</a>
    </div>
  </div>
</section>
```

## Styling Guidelines

### Color Usage
- **Primary Blue (#1e3a8a)**: Headers, links, primary buttons
- **Secondary Purple (#3730a3)**: Gradients, accents
- **Gray Scale**: Text hierarchy, backgrounds
- **White**: Primary backgrounds, inverse text

### Typography Rules
- **Headings**: System fonts, bold weight
- **Body**: 1.0625rem base size, 1.7 line height
- **Mobile**: Scale down by ~20%

### Spacing Patterns
- **Sections**: 80px vertical padding (60px mobile)
- **Container**: 1200px max-width, 20px horizontal padding
- **Grid Gap**: 30px standard
- **Component Padding**: 30px cards, 20px mobile

### Responsive Breakpoints
```scss
$mobile: 768px;
$tablet: 1024px;
$desktop: 1280px;
$wide: 1536px;
```

## Component States

### Interactive Elements
```css
/* Default */
.btn { background: #1e3a8a; }

/* Hover */
.btn:hover { 
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(30, 58, 138, 0.3);
}

/* Focus */
.btn:focus-visible { 
  outline: 2px solid #1e3a8a;
  outline-offset: 2px;
}

/* Active */
.btn:active { 
  transform: translateY(0);
}
```

### Form Elements
```css
/* Input states */
input:focus { border-color: #1e3a8a; }
input:invalid { border-color: #ef4444; }
input:disabled { opacity: 0.6; }
```

## Performance Optimization

### Critical CSS
- Inline critical styles in `<head>`
- Lazy load non-critical CSS
- Use CSS custom properties for theming

### Image Optimization
- Use WebP with fallbacks
- Implement lazy loading
- Responsive images with srcset

### JavaScript Loading
```html
<!-- Defer non-critical scripts -->
<script src="/js/main.js" defer></script>

<!-- Async for independent scripts -->
<script src="/js/analytics.js" async></script>
```

## Accessibility Requirements

### WCAG 2.1 AA Compliance
- **Color Contrast**: 4.5:1 for normal text, 3:1 for large
- **Focus Indicators**: Visible focus states for all interactive elements
- **Keyboard Navigation**: Full keyboard support
- **Screen Readers**: Semantic HTML, ARIA labels where needed

### Testing Checklist
- [ ] Keyboard navigation works throughout
- [ ] Focus indicators are visible
- [ ] Color contrast passes WCAG AA
- [ ] Images have alt text
- [ ] Forms have proper labels
- [ ] Headings follow logical hierarchy
- [ ] Links have descriptive text

## Browser Support

### Target Browsers
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile Safari 14+
- Chrome Mobile 90+

### Progressive Enhancement
1. Core content accessible without JS
2. CSS Grid with Flexbox fallbacks
3. Modern CSS with fallbacks

## Development Workflow

### Local Development
```bash
# Install dependencies
bundle install

# Start development server
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Run with drafts
bundle exec jekyll serve --drafts
```

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/component-name

# Make changes and test
# ... edit files ...
bundle exec jekyll build

# Commit with semantic message
git add .
git commit -m "feat: add new component"

# Push and create PR
git push origin feature/component-name
```

### Testing Process
1. **Visual Testing**: Check all breakpoints
2. **Interaction Testing**: Verify all states
3. **Cross-browser Testing**: Test in target browsers
4. **Accessibility Testing**: Run axe DevTools
5. **Performance Testing**: Check Lighthouse scores

## Common Issues & Solutions

### Issue: Navigation not fixed on city pages
**Solution**: City pages use raw HTML. Run `fix-all-city-pages.py` to update.

### Issue: Text color inheritance
**Solution**: Use `!important` flags in override CSS files.

### Issue: Hero text not white
**Solution**: Apply gradient background and force white text color.

### Issue: Inconsistent spacing
**Solution**: Use design system spacing tokens consistently.

## Component Library

### Available Components
- Navigation (fixed header with dropdowns)
- Hero sections (gradient backgrounds)
- Service cards (hover effects)
- Location cards (grid layout)
- CTA sections (blue/gradient variants)
- Contact forms (validated inputs)
- Footer (multi-column layout)

### Adding New Components
1. Define in DESIGN-SYSTEM.md
2. Create HTML structure in _includes/
3. Add styles following BEM naming
4. Test across breakpoints
5. Document usage in this file

## Performance Metrics

### Target Metrics
- **LCP**: < 2.5s
- **FID**: < 100ms
- **CLS**: < 0.1
- **Lighthouse Score**: > 90

### Optimization Strategies
- Minimize CSS/JS
- Optimize images
- Use resource hints
- Implement caching headers
- Reduce DOM complexity

## Deployment

### Production Build
```bash
# Clean build directory
rm -rf _site

# Build with production config
JEKYLL_ENV=production bundle exec jekyll build

# Verify build
ls -la _site/
```

### GitHub Pages
- Automatic deployment on push to main
- Uses GitHub Actions for building
- Custom domain: skerritteconomics.com

## Maintenance

### Regular Tasks
- Update dependencies monthly
- Audit accessibility quarterly
- Review analytics for UX issues
- Test forms and CTAs
- Monitor page speed

### Version Control
- Semantic versioning for releases
- Changelog maintenance
- Git tags for major updates