import BaseHTTPServer
from proxylistener import ProxyListener

class ProxyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    listener = ProxyListener()
    
    def do_GET(self):
        path     = self.path
        response = self.listener.from_proxy(path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response)
        

class HTTTProxy():
    def listen(self,port,listener):
        ProxyHandler.listener = listener
        httpd = BaseHTTPServer.HTTPServer(('', port), ProxyHandler)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
            
        
if __name__ == "__main__":
    httpd = BaseHTTPServer.HTTPServer(('', 8080), HTTTProxy)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
