#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Recycle this code: example for dynamic openbox pipe menu:
# This is no a part of the project but is only a funny way for recycle this

#    HOW TO USE:
#    Edit your openbox menu.xml
#    Add a new pipe menu just adding this line:
#       <menu execute="~/.scripts/mylaunchpad-master/ob_pipe_menu.py default All" id="pipe-menu" label="Applications Menu"/>
#
#    *You can change the default menu with your favorite xdg-menu like xfce-applications or lxde-aplications
#    *You can change All with the ID of a specific category

      
import os, sys
import threading
from appsmenu import MenuCache

try:
    from lxml import etree
except:
    print "lxml missing, please install pyhton-lxml "


class OBMenu:
    def __init__(self):
        
        # Get Menu
        menu = MenuCache(AUTO_UPDATE=False, tag="openbox_pipe_menu", cache_dir = "openbox",  file_name = "openbox-xdg-menu-cache.xml")
        self.appsmenu = menu.getMenu()

        #update cache in the background
        t = threading.Thread(target=menu.updateCache())  
        t.start() 
        

    def getMenu(self, Category = "All"):
       root = etree.parse(self.appsmenu)
       if Category == "All":
           print etree.tostring(root, pretty_print=True, encoding='UTF-8')
       else:
           print '<?xml version="1.0" encoding="UTF-8"?>\n'
           print '<openbox_pipe_menu>\n'
           for item in root.xpath("/openbox_pipe_menu/menu[@id='"+Category+"']/item"):
               print etree.tostring(item, pretty_print=True, encoding='UTF-8')
           print '</openbox_pipe_menu>\n'
           
#main
menu = OBMenu()
if len(sys.argv) > 2:
    menu.getMenu(sys.argv[2])
else:
    menu.getMenu()
