# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import glob
import os
import csv
import datetime

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
    def do_GET(self):
        last_reading = get_temp_humidity()
        last_photo = get_last_photo()

        if self.path=="/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Live from 1405!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Time: {}</p><p>Temperature: {} C</p><p>Relative Humidity: {} %</p>".format(datetime.datetime.fromisoformat(last_reading[0]).strftime('%c'),*last_reading[1:]), "utf-8"))
            self.wfile.write(bytes("<table><tr><td><img src=\"{}\" alt=\"{}\" /></td></tr></table>".format(last_photo,last_photo), "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        try:
            send_reply = False
            is_binary = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                send_reply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                send_reply = True
                is_binary = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                send_reply = True
                is_binary = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                send_reply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                send_reply = True

            open_mode = 'rb' if is_binary == True else 'r'

            if send_reply == True:
                with open(os.curdir + os.sep + self.path, open_mode) as f:
                    print('trying to open',os.curdir+os.sep+self.path)
                    self.send_response(200)
                    self.send_header('Content-type', mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())
            return
        
        except IOError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
