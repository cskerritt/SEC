# Page Review System Guide

## Overview

This comprehensive page review system allows you to:
- View all 3,821 pages in your Jekyll site
- Paginate through pages (10, 25, 50, or 100 at a time)
- Approve or decline individual pages
- Add notes for editing on each page
- Take screenshots of pages
- Export review data as JSON or CSV
- Filter by status, page type, and search terms

## Setup Instructions

### 1. Install Dependencies (for screenshots)

```bash
# Install Playwright for screenshot functionality
npm install --save playwright

# Or use the provided package file
npm install --package-lock-only --package=package-screenshot.json
```

### 2. Start Jekyll Server

```bash
# Make sure Jekyll is running on port 4001
bundle exec jekyll serve --port 4001
```

### 3. Open the Review System

```bash
# Open the review interface in your browser
open page-review-system.html

# Or navigate to:
file:///Users/chrisskerritt/SEC/page-review-system.html
```

## Using the Review System

### Main Features

1. **Page List View**
   - Shows page title, path, type, and status
   - Each page has approve/decline buttons
   - Notes field for editing instructions
   - Screenshot button for visual capture

2. **Filtering Options**
   - Search by page path or title
   - Filter by status: Pending, Approved, Declined
   - Filter by type: Services, Locations, Blog, Practice Areas, Other
   - Adjust items per page: 10, 25, 50, or 100

3. **Bulk Actions**
   - Select multiple pages using checkboxes
   - Bulk approve selected pages
   - Bulk decline selected pages
   - Bulk screenshot selected pages

4. **Page Preview**
   - Click any page title to preview in modal
   - Full page preview with scrolling
   - Close with X button or Escape key

### Workflow Example

1. **Review Pages by Type**
   - Use filters to show only "Services" pages
   - Review each page and add notes
   - Approve pages that are ready
   - Decline pages that need work

2. **Export Review Data**
   - Click "Export Review Data (JSON)" to save all reviews
   - Click "Export to CSV" for spreadsheet format
   - Reviews are auto-saved to browser localStorage

3. **Take Screenshots**
   - Individual: Click 📸 button on any page
   - Bulk: Select multiple pages and click "Bulk Screenshot"
   - Screenshots are saved with timestamp

## Screenshot Tool Usage

### Running the Screenshot Script

```bash
# First, ensure all pages are listed
find _site -name "*.html" -type f | grep -v "node_modules" | sort > all-pages.txt

# Run the screenshot tool
node screenshot-pages.js
```

### Screenshot Output

The tool creates:
- `page-screenshots/` directory with all PNG files
- `page-screenshots/screenshot-report.json` with metadata
- `page-screenshots/gallery.html` for visual browsing

### Screenshot Gallery Features

- Grid view of all successful screenshots
- Click any screenshot to view full size
- Filter screenshots by path
- Shows page title and path for each screenshot

## Data Storage

### Local Storage
- All reviews are automatically saved to browser localStorage
- Data persists between sessions
- No server required

### Export Formats

1. **JSON Export**
   - Complete review data with all fields
   - Includes status, notes, timestamps
   - Can be re-imported later

2. **CSV Export**
   - Spreadsheet-compatible format
   - Includes: Path, Title, Type, Status, Notes, Last Reviewed, Screenshot
   - Perfect for reporting

### Example Review Data Structure

```json
{
  "about/index.html": {
    "status": "approved",
    "notes": "Page looks good, but add more team photos",
    "lastReviewed": "2024-01-15T10:30:00.000Z",
    "screenshot": {
      "url": "about/index.html",
      "timestamp": "2024-01-15T10:30:00.000Z",
      "filename": "screenshot-about-index-1705315800000.png"
    }
  }
}
```

## Page Statistics

The system tracks:
- Total pages: 3,821
- Approved pages
- Declined pages
- Pending review pages

## Keyboard Shortcuts

- `Escape` - Close preview modal
- `Ctrl/Cmd + F` - Use browser search within current page view

## Tips for Efficient Review

1. **Start with High-Priority Pages**
   - Filter by "Services" or "Practice Areas"
   - These are typically the most important pages

2. **Use Bulk Actions**
   - Select all similar pages that need the same treatment
   - Bulk approve pages that follow the same template

3. **Add Detailed Notes**
   - Include specific editing instructions
   - Reference design issues or content problems
   - Notes are searchable in exports

4. **Regular Exports**
   - Export data regularly as backup
   - Share CSV with team members
   - Track progress over time

## Troubleshooting

### Pages Not Loading?
- Ensure Jekyll server is running on port 4001
- Check browser console for errors
- Try refreshing the page

### Screenshots Not Working?
- Install Playwright: `npm install playwright`
- Ensure Jekyll server is accessible
- Check console for error messages

### Data Not Saving?
- Check browser localStorage limits
- Try exporting and clearing old data
- Ensure browser allows localStorage

## Next Steps

After reviewing all pages:
1. Export final review data
2. Use declined pages list for editing priorities
3. Reference notes when making updates
4. Re-run review after changes