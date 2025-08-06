#!/bin/bash

# Batch Migration Script for City Pages
# This script migrates city pages to the new UI library in manageable batches

echo "=================================="
echo "City Pages UI Library Migration"
echo "=================================="

# Configuration
BATCH_SIZE=50
DRY_RUN=false
CITY_DIR="locations/cities"
LOG_FILE="migration-log.txt"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --batch-size)
            BATCH_SIZE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Count total city pages
TOTAL_FILES=$(find "$CITY_DIR" -name "*.html" -type f | wc -l | tr -d ' ')
echo "Total city pages found: $TOTAL_FILES"
echo ""

# Create batches by state
echo "Creating migration batches by state..."
echo ""

# States array
STATES=("al" "ak" "az" "ar" "ca" "co" "ct" "de" "fl" "ga" "hi" "id" "il" "in" "ia" "ks" "ky" "la" "me" "md" "ma" "mi" "mn" "ms" "mo" "mt" "ne" "nv" "nh" "nj" "nm" "ny" "nc" "nd" "oh" "ok" "or" "pa" "ri" "sc" "sd" "tn" "tx" "ut" "vt" "va" "wa" "wv" "wi" "wy")

# Process each state
for STATE in "${STATES[@]}"; do
    # Count files for this state
    STATE_FILES=$(find "$CITY_DIR" -name "*-${STATE}-*.html" -type f | wc -l | tr -d ' ')
    
    if [ "$STATE_FILES" -gt 0 ]; then
        echo "State: ${STATE^^} - $STATE_FILES files"
        
        # Process in batches
        BATCH_NUM=0
        find "$CITY_DIR" -name "*-${STATE}-*.html" -type f | while read -r FILE; do
            if [ $((BATCH_NUM % BATCH_SIZE)) -eq 0 ]; then
                echo "  Processing batch $((BATCH_NUM / BATCH_SIZE + 1))..."
            fi
            
            # Run migration
            if [ "$DRY_RUN" = true ]; then
                python3 migrate-ui-simple.py "$FILE" --dry-run >> "$LOG_FILE" 2>&1
            else
                python3 migrate-ui-simple.py "$FILE" >> "$LOG_FILE" 2>&1
            fi
            
            ((BATCH_NUM++))
            
            # Add a small delay every batch to prevent overwhelming the system
            if [ $((BATCH_NUM % BATCH_SIZE)) -eq 0 ]; then
                echo "  Completed batch $((BATCH_NUM / BATCH_SIZE)). Pausing..."
                sleep 1
            fi
        done
        
        echo "  ✓ Completed ${STATE^^}"
        echo ""
    fi
done

# Process service-specific pages
echo "Processing service-specific city pages..."

# Service types
SERVICES=("forensic-economist" "life-care-planner" "vocational-expert" "business-valuation-analyst")

for SERVICE in "${SERVICES[@]}"; do
    SERVICE_FILES=$(find "$CITY_DIR" -name "*-${SERVICE}.html" -type f | wc -l | tr -d ' ')
    
    if [ "$SERVICE_FILES" -gt 0 ]; then
        echo "Service: $SERVICE - $SERVICE_FILES files"
        
        # Process all files for this service
        if [ "$DRY_RUN" = true ]; then
            python3 migrate-ui-simple.py "$CITY_DIR" --pattern "*-${SERVICE}.html" --dry-run
        else
            python3 migrate-ui-simple.py "$CITY_DIR" --pattern "*-${SERVICE}.html"
        fi
        
        echo "  ✓ Completed $SERVICE"
        echo ""
    fi
done

echo "=================================="
echo "Migration Complete!"
echo "=================================="
echo "Check $LOG_FILE for detailed results"

# Generate summary
echo ""
echo "Generating summary report..."

if [ "$DRY_RUN" = true ]; then
    echo "This was a DRY RUN - no files were modified"
    echo "Run without --dry-run to apply changes"
else
    # Count migrated files
    MIGRATED=$(grep -c "✓ Migrated successfully" "$LOG_FILE")
    SKIPPED=$(grep -c "→ Already migrated" "$LOG_FILE")
    ERRORS=$(grep -c "✗ Error:" "$LOG_FILE")
    
    echo "Files migrated: $MIGRATED"
    echo "Files skipped (already migrated): $SKIPPED"
    echo "Errors: $ERRORS"
fi