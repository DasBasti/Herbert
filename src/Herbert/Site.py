'''
Created on 26.12.2014

@author: basti
'''
import ConfigParser
import importlib

    
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

def LoadIndex():
    html = open("index.html", 'r').read()
    menu = ""
    snipet = ""
    
    for index, section in enumerate(Config.sections()):
        #add menu item
        menu += "<li class=\"active\"><a href=\"#tab"+section+"\">"+Config.get(section, 'name')+"</a></li>"
        #add code to snipets
        snipet += "<div id=\"tab"+section+"\" class=\"tab"
        if index == 0: 
            snipet += " active"
        snipet += "\">"
       
        for index, field in enumerate(Config.options(section)):
            # call CreateLink function of module to poulate section part
            if field != "name":
                try:
                    snipet += getattr(importlib.import_module(section),"CreateLink")(index, Config.get(section, field), field)
                except:
                    snipet += "no config method found! "
                    break

        try:
            snipet += getattr(importlib.import_module(section),"CreateText")()
        except:
            pass

        snipet += " </div>"
    # add menu to html
    html = html.replace("%menu%", menu)
    # add body content
    html = html.replace("%content%", snipet)
   
    return html

