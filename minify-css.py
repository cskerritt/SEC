#!/usr/bin/env python3
"""
Simple CSS minifier for the site
"""
import re
import os
import sys

def minify_css(css):
    """Basic CSS minification"""
    # Remove comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    
    # Remove unnecessary whitespace
    css = re.sub(r'\s+', ' ', css)
    
    # Remove space around specific characters
    css = re.sub(r'\s*([{}:;,>~+])\s*', r'\1', css)
    
    # Remove trailing semicolon before closing brace
    css = re.sub(r';\}', '}', css)
    
    # Remove unnecessary quotes in urls
    css = re.sub(r'url\((["\'])([^"\']+)\1\)', r'url(\2)', css)
    
    # Remove space after opening brace
    css = re.sub(r'{\s+', '{', css)
    
    # Remove final newline
    css = css.strip()
    
    return css

def process_file(input_file, output_file):
    """Process a single CSS file"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            css = f.read()
        
        minified = minify_css(css)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(minified)
        
        # Calculate compression ratio
        original_size = len(css)
        minified_size = len(minified)
        ratio = (1 - minified_size / original_size) * 100
        
        print(f"✓ {input_file} -> {output_file}")
        print(f"  Original: {original_size:,} bytes")
        print(f"  Minified: {minified_size:,} bytes")
        print(f"  Reduced by: {ratio:.1f}%\n")
        
    except Exception as e:
        print(f"✗ Error processing {input_file}: {e}")
        return False
    
    return True

def main():
    """Main function"""
    css_dir = "/Users/chrisskerritt/SEC/css"
    
    # Files to minify
    files_to_minify = [
        "styles.css",
        "mobile-optimized.css",
        "mobile-fixes.css",
        "homepage.css",
        "city-pages.css",
        "about.css",
        "contact.css",
        "services.css"
    ]
    
    success_count = 0
    
    for filename in files_to_minify:
        input_path = os.path.join(css_dir, filename)
        output_path = os.path.join(css_dir, filename.replace('.css', '.min.css'))
        
        if os.path.exists(input_path):
            if process_file(input_path, output_path):
                success_count += 1
        else:
            print(f"⚠ File not found: {input_path}")
    
    print(f"\nMinification complete: {success_count}/{len(files_to_minify)} files processed")

if __name__ == "__main__":
    main()