
# 2. Make executable
chmod +x server.py

# 3. Run server
python3 server.py


FOR CLOUDFLARE LINK 

# Ubuntu/Debian
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# OR Mac
brew install cloudflared

# OR Windows (PowerShell)
winget install Cloudflare.cloudflared

#login here
cloudflared tunnel login

#host 
# Terminal 2 - Create tunnel
cloudflared tunnel create photo-phish

# Run tunnel (copies public URL automatically!)
cloudflared tunnel --url http://localhost:8080
