#!/usr/bin/env python3
"""
Performance Monitoring Script for UI Library Migration
Tracks page load times, file sizes, and performance metrics
"""

import os
import json
import time
import gzip
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin

class PerformanceMonitor:
    def __init__(self):
        self.results = {
            'pages': [],
            'summary': {
                'total_pages': 0,
                'avg_size': 0,
                'avg_size_reduction': 0,
                'total_size_saved': 0,
                'lighthouse_scores': []
            }
        }
        
        # Baseline sizes for comparison (pre-migration averages)
        self.baseline_sizes = {
            'city_page': 45000,  # 45KB average
            'service_page': 60000,  # 60KB average
            'practice_page': 55000  # 55KB average
        }

    def analyze_file(self, filepath):
        """Analyze a single HTML file for performance metrics"""
        try:
            # Get file size
            file_size = os.path.getsize(filepath)
            
            # Read file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate compressed size (simulated gzip)
            compressed_size = len(gzip.compress(content.encode('utf-8')))
            
            # Determine page type
            page_type = self.get_page_type(filepath)
            baseline_size = self.baseline_sizes.get(page_type, 50000)
            
            # Calculate size reduction
            size_reduction = baseline_size - file_size
            reduction_percentage = (size_reduction / baseline_size) * 100 if baseline_size > 0 else 0
            
            # Count resources
            metrics = {
                'filepath': filepath,
                'file_size': file_size,
                'compressed_size': compressed_size,
                'baseline_size': baseline_size,
                'size_reduction': size_reduction,
                'reduction_percentage': reduction_percentage,
                'resources': self.count_resources(content),
                'has_bootstrap': self.check_bootstrap(content),
                'performance_score': self.estimate_performance_score(content, file_size)
            }
            
            self.results['pages'].append(metrics)
            return metrics
            
        except Exception as e:
            print(f"Error analyzing {filepath}: {str(e)}")
            return None

    def get_page_type(self, filepath):
        """Determine the type of page"""
        if 'cities' in filepath:
            return 'city_page'
        elif 'services' in filepath:
            return 'service_page'
        elif 'practice-areas' in filepath:
            return 'practice_page'
        else:
            return 'other_page'

    def count_resources(self, content):
        """Count external resources in the page"""
        resources = {
            'css_files': content.count('<link') + content.count('stylesheet'),
            'js_files': content.count('<script'),
            'images': content.count('<img'),
            'total_requests': 0
        }
        
        # Check for CDN resources (optimized)
        cdn_resources = sum([
            content.count('cdn.jsdelivr.net'),
            content.count('cdnjs.cloudflare.com'),
            content.count('unpkg.com')
        ])
        
        resources['cdn_resources'] = cdn_resources
        resources['total_requests'] = (resources['css_files'] + 
                                     resources['js_files'] + 
                                     resources['images'])
        
        return resources

    def check_bootstrap(self, content):
        """Check if page has Bootstrap integration"""
        bootstrap_indicators = [
            'bootstrap@5.3.2',
            'bootstrap.min.css',
            'ui-library-setup.html',
            'ui-library-bootstrap.css'
        ]
        
        return any(indicator in content for indicator in bootstrap_indicators)

    def estimate_performance_score(self, content, file_size):
        """Estimate a performance score based on various factors"""
        score = 100
        
        # Penalize for large file size
        if file_size > 100000:  # > 100KB
            score -= 20
        elif file_size > 50000:  # > 50KB
            score -= 10
        
        # Bonus for CDN usage
        if 'cdn.jsdelivr.net' in content:
            score += 5
        
        # Bonus for minified resources
        if '.min.css' in content or '.min.js' in content:
            score += 5
        
        # Penalize for too many requests
        resources = self.count_resources(content)
        if resources['total_requests'] > 20:
            score -= 15
        elif resources['total_requests'] > 10:
            score -= 5
        
        # Bonus for lazy loading
        if 'loading="lazy"' in content:
            score += 5
        
        # Bonus for async/defer scripts
        if 'defer' in content or 'async' in content:
            score += 5
        
        return max(0, min(100, score))

    def analyze_directory(self, directory_path):
        """Analyze all HTML files in a directory"""
        html_files = list(Path(directory_path).rglob('*.html'))
        html_files = [f for f in html_files if '_site' not in str(f)]
        
        print(f"Analyzing {len(html_files)} HTML files for performance...\n")
        
        for filepath in html_files:
            self.analyze_file(str(filepath))
        
        self.calculate_summary()
        self.print_report()

    def calculate_summary(self):
        """Calculate summary statistics"""
        if not self.results['pages']:
            return
        
        total_pages = len(self.results['pages'])
        total_size = sum(p['file_size'] for p in self.results['pages'])
        total_reduction = sum(p['size_reduction'] for p in self.results['pages'])
        
        self.results['summary'] = {
            'total_pages': total_pages,
            'avg_size': total_size / total_pages,
            'avg_size_reduction': total_reduction / total_pages,
            'total_size_saved': total_reduction,
            'avg_performance_score': sum(p['performance_score'] for p in self.results['pages']) / total_pages,
            'bootstrap_adoption': sum(1 for p in self.results['pages'] if p['has_bootstrap']) / total_pages * 100
        }

    def print_report(self):
        """Print performance monitoring report"""
        print('=' * 70)
        print('Performance Monitoring Report')
        print('=' * 70)
        
        summary = self.results['summary']
        
        print(f"\nTotal Pages Analyzed: {summary['total_pages']}")
        print(f"Average Page Size: {summary['avg_size'] / 1024:.1f} KB")
        print(f"Average Size Reduction: {summary['avg_size_reduction'] / 1024:.1f} KB ({summary['avg_size_reduction'] / summary['avg_size'] * 100:.1f}%)")
        print(f"Total Size Saved: {summary['total_size_saved'] / 1024 / 1024:.2f} MB")
        print(f"Bootstrap Adoption: {summary['bootstrap_adoption']:.1f}%")
        print(f"Average Performance Score: {summary['avg_performance_score']:.1f}/100")
        
        # Find best and worst performing pages
        sorted_pages = sorted(self.results['pages'], 
                            key=lambda x: x['performance_score'], 
                            reverse=True)
        
        print("\n🏆 Top 5 Best Performing Pages:")
        print("-" * 70)
        for page in sorted_pages[:5]:
            print(f"{page['filepath']}")
            print(f"  Size: {page['file_size'] / 1024:.1f} KB | Score: {page['performance_score']} | Resources: {page['resources']['total_requests']}")
        
        print("\n⚠️  Bottom 5 Pages Needing Optimization:")
        print("-" * 70)
        for page in sorted_pages[-5:]:
            print(f"{page['filepath']}")
            print(f"  Size: {page['file_size'] / 1024:.1f} KB | Score: {page['performance_score']} | Resources: {page['resources']['total_requests']}")
        
        # Resource usage statistics
        print("\n📊 Resource Usage Statistics:")
        print("-" * 70)
        
        total_css = sum(p['resources']['css_files'] for p in self.results['pages'])
        total_js = sum(p['resources']['js_files'] for p in self.results['pages'])
        total_images = sum(p['resources']['images'] for p in self.results['pages'])
        total_cdn = sum(p['resources']['cdn_resources'] for p in self.results['pages'])
        
        print(f"Average CSS files per page: {total_css / summary['total_pages']:.1f}")
        print(f"Average JS files per page: {total_js / summary['total_pages']:.1f}")
        print(f"Average images per page: {total_images / summary['total_pages']:.1f}")
        print(f"CDN resources used: {total_cdn}")
        
        # Recommendations
        print("\n💡 Recommendations:")
        print("-" * 70)
        
        if summary['bootstrap_adoption'] < 50:
            print("⚠️  Low Bootstrap adoption - continue migration to improve consistency")
        
        if summary['avg_size'] > 50000:
            print("⚠️  Average page size is high - consider optimizing images and minifying resources")
        
        large_pages = [p for p in self.results['pages'] if p['file_size'] > 100000]
        if large_pages:
            print(f"⚠️  {len(large_pages)} pages are over 100KB - review and optimize")
        
        # Save detailed report
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': self.results['summary'],
            'pages': sorted(self.results['pages'], 
                          key=lambda x: x['performance_score'])[:50]  # Top 50 for detail
        }
        
        with open('performance-report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print("\n📄 Detailed report saved to: performance-report.json")

def main():
    parser = argparse.ArgumentParser(description='Monitor performance of migrated pages')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Path to analyze')
    parser.add_argument('--compare', action='store_true',
                       help='Compare with baseline metrics')
    
    args = parser.parse_args()
    
    monitor = PerformanceMonitor()
    
    print('📊 Performance Monitoring Script')
    print('Analyzing page performance metrics...\n')
    
    if os.path.isfile(args.path):
        result = monitor.analyze_file(args.path)
        if result:
            print(f"File: {args.path}")
            print(f"Size: {result['file_size'] / 1024:.1f} KB")
            print(f"Performance Score: {result['performance_score']}")
            print(f"Bootstrap: {'Yes' if result['has_bootstrap'] else 'No'}")
    else:
        monitor.analyze_directory(args.path)

if __name__ == '__main__':
    main()