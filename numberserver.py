from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import socket

class NumberServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        
        # Try and open number file and read number
        try:
            f = open("number.txt", "r")
            number = int(f.read())
            f.close()
        except IOError, ValueError:
            # if we fail then just assume 1
            number = 1

        # send the number to the client
        self.wfile.write(str(number))
        
        # write incremented number back to file
        f = open("number.txt", "w")
        number = str(number+1)
        f.write(number)
        f.close()

    def do_HEAD(self):
        self._set_headers()

class HTTPServerV6(HTTPServer):
  address_family = socket.AF_INET6        
        
def run(server_class=HTTPServerV6, handler_class=NumberServer, port=80):
    server_address = ('::', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting number server...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
