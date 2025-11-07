# Network Testing
ping google.com                         # Test connectivity
ping -c 4 google.com                    # Ping 4 times and stop
traceroute google.com                   # Trace network path
nslookup google.com                     # DNS lookup
dig google.com                          # Detailed DNS information

# HTTP Requests
curl -I https://api.example.com         # HTTP HEAD request
curl -s https://api.example.com         # Silent mode (no progress bar)
curl -o output.txt https://url          # Download to file
curl -X POST -d "data" https://url      # POST request
wget https://example.com/file.zip       # Download file
wget -r -p -k https://example.com       # Download entire website

# SSH and Remote Access
ssh user@server.com                     # Connect to remote server
ssh -p 2222 user@server.com             # Connect to custom port
ssh -i keyfile.pem user@server.com      # Connect with private key
scp file.txt user@server:/path/         # Copy file to remote server
scp -r directory/ user@server:/path/    # Copy directory recursively

# Port and Service
netstat -tulpn                          # Show listening ports
ss -tulpn                               # Modern alternative
lsof -i :80                             # Process using port 80
lsof -i TCP                             # All TCP connections
telnet server.com 80                    # Test port connectivity
nc -zv server.com 80                    # Netcat port test
