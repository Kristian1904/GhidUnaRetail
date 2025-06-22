import http.server
import socketserver
import socket
import os

# Define the port to serve the directory
PORT = 8000

# Automatically use the current directory as the root directory to be served
directory_to_serve = os.getcwd()

# Custom handler to serve the specified directory
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory_to_serve, **kwargs)

# Function to get the local IP address
def get_local_ip():
    try:
        # Connect to an external IP to get the local network IP (without sending data)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"  # Fallback to localhost if unable to determine IP

# Set up and start the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    local_ip = get_local_ip()
    print(f"Serving directory '{directory_to_serve}' on {local_ip}:{PORT}")
    print(f"Access the directory on other devices: http://{local_ip}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()
