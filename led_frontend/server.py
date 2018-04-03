import http.server
import socketserver
import os


PORT = 20000

Handler = http.server.SimpleHTTPRequestHandler

# Change directory to html folder
html_dir = os.path.join(os.path.dirname(__file__), 'www_data')
os.chdir(html_dir)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
