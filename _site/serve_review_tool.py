#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import threading
import time
from pathlib import Path

def start_server():
    os.chdir(Path(__file__).resolve().parent)
    PORT = 8000
    
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', '*')
            super().end_headers()
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"Review tool: http://localhost:{PORT}/city-pages-review-server.html")
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(1)
            webbrowser.open(f'http://localhost:{PORT}/city-pages-review-server.html')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    start_server()