#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.handle_root()
        elif self.path == "/data":
            self.handle_data()
        elif self.path == "/status":
            self.handle_status()
        elif self.path == "/info":
            self.handle_info()
        else:
            self.handle_not_found()

    def handle_root(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(data).encode())

    def handle_status(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        status = {"status": "OK"}
        self.wfile.write(json.dumps(status).encode())

    def handle_info(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"}
        self.wfile.write(json.dumps(info).encode())

    def handle_not_found(self):
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        error_message = {"error": "Endpoint not found"}
        self.wfile.write(json.dumps(error_message).encode())


def run(
        server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
