#!/usr/bin/env python3
"""
Content Migration Script for Skerritt Economics WordPress Site
Converts existing Jekyll/HTML content to WordPress-ready SQL
"""

import os
import re
import json
from datetime import datetime
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {'script', 'style', 'meta', 'link'}
        self.current_tag = None

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_endtag(self, tag):
        self.current_tag = None

    def handle_data(self, data):
        if self.current_tag not in self.skip_tags:
            self.text_parts.append(data.strip())

    def get_text(self):
        return ' '.join(filter(None, self.text_parts))

def extract_content_from_file(filepath):
    """Extract content from Jekyll markdown or HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's a Jekyll file with front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1].strip()
            body = parts[2].strip()
            
            # Parse front matter
            meta = {}
            for line in front_matter.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    meta[key.strip()] = value.strip().strip('"\'')
            
            return {
                'title': meta.get('title', ''),
                'content': body,
                'description': meta.get('description', ''),
                'layout': meta.get('layout', 'default')
            }
    
    # Otherwise, try to extract from HTML
    parser = HTMLTextExtractor()
    parser.feed(content)
    
    # Try to find title
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else os.path.basename(filepath).replace('.html', '').replace('-', ' ').title()
    
    return {
        'title': title,
        'content': content,
        'description': '',
        'layout': 'default'
    }

def generate_wordpress_pages():
    """Generate WordPress page data from existing site structure."""
    pages = []
    
    # Main pages to migrate
    page_files = [
        ('index.md', 'Home', 'home', 'front-page'),
        ('about.md', 'About', 'about', 'default'),
        ('contact.md', 'Contact', 'contact', 'contact'),
        ('services/index.html', 'Services', 'services', 'default'),
        ('practice-areas/index.html', 'Practice Areas', 'practice-areas', 'default'),
        ('resources.md', 'Resources', 'resources', 'default'),
        ('case-studies/index.html', 'Case Studies', 'case-studies', 'default'),
        ('life-care-planning/index.html', 'Life Care Planning', 'life-care-planning', 'default'),
        ('vocational-expert/index.html', 'Vocational Expert', 'vocational-expert', 'default'),
    ]
    
    for filepath, title, slug, template in page_files:
        if os.path.exists(filepath):
            data = extract_content_from_file(filepath)
            pages.append({
                'title': data.get('title', title),
                'slug': slug,
                'content': data['content'],
                'template': template,
                'description': data.get('description', ''),
                'status': 'publish',
                'type': 'page'
            })
    
    return pages

def generate_services_posts():
    """Generate service custom post type data."""
    services = [
        {
            'title': 'Forensic Economics',
            'slug': 'forensic-economics',
            'content': '''<p>Expert economic analysis for litigation support, specializing in calculating economic damages for personal injury, wrongful death, and employment cases.</p>
            
            <h2>Our Forensic Economics Services Include:</h2>
            <ul>
                <li>Lost earnings and earning capacity calculations</li>
                <li>Medical cost projections</li>
                <li>Household services valuations</li>
                <li>Pension and benefits analysis</li>
                <li>Present value calculations</li>
            </ul>''',
            'excerpt': 'Court-tested economic damage assessments for personal injury, wrongful death, and employment litigation.',
            'icon': '📊'
        },
        {
            'title': 'Business Valuation',
            'slug': 'business-valuation',
            'content': '''<p>Comprehensive business valuation services for litigation, transactions, and strategic planning.</p>
            
            <h2>Business Valuation Services:</h2>
            <ul>
                <li>Fair market value assessments</li>
                <li>Buy-sell agreement valuations</li>
                <li>Shareholder dispute resolution</li>
                <li>Economic damages in commercial litigation</li>
                <li>Marital dissolution business valuations</li>
            </ul>''',
            'excerpt': 'Professional business valuations for litigation, transactions, tax matters, and strategic planning.',
            'icon': '💼'
        },
        {
            'title': 'Life Care Planning',
            'slug': 'life-care-planning',
            'content': '''<p>Detailed life care plans that project future medical and care needs for catastrophically injured individuals.</p>
            
            <h2>Life Care Planning Services:</h2>
            <ul>
                <li>Future medical cost projections</li>
                <li>Rehabilitation needs assessment</li>
                <li>Home modification requirements</li>
                <li>Assistive technology needs</li>
                <li>Long-term care planning</li>
            </ul>''',
            'excerpt': 'Comprehensive life care plans projecting future medical and care needs for catastrophic injury cases.',
            'icon': '🏥'
        },
        {
            'title': 'Vocational Expert Services',
            'slug': 'vocational-expert-services',
            'content': '''<p>Expert vocational assessments for employment litigation, disability claims, and personal injury cases.</p>
            
            <h2>Vocational Services Include:</h2>
            <ul>
                <li>Employability assessments</li>
                <li>Labor market analysis</li>
                <li>Transferable skills analysis</li>
                <li>Job placement feasibility</li>
                <li>Vocational rehabilitation planning</li>
            </ul>''',
            'excerpt': 'Professional vocational assessments for employment disputes, disability claims, and injury cases.',
            'icon': '👔'
        }
    ]
    
    return services

def generate_practice_areas_posts():
    """Generate practice area custom post type data."""
    practice_areas = [
        {
            'title': 'Personal Injury',
            'slug': 'personal-injury',
            'content': '''<p>Economic damage calculations for personal injury cases, including motor vehicle accidents, premises liability, and product liability claims.</p>''',
            'icon': '⚖️'
        },
        {
            'title': 'Medical Malpractice',
            'slug': 'medical-malpractice',
            'content': '''<p>Expert economic analysis for medical malpractice cases, calculating lost earnings, medical costs, and care requirements.</p>''',
            'icon': '🏥'
        },
        {
            'title': 'Employment Litigation',
            'slug': 'employment-litigation',
            'content': '''<p>Economic assessments for wrongful termination, discrimination, and other employment-related disputes.</p>''',
            'icon': '💼'
        },
        {
            'title': 'Commercial Disputes',
            'slug': 'commercial-disputes',
            'content': '''<p>Business valuation and economic damage analysis for breach of contract, partnership disputes, and other commercial litigation.</p>''',
            'icon': '📊'
        },
        {
            'title': 'Wrongful Death',
            'slug': 'wrongful-death',
            'content': '''<p>Comprehensive economic loss calculations for wrongful death cases, including lost support and services.</p>''',
            'icon': '🏛️'
        }
    ]
    
    return practice_areas

def generate_sql_import():
    """Generate SQL import file for WordPress content."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql_lines = []
    
    # Add header
    sql_lines.append("-- WordPress Content Import for Skerritt Economics & Consulting")
    sql_lines.append(f"-- Generated: {timestamp}")
    sql_lines.append("-- Make sure to update wp_ prefix if your WordPress uses a different prefix")
    sql_lines.append("")
    
    # Generate pages
    pages = generate_wordpress_pages()
    post_id = 100  # Start with ID 100 to avoid conflicts
    
    sql_lines.append("-- Pages")
    for page in pages:
        sql_lines.append(f"""INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_name, post_modified, post_modified_gmt, post_type, post_mime_type) 
VALUES 
({post_id}, 1, '{timestamp}', '{timestamp}', '{page['content'].replace("'", "''")}', '{page['title']}', '{page['description']}', 'publish', 'closed', 'closed', '{page['slug']}', '{timestamp}', '{timestamp}', 'page', '');""")
        
        if page['template'] != 'default':
            sql_lines.append(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({post_id}, '_wp_page_template', '{page['template']}.php');")
        
        post_id += 1
        sql_lines.append("")
    
    # Generate services
    services = generate_services_posts()
    sql_lines.append("-- Services (Custom Post Type)")
    for service in services:
        sql_lines.append(f"""INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_name, post_modified, post_modified_gmt, post_type, post_mime_type) 
VALUES 
({post_id}, 1, '{timestamp}', '{timestamp}', '{service['content'].replace("'", "''")}', '{service['title']}', '{service['excerpt']}', 'publish', 'closed', 'closed', '{service['slug']}', '{timestamp}', '{timestamp}', 'service', '');""")
        
        sql_lines.append(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({post_id}, 'service_icon', '{service['icon']}');")
        post_id += 1
        sql_lines.append("")
    
    # Generate practice areas
    practice_areas = generate_practice_areas_posts()
    sql_lines.append("-- Practice Areas (Custom Post Type)")
    for area in practice_areas:
        sql_lines.append(f"""INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_name, post_modified, post_modified_gmt, post_type, post_mime_type) 
VALUES 
({post_id}, 1, '{timestamp}', '{timestamp}', '{area['content'].replace("'", "''")}', '{area['title']}', '', 'publish', 'closed', 'closed', '{area['slug']}', '{timestamp}', '{timestamp}', 'practice-area', '');""")
        
        sql_lines.append(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({post_id}, 'practice_area_icon', '{area['icon']}');")
        post_id += 1
        sql_lines.append("")
    
    # Write SQL file
    with open('wordpress-content-import.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_lines))
    
    print(f"✅ Generated wordpress-content-import.sql with {len(pages)} pages, {len(services)} services, and {len(practice_areas)} practice areas")
    return len(pages) + len(services) + len(practice_areas)

if __name__ == "__main__":
    print("WordPress Content Migration Script")
    print("==================================")
    print()
    
    # Check current directory
    if not os.path.exists('index.md') and not os.path.exists('index.html'):
        print("❌ Error: This script should be run from the site root directory")
        exit(1)
    
    # Generate SQL import
    total_items = generate_sql_import()
    
    print()
    print("Migration complete!")
    print()
    print("Next steps:")
    print("1. Complete WordPress installation")
    print("2. Activate the 'Skerritt Economics & Consulting' theme")
    print("3. Import the content using:")
    print("   mysql -u your_user -p your_database < wordpress-content-import.sql")
    print()
    print("Note: You may need to adjust the SQL file if your WordPress uses a different table prefix than 'wp_'")