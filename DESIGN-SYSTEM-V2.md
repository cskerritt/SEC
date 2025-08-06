# Skerritt Economics Design System V2
## Based on Modern UI Reference

## 1. Color Palette (HSL Format)

### Primary Colors
```css
:root {
  /* Deep Blue - Primary Brand Color */
  --primary: hsl(217, 91%, 15%);          /* #032b5b */
  --primary-foreground: hsl(0, 0%, 98%);  /* #fafafa */
  --primary-50: hsl(217, 91%, 95%);
  --primary-100: hsl(217, 91%, 90%);
  --primary-200: hsl(217, 91%, 80%);
  --primary-300: hsl(217, 91%, 70%);
  --primary-400: hsl(217, 91%, 60%);
  --primary-500: hsl(217, 91%, 50%);
  --primary-600: hsl(217, 91%, 40%);
  --primary-700: hsl(217, 91%, 30%);
  --primary-800: hsl(217, 91%, 20%);
  --primary-900: hsl(217, 91%, 15%);
  --primary-950: hsl(217, 91%, 10%);

  /* Golden Accent - Highlight Color */
  --accent: hsl(43, 74%, 49%);            /* #d4a11e */
  --accent-foreground: hsl(210, 20%, 15%);
  --accent-50: hsl(43, 74%, 95%);
  --accent-100: hsl(43, 74%, 90%);
  --accent-200: hsl(43, 74%, 80%);
  --accent-300: hsl(43, 74%, 70%);
  --accent-400: hsl(43, 74%, 60%);
  --accent-500: hsl(43, 74%, 49%);
  --accent-600: hsl(43, 74%, 40%);
  --accent-700: hsl(43, 74%, 30%);
  --accent-800: hsl(43, 74%, 20%);
  --accent-900: hsl(43, 74%, 10%);
}
```

### Neutral Colors
```css
:root {
  --background: hsl(0, 0%, 100%);         /* #ffffff */
  --foreground: hsl(210, 20%, 15%);       /* #1f2937 */
  
  --card: hsl(0, 0%, 100%);
  --card-foreground: hsl(210, 20%, 15%);
  
  --popover: hsl(0, 0%, 100%);
  --popover-foreground: hsl(210, 20%, 15%);
  
  --secondary: hsl(210, 40%, 96%);        /* #f1f5f9 */
  --secondary-foreground: hsl(210, 20%, 15%);
  
  --muted: hsl(210, 40%, 96%);
  --muted-foreground: hsl(215, 16%, 47%);
  
  --border: hsl(214, 32%, 91%);           /* #e2e8f0 */
  --input: hsl(214, 32%, 91%);
  --ring: hsl(217, 91%, 15%);
}
```

### Gradients
```css
:root {
  --gradient-primary: linear-gradient(135deg, hsl(217, 91%, 15%), hsl(217, 91%, 25%));
  --gradient-hero: linear-gradient(135deg, hsl(217, 91%, 15%) 0%, hsl(217, 91%, 20%) 50%, hsl(43, 74%, 49%) 100%);
  --gradient-subtle: linear-gradient(180deg, hsl(0, 0%, 100%), hsl(210, 40%, 98%));
  --gradient-card: linear-gradient(145deg, hsl(0, 0%, 100%), hsl(210, 40%, 97%));
}
```

### Shadows
```css
:root {
  --shadow-elegant: 0 10px 30px -10px hsl(217 91% 15% / 0.2);
  --shadow-card: 0 4px 20px -4px hsl(217 91% 15% / 0.1);
  --shadow-sm: 0 2px 8px -2px hsl(217 91% 15% / 0.08);
  --shadow-lg: 0 20px 40px -10px hsl(217 91% 15% / 0.15);
  --shadow-xl: 0 25px 50px -12px hsl(217 91% 15% / 0.2);
}
```

## 2. Typography

### Font Stack
```css
:root {
  --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-mono: 'Monaco', 'Courier New', monospace;
}
```

### Type Scale
```css
:root {
  /* Font Sizes */
  --text-xs: 0.75rem;      /* 12px */
  --text-sm: 0.875rem;     /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.125rem;     /* 18px */
  --text-xl: 1.25rem;      /* 20px */
  --text-2xl: 1.5rem;      /* 24px */
  --text-3xl: 1.875rem;    /* 30px */
  --text-4xl: 2.25rem;     /* 36px */
  --text-5xl: 3rem;        /* 48px */
  --text-6xl: 3.75rem;     /* 60px */

  /* Font Weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Line Heights */
  --leading-tight: 1.2;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}
```

### Heading Styles
```css
h1 {
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  color: var(--primary);
}

h2 {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
  font-weight: var(--font-bold);
  line-height: var(--leading-snug);
  color: var(--primary);
}

h3 {
  font-size: clamp(1.25rem, 3vw, 1.875rem);
  font-weight: var(--font-semibold);
  line-height: var(--leading-snug);
  color: var(--primary);
}
```

## 3. Spacing System (8-point Grid)

```css
:root {
  --spacing-0: 0;
  --spacing-1: 0.25rem;    /* 4px */
  --spacing-2: 0.5rem;     /* 8px */
  --spacing-3: 0.75rem;    /* 12px */
  --spacing-4: 1rem;       /* 16px */
  --spacing-5: 1.25rem;    /* 20px */
  --spacing-6: 1.5rem;     /* 24px */
  --spacing-8: 2rem;       /* 32px */
  --spacing-10: 2.5rem;    /* 40px */
  --spacing-12: 3rem;      /* 48px */
  --spacing-16: 4rem;      /* 64px */
  --spacing-20: 5rem;      /* 80px */
  --spacing-24: 6rem;      /* 96px */
}
```

## 4. Component Specifications

### Modern Button Styles
```css
.btn {
  /* Base Styles */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  font-size: var(--text-base);
  font-weight: var(--font-medium);
  line-height: 1;
  border-radius: 0.5rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  border: none;
  min-height: 48px;
  white-space: nowrap;
}

/* Primary Button */
.btn-primary {
  background: var(--primary);
  color: var(--primary-foreground);
}

.btn-primary:hover {
  background: var(--primary-800);
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* Professional Gradient Button */
.btn-professional {
  background: var(--gradient-primary);
  color: var(--primary-foreground);
}

.btn-professional:hover {
  box-shadow: var(--shadow-elegant);
  transform: translateY(-2px);
}

/* Accent Button */
.btn-accent {
  background: var(--accent);
  color: var(--accent-foreground);
  box-shadow: var(--shadow-card);
}

.btn-accent:hover {
  background: var(--accent-600);
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* Outline Button */
.btn-outline {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--border);
}

.btn-outline:hover {
  background: var(--secondary);
  border-color: var(--primary);
}

/* Button Sizes */
.btn-sm {
  padding: 0.625rem 1.25rem;
  font-size: var(--text-sm);
  min-height: 40px;
}

.btn-lg {
  padding: 1rem 2rem;
  font-size: var(--text-lg);
  min-height: 56px;
}
```

### Modern Card Component
```css
.card {
  background: var(--card);
  border-radius: 0.75rem;
  padding: 2rem;
  box-shadow: var(--shadow-card);
  transition: all 0.3s ease;
  border: 1px solid transparent;
}

.card:hover {
  box-shadow: var(--shadow-elegant);
  transform: translateY(-5px);
}

.card-header {
  margin-bottom: 1.5rem;
}

.card-title {
  font-size: var(--text-xl);
  font-weight: var(--font-semibold);
  color: var(--primary);
  margin-bottom: 0.5rem;
}

.card-description {
  font-size: var(--text-base);
  color: var(--muted-foreground);
  line-height: var(--leading-relaxed);
}

.card-content {
  font-size: var(--text-base);
  color: var(--foreground);
  line-height: var(--leading-normal);
}
```

### Modern Badge Component
```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  font-size: var(--text-xs);
  font-weight: var(--font-medium);
  border-radius: 9999px;
  transition: all 0.2s ease;
}

.badge-secondary {
  background: var(--secondary);
  color: var(--secondary-foreground);
}

.badge-accent {
  background: var(--accent-100);
  color: var(--accent-800);
}

.badge-primary {
  background: var(--primary-100);
  color: var(--primary-800);
}
```

### Modern Header with Backdrop Blur
```css
.header {
  position: fixed;
  top: 0;
  width: 100%;
  background: hsl(0 0% 100% / 0.95);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 50;
  border-bottom: 1px solid var(--border);
  transition: all 0.3s ease;
}

@supports (backdrop-filter: blur(10px)) {
  .header {
    background: hsl(0 0% 100% / 0.6);
  }
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

### Hero Section with Gradient Overlay
```css
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-background img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: var(--gradient-hero);
  opacity: 0.9;
}

.hero-content {
  position: relative;
  z-index: 10;
  text-align: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.hero-title {
  font-size: clamp(2.5rem, 6vw, 3.75rem);
  font-weight: var(--font-bold);
  color: var(--primary-foreground);
  margin-bottom: 1.5rem;
  line-height: var(--leading-tight);
}

.hero-subtitle {
  font-size: clamp(1.125rem, 2vw, 1.5rem);
  color: hsl(0 0% 100% / 0.9);
  margin-bottom: 2rem;
  line-height: var(--leading-relaxed);
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
}
```

## 5. Layout Components

### Container
```css
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

@media (min-width: 640px) {
  .container {
    padding: 0 1.5rem;
  }
}

@media (min-width: 1024px) {
  .container {
    padding: 0 2rem;
  }
}
```

### Section Spacing
```css
.section {
  padding: 3rem 0;
}

@media (min-width: 640px) {
  .section {
    padding: 4rem 0;
  }
}

@media (min-width: 1024px) {
  .section {
    padding: 5rem 0;
  }
}
```

### Grid System
```css
.grid {
  display: grid;
  gap: 2rem;
}

.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

@media (min-width: 640px) {
  .grid-cols-sm-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 768px) {
  .grid-cols-md-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .grid-cols-md-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .grid-cols-lg-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  
  .grid-cols-lg-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}
```

## 6. Animation Classes

```css
/* Smooth Transitions */
.transition-all {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.transition-colors {
  transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
}

.transition-transform {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hover Effects */
.hover-lift:hover {
  transform: translateY(-5px);
}

.hover-scale:hover {
  transform: scale(1.05);
}

/* Fade In Animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.6s ease forwards;
}
```

## 7. Utility Classes

```css
/* Text Alignment */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

/* Flexbox Utilities */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.gap-4 { gap: 1rem; }
.gap-6 { gap: 1.5rem; }
.gap-8 { gap: 2rem; }

/* Spacing Utilities */
.mt-4 { margin-top: 1rem; }
.mt-8 { margin-top: 2rem; }
.mb-4 { margin-bottom: 1rem; }
.mb-8 { margin-bottom: 2rem; }
.mx-auto { margin-left: auto; margin-right: auto; }

/* Max Width Utilities */
.max-w-sm { max-width: 24rem; }
.max-w-md { max-width: 28rem; }
.max-w-lg { max-width: 32rem; }
.max-w-xl { max-width: 36rem; }
.max-w-2xl { max-width: 42rem; }
.max-w-3xl { max-width: 48rem; }
.max-w-4xl { max-width: 56rem; }

/* Border Radius */
.rounded { border-radius: 0.25rem; }
.rounded-md { border-radius: 0.375rem; }
.rounded-lg { border-radius: 0.5rem; }
.rounded-xl { border-radius: 0.75rem; }
.rounded-full { border-radius: 9999px; }
```

## 8. Responsive Breakpoints

```css
/* Mobile First Breakpoints */
/* Default: 0px+ */
/* sm: 640px+ */
/* md: 768px+ */
/* lg: 1024px+ */
/* xl: 1280px+ */
/* 2xl: 1536px+ */

/* Example Usage */
@media (min-width: 640px) {
  /* Tablet styles */
}

@media (min-width: 1024px) {
  /* Desktop styles */
}
```

## Implementation Notes

1. **Use CSS Custom Properties**: All colors, spacing, and sizing should use the CSS custom properties defined above
2. **Mobile First**: Start with mobile styles and add complexity for larger screens
3. **Semantic HTML**: Use proper HTML elements before adding classes
4. **Accessibility**: Ensure all interactive elements have proper focus states and ARIA labels
5. **Performance**: Use `will-change` sparingly and remove after animations
6. **Browser Support**: Include vendor prefixes for backdrop-filter and other modern properties