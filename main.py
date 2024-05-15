import http.server
import json
from order_service import create_order

class OrderHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/orders":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)
            components = data.get('components')

            if not components:
                self.send_error(400, "Missing 'components' in request")
                return

            order = create_order(components)
            if order:
                self.send_response(201)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(order).encode())
            else:
                self.send_error(400, "Invalid order")
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, OrderHandler)
    print(f"Serving on http://localhost:{8000}")
    httpd.serve_forever()