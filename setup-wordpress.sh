#!/bin/bash

# WordPress Setup Script for Skerritt Economics & Consulting
# This script helps automate the WordPress installation process

echo "WordPress Setup Script for Skerritt Economics & Consulting"
echo "=========================================================="

# Check if running on macOS or Linux
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Running on macOS"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Running on Linux"
else
    echo "This script is designed for macOS or Linux"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required commands
echo ""
echo "Checking requirements..."

if ! command_exists php; then
    echo "❌ PHP is not installed. Please install PHP 7.4 or higher."
    exit 1
else
    echo "✅ PHP is installed: $(php -v | head -n 1)"
fi

if ! command_exists mysql; then
    echo "❌ MySQL client is not installed. Please install MySQL."
    exit 1
else
    echo "✅ MySQL is installed"
fi

if ! command_exists curl; then
    echo "❌ curl is not installed. Please install curl."
    exit 1
else
    echo "✅ curl is installed"
fi

# Download WordPress
echo ""
echo "Downloading WordPress..."
if [ ! -f "wordpress.tar.gz" ]; then
    curl -O https://wordpress.org/latest.tar.gz
    mv latest.tar.gz wordpress.tar.gz
    echo "✅ WordPress downloaded"
else
    echo "✅ WordPress archive already exists"
fi

# Extract WordPress
echo ""
echo "Extracting WordPress..."
tar -xzf wordpress.tar.gz
echo "✅ WordPress extracted"

# Move WordPress files
echo ""
echo "Setting up WordPress files..."
cp -n wordpress/wp-*.php .
cp -n wordpress/index.php .
cp -n wordpress/license.txt .
cp -n wordpress/readme.html .
cp -n wordpress/xmlrpc.php .
cp -rn wordpress/wp-admin .
cp -rn wordpress/wp-includes .

# Ensure wp-content directories exist
mkdir -p wp-content/plugins
mkdir -p wp-content/uploads
mkdir -p wp-content/upgrade

# Set up configuration
if [ ! -f "wp-config.php" ]; then
    cp wp-config-sample.php wp-config.php
    echo "✅ Created wp-config.php - Please edit with your database details"
else
    echo "✅ wp-config.php already exists"
fi

# Set permissions
echo ""
echo "Setting file permissions..."
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
chmod -R 775 wp-content/uploads
echo "✅ Permissions set"

# Clean up
echo ""
echo "Cleaning up..."
rm -rf wordpress/
rm -f wordpress.tar.gz
echo "✅ Cleanup complete"

# Database setup instructions
echo ""
echo "=========================================================="
echo "WordPress files are now in place!"
echo ""
echo "Next steps:"
echo "1. Create a MySQL database and user:"
echo "   mysql -u root -p"
echo "   CREATE DATABASE skerritt_wp;"
echo "   CREATE USER 'skerritt_user'@'localhost' IDENTIFIED BY 'your_password';"
echo "   GRANT ALL PRIVILEGES ON skerritt_wp.* TO 'skerritt_user'@'localhost';"
echo "   FLUSH PRIVILEGES;"
echo ""
echo "2. Edit wp-config.php with your database details"
echo ""
echo "3. Visit your site URL to complete WordPress installation"
echo ""
echo "4. After installation, activate the 'Skerritt Economics & Consulting' theme"
echo ""
echo "5. Import content using the provided SQL file (if available)"
echo "=========================================================="