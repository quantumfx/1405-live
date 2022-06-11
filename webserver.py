# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import glob
import os
import csv

host_name = "localhost"
server_port = 8000

photo_dir = 'photos/'
data_file = 'temp_humidity.csv'

def get_last_photo(photo_dir = photo_dir):
    files = glob.glob(photo_dir+'*')
    files.sort(key = os.path.getmtime)
    photo = files[-1]
    return photo

def get_temp_humidity(file = data_file):
    with open(data_file, 'r') as f:
        reader = csv.reader(f)
        last_reading = list(reader)[-1]
    return last_reading

class MyServer(BaseHTTPRequestHandler):
    extensions_map={
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js':	'application/x-javascript',
        '': 'application/octet-stream', # Default
    }

    def do_GET(self):
        last_reading = get_temp_humidity()
        last_photo = get_last_photo()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Live from 1405!</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Time: {}<br>Temperature: {}C<br>Relative Humidity: {}</p>".format(*last_reading), "utf-8"))
        self.wfile.write(bytes("<table><tr><td><img src=\"{}\" alt=\"{}\" /></td></tr></table>".format(last_photo,last_photo), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
