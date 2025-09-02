#!/usr/bin/env python3
import http.server
import socketserver
import os

class AlwaysBlockedHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always serve the index.html file regardless of the requested path
        # This makes it appear that the entire domain is blocked
        self.path = '/index.html'
        return super().do_GET()
    
    def do_HEAD(self):
        # Handle HEAD requests the same way
        self.path = '/index.html'
        return super().do_HEAD()
    
    def end_headers(self):
        # Add security headers to make it more official
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

PORT = 5000
Handler = AlwaysBlockedHandler

# Allow port reuse to avoid "Address already in use" errors
class ReusePortServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusePortServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server running on port {PORT}")
    print("All paths will show the government blocking page")
    httpd.serve_forever()