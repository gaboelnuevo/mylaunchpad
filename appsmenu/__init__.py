#!/usr/bin/env python
import gmenu, re, sys, os
from xml.sax.saxutils import escape

HOME_PATH = os.path.realpath(os.path.expanduser('~'))
CACHE_PATH = ".cache/mylaunchpad"
MENU_CACHE = "xdg-menu-cache.xml"

class MenuCache:
    def __init__(self):

       self.file_name = HOME_PATH + '/' + CACHE_PATH + '/' + MENU_CACHE

       if len(sys.argv) > 1:
          menu = sys.argv[1] + '.menu'
       else:
          menu = 'applications.menu'
       
       # write menu cache
       self.createFile(self.file_name)
       self.file=open(self.file_name,'a')
       self.file.write( '<?xml version="1.0" encoding="UTF-8"?>\n')
       self.file.write( '<xdg-menu>\n')
       map(self.walk_menu, gmenu.lookup_tree(menu).root.get_contents())
       self.file.write('</xdg-menu>\n')
       self.file.close()
    def getMenu(self):
        print HOME_PATH + '/' + CACHE_PATH + '/' + MENU_CACHE
	return  HOME_PATH + '/' + CACHE_PATH + '/' + MENU_CACHE
    def walk_menu(self, entry):
       if entry.get_type() == gmenu.TYPE_DIRECTORY:
          self.file.write( '<menu id="%s" label="%s">\n' \
             % (escape(entry.menu_id), escape(entry.get_name())) )
          map(self.walk_menu, entry.get_contents())
          self.file.write('</menu>\n' )
       elif entry.get_type() == gmenu.TYPE_ENTRY and not entry.is_excluded:
          self.file.write( '<item label="%s" icon="%s">\n' % (escape(entry.get_name()), escape(entry.get_icon())) )
          command = re.sub(' [^ ]*%[fFuUdDnNickvm]', '', entry.get_exec())
          if entry.launch_in_terminal:
             command = 'xterm -title "%s" -e %s' % \
                (entry.get_name(), command)
          self.file.write( '<action name="Execute">\n' + \
             '<command>%s</command></action>\n' % escape(command) )
          self.file.write( '</item>\n' )

    def createFile(self, file_name):
       if not os.path.exists(HOME_PATH+'/'+CACHE_PATH):
           os.system('mkdir %s' %HOME_PATH+'/'+CACHE_PATH)
       file=open(file_name,'w')
       file.close()
