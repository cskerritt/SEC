#!/usr/bin/env python3
"""
Migration Report Generator
Creates comprehensive reports on UI library migration progress
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
import argparse

class MigrationReportGenerator:
    def __init__(self):
        self.stats = {
            'total_html_files': 0,
            'migrated_files': 0,
            'pending_files': 0,
            'backup_files': 0,
            'by_type': {},
            'by_state': {},
            'migration_timeline': [],
            'issues': []
        }
        
    def scan_directory(self, directory_path):
        """Scan directory for migration status"""
        print(f"Scanning {directory_path} for migration status...")
        
        # Find all HTML files
        html_files = list(Path(directory_path).rglob('*.html'))
        html_files = [f for f in html_files if '_site' not in str(f)]
        
        self.stats['total_html_files'] = len(html_files)
        
        # Check each file
        for filepath in html_files:
            self.analyze_file(filepath)
        
        # Find backup files
        backup_files = list(Path(directory_path).rglob('*.pre-ui-backup'))
        self.stats['backup_files'] = len(backup_files)
        
        # Generate timeline from backup files
        self.generate_timeline(backup_files)
        
    def analyze_file(self, filepath):
        """Analyze a single file's migration status"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine migration status
            is_migrated = any([
                'bootstrap@5.3.2' in content,
                'bootstrap.min.css' in content,
                'ui-library-setup.html' in content,
                'ui-library-bootstrap.css' in content
            ])
            
            # Categorize file
            file_type = self.get_file_type(str(filepath))
            
            if file_type not in self.stats['by_type']:
                self.stats['by_type'][file_type] = {
                    'total': 0,
                    'migrated': 0,
                    'pending': 0
                }
            
            self.stats['by_type'][file_type]['total'] += 1
            
            if is_migrated:
                self.stats['migrated_files'] += 1
                self.stats['by_type'][file_type]['migrated'] += 1
                
                # Check for issues in migrated files
                self.check_migrated_file_issues(filepath, content)
            else:
                self.stats['pending_files'] += 1
                self.stats['by_type'][file_type]['pending'] += 1
            
            # Track by state for city pages
            if 'cities' in str(filepath):
                state = self.extract_state(str(filepath))
                if state:
                    if state not in self.stats['by_state']:
                        self.stats['by_state'][state] = {
                            'total': 0,
                            'migrated': 0,
                            'pending': 0
                        }
                    
                    self.stats['by_state'][state]['total'] += 1
                    if is_migrated:
                        self.stats['by_state'][state]['migrated'] += 1
                    else:
                        self.stats['by_state'][state]['pending'] += 1
                        
        except Exception as e:
            self.stats['issues'].append({
                'file': str(filepath),
                'error': str(e)
            })
    
    def get_file_type(self, filepath):
        """Determine the type of file"""
        if 'cities' in filepath:
            if 'forensic-economist' in filepath:
                return 'city_forensic_economist'
            elif 'life-care-planner' in filepath:
                return 'city_life_care_planner'
            elif 'vocational-expert' in filepath:
                return 'city_vocational_expert'
            elif 'business-valuation' in filepath:
                return 'city_business_valuation'
            else:
                return 'city_other'
        elif 'services' in filepath:
            return 'service_page'
        elif 'practice-areas' in filepath:
            return 'practice_area'
        elif 'locations' in filepath and 'cities' not in filepath:
            return 'location_page'
        elif 'blog' in filepath:
            return 'blog_post'
        else:
            return 'other'
    
    def extract_state(self, filepath):
        """Extract state code from city file path"""
        match = re.search(r'-([a-z]{2})-(?:forensic|life|vocational|business)', filepath)
        if match:
            return match.group(1).upper()
        return None
    
    def check_migrated_file_issues(self, filepath, content):
        """Check for common issues in migrated files"""
        issues = []
        
        # Check for old button classes
        if re.search(r'class=["\']button["\']', content):
            issues.append('Old button class still present')
        
        # Check for missing viewport meta
        if '<head>' in content and 'viewport' not in content:
            issues.append('Missing viewport meta tag')
        
        # Check for inline styles
        if 'style=' in content:
            inline_count = content.count('style=')
            if inline_count > 5:
                issues.append(f'High inline style count: {inline_count}')
        
        if issues:
            self.stats['issues'].append({
                'file': str(filepath),
                'issues': issues
            })
    
    def generate_timeline(self, backup_files):
        """Generate migration timeline from backup files"""
        timeline = {}
        
        for backup_file in backup_files:
            # Get modification time
            mtime = os.path.getmtime(backup_file)
            date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            
            if date not in timeline:
                timeline[date] = 0
            timeline[date] += 1
        
        # Convert to list format
        self.stats['migration_timeline'] = [
            {'date': date, 'count': count}
            for date, count in sorted(timeline.items())
        ]
    
    def generate_html_report(self):
        """Generate HTML report"""
        completion_rate = (self.stats['migrated_files'] / self.stats['total_html_files'] * 100) if self.stats['total_html_files'] > 0 else 0
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI Migration Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .stat-card {{
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            padding: 2rem;
            height: 100%;
            transition: transform 0.3s ease;
        }}
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        .stat-number {{
            font-size: 3rem;
            font-weight: 700;
            line-height: 1;
        }}
        .progress-ring {{
            transform: rotate(-90deg);
        }}
        .table-container {{
            max-height: 400px;
            overflow-y: auto;
        }}
    </style>
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="display-4 text-center mb-5">UI Migration Report</h1>
        <p class="text-center text-muted mb-5">Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        
        <!-- Overall Progress -->
        <div class="row mb-5">
            <div class="col-12">
                <div class="stat-card">
                    <h2 class="h4 mb-4">Overall Migration Progress</h2>
                    <div class="progress" style="height: 40px;">
                        <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" 
                             style="width: {completion_rate:.1f}%">
                            {completion_rate:.1f}% Complete
                        </div>
                    </div>
                    <div class="row mt-4 text-center">
                        <div class="col-md-3">
                            <div class="stat-number text-primary">{self.stats['total_html_files']:,}</div>
                            <p class="text-muted mb-0">Total Pages</p>
                        </div>
                        <div class="col-md-3">
                            <div class="stat-number text-success">{self.stats['migrated_files']:,}</div>
                            <p class="text-muted mb-0">Migrated</p>
                        </div>
                        <div class="col-md-3">
                            <div class="stat-number text-warning">{self.stats['pending_files']:,}</div>
                            <p class="text-muted mb-0">Pending</p>
                        </div>
                        <div class="col-md-3">
                            <div class="stat-number text-info">{self.stats['backup_files']:,}</div>
                            <p class="text-muted mb-0">Backups</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Progress by Type -->
        <div class="row mb-5">
            <div class="col-md-6">
                <div class="stat-card">
                    <h3 class="h5 mb-4">Progress by Page Type</h3>
                    <canvas id="typeChart"></canvas>
                </div>
            </div>
            <div class="col-md-6">
                <div class="stat-card">
                    <h3 class="h5 mb-4">Migration Timeline</h3>
                    <canvas id="timelineChart"></canvas>
                </div>
            </div>
        </div>
        
        <!-- State Progress (for city pages) -->
        {self._generate_state_section()}
        
        <!-- Issues Section -->
        {self._generate_issues_section()}
        
        <!-- Detailed Stats -->
        <div class="row">
            <div class="col-12">
                <div class="stat-card">
                    <h3 class="h5 mb-4">Detailed Statistics</h3>
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Page Type</th>
                                    <th>Total</th>
                                    <th>Migrated</th>
                                    <th>Pending</th>
                                    <th>Progress</th>
                                </tr>
                            </thead>
                            <tbody>
                                {self._generate_type_rows()}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Type Chart
        const typeCtx = document.getElementById('typeChart').getContext('2d');
        new Chart(typeCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['Migrated', 'Pending'],
                datasets: [{{
                    data: [{self.stats['migrated_files']}, {self.stats['pending_files']}],
                    backgroundColor: ['#28a745', '#ffc107']
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // Timeline Chart
        const timelineCtx = document.getElementById('timelineChart').getContext('2d');
        new Chart(timelineCtx, {{
            type: 'line',
            data: {{
                labels: {json.dumps([item['date'] for item in self.stats['migration_timeline']])},
                datasets: [{{
                    label: 'Files Migrated',
                    data: {json.dumps([item['count'] for item in self.stats['migration_timeline']])},
                    borderColor: '#007bff',
                    tension: 0.1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
    </script>
</body>
</html>"""
        
        return html_content
    
    def _generate_state_section(self):
        """Generate state progress section"""
        if not self.stats['by_state']:
            return ""
        
        rows = ""
        for state, data in sorted(self.stats['by_state'].items()):
            progress = (data['migrated'] / data['total'] * 100) if data['total'] > 0 else 0
            rows += f"""
                <tr>
                    <td>{state}</td>
                    <td>{data['total']:,}</td>
                    <td>{data['migrated']:,}</td>
                    <td>{data['pending']:,}</td>
                    <td>
                        <div class="progress" style="height: 20px;">
                            <div class="progress-bar bg-success" style="width: {progress:.1f}%">
                                {progress:.0f}%
                            </div>
                        </div>
                    </td>
                </tr>
            """
        
        return f"""
        <div class="row mb-5">
            <div class="col-12">
                <div class="stat-card">
                    <h3 class="h5 mb-4">City Pages by State</h3>
                    <div class="table-container">
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th>State</th>
                                    <th>Total</th>
                                    <th>Migrated</th>
                                    <th>Pending</th>
                                    <th>Progress</th>
                                </tr>
                            </thead>
                            <tbody>
                                {rows}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _generate_issues_section(self):
        """Generate issues section"""
        if not self.stats['issues']:
            return ""
        
        issue_rows = ""
        for issue in self.stats['issues'][:20]:  # Show first 20 issues
            if 'error' in issue:
                issue_rows += f"""
                    <tr>
                        <td>{issue['file']}</td>
                        <td><span class="badge bg-danger">Error</span></td>
                        <td>{issue['error']}</td>
                    </tr>
                """
            else:
                issue_rows += f"""
                    <tr>
                        <td>{issue['file']}</td>
                        <td><span class="badge bg-warning">Issues</span></td>
                        <td>{', '.join(issue['issues'])}</td>
                    </tr>
                """
        
        return f"""
        <div class="row mb-5">
            <div class="col-12">
                <div class="stat-card">
                    <h3 class="h5 mb-4">Issues Found ({len(self.stats['issues'])} total)</h3>
                    <div class="table-responsive">
                        <table class="table table-sm">
                            <thead>
                                <tr>
                                    <th>File</th>
                                    <th>Type</th>
                                    <th>Description</th>
                                </tr>
                            </thead>
                            <tbody>
                                {issue_rows}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _generate_type_rows(self):
        """Generate table rows for page types"""
        rows = ""
        for page_type, data in self.stats['by_type'].items():
            progress = (data['migrated'] / data['total'] * 100) if data['total'] > 0 else 0
            rows += f"""
                <tr>
                    <td>{page_type.replace('_', ' ').title()}</td>
                    <td>{data['total']:,}</td>
                    <td>{data['migrated']:,}</td>
                    <td>{data['pending']:,}</td>
                    <td>
                        <div class="progress" style="height: 20px;">
                            <div class="progress-bar bg-success" style="width: {progress:.1f}%">
                                {progress:.0f}%
                            </div>
                        </div>
                    </td>
                </tr>
            """
        return rows
    
    def save_reports(self, output_dir='.'):
        """Save both JSON and HTML reports"""
        # Save JSON report
        json_report = {
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats
        }
        
        json_path = os.path.join(output_dir, 'migration-report.json')
        with open(json_path, 'w') as f:
            json.dump(json_report, f, indent=2)
        
        # Save HTML report
        html_path = os.path.join(output_dir, 'migration-report.html')
        with open(html_path, 'w') as f:
            f.write(self.generate_html_report())
        
        print(f"\n✅ Reports saved:")
        print(f"  - JSON: {json_path}")
        print(f"  - HTML: {html_path}")
        
        # Print summary
        completion_rate = (self.stats['migrated_files'] / self.stats['total_html_files'] * 100) if self.stats['total_html_files'] > 0 else 0
        print(f"\n📊 Migration Summary:")
        print(f"  - Total Pages: {self.stats['total_html_files']:,}")
        print(f"  - Migrated: {self.stats['migrated_files']:,} ({completion_rate:.1f}%)")
        print(f"  - Pending: {self.stats['pending_files']:,}")
        print(f"  - Issues Found: {len(self.stats['issues'])}")

def main():
    parser = argparse.ArgumentParser(description='Generate UI migration report')
    parser.add_argument('path', nargs='?', default='.', 
                       help='Path to scan')
    parser.add_argument('--output', '-o', default='.', 
                       help='Output directory for reports')
    
    args = parser.parse_args()
    
    print('📊 Migration Report Generator')
    print('Scanning for migration status...\n')
    
    generator = MigrationReportGenerator()
    generator.scan_directory(args.path)
    generator.save_reports(args.output)

if __name__ == '__main__':
    main()