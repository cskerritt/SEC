# WordPress Setup Instructions

## Overview
This branch contains the WordPress conversion of the Skerritt Economics & Consulting website. The custom theme preserves the existing design while adding WordPress content management capabilities.

## Installation Steps

1. **Download WordPress**
   - Download the latest WordPress from https://wordpress.org/download/
   - Extract WordPress files to your server root directory

2. **Move Theme Files**
   - Copy the `wp-content/themes/skerritt-economics` folder to your WordPress installation's `wp-content/themes/` directory

3. **Database Setup**
   - Create a MySQL database for WordPress
   - Create a database user with all privileges on the database

4. **Configure WordPress**
   - Copy `wp-config-sample.php` to `wp-config.php`
   - Update database credentials in `wp-config.php`
   - Generate security keys from https://api.wordpress.org/secret-key/1.1/salt/
   - Replace the placeholder keys in `wp-config.php`

5. **Run WordPress Installation**
   - Visit your site URL in a browser
   - Follow the WordPress installation wizard
   - Create an admin account

6. **Activate Theme**
   - Log into WordPress admin
   - Go to Appearance > Themes
   - Activate "Skerritt Economics & Consulting" theme

7. **Configure Menus**
   - Go to Appearance > Menus
   - Create menus for:
     - Primary Menu
     - Footer Services Menu
     - Footer Practice Areas Menu
     - Footer Resources Menu

8. **Import Content**
   - Create pages for: About, Contact, Services, Practice Areas, Resources, etc.
   - Create Service posts for each service offering
   - Create Practice Area posts for each practice area

## Theme Features

- Custom post types for Services and Practice Areas
- Responsive design preserved from original site
- SEO-friendly structure
- Performance optimized with minified assets
- Accessibility features maintained

## Required Plugins (Recommended)

- Yoast SEO or Rank Math for SEO management
- Contact Form 7 or WPForms for contact forms
- UpdraftPlus for backups
- Wordfence for security

## Content Migration

The existing static content needs to be manually migrated to WordPress:

1. **Pages to Create:**
   - Home (use front-page.php template)
   - About
   - Services (archive page)
   - Practice Areas (archive page)
   - Contact
   - Resources
   - Privacy Policy
   - Terms of Service

2. **Service Posts:**
   - Forensic Economics
   - Business Valuation
   - Life Care Planning
   - Vocational Expert

3. **Practice Area Posts:**
   - Personal Injury
   - Medical Malpractice
   - Employment Litigation
   - Commercial Disputes
   - Wrongful Death

## Customization

- Site identity: Add logo via Customizer
- Colors and fonts: Edit `style.css` in theme
- Homepage content: Use Customizer or edit `front-page.php`

## Notes

- The theme maintains all existing CSS and JavaScript
- City-specific pages will need custom page templates or a location CPT
- Blog functionality is built-in but needs content
- Form submissions require a form plugin installation