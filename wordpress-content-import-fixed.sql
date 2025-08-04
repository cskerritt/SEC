-- WordPress Content Import for Skerritt Economics & Consulting
-- Generated: 2025-08-01
-- Fixed version with all required fields

-- Set SQL mode to be more permissive
SET SQL_MODE='';

-- Pages
INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(100, 1, NOW(), NOW(), '<h1>Welcome to Skerritt Economics & Consulting</h1><p>Court-tested forensic economics and business valuation expertise for personal injury, medical malpractice, employment, and commercial litigation across Rhode Island, Massachusetts, and New England.</p>', 'Home', 'Court-tested economic damage assessments and business valuations for lawyers across Rhode Island, Massachusetts, and New England.', 'publish', 'closed', 'closed', '', 'home', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=100', 0, 'page', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(101, 1, NOW(), NOW(), '<h1>About Christopher Skerritt</h1><p>With over 25 years of experience in forensic economics and business valuation, Christopher Skerritt provides expert testimony and analysis for attorneys throughout New England.</p>', 'About', 'Learn about Christopher Skerritt, MBA - Forensic Economist and Business Valuation Expert', 'publish', 'closed', 'closed', '', 'about', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=101', 0, 'page', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(102, 1, NOW(), NOW(), '<h1>Our Services</h1><p>Comprehensive economic analysis and valuation services for legal professionals.</p>', 'Services', 'Expert forensic economics, business valuation, life care planning, and vocational assessment services', 'publish', 'closed', 'closed', '', 'services', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=102', 0, 'page', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(103, 1, NOW(), NOW(), '<h1>Practice Areas</h1><p>We provide economic analysis for various types of legal matters.</p>', 'Practice Areas', 'Personal injury, medical malpractice, employment litigation, and commercial dispute expertise', 'publish', 'closed', 'closed', '', 'practice-areas', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=103', 0, 'page', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(104, 1, NOW(), NOW(), '<h1>Resources</h1><p>Helpful resources and information for attorneys working with economic experts.</p>', 'Resources', 'Resources and information for attorneys', 'publish', 'closed', 'closed', '', 'resources', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=104', 0, 'page', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(105, 1, NOW(), NOW(), '<h1>Contact Us</h1><p>Contact Skerritt Economics & Consulting for a confidential consultation about your case.</p>', 'Contact', 'Contact Skerritt Economics & Consulting for expert economic analysis', 'publish', 'closed', 'closed', '', 'contact', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?page_id=105', 0, 'page', '', 0);

-- Set page templates
INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES (100, '_wp_page_template', 'front-page.php');
INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES (105, '_wp_page_template', 'page-contact.php');

-- Services (Custom Post Type)
INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(110, 1, NOW(), NOW(), '<p>Expert economic analysis for litigation support, specializing in calculating economic damages for personal injury, wrongful death, and employment cases.</p><h2>Our Forensic Economics Services Include:</h2><ul><li>Lost earnings and earning capacity calculations</li><li>Medical cost projections</li><li>Household services valuations</li><li>Pension and benefits analysis</li><li>Present value calculations</li></ul>', 'Forensic Economics', 'Court-tested economic damage assessments for personal injury, wrongful death, and employment litigation.', 'publish', 'closed', 'closed', '', 'forensic-economics', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?post_type=service&p=110', 0, 'service', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(111, 1, NOW(), NOW(), '<p>Comprehensive business valuation services for litigation, transactions, and strategic planning.</p><h2>Business Valuation Services:</h2><ul><li>Fair market value assessments</li><li>Buy-sell agreement valuations</li><li>Shareholder dispute resolution</li><li>Economic damages in commercial litigation</li><li>Marital dissolution business valuations</li></ul>', 'Business Valuation', 'Professional business valuations for litigation, transactions, tax matters, and strategic planning.', 'publish', 'closed', 'closed', '', 'business-valuation', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?post_type=service&p=111', 0, 'service', '', 0);

-- Practice Areas (Custom Post Type)
INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(120, 1, NOW(), NOW(), '<p>Economic damage calculations for personal injury cases, including motor vehicle accidents, premises liability, and product liability claims.</p>', 'Personal Injury', '', 'publish', 'closed', 'closed', '', 'personal-injury', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?post_type=practice-area&p=120', 0, 'practice-area', '', 0);

INSERT INTO wp_posts 
(ID, post_author, post_date, post_date_gmt, post_content, post_title, post_excerpt, post_status, comment_status, ping_status, post_password, post_name, to_ping, pinged, post_modified, post_modified_gmt, post_content_filtered, post_parent, guid, menu_order, post_type, post_mime_type, comment_count) 
VALUES 
(121, 1, NOW(), NOW(), '<p>Expert economic analysis for medical malpractice cases, calculating lost earnings, medical costs, and care requirements.</p>', 'Medical Malpractice', '', 'publish', 'closed', 'closed', '', 'medical-malpractice', '', '', NOW(), NOW(), '', 0, 'https://skerritteconomics.com/?post_type=practice-area&p=121', 0, 'practice-area', '', 0);