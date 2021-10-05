#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HTML_FILE = Path(__file__).resolve().parent / 'index.html'
with HTML_FILE.open() as f:
    HTML = f.read()



class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.connection.send(HTML.encode('ascii'))

    def do_POST(self):
        c_len = int(self.headers['Content-Length'])
        print(self.rfile.read(c_len).decode())


def main():
    with ThreadingHTTPServer(('', 8080), Handler) as srv:
        srv.serve_forever()


if __name__ == '__main__':
    main()
