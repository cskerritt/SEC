# Complete WordPress Setup Guide for Skerritt Economics & Consulting

## Quick Start (Automated Setup)

### Step 1: Run the Setup Script
```bash
./setup-wordpress.sh
```

This script will:
- Download WordPress core files
- Extract and organize files
- Set up directory structure
- Create wp-config.php template

### Step 2: Database Setup
```sql
mysql -u root -p
CREATE DATABASE skerritt_wp;
CREATE USER 'skerritt_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON skerritt_wp.* TO 'skerritt_user'@'localhost';
FLUSH PRIVILEGES;
exit;
```

### Step 3: Configure WordPress
Edit `wp-config.php` and update:
```php
define( 'DB_NAME', 'skerritt_wp' );
define( 'DB_USER', 'skerritt_user' );
define( 'DB_PASSWORD', 'your_secure_password' );
define( 'DB_HOST', 'localhost' );
```

Generate security keys from: https://api.wordpress.org/secret-key/1.1/salt/
Replace the placeholder keys in wp-config.php

### Step 4: Run WordPress Installation
1. Visit your site URL in a web browser
2. Follow the WordPress installation wizard:
   - Site Title: Skerritt Economics & Consulting
   - Username: (your admin username)
   - Password: (strong password)
   - Email: chris@skerritteconomics.com

### Step 5: Activate Theme
1. Log into WordPress admin (yoursite.com/wp-admin)
2. Go to Appearance > Themes
3. Activate "Skerritt Economics & Consulting"

### Step 6: Import Content
```bash
mysql -u skerritt_user -p skerritt_wp < wordpress-content-import.sql
```

### Step 7: Configure Menus
1. Go to Appearance > Menus
2. Create these menus:

**Primary Menu:**
- Home
- About
- Services
- Practice Areas
- Resources
- Contact

**Footer Services Menu:**
- Forensic Economics
- Business Valuation
- Life Care Planning
- Vocational Expert Services

**Footer Practice Areas Menu:**
- Personal Injury
- Medical Malpractice
- Employment Litigation
- Commercial Disputes
- Wrongful Death

**Footer Resources Menu:**
- Case Studies
- About
- Contact
- Sitemap

### Step 8: Install Essential Plugins

1. **Contact Form 7** (for contact forms)
   - Create a form with fields: Name, Email, Phone, Case Type, Message
   - Add the shortcode to the Contact page

2. **Yoast SEO** (for search engine optimization)
   - Import settings from existing meta descriptions

3. **UpdraftPlus** (for backups)
   - Configure automated backups

4. **Wordfence** (for security)
   - Enable firewall and security scanning

## Manual Setup (Alternative)

If you prefer manual setup:

1. Download WordPress from https://wordpress.org/download/
2. Upload files to your server
3. Copy the theme folder: `wp-content/themes/skerritt-economics/`
4. Follow steps 2-8 above

## Post-Installation Tasks

### 1. Update Permalinks
- Go to Settings > Permalinks
- Select "Post name" structure
- Save changes

### 2. Configure Homepage
- Go to Settings > Reading
- Set "Your homepage displays" to "A static page"
- Homepage: Home
- Posts page: (leave blank or create a News page)

### 3. Update Site Settings
- Go to Settings > General
- Site Title: Skerritt Economics & Consulting
- Tagline: Expert Forensic Economics & Business Valuation Services
- WordPress Address (URL): https://skerritteconomics.com
- Site Address (URL): https://skerritteconomics.com

### 4. Theme Customization
- Go to Appearance > Customize
- Upload logo: sec-logo.png
- Adjust colors if needed

### 5. City Pages Migration
For the numerous city-specific pages:
1. Create a custom post type for "Locations"
2. Use a bulk import plugin like "WP All Import"
3. Or create a custom import script

## Testing Checklist

- [ ] Homepage displays correctly
- [ ] Navigation menus work
- [ ] Contact form submits properly
- [ ] All service pages load
- [ ] Practice area pages display
- [ ] Mobile responsive design works
- [ ] Page load speed is acceptable

## Maintenance

### Regular Tasks
- Update WordPress core, themes, and plugins monthly
- Run backups before any updates
- Monitor security logs
- Review and optimize database periodically

### Performance Optimization
- Install a caching plugin (W3 Total Cache or WP Rocket)
- Use a CDN for static assets
- Optimize images with an image optimization plugin

## Troubleshooting

### Common Issues

**White Screen of Death**
- Check PHP error logs
- Increase PHP memory limit in wp-config.php:
  ```php
  define('WP_MEMORY_LIMIT', '256M');
  ```

**404 Errors on Pages**
- Go to Settings > Permalinks
- Click "Save Changes" to refresh rewrite rules

**Theme Not Displaying Correctly**
- Clear browser cache
- Check that all theme files uploaded correctly
- Verify CSS/JS files are loading

## Support Resources

- WordPress Codex: https://codex.wordpress.org/
- Theme documentation: See WORDPRESS_SETUP.md
- Plugin documentation: Check each plugin's website

## Migration from Jekyll

The site has been converted from Jekyll to WordPress while preserving:
- All existing URLs (with redirects if needed)
- Design and layout
- SEO meta data
- Content structure
- Performance optimizations

For questions specific to this migration, refer to the theme's functions.php file for custom implementations.