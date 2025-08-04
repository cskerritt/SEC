# Skerritt Economics Design System

## 1. Color Palette

### Primary Colors
```json
{
  "primary": {
    "50": "#eff6ff",
    "100": "#dbeafe",
    "200": "#bfdbfe",
    "300": "#93c5fd",
    "400": "#60a5fa",
    "500": "#3b82f6",
    "600": "#2563eb",
    "700": "#1d4ed8",
    "800": "#1e40af",
    "900": "#1e3a8a",
    "950": "#172554"
  },
  "secondary": {
    "500": "#8b5cf6",
    "600": "#7c3aed",
    "700": "#6d28d9",
    "800": "#5b21b6",
    "900": "#4c1d95"
  }
}
```

### Neutral Colors
```json
{
  "gray": {
    "50": "#f9fafb",
    "100": "#f3f4f6",
    "200": "#e5e7eb",
    "300": "#d1d5db",
    "400": "#9ca3af",
    "500": "#6b7280",
    "600": "#4b5563",
    "700": "#374151",
    "800": "#1f2937",
    "900": "#111827",
    "950": "#030712"
  }
}
```

### Semantic Colors
```json
{
  "success": "#10b981",
  "warning": "#f59e0b",
  "error": "#ef4444",
  "info": "#3b82f6",
  "background": "#ffffff",
  "surface": "#f9fafb",
  "text": {
    "primary": "#1f2937",
    "secondary": "#4b5563",
    "tertiary": "#6b7280",
    "inverse": "#ffffff"
  }
}
```

## 2. Typography Scale

### Font Family
```css
--font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
--font-mono: 'Monaco', 'Courier New', monospace;
```

### Type Scale
```json
{
  "fontSize": {
    "xs": "0.75rem",     // 12px
    "sm": "0.875rem",    // 14px
    "base": "1rem",      // 16px
    "lg": "1.125rem",    // 18px
    "xl": "1.25rem",     // 20px
    "2xl": "1.5rem",     // 24px
    "3xl": "1.875rem",   // 30px
    "4xl": "2.25rem",    // 36px
    "5xl": "3rem",       // 48px
    "6xl": "3.75rem"     // 60px
  },
  "fontWeight": {
    "normal": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700
  },
  "lineHeight": {
    "tight": 1.1,
    "snug": 1.2,
    "normal": 1.5,
    "relaxed": 1.625,
    "loose": 2
  }
}
```

### Text Styles
```json
{
  "h1": {
    "desktop": { "size": "3rem", "weight": 700, "lineHeight": 1.2 },
    "mobile": { "size": "2rem", "weight": 700, "lineHeight": 1.2 }
  },
  "h2": {
    "desktop": { "size": "2.25rem", "weight": 700, "lineHeight": 1.3 },
    "mobile": { "size": "1.75rem", "weight": 700, "lineHeight": 1.3 }
  },
  "h3": {
    "desktop": { "size": "1.875rem", "weight": 600, "lineHeight": 1.4 },
    "mobile": { "size": "1.5rem", "weight": 600, "lineHeight": 1.4 }
  },
  "h4": {
    "desktop": { "size": "1.5rem", "weight": 600, "lineHeight": 1.4 },
    "mobile": { "size": "1.25rem", "weight": 600, "lineHeight": 1.4 }
  },
  "body": {
    "large": { "size": "1.125rem", "weight": 400, "lineHeight": 1.7 },
    "base": { "size": "1rem", "weight": 400, "lineHeight": 1.6 },
    "small": { "size": "0.875rem", "weight": 400, "lineHeight": 1.5 }
  }
}
```

## 3. Spacing System

### Base Unit: 4px
```json
{
  "spacing": {
    "0": "0",
    "1": "0.25rem",   // 4px
    "2": "0.5rem",    // 8px
    "3": "0.75rem",   // 12px
    "4": "1rem",      // 16px
    "5": "1.25rem",   // 20px
    "6": "1.5rem",    // 24px
    "8": "2rem",      // 32px
    "10": "2.5rem",   // 40px
    "12": "3rem",     // 48px
    "16": "4rem",     // 64px
    "20": "5rem",     // 80px
    "24": "6rem",     // 96px
    "32": "8rem",     // 128px
    "40": "10rem",    // 160px
    "48": "12rem",    // 192px
    "56": "14rem",    // 224px
    "64": "16rem"     // 256px
  }
}
```

## 4. Component Specifications

### Buttons
```json
{
  "button": {
    "base": {
      "padding": "14px 28px",
      "fontSize": "1rem",
      "fontWeight": 600,
      "borderRadius": "8px",
      "minHeight": "48px",
      "transition": "all 0.3s ease"
    },
    "variants": {
      "primary": {
        "background": "#1e3a8a",
        "color": "#ffffff",
        "hover": {
          "background": "#1e40af",
          "transform": "translateY(-2px)",
          "boxShadow": "0 4px 12px rgba(30, 58, 138, 0.3)"
        }
      },
      "secondary": {
        "background": "transparent",
        "color": "#1e3a8a",
        "border": "2px solid #1e3a8a",
        "hover": {
          "background": "#1e3a8a",
          "color": "#ffffff"
        }
      },
      "ghost": {
        "background": "transparent",
        "color": "#4b5563",
        "hover": {
          "background": "#f3f4f6"
        }
      }
    },
    "sizes": {
      "small": { "padding": "10px 20px", "fontSize": "0.875rem", "minHeight": "40px" },
      "medium": { "padding": "14px 28px", "fontSize": "1rem", "minHeight": "48px" },
      "large": { "padding": "18px 36px", "fontSize": "1.125rem", "minHeight": "56px" }
    }
  }
}
```

### Input Fields
```json
{
  "input": {
    "base": {
      "padding": "12px 16px",
      "fontSize": "1rem",
      "borderRadius": "8px",
      "border": "1px solid #d1d5db",
      "minHeight": "48px",
      "transition": "all 0.2s ease"
    },
    "states": {
      "focus": {
        "borderColor": "#1e3a8a",
        "boxShadow": "0 0 0 3px rgba(30, 58, 138, 0.1)"
      },
      "error": {
        "borderColor": "#ef4444",
        "boxShadow": "0 0 0 3px rgba(239, 68, 68, 0.1)"
      },
      "disabled": {
        "background": "#f3f4f6",
        "cursor": "not-allowed",
        "opacity": 0.6
      }
    }
  }
}
```

### Cards
```json
{
  "card": {
    "base": {
      "background": "#ffffff",
      "borderRadius": "12px",
      "padding": "30px",
      "boxShadow": "0 4px 6px rgba(0, 0, 0, 0.07)",
      "transition": "all 0.3s ease"
    },
    "hover": {
      "transform": "translateY(-5px)",
      "boxShadow": "0 12px 24px rgba(0, 0, 0, 0.12)"
    },
    "variants": {
      "elevated": {
        "boxShadow": "0 10px 25px rgba(0, 0, 0, 0.1)"
      },
      "outlined": {
        "border": "1px solid #e5e7eb",
        "boxShadow": "none"
      },
      "filled": {
        "background": "#f9fafb"
      }
    }
  }
}
```

### Containers
```json
{
  "container": {
    "maxWidth": {
      "sm": "640px",
      "md": "768px",
      "lg": "1024px",
      "xl": "1280px",
      "2xl": "1536px",
      "default": "1200px"
    },
    "padding": {
      "mobile": "16px",
      "tablet": "24px",
      "desktop": "32px"
    }
  }
}
```

## 5. Layout System

### Grid System
```json
{
  "grid": {
    "columns": 12,
    "gap": {
      "small": "16px",
      "medium": "24px",
      "large": "32px",
      "default": "30px"
    },
    "breakpoints": {
      "sm": "640px",
      "md": "768px",
      "lg": "1024px",
      "xl": "1280px",
      "2xl": "1536px"
    }
  }
}
```

### Section Spacing
```json
{
  "sections": {
    "padding": {
      "mobile": "60px 0",
      "tablet": "80px 0",
      "desktop": "100px 0"
    }
  }
}
```

## 6. Animation & Transitions

```json
{
  "transitions": {
    "fast": "150ms ease",
    "base": "300ms ease",
    "slow": "500ms ease",
    "verySlow": "700ms ease"
  },
  "animations": {
    "fadeIn": "fadeIn 0.6s ease forwards",
    "slideUp": "slideUp 0.5s ease forwards",
    "pulse": "pulse 2s infinite"
  }
}
```

## 7. Shadows

```json
{
  "shadows": {
    "xs": "0 1px 2px rgba(0, 0, 0, 0.05)",
    "sm": "0 2px 4px rgba(0, 0, 0, 0.06)",
    "md": "0 4px 6px rgba(0, 0, 0, 0.07)",
    "lg": "0 10px 15px rgba(0, 0, 0, 0.1)",
    "xl": "0 20px 25px rgba(0, 0, 0, 0.1)",
    "2xl": "0 25px 50px rgba(0, 0, 0, 0.15)",
    "inner": "inset 0 2px 4px rgba(0, 0, 0, 0.06)"
  }
}
```

## 8. Border Radius

```json
{
  "borderRadius": {
    "none": "0",
    "sm": "4px",
    "md": "6px",
    "lg": "8px",
    "xl": "12px",
    "2xl": "16px",
    "full": "9999px"
  }
}
```

## 9. Z-Index Scale

```json
{
  "zIndex": {
    "dropdown": 1000,
    "sticky": 1020,
    "fixed": 1030,
    "modalBackdrop": 1040,
    "modal": 1050,
    "popover": 1060,
    "tooltip": 1070
  }
}
```

## 10. Responsive Design Rules

### Breakpoint Strategy
- Mobile First: Start with mobile styles, add complexity for larger screens
- Content-driven breakpoints: Add breakpoints when content needs it
- No absolute positioning: Use flexbox and grid for layouts
- Fluid typography: Use clamp() for smooth scaling

### Component Behavior
```json
{
  "responsive": {
    "navigation": {
      "mobile": "hamburger menu",
      "tablet": "horizontal menu",
      "desktop": "horizontal menu with dropdowns"
    },
    "grid": {
      "mobile": "1 column",
      "tablet": "2 columns",
      "desktop": "3-4 columns"
    },
    "spacing": {
      "mobile": "reduced by 25%",
      "tablet": "standard",
      "desktop": "standard or increased"
    }
  }
}
```

## Implementation Guidelines

1. **Never use absolute positioning** unless absolutely necessary (modals, tooltips)
2. **Always use rem units** for typography and spacing
3. **Use CSS custom properties** for all design tokens
4. **Ensure 4.5:1 contrast ratio** for normal text, 3:1 for large text
5. **Test all interactive elements** at 48px minimum touch target
6. **Use semantic HTML** before adding ARIA attributes
7. **Implement focus-visible styles** for keyboard navigation
8. **Test responsive design** at all major breakpoints
9. **Use CSS Grid for layouts**, Flexbox for components
10. **Maintain 8-point grid** for consistent spacing