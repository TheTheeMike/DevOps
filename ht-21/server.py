from http.server import BaseHTTPRequestHandler as BaseHTTPR, HTTPServer as HTTP
import os

class MyServer(BaseHTTPR):
    def do_GET(self):
        message = "Hello, you've connected!\n"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))

        log_file_path = '/app/access_log.txt'
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"GET request received from {self.client_address[0]}\n")

if __name__ == '__main__':
    server_address = ('', 80)
    httpd = HTTP(server_address, MyServer)
    print('Server is running on port 80')
    httpd.serve_forever()
