# UI Library Rollback Guide

## Overview

This guide provides procedures for safely rolling back the UI library migration if issues arise. All migrated files have automatic backups with `.pre-ui-backup` extension.

## Quick Rollback Commands

### 1. Rollback Everything
```bash
# Preview what will be rolled back
./rollback-procedures.sh --dry-run

# Perform full rollback
./rollback-procedures.sh
```

### 2. Rollback Specific Directory
```bash
# Rollback service pages only
./rollback-procedures.sh services/

# Rollback city pages only
./rollback-procedures.sh locations/cities/
```

### 3. Rollback Single File
```bash
# Rollback specific file
./rollback-procedures.sh services/forensic-economics/index.html
```

## Manual Rollback Procedures

### Method 1: Using Backup Files
```bash
# Find all backup files
find . -name "*.pre-ui-backup"

# Restore single file
cp page.html.pre-ui-backup page.html

# Restore multiple files
for backup in *.pre-ui-backup; do
    cp "$backup" "${backup%.pre-ui-backup}"
done
```

### Method 2: Using Git
```bash
# View migration commits
git log --oneline --grep="UI"

# Revert last commit
git revert HEAD

# Revert specific commit
git revert <commit-hash>

# Hard reset (CAUTION: loses all uncommitted changes)
git reset --hard HEAD~1
```

### Method 3: Selective Rollback
```bash
# Rollback only failed pages
python3 test-ui-components.py . > test-results.txt
grep "Failed" test-results.txt | awk '{print $2}' | while read file; do
    if [ -f "${file}.pre-ui-backup" ]; then
        cp "${file}.pre-ui-backup" "$file"
    fi
done
```

## Rollback Scenarios

### Scenario 1: Performance Issues
**Problem:** Pages loading slowly after migration

**Solution:**
```bash
# 1. Identify slow pages
python3 monitor-performance.py . > performance.txt

# 2. Rollback pages with score < 50
grep "Score: [0-4][0-9]" performance.txt | while read line; do
    # Extract filename and rollback
done

# 3. Re-migrate with optimization
python3 migrate-ui-simple.py --optimize <file>
```

### Scenario 2: Visual Breaking
**Problem:** Layout broken on certain pages

**Solution:**
```bash
# 1. Test specific page type
python3 test-ui-components.py locations/cities/*-ga-*.html

# 2. Rollback affected pages
./rollback-procedures.sh locations/cities/ --pattern "*-ga-*.html"

# 3. Debug and fix migration script
# Then re-migrate
```

### Scenario 3: JavaScript Errors
**Problem:** Interactive features not working

**Solution:**
```bash
# 1. Rollback to identify issue
./rollback-procedures.sh --dry-run

# 2. Check browser console for errors
# Common: Bootstrap/Alpine.js conflicts

# 3. Fix in migration script and re-run
```

## Partial Rollback Strategy

### 1. Keep Good Migrations
```bash
# Test all pages
python3 test-ui-components.py . > results.json

# Extract passed pages
python3 -c "
import json
with open('results.json') as f:
    data = json.load(f)
    for page in data['passed']:
        print(f'rm {page}.pre-ui-backup')
" | bash
```

### 2. Rollback Only Failures
```bash
# Create failure list
python3 test-ui-components.py . | grep "Failed" > failed.txt

# Rollback failures only
while read line; do
    file=$(echo $line | awk '{print $2}')
    ./rollback-procedures.sh "$file"
done < failed.txt
```

## Recovery Procedures

### If Rollback Fails

1. **Check for migrated backups:**
   ```bash
   ls *.migrated-*
   ```

2. **Use Git history:**
   ```bash
   git checkout HEAD~1 -- path/to/file.html
   ```

3. **Download from production:**
   ```bash
   curl https://skerritteconomics.com/path/to/page.html > page.html
   ```

### Clean Up After Rollback

```bash
# Remove backup files after confirming rollback success
find . -name "*.pre-ui-backup" -mtime +7 -delete

# Remove migrated versions
find . -name "*.migrated-*" -mtime +7 -delete

# Update git
git add .
git commit -m "Rollback UI migration for affected pages"
```

## Prevention for Future

### Before Migration
1. **Always backup:**
   ```bash
   tar -czf backup-$(date +%Y%m%d).tar.gz *.html
   ```

2. **Test small batch first:**
   ```bash
   python3 migrate-ui-simple.py test-page.html
   python3 test-ui-components.py test-page.html
   ```

3. **Monitor performance:**
   ```bash
   python3 monitor-performance.py test-page.html
   ```

### During Migration
1. **Migrate in stages**
2. **Test after each batch**
3. **Keep detailed logs**

### After Migration
1. **Run full test suite**
2. **Check performance metrics**
3. **User acceptance testing**

## Emergency Contacts

If critical issues arise:

1. **Check documentation:**
   - `/TROUBLESHOOTING-GUIDE.md`
   - `/UI-LIBRARY-GUIDE.md`

2. **Review logs:**
   - `rollback-log-*.txt`
   - `ui-migration-report.json`
   - `performance-report.json`

3. **Quick fixes:**
   ```bash
   # Disable Bootstrap temporarily
   find . -name "*.html" -exec sed -i 's/bootstrap@5.3.2/bootstrap@5.3.2.disabled/g' {} \;
   
   # Remove UI library includes
   find . -name "*.html" -exec sed -i '/ui-library-setup.html/d' {} \;
   ```

Remember: Always test rollback procedures on a few files before running on entire site!