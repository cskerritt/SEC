#!/usr/bin/env python3
"""
Simple development server for reviewing the website
"""

import http.server
import socketserver
import os
import webbrowser
from datetime import datetime

PORT = 8080
DIRECTORY = "_site"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging with timestamp
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {format % args}")

def start_server():
    """Start the development server"""
    
    # Check if _site directory exists
    if not os.path.exists(DIRECTORY):
        print(f"❌ Error: {DIRECTORY} directory not found!")
        print("Run 'bundle exec jekyll build' first to generate the site.")
        return
    
    print(f"""
╔════════════════════════════════════════════════════════════╗
║           SKERRITT ECONOMICS DEVELOPMENT SERVER            ║
╚════════════════════════════════════════════════════════════╝

Starting server on http://localhost:{PORT}
Serving files from: {os.path.abspath(DIRECTORY)}

Press Ctrl+C to stop the server.

Key pages to review:
- http://localhost:{PORT}/ (Homepage)
- http://localhost:{PORT}/services/ (Services)
- http://localhost:{PORT}/locations/cities/ (City Pages Directory)
- http://localhost:{PORT}/locations/cities/providence-ri-forensic-economist.html
- http://localhost:{PORT}/locations/cities/los-angeles-ca-business-valuation-analyst.html
- http://localhost:{PORT}/ui-migration-preview.html (Migration Preview)

""")
    
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 Server running at http://localhost:{PORT}/")
            print("\nOpen your browser to review the site.")
            print("All UI enhancements are applied to the city pages.\n")
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}/')
            except:
                pass
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped.")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ Port {PORT} is already in use.")
            print(f"Try: python3 start-dev-server.py --port {PORT + 1}")
        else:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    import sys
    
    # Simple port override
    if len(sys.argv) > 2 and sys.argv[1] == "--port":
        try:
            PORT = int(sys.argv[2])
        except:
            print("Invalid port number")
            sys.exit(1)
    
    start_server()