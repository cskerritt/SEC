#!/usr/bin/env python3
"""
Image optimization script for website performance
Requires: pip install pillow
"""

import os
import sys
from PIL import Image
import argparse
from pathlib import Path

def optimize_image(input_path, output_path=None, quality=85, max_width=1920):
    """Optimize a single image"""
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if needed (for JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        # Resize if too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # Set output path
        if output_path is None:
            output_path = input_path
        
        # Save optimized image
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        # Get file sizes
        original_size = os.path.getsize(input_path)
        new_size = os.path.getsize(output_path)
        reduction = (1 - new_size/original_size) * 100
        
        print(f"✓ {input_path}")
        print(f"  Original: {original_size:,} bytes")
        print(f"  Optimized: {new_size:,} bytes")
        print(f"  Reduction: {reduction:.1f}%\n")
        
        return True
        
    except Exception as e:
        print(f"✗ Error optimizing {input_path}: {e}")
        return False

def create_webp_version(input_path):
    """Create a WebP version of the image"""
    try:
        img = Image.open(input_path)
        webp_path = input_path.rsplit('.', 1)[0] + '.webp'
        
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = background
        
        img.save(webp_path, 'WEBP', quality=85, method=6)
        
        original_size = os.path.getsize(input_path)
        webp_size = os.path.getsize(webp_path)
        reduction = (1 - webp_size/original_size) * 100
        
        print(f"✓ Created WebP: {webp_path}")
        print(f"  Size: {webp_size:,} bytes ({reduction:.1f}% smaller than original)\n")
        
        return True
        
    except Exception as e:
        print(f"✗ Error creating WebP for {input_path}: {e}")
        return False

def add_lazy_loading_to_html(directory):
    """Add loading='lazy' to img tags in HTML files"""
    import re
    
    html_files = list(Path(directory).rglob('*.html'))
    modified_count = 0
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Skip if already has lazy loading
            if 'loading="lazy"' in content or "loading='lazy'" in content:
                continue
            
            # Add loading="lazy" to img tags (except those in hero sections)
            original_content = content
            
            # Pattern to match img tags not in hero sections and without loading attribute
            pattern = r'(<img(?![^>]*loading)[^>]*?)(/?>)'
            
            def add_lazy(match):
                tag = match.group(1)
                closing = match.group(2)
                
                # Skip if it's in a hero section (check previous 200 chars)
                start = max(0, match.start() - 200)
                context = content[start:match.start()].lower()
                if 'hero' in context or 'banner' in context or 'above-the-fold' in context:
                    return match.group(0)
                
                return f'{tag} loading="lazy"{closing}'
            
            content = re.sub(pattern, add_lazy, content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"✓ Added lazy loading to: {html_file}")
        
        except Exception as e:
            print(f"✗ Error processing {html_file}: {e}")
    
    print(f"\nModified {modified_count} HTML files with lazy loading")

def main():
    parser = argparse.ArgumentParser(description='Optimize images for web performance')
    parser.add_argument('path', nargs='?', default='.', help='Path to directory or image file')
    parser.add_argument('--quality', type=int, default=85, help='JPEG quality (1-100, default: 85)')
    parser.add_argument('--max-width', type=int, default=1920, help='Maximum width in pixels (default: 1920)')
    parser.add_argument('--webp', action='store_true', help='Also create WebP versions')
    parser.add_argument('--lazy', action='store_true', help='Add lazy loading to HTML files')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file():
        # Single file optimization
        if path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            optimize_image(str(path), quality=args.quality, max_width=args.max_width)
            if args.webp:
                create_webp_version(str(path))
        else:
            print(f"Error: {path} is not a supported image format")
    
    elif path.is_dir():
        # Directory optimization
        image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        image_files = []
        
        for ext in image_extensions:
            image_files.extend(path.rglob(ext))
        
        print(f"Found {len(image_files)} images to optimize\n")
        
        success_count = 0
        for img_path in image_files:
            # Skip already optimized images
            if '-optimized' in str(img_path):
                continue
                
            if optimize_image(str(img_path), quality=args.quality, max_width=args.max_width):
                success_count += 1
                
                if args.webp:
                    create_webp_version(str(img_path))
        
        print(f"\nOptimized {success_count}/{len(image_files)} images successfully")
        
        if args.lazy:
            add_lazy_loading_to_html(str(path))
    
    else:
        print(f"Error: {path} not found")
        sys.exit(1)

if __name__ == "__main__":
    main()