'''
Created on 26.12.2014

@author: basti
'''
import ConfigParser
    
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

def LoadIndex():
    html = open("index.html", 'r').read()

    for s in Config.sections():
        for f in Config.options(s):
            html = html.replace("%"+f+"%",Config.get(s, f))
   
    return html

