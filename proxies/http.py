import BaseHTTPServer

class HTTTProxy(BaseHTTPServer.BaseHTTPRequestHandler):
    html_hello_world = """
    <h1>Hello World!</h1>
    """
    def do_GET(self):
        path = self.path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(self.html_hello_world)
        request = path.split("/")
        self.wfile.write(request[1])
        self.wfile.write(request[2])
        
        
        
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(('', 8080), HTTTProxy)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
