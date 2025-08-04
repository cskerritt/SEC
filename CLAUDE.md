# CLAUDE.md - AI Development Guidelines

## Project Context
You are working on the Skerritt Economics & Consulting website, a Jekyll-based static site for forensic economics and business valuation services. This document contains critical instructions for maintaining consistency and quality.

## CRITICAL: Always Reference These Files
1. **DESIGN-SYSTEM.md** - Color palette, typography, spacing, components
2. **FRONTEND.md** - Architecture, patterns, workflows
3. **CLAUDE.md** - This file, AI-specific guidelines

## UI/UX Development Rules

### 1. NEVER Use Absolute Positioning
- Use CSS Grid for layouts
- Use Flexbox for component alignment
- Only exception: modals, tooltips, dropdowns

### 2. Follow the Design System Strictly
```css
/* ALWAYS use design tokens */
color: var(--primary-800); /* NOT: #1e3a8a */
padding: var(--spacing-6); /* NOT: 24px */
font-size: var(--text-lg); /* NOT: 1.125rem */
```

### 3. Component-First Development
- Build components in isolation first
- Test at all breakpoints before integration
- One component per file in _includes/

### 4. Mobile-First Responsive Design
```css
/* Start with mobile */
.component { 
  padding: 1rem; 
}

/* Add complexity for larger screens */
@media (min-width: 768px) {
  .component { 
    padding: 2rem; 
  }
}
```

### 5. Accessibility is Non-Negotiable
- Semantic HTML first, ARIA second
- 4.5:1 contrast ratio minimum
- 48px touch targets minimum
- Keyboard navigation for everything

## CSS Architecture Rules

### File Organization
```
css/
├── base/           # Reset, typography, variables
├── components/     # Individual component styles
├── layouts/        # Page layouts, grids
├── pages/          # Page-specific styles
└── utils/          # Helpers, overrides
```

### Naming Convention (BEM)
```css
.block {}
.block__element {}
.block--modifier {}
.block__element--modifier {}
```

### Specificity Management
1. Use classes, not IDs for styling
2. Maximum nesting depth: 3 levels
3. Use `!important` only in override files
4. Scope components with unique class names

## JavaScript Guidelines

### Progressive Enhancement
```javascript
// Check if feature is supported
if ('IntersectionObserver' in window) {
  // Use modern feature
} else {
  // Provide fallback
}
```

### Event Handling
```javascript
// Use event delegation
document.addEventListener('click', (e) => {
  if (e.target.matches('.btn')) {
    // Handle button click
  }
});
```

### Performance
- Debounce scroll/resize events
- Use requestAnimationFrame for animations
- Lazy load non-critical resources

## Common Patterns

### Hero Section
```html
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <h1>{{ heading }}</h1>
      <p class="hero-subtitle">{{ subtitle }}</p>
      <div class="hero-cta">
        <a href="#" class="btn btn-primary">CTA</a>
      </div>
    </div>
  </div>
</section>
```

### Service Card
```html
<article class="service-card">
  <div class="card-icon">
    <i class="icon"></i>
  </div>
  <h3 class="card-title">{{ title }}</h3>
  <p class="card-description">{{ description }}</p>
  <a href="#" class="card-link">Learn More →</a>
</article>
```

### CTA Section
```html
<section class="cta-section">
  <div class="container">
    <h2>{{ heading }}</h2>
    <p>{{ description }}</p>
    <a href="#" class="btn btn-primary btn-large">{{ cta }}</a>
  </div>
</section>
```

## Testing Checklist

### Before Every Change
- [ ] Check DESIGN-SYSTEM.md for tokens
- [ ] Reference FRONTEND.md for patterns
- [ ] Test on mobile viewport first
- [ ] Verify accessibility with keyboard
- [ ] Check color contrast ratios
- [ ] Test in Chrome, Firefox, Safari
- [ ] Run Lighthouse audit

### Before Committing
- [ ] Remove console.logs
- [ ] Minimize CSS/JS for production
- [ ] Optimize images
- [ ] Update documentation if needed
- [ ] Write semantic commit message

## City Pages Special Instructions

The site has 3,155 city-specific pages in `/locations/cities/`. These are raw HTML files, not Jekyll templates.

### Updating City Pages
```python
# Use the fix-all-city-pages.py script
# These pages need manual CSS/JS injection
# Always test a sample before bulk updates
```

## Known Issues & Solutions

### Issue: Navigation dropdown not clickable
**Solution**: Check z-index and position: fixed

### Issue: Text color inheritance problems
**Solution**: Use !important in override CSS files

### Issue: Hero gradient not showing
**Solution**: Check background shorthand property order

### Issue: Mobile menu not working
**Solution**: Verify JavaScript event listeners

## Git Commit Standards

### Commit Message Format
```
type: description

- Detail 1
- Detail 2

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `style`: CSS/formatting changes
- `refactor`: Code restructuring
- `docs`: Documentation updates
- `test`: Test additions/changes
- `chore`: Maintenance tasks

## Performance Targets

### Core Web Vitals
- **LCP**: < 2.5 seconds
- **FID**: < 100 milliseconds
- **CLS**: < 0.1

### Lighthouse Scores
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 90
- SEO: > 95

## Resource Limits

### File Sizes
- CSS: < 50KB per file
- JS: < 30KB per file
- Images: < 200KB (optimize with WebP)
- Total page weight: < 1MB

### Complexity Limits
- Max DOM depth: 15 levels
- Max CSS selectors: 4000
- Max inline styles: 0 (use classes)

## Quality Assurance

### Visual Consistency
1. Screenshot reference designs
2. Use browser DevTools for pixel-perfect matching
3. Test all interactive states (hover, focus, active)
4. Verify animations are smooth (60fps)

### Code Quality
1. No inline styles
2. No inline JavaScript
3. No deprecated HTML elements
4. Valid HTML5 markup
5. Valid CSS3
6. ESLint-clean JavaScript

## Emergency Fixes

### If the site breaks:
1. Check browser console for errors
2. Verify Jekyll build succeeded
3. Check CSS cascade order
4. Inspect element for computed styles
5. Test in incognito mode (no cache)

### Quick Rollback
```bash
git revert HEAD
git push origin main
```

## Remember

1. **Design System First**: Always check DESIGN-SYSTEM.md
2. **Mobile First**: Start simple, add complexity
3. **Accessibility Always**: Never compromise on a11y
4. **Performance Matters**: Every KB counts
5. **Test Everything**: Manual testing catches what automation misses
6. **Document Changes**: Update relevant .md files
7. **Semantic HTML**: Right element for the job
8. **Progressive Enhancement**: Core functionality without JS
9. **Consistent Spacing**: Use the 8-point grid
10. **User First**: UX > DX (User Experience over Developer Experience)