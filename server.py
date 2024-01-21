# Import the HTTP server class from the http.server module
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Specify the server address and port
host = "localhost"
port = 8000

# Create a handler for serving files
handler = SimpleHTTPRequestHandler

# Create the server
httpd = TCPServer((host, port), handler)

# Print a message indicating the server is running
print(f"Serving on {host}:{port}")

# Start the server
httpd.serve_forever()

#in this video i am going to tell
