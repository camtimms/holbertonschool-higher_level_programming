#!/usr/bin/python3
"""
Developing a simple API using Python
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Request_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check which endpoint was requested
        if self.path == '/':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # Send response body
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode('utf-8'))

        elif self.path == '/data':
            # Send JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Create JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            json_response = json.dumps(data)
            self.wfile.write(json_response.encode('utf-8'))

        elif self.path == '/status':
            # Send status response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "OK"
            self.wfile.write(message.encode('utf-8'))

        else:
            # Handle 404 - endpoint not found
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Endpoint not found"
            self.wfile.write(message.encode('utf-8'))

def run_server():
    # Server configuration
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Request_Handler)

    print("Starting server on http://localhost:8000")
    print("Press Ctrl+C to stop the server")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()