#!/usr/bin/env python3
import os
import re

def remove_hyperlinks(content):
    """Remove all HTML hyperlinks but keep the link text."""
    # Pattern to match <a href="...">text</a>
    pattern = r'<a\s+(?:[^>]*?\s+)?href="[^"]*"[^>]*?>(.*?)</a>'
    
    # Replace with just the text content
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def process_blog_posts():
    """Process all blog posts to remove hyperlinks."""
    blog_dir = '/Users/chrisskerritt/SEC/blog/2025/01'
    
    if not os.path.exists(blog_dir):
        print(f"Blog directory not found: {blog_dir}")
        return
    
    # Get all HTML files in the blog directory
    blog_files = [f for f in os.listdir(blog_dir) if f.endswith('.html')]
    
    files_processed = 0
    
    for filename in blog_files:
        filepath = os.path.join(blog_dir, filename)
        
        try:
            # Read the file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if there are any hyperlinks
            if '<a href=' in content:
                # Remove hyperlinks
                modified_content = remove_hyperlinks(content)
                
                # Write back the modified content
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"Processed: {filename}")
                files_processed += 1
            else:
                print(f"No hyperlinks found in: {filename}")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    print(f"\nTotal files processed: {files_processed}")
    print(f"Total blog posts checked: {len(blog_files)}")

if __name__ == "__main__":
    process_blog_posts()