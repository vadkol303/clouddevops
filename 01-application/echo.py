import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
import dotenv

dotenv.load_dotenv()

class Echo(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        author = os.environ.get('AUTHOR', 'Неизвестный автор')
        
        response = f"Имя хоста: {hostname}\nIP адрес: {ip_address}\nАвтор: {author}"
        self.wfile.write(response.encode('utf-8'))

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Echo)
    print('Сервер запущен на порту 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run() 