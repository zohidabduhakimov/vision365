"""
====================================================================
VISION 365 — MULTITHREADED MOBILE LOCAL PREVIEW & PWA TESTING SERVER
====================================================================
"""

import http.server
import socket
import socketserver
import os
import sys

PORT = 8888
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def guess_type(self, path):
        if path.endswith('.json') or path.endswith('manifest.json'):
            return 'application/manifest+json'
        if path.endswith('.js') or path.endswith('sw.js'):
            return 'application/javascript'
        return super().guess_type(path)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

def main():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:{PORT}"

    print("=" * 65, flush=True)
    print(" 🚀 VISION 365 — MOBIL ILOVA SERVERI ISHLAMOQDA!", flush=True)
    print("=" * 65, flush=True)
    print(f"\n 📱 TELEFONDA OCHISH UCHUN MANZIL:", flush=True)
    print(f"    👉  {url}", flush=True)
    print(f"    👉  http://localhost:{PORT} (Kompyuterda)", flush=True)
    print("-" * 65, flush=True)
    print(f" Papka: {WEB_DIR}", flush=True)
    print("=" * 65, flush=True)

    with ThreadedHTTPServer(("0.0.0.0", PORT), CustomHandler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    main()
