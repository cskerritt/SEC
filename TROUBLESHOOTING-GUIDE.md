# UI Library Troubleshooting Guide

## Common Issues and Solutions

### 1. Bootstrap Not Loading

**Symptoms:**
- Buttons appear unstyled
- Grid layout not working
- No responsive behavior

**Solutions:**

1. **Check if Bootstrap CSS is included:**
   ```html
   <!-- In Jekyll layouts -->
   {% include ui-library-setup.html %}
   
   <!-- Or in raw HTML -->
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
   ```

2. **Verify CDN is accessible:**
   ```bash
   curl -I https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css
   ```

3. **Check for CSS conflicts:**
   - Ensure Bootstrap CSS loads before custom CSS
   - Look for `!important` overrides
   - Check browser console for 404 errors

### 2. JavaScript Not Working

**Symptoms:**
- Dropdowns not opening
- Modals not appearing
- Alpine.js components static

**Solutions:**

1. **Ensure scripts load in correct order:**
   ```html
   <!-- Alpine.js with defer -->
   <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js"></script>
   
   <!-- Bootstrap Bundle at end of body -->
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
   ```

2. **Check for JavaScript errors:**
   ```javascript
   // Open browser console
   // Look for red error messages
   // Common: "Bootstrap is not defined"
   ```

3. **Test Alpine.js:**
   ```html
   <div x-data="{ test: 'working' }" x-text="test"></div>
   <!-- Should display: working -->
   ```

### 3. Mobile Menu Issues

**Symptoms:**
- Menu not opening on mobile
- Menu overlapping content
- Menu not closing

**Solutions:**

1. **Check data attributes:**
   ```html
   <button class="navbar-toggler" 
           type="button" 
           data-bs-toggle="collapse" 
           data-bs-target="#navbarNav">
   ```

2. **Verify z-index:**
   ```css
   .navbar {
       z-index: 1030; /* Bootstrap default */
   }
   ```

3. **Test in mobile view:**
   - Chrome DevTools > Toggle device toolbar
   - Test at 375px, 768px, 1024px widths

### 4. Layout Breaking

**Symptoms:**
- Content overflowing
- Columns not stacking
- Weird spacing

**Solutions:**

1. **Check container structure:**
   ```html
   <div class="container">
     <div class="row">
       <div class="col-md-6">Content</div>
       <div class="col-md-6">Content</div>
     </div>
   </div>
   ```

2. **Verify viewport meta tag:**
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1">
   ```

3. **Remove conflicting CSS:**
   ```css
   /* Bad - conflicts with Bootstrap */
   * { box-sizing: content-box; }
   
   /* Good - Bootstrap default */
   * { box-sizing: border-box; }
   ```

### 5. Slow Page Load

**Symptoms:**
- Long load times
- Layout shift
- Flash of unstyled content

**Solutions:**

1. **Optimize resource loading:**
   ```html
   <!-- Preload critical resources -->
   <link rel="preload" href="/css/ui-library-bootstrap.css" as="style">
   <link rel="preconnect" href="https://cdn.jsdelivr.net">
   ```

2. **Use minified versions:**
   ```html
   <!-- Use .min.css and .min.js files -->
   <link href="...bootstrap.min.css" rel="stylesheet">
   ```

3. **Enable compression:**
   ```yaml
   # In _config.yml
   plugins:
     - jekyll-gzip
   ```

### 6. Style Conflicts

**Symptoms:**
- Wrong colors appearing
- Unexpected margins/padding
- Buttons look wrong

**Solutions:**

1. **Check CSS specificity:**
   ```css
   /* Too specific - hard to override */
   body div.container section.hero h1.title { }
   
   /* Better - easier to work with */
   .hero-title { }
   ```

2. **Use Bootstrap utilities:**
   ```html
   <!-- Instead of custom CSS -->
   <div class="mt-4 mb-3 text-center">
   
   <!-- Not inline styles -->
   <div style="margin-top: 20px;">
   ```

3. **Check cascade order:**
   ```html
   <!-- Correct order -->
   <link href="bootstrap.css" rel="stylesheet">
   <link href="custom.css" rel="stylesheet">
   ```

### 7. Migration Issues

**Symptoms:**
- Old styles still showing
- Partial migration
- Broken pages after migration

**Solutions:**

1. **Check backup files:**
   ```bash
   # Find backup files
   find . -name "*.pre-ui-backup"
   
   # Restore if needed
   cp page.html.pre-ui-backup page.html
   ```

2. **Re-run migration:**
   ```bash
   # Test first
   python3 migrate-ui-simple.py page.html --dry-run
   
   # Then migrate
   python3 migrate-ui-simple.py page.html
   ```

3. **Verify migration:**
   ```bash
   # Test the page
   python3 test-ui-components.py page.html
   ```

## Debugging Tools

### Browser DevTools

1. **Inspect Element:**
   - Right-click > Inspect
   - Check computed styles
   - View box model

2. **Console:**
   - Check for errors
   - Test JavaScript
   - Log variables

3. **Network Tab:**
   - Check resource loading
   - Verify CDN requests
   - Monitor load times

### Command Line Tools

```bash
# Check which pages need migration
find . -name "*.html" -exec grep -L "bootstrap" {} \;

# Test specific page
python3 test-ui-components.py path/to/page.html

# Monitor performance
python3 monitor-performance.py path/to/directory/

# Validate HTML
python3 -m http.server 8000
# Then use W3C validator
```

### Quick Fixes

```bash
# Fix all buttons in a file
sed -i 's/class="button"/class="btn btn-primary"/g' file.html

# Add viewport meta to all pages missing it
find . -name "*.html" -exec grep -L "viewport" {} \; | \
xargs -I {} sed -i '/<head>/a <meta name="viewport" content="width=device-width, initial-scale=1">' {}

# Add Bootstrap to pages missing it
find . -name "*.html" -exec grep -L "bootstrap" {} \; | \
xargs -I {} python3 migrate-ui-simple.py {}
```

## Prevention Tips

1. **Always test locally first:**
   ```bash
   jekyll serve
   # Visit http://localhost:4000
   ```

2. **Use version control:**
   ```bash
   git add .
   git commit -m "Before UI migration"
   ```

3. **Test on multiple devices:**
   - Desktop (1920px)
   - Tablet (768px)
   - Mobile (375px)

4. **Check accessibility:**
   - Keyboard navigation
   - Screen reader testing
   - Color contrast

5. **Monitor performance:**
   ```bash
   # Before and after migration
   python3 monitor-performance.py
   ```

## Getting Help

1. **Check documentation:**
   - `/UI-LIBRARY-GUIDE.md`
   - `/UI-IMPLEMENTATION-PLAN.md`
   - Bootstrap docs: https://getbootstrap.com/docs/5.3/

2. **View examples:**
   - `/ui-library-demo.html`
   - `/ui-comparison.html`
   - `/test-ui-library.html`

3. **Run diagnostics:**
   ```bash
   # Full site test
   python3 test-ui-components.py .
   
   # Performance check
   python3 monitor-performance.py .
   ```

Remember: Most issues are caused by missing includes, wrong order, or CSS conflicts. Check these first!