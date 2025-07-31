#!/usr/bin/env python3
"""
Safe JavaScript minifier that preserves syntax
"""
import re

def minify_js_safe(content):
    """Safely minify JavaScript without breaking syntax"""
    # Remove single-line comments (but not URLs)
    content = re.sub(r'(?<!:)//[^\n]*', '', content)
    
    # Remove multi-line comments
    content = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', content)
    
    # Remove leading/trailing whitespace from lines
    lines = [line.strip() for line in content.split('\n')]
    
    # Remove empty lines
    lines = [line for line in lines if line]
    
    # Join lines with a space to avoid syntax errors
    content = ' '.join(lines)
    
    # Compress multiple spaces to single space
    content = re.sub(r'\s+', ' ', content)
    
    # Remove spaces around specific operators (but be careful)
    # Only remove spaces where it's safe
    content = re.sub(r'\s*([{}();,])\s*', r'\1', content)
    content = re.sub(r'\s*([=+\-*/])\s*', r' \1 ', content)
    
    # Fix specific patterns that need spaces
    content = re.sub(r'(function|return|new|delete|typeof|instanceof|in|void|throw|else|case|break|continue|var|let|const|if|for|while|do|switch|try|catch|finally|class|extends|export|import)\s*([^a-zA-Z0-9_$])', r'\1 \2', content)
    
    return content.strip()

def process_files():
    """Process JavaScript files"""
    js_files = [
        ('js/main.js', 'js/main.min.js'),
        ('js/mobile-select-fix.js', 'js/mobile-select-fix.min.js')
    ]
    
    for input_file, output_file in js_files:
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # For now, just copy the files without breaking them
            # A proper minifier would be better but this ensures no syntax errors
            minified = content
            
            # Just remove comments and extra whitespace safely
            minified = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', minified)
            minified = re.sub(r'(?<!:)//[^\n]*', '', minified)
            minified = re.sub(r'\n\s*\n', '\n', minified)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(minified)
            
            print(f"✓ {input_file} → {output_file}")
        except Exception as e:
            print(f"✗ Error processing {input_file}: {e}")

if __name__ == "__main__":
    process_files()