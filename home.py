from http.server import HTTPServer,BaseHTTPRequestHandler ,HTTPServer
import time


HOST ="127.0.0.1"

#define the class that handels requests
class Serv(BaseHTTPRequestHandler):

    #Get is for handeling requests
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type" , "text/html")
        self.end_headers()

        #what the client sees on the web page
        self.wfile.write(bytes("<html><body><h2>HELLO WORLD!!!</h2></body></htlm>","utf-8"))


    #Handls Post requects
    def do_POST(self):
        self.send_response(200)
        self.send_header("content-type" , "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8 "))

#set up and start the server
PORT = 9999
server = HTTPServer((HOST, PORT), Serv)
  
print("server is running . . .")


try:
    server.serve_forever()
except KeyboardInterrupt:
    pass


server.server_close() 

print("server is donn !!:D")