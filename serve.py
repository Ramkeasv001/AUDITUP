#!/usr/bin/env python3
"""ADITUP local server — serves the PWA over http://localhost so the
service worker and 'Install app' prompt work. (PWAs cannot run from a
file:// path.) Requires Python 3; no other dependencies.

Usage:
    python3 serve.py            # serves on http://localhost:8000
    python3 serve.py 8080       # custom port
"""
import http.server
import socketserver
import sys
import webbrowser
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # correct MIME for the manifest, and no-cache so updates show immediately
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".webmanifest"):
            return "application/manifest+json"
        return super().guess_type(path)

    def log_message(self, *args):
        pass  # quiet


class Server(socketserver.TCPServer):
    allow_reuse_address = True


def run(port):
    try:
        return Server(("", port), Handler)
    except OSError:
        return None


httpd = run(PORT)
if httpd is None:
    # port busy — try the next few
    for alt in range(PORT + 1, PORT + 11):
        httpd = run(alt)
        if httpd:
            PORT = alt
            break
if httpd is None:
    print(f"Could not bind to port {PORT} (or the next 10). Close the other "
          f"server or pass a free port: python3 serve.py 8123")
    sys.exit(1)

with httpd:
    url = f"http://localhost:{PORT}/index.html"
    print("\n  ADITUP is running at:  " + url)
    print("  Open that URL, then use your browser's 'Install app' option.")
    print("  Press Ctrl+C to stop.\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.")
