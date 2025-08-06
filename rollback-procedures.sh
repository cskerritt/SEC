#!/bin/bash

# UI Library Migration Rollback Script
# Safely reverts pages to pre-migration state

set -e

echo "=================================="
echo "UI Library Migration Rollback"
echo "=================================="
echo ""

# Configuration
BACKUP_EXTENSION=".pre-ui-backup"
LOG_FILE="rollback-log-$(date +%Y%m%d-%H%M%S).txt"
DRY_RUN=false

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            echo -e "${YELLOW}DRY RUN MODE - No files will be modified${NC}"
            shift
            ;;
        --help)
            echo "Usage: $0 [OPTIONS] [PATH]"
            echo ""
            echo "Options:"
            echo "  --dry-run    Preview rollback without making changes"
            echo "  --force      Skip confirmation prompts"
            echo "  --pattern    File pattern to match (default: *.html)"
            echo ""
            echo "Examples:"
            echo "  $0                    # Rollback all files in current directory"
            echo "  $0 services/          # Rollback all files in services directory"
            echo "  $0 --dry-run          # Preview what would be rolled back"
            echo "  $0 file.html          # Rollback specific file"
            exit 0
            ;;
        --force)
            FORCE=true
            shift
            ;;
        --pattern)
            PATTERN="$2"
            shift 2
            ;;
        *)
            TARGET_PATH="$1"
            shift
            ;;
    esac
done

# Set defaults
TARGET_PATH=${TARGET_PATH:-.}
PATTERN=${PATTERN:-"*.html"}

# Function to log messages
log_message() {
    echo "$1" | tee -a "$LOG_FILE"
}

# Function to find backup files
find_backup_files() {
    if [ -f "$TARGET_PATH" ]; then
        # Single file
        if [ -f "${TARGET_PATH}${BACKUP_EXTENSION}" ]; then
            echo "${TARGET_PATH}${BACKUP_EXTENSION}"
        fi
    else
        # Directory
        find "$TARGET_PATH" -name "*${BACKUP_EXTENSION}" -type f 2>/dev/null | sort
    fi
}

# Function to rollback a single file
rollback_file() {
    local backup_file="$1"
    local original_file="${backup_file%$BACKUP_EXTENSION}"
    
    if [ "$DRY_RUN" = true ]; then
        echo -e "${YELLOW}[DRY RUN]${NC} Would rollback: $original_file"
        return 0
    fi
    
    # Check if original file exists
    if [ ! -f "$original_file" ]; then
        log_message "${RED}Error: Original file not found: $original_file${NC}"
        return 1
    fi
    
    # Create a safety backup of current migrated version
    cp "$original_file" "${original_file}.migrated-$(date +%Y%m%d-%H%M%S)"
    
    # Restore from backup
    cp "$backup_file" "$original_file"
    
    # Remove the backup file after successful restore
    rm "$backup_file"
    
    log_message "${GREEN}✓ Rolled back: $original_file${NC}"
    return 0
}

# Function to show rollback summary
show_summary() {
    local backup_files=("$@")
    local total=${#backup_files[@]}
    
    echo ""
    echo "Rollback Summary:"
    echo "=================="
    echo "Total backup files found: $total"
    
    if [ $total -eq 0 ]; then
        echo -e "${YELLOW}No backup files found. Nothing to rollback.${NC}"
        exit 0
    fi
    
    # Show sample of files
    echo ""
    echo "Files to be rolled back:"
    for file in "${backup_files[@]:0:10}"; do
        echo "  - ${file%$BACKUP_EXTENSION}"
    done
    
    if [ $total -gt 10 ]; then
        echo "  ... and $((total - 10)) more files"
    fi
    
    echo ""
}

# Function to confirm rollback
confirm_rollback() {
    if [ "$FORCE" = true ]; then
        return 0
    fi
    
    echo -e "${YELLOW}Warning: This will restore files to their pre-migration state.${NC}"
    echo "Current migrated versions will be backed up with .migrated-* extension."
    echo ""
    read -p "Do you want to continue? (yes/no): " -n 1 -r
    echo ""
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Rollback cancelled."
        exit 1
    fi
}

# Main execution
log_message "Starting rollback process at $(date)"
log_message "Target path: $TARGET_PATH"
log_message "Pattern: $PATTERN"

# Find all backup files
echo "Searching for backup files..."
backup_files=($(find_backup_files))

# Show summary
show_summary "${backup_files[@]}"

# Confirm before proceeding
if [ ${#backup_files[@]} -gt 0 ]; then
    confirm_rollback
fi

# Process rollbacks
success_count=0
error_count=0

for backup_file in "${backup_files[@]}"; do
    if rollback_file "$backup_file"; then
        ((success_count++))
    else
        ((error_count++))
    fi
done

# Final report
echo ""
echo "=================================="
echo "Rollback Complete"
echo "=================================="
log_message "Successfully rolled back: $success_count files"
log_message "Errors: $error_count files"

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a dry run - no files were modified${NC}"
fi

echo ""
echo "Log file: $LOG_FILE"

# Create a rollback summary file
if [ "$DRY_RUN" = false ] && [ $success_count -gt 0 ]; then
    cat > "rollback-summary-$(date +%Y%m%d-%H%M%S).json" << EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "target_path": "$TARGET_PATH",
  "files_rolled_back": $success_count,
  "errors": $error_count,
  "log_file": "$LOG_FILE"
}
EOF
    echo "Summary file created: rollback-summary-$(date +%Y%m%d-%H%M%S).json"
fi

# Exit with appropriate code
if [ $error_count -gt 0 ]; then
    exit 1
else
    exit 0
fi