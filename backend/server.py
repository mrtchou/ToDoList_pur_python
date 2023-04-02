import http.server
import socketserver
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Set the directory to the "frontend" folder
os.chdir("../frontend")

# Override the default SimpleHTTPRequestHandler to serve index.html by default
class MyHttpRequestHandler(Handler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start the server with the custom handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
