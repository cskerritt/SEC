# Google Analytics 4 Setup Instructions

## Overview
Your website has been prepared with Google Analytics 4 (GA4) tracking code. The placeholder `GA_MEASUREMENT_ID` needs to be replaced with your actual Google Analytics measurement ID to begin tracking.

## Files Updated
The following files have been updated with Google Analytics tracking code and placeholders:

### 1. Main Homepage
- **File**: `/index.html`
- **Status**: Updated with GA4 code and detailed comments
- **Features**: Page views, phone clicks, email clicks, form submissions

### 2. Contact Page
- **File**: `/contact/index.html`
- **Status**: Updated with GA4 code and tracking functions
- **Features**: Page views, phone clicks, email clicks, form submissions

### 3. Jekyll Template (City Pages)
- **File**: `/_includes/head.html`
- **Status**: Updated with GA4 code for all Jekyll-generated pages
- **Features**: Page views, phone clicks, email clicks, form submissions
- **Note**: This will automatically include analytics on all city pages when Jekyll builds the site

## How to Get Your Google Analytics Measurement ID

### Step 1: Create Google Analytics Account
1. Go to [https://analytics.google.com/](https://analytics.google.com/)
2. Sign in with your Google account
3. Click "Start measuring" if you don't have an account

### Step 2: Create a Property
1. Click "Admin" (gear icon) in the bottom left
2. Under "Property" column, click "Create Property"
3. Enter property details:
   - Property name: "Skerritt Economics & Consulting"
   - Reporting time zone: Select your timezone (likely "United States/Eastern")
   - Currency: USD

### Step 3: Set Up Data Stream
1. Select "Web" as your platform
2. Enter your website details:
   - Website URL: `https://skerritteconomics.com`
   - Stream name: "Skerritt Economics Website"
3. Click "Create stream"

### Step 4: Get Your Measurement ID
1. After creating the stream, you'll see your **Measurement ID**
2. It will be in the format `G-XXXXXXXXXX` (starts with "G-")
3. Copy this ID

## Implementation Steps

### Step 1: Replace Placeholder in Files
Replace `GA_MEASUREMENT_ID` with your actual measurement ID in these files:

1. **index.html** (lines 76 and 81)
2. **contact/index.html** (lines 546 and 551)
3. **_includes/head.html** (lines 19 and 24)

### Step 2: Find and Replace
Use find and replace across all files:
- **Find**: `GA_MEASUREMENT_ID`
- **Replace**: Your actual measurement ID (e.g., `G-ABC123DEF4`)

### Step 3: Verify Installation
1. After updating the files, visit your website
2. In Google Analytics, go to "Reports" > "Realtime"
3. Navigate around your site - you should see activity in real-time

## Tracking Features Implemented

### 1. Page Views
- Automatically tracks all page visits
- Tracks unique visitors and sessions

### 2. Phone Number Clicks
- Tracks when visitors click phone numbers
- Event category: "engagement"
- Event label: "phone_number_click"

### 3. Email Clicks
- Tracks when visitors click email addresses
- Event category: "engagement"
- Event label: "email_address_click"

### 4. Form Submissions
- Tracks consultation form submissions
- Event category: "conversion"
- Custom parameter: "consultation_requests"

## Additional Tool Pages
The following tool pages have placeholder analytics code that may need updating:
- `/tools/business-valuation/index.html`
- `/tools/household-services/index.html`
- `/tools/life-expectancy/index.html`
- `/tools/medical-cost/index.html`
- `/tools/present-value/index.html`
- `/tools/wage-growth/index.html`

These pages currently have console.log statements for lead tracking but no GA4 implementation.

## Next Steps After Setup

### 1. Verify Tracking
- Check Google Analytics "Realtime" reports
- Test phone number and email clicks
- Submit test forms to verify conversion tracking

### 2. Set Up Goals
1. In Google Analytics, go to "Admin" > "Conversions"
2. Create conversion events for:
   - Phone calls (`phone_call`)
   - Email clicks (`email_click`)
   - Form submissions (`form_submission`)

### 3. Enhanced Ecommerce (Optional)
Consider setting up enhanced ecommerce tracking for consultation bookings and service inquiries.

### 4. Google Search Console Connection
1. Go to "Admin" > "Property Settings"
2. Click "Search Console links"
3. Link your Google Search Console property

## Troubleshooting

### If tracking isn't working:
1. Check browser console for JavaScript errors
2. Verify the measurement ID is correct
3. Ensure gtag.js script is loading (check Network tab in DevTools)
4. Make sure ad blockers aren't blocking Google Analytics

### Common Issues:
- **Measurement ID format**: Must start with "G-" followed by 10 characters
- **Script loading**: Ensure the gtag script loads before any tracking calls
- **HTTPS required**: Google Analytics requires HTTPS (your site already uses HTTPS)

## Support
If you need assistance with setup, refer to the [Google Analytics Help Center](https://support.google.com/analytics/) or contact a web developer familiar with GA4 implementation.