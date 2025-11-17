import http.server
import socketserver
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(INDEX_FILE, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File Not Found")

PORT = 8080
print(f"Server running on http://0.0.0.0:{PORT}")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
