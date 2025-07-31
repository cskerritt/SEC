#!/usr/bin/env python3
"""
Simple CSS and JavaScript minifier for performance optimization
"""
import re
import os

def minify_css(content):
    """Minify CSS content"""
    # Remove comments
    content = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', content)
    # Remove unnecessary whitespace
    content = re.sub(r'\s+', ' ', content)
    # Remove spaces around specific characters
    content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', content)
    # Remove trailing semicolon before closing brace
    content = re.sub(r';\}', '}', content)
    # Remove quotes from urls when possible
    content = re.sub(r'url\(["\']?([^"\'()]+)["\']?\)', r'url(\1)', content)
    return content.strip()

def minify_js(content):
    """Basic JavaScript minifier - preserves strings and essential spaces"""
    # Preserve strings
    strings = []
    def preserve_string(match):
        strings.append(match.group(0))
        return f'__STRING_{len(strings)-1}__'
    
    # Temporarily replace strings
    content = re.sub(r'"(?:[^"\\]|\\.)*"', preserve_string, content)
    content = re.sub(r"'(?:[^'\\]|\\.)*'", preserve_string, content)
    content = re.sub(r'`(?:[^`\\]|\\.)*`', preserve_string, content)
    
    # Remove single-line comments (but not URLs)
    content = re.sub(r'(?<!:)//[^\n]*', '', content)
    # Remove multi-line comments
    content = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', content)
    # Remove unnecessary whitespace
    content = re.sub(r'\s+', ' ', content)
    # Remove spaces around operators
    content = re.sub(r'\s*([=+\-*/%<>!&|^~?:,;{}()\[\]])\s*', r'\1', content)
    # Add necessary spaces back
    content = re.sub(r'(return|new|delete|typeof|instanceof|in|void|throw|else|case|break|continue|function|var|let|const|if|for|while|do|switch|try|catch|finally|class|extends|export|import)([^a-zA-Z0-9_$])', r'\1 \2', content)
    
    # Restore strings
    for i, string in enumerate(strings):
        content = content.replace(f'__STRING_{i}__', string)
    
    return content.strip()

def process_file(input_path, output_path, minifier):
    """Process a single file"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        minified = minifier(content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minified)
        
        original_size = len(content)
        minified_size = len(minified)
        savings = original_size - minified_size
        percentage = (savings / original_size) * 100 if original_size > 0 else 0
        
        print(f"✓ {os.path.basename(input_path)}: {original_size} → {minified_size} bytes (-{savings} bytes, -{percentage:.1f}%)")
        return True
    except Exception as e:
        print(f"✗ Error processing {input_path}: {e}")
        return False

def main():
    """Main function"""
    css_files = [
        ('css/styles.css', 'css/styles.min.css'),
        ('css/homepage.css', 'css/homepage.min.css'),
        ('css/icons.css', 'css/icons.min.css'),
        ('css/faq-redesign.css', 'css/faq-redesign.min.css'),
        ('css/mobile-fixes.css', 'css/mobile-fixes.min.css')
    ]
    
    js_files = [
        ('js/main.js', 'js/main.min.js'),
        ('js/mobile-select-fix.js', 'js/mobile-select-fix.min.js')
    ]
    
    print("Minifying CSS files...")
    for input_file, output_file in css_files:
        if os.path.exists(input_file):
            process_file(input_file, output_file, minify_css)
    
    print("\nMinifying JavaScript files...")
    for input_file, output_file in js_files:
        if os.path.exists(input_file):
            process_file(input_file, output_file, minify_js)
    
    print("\nMinification complete!")

if __name__ == "__main__":
    main()