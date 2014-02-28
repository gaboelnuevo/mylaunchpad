#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Recycle code for dynamic openbox pipe menu:
#This is no a part of the project code is only a example for recycle it

import os
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

    def getMenu(self):
       root = etree.parse(self.appsmenu)
       print etree.tostring(root, pretty_print=True, encoding='UTF-8')

menu = OBMenu()
menu.getMenu()
