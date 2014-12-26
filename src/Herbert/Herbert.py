'''
Created on 26.12.2014

@author: basti
'''
#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import PowerSocket
import Site
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")

PORT_NUMBER = 8000
HTML = Site.LoadIndex()

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        
        
        path = self.path.split("/")
        if len(path) == 4:            
            # Call Module path[1] and function path[2] with param path[3]
            ret = getattr(globals()[path[1]],path[2])(path[3])
            # make sure we change the url
            # HTTP/1.1 302 Found
            # Location: /articles/
            self.send_response(302) # accepted processing offline
            self.send_header('Location', "/")
            
        else :
            ret = " "
            self.send_response(200)
        
        
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        
        self.wfile.write(HTML.replace("%msg%", ret))
        
        return


try:
    PowerSocket.Setup()
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer((Config.get("System", "bindto"), PORT_NUMBER), myHandler)
    print 'Started httpserver on ', server.server_address
    
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
    PowerSocket.Unset()