# UI Library Implementation Plan

## Executive Summary

This plan outlines the phased implementation of Bootstrap 5, Alpine.js, and supporting UI libraries across the Skerritt Economics website. The implementation will ensure consistent, professional, and accessible UI across all 3,155+ pages while maintaining site performance.

## Phase 1: Foundation (Week 1)

### 1.1 Setup & Testing
- [x] Create UI library components
- [x] Compile Bootstrap custom theme  
- [x] Create demo page
- [x] Test on modern service page example
- [ ] Browser compatibility testing
- [ ] Performance benchmarking

### 1.2 Core Pages Migration
Start with high-impact pages:
1. **Homepage** (`index.md`)
2. **Service Pages** (4 pages)
   - `/services/forensic-economics/`
   - `/services/life-care-planning/`
   - `/services/vocational-expert/`
   - `/services/business-valuation/`
3. **Contact Page** (`/contact/`)
4. **About Page** (`/about/`)

**Migration Command:**
```bash
# Migrate service pages
python3 migrate-ui-simple.py services/ --dry-run
python3 migrate-ui-simple.py services/

# Migrate individual pages
python3 migrate-ui-simple.py index.md
python3 migrate-ui-simple.py contact.md
python3 migrate-ui-simple.py about.md
```

## Phase 2: Practice Areas & Locations (Week 2)

### 2.1 Practice Area Pages
- `/practice-areas/personal-injury/`
- `/practice-areas/medical-malpractice/`
- `/practice-areas/employment/`
- `/practice-areas/commercial-disputes/`

### 2.2 State Location Pages
- `/locations/rhode-island/`
- `/locations/massachusetts/`
- `/locations/connecticut/`
- `/locations/new-hampshire/`
- `/locations/maine/`
- `/locations/vermont/`

**Migration Command:**
```bash
python3 migrate-ui-simple.py practice-areas/
python3 migrate-ui-simple.py locations/ --pattern "*.html"
```

## Phase 3: City Pages - By State (Weeks 3-4)

### 3.1 Priority States (Most Pages)
1. **California** (~300 pages)
2. **Texas** (~250 pages)
3. **Florida** (~200 pages)
4. **New York** (~180 pages)

**Migration Command:**
```bash
# Run in batches by state
./batch-migrate-city-pages.sh --batch-size 50

# Or migrate specific states
python3 migrate-ui-simple.py locations/cities/ --pattern "*-ca-*.html"
python3 migrate-ui-simple.py locations/cities/ --pattern "*-tx-*.html"
```

### 3.2 Remaining States
Process remaining states in alphabetical order, 2-3 states per day.

## Phase 4: Quality Assurance (Week 5)

### 4.1 Automated Testing
Create automated tests for:
- [ ] Bootstrap class presence
- [ ] Responsive breakpoints
- [ ] Accessibility compliance
- [ ] Performance metrics

### 4.2 Manual Review
- [ ] Visual regression testing
- [ ] Cross-browser testing
- [ ] Mobile device testing
- [ ] Screen reader testing

## Implementation Checklist

### Pre-Migration
- [x] Backup all files
- [x] Create git worktree
- [x] Document existing styles
- [x] Create migration scripts
- [ ] Test migration on sample files
- [ ] Create rollback plan

### During Migration
- [ ] Run migrations in batches
- [ ] Monitor for errors
- [ ] Test each batch
- [ ] Document issues
- [ ] Update progress tracking

### Post-Migration
- [ ] Run full site audit
- [ ] Performance testing
- [ ] SEO impact check
- [ ] Update documentation
- [ ] Train team on new components

## Monitoring & Metrics

### Key Performance Indicators
1. **Page Load Time**: Target < 3s
2. **Lighthouse Score**: Target > 90
3. **Accessibility Score**: Target > 95
4. **Mobile Usability**: 100% pass

### Tracking Tools
- Google PageSpeed Insights
- Lighthouse CI
- WebAIM WAVE
- BrowserStack

## Rollback Plan

If issues arise:

1. **Immediate Rollback**
   ```bash
   # Restore from backup
   find . -name "*.pre-ui-backup" -exec bash -c 'mv "$0" "${0%.pre-ui-backup}"' {} \;
   ```

2. **Selective Rollback**
   ```bash
   # Restore specific files
   cp locations/cities/atlanta-ga-forensic-economist.html.pre-ui-backup locations/cities/atlanta-ga-forensic-economist.html
   ```

3. **Git Rollback**
   ```bash
   # Revert to previous commit
   git revert HEAD
   ```

## Common Issues & Solutions

### Issue 1: JavaScript Conflicts
**Solution**: Ensure Alpine.js is loaded with `defer` attribute and after other scripts.

### Issue 2: CSS Specificity
**Solution**: Use Bootstrap utility classes with `!important` flag sparingly.

### Issue 3: Mobile Menu Issues
**Solution**: Check z-index values and ensure proper data attributes.

### Issue 4: Slow Page Load
**Solution**: Use CDN for libraries, minimize custom CSS, lazy load images.

## Success Criteria

The implementation is successful when:
- ✅ All pages use consistent UI components
- ✅ Mobile experience is improved
- ✅ Accessibility scores increase
- ✅ Page load times remain under 3s
- ✅ No broken functionality
- ✅ Positive user feedback

## Timeline Summary

| Week | Phase | Pages | Status |
|------|-------|-------|--------|
| 1 | Foundation | 10 | Ready |
| 2 | Practice/Locations | 20 | Pending |
| 3-4 | City Pages | 3,155 | Pending |
| 5 | QA & Launch | All | Pending |

## Next Steps

1. **Today**: Test migration on 5 sample city pages
2. **Tomorrow**: Migrate all service pages
3. **This Week**: Complete Phase 1
4. **Next Week**: Begin Phase 2

## Commands Reference

```bash
# Single file migration
python3 migrate-ui-simple.py path/to/file.html

# Directory migration
python3 migrate-ui-simple.py path/to/directory/

# Pattern-based migration
python3 migrate-ui-simple.py locations/cities/ --pattern "*-ca-*.html"

# Dry run (preview only)
python3 migrate-ui-simple.py path/to/files/ --dry-run

# Batch migration by state
./batch-migrate-city-pages.sh --batch-size 50 --dry-run

# Check migration status
grep -c "bootstrap@5.3.2" locations/cities/*.html

# Find unmigrated files
find locations/cities -name "*.html" -exec grep -L "bootstrap@5.3.2" {} \;
```

## Support Resources

- Bootstrap 5 Docs: https://getbootstrap.com/docs/5.3/
- Alpine.js Docs: https://alpinejs.dev/
- UI Library Guide: `/UI-LIBRARY-GUIDE.md`
- Demo Page: `/ui-library-demo.html`
- Component Examples: `/_includes/components/`

Remember: Consistency and quality over speed. Test thoroughly at each phase.