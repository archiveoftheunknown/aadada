#!/usr/bin/env python3
import http.server
import socketserver
import os

class AlwaysBlockedHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If accessing any path other than root, show redirect page then redirect
        if self.path != '/' and self.path != '/index.html':
            # Send a brief HTML page that redirects using JavaScript
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            
            redirect_html = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mengarahkan...</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .redirect-box {
            text-align: center;
            animation: fadeIn 0.3s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid #ddd;
            border-top: 3px solid #991b1b;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin: 0 auto 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        p {
            color: #555;
            font-size: 14px;
            margin: 10px 0;
        }
        .url-text {
            color: #991b1b;
            font-weight: 600;
            font-size: 12px;
        }
    </style>
    <script>
        // Redirect after a brief moment to show the redirect is happening
        setTimeout(function() {
            window.location.href = '/';
        }, 2000);
    </script>
</head>
<body>
    <div class="redirect-box">
        <div class="spinner"></div>
        <p>Mengarahkan ke halaman utama...</p>
        <p class="url-text">layanan.komdigi.go.id</p>
    </div>
</body>
</html>'''
            
            self.wfile.write(redirect_html.encode())
            return
        
        # For root path, serve the index.html
        self.path = '/index.html'
        return super().do_GET()
    
    def do_HEAD(self):
        # Handle HEAD requests with redirect
        if self.path != '/' and self.path != '/index.html':
            self.send_response(301)
            self.send_header('Location', '/')
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()
            return
        
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