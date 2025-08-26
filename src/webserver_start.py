#!/usr/bin/env python3

import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000
root_path = Path(__file__).parent.parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=root_path, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Server running at: {url}")
    webbrowser.open(url)
    httpd.serve_forever()