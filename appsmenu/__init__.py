#!/usr/bin/python
# -*- coding: utf-8 -*-
# based in archbang script

import re
import sys
import os
from xml.sax.saxutils import escape

try:
    import gmenu
except:
    print 'gmenu missing, please install python-gmenu '

MENU_CACHE_FILE = 'xdg-menu-cache.xml'
CACHE_DIR = 'mylaunchpad'


class MenuCache:

    def __init__(
        self,
        tag='xdg-menu',
        AUTO_UPDATE=True,
        cache_dir=CACHE_DIR,
        file_name=MENU_CACHE_FILE,
        xdg_menu='default',
        ):
        self.tag = tag
        home_path = os.path.realpath(os.path.expanduser('~'))
        self.cache_dir_path = home_path + '/' + '.cache/' + cache_dir

        self.xdg_menu = xdg_menu

        self.file_path = self.cache_dir_path + '/' + file_name
        if not os.path.exists(self.file_path) or AUTO_UPDATE == True:
            self.updateCache()

    def updateCache(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == 'default':
                menu = 'applications.menu'
            else:
                menu = sys.argv[1] + '.menu'
        else:
            if self.xdg_menu == 'default':
                menu = 'applications.menu'
            else:
                menu = self.xdg_menu + '.menu'

       # # xdg-menu

        if not os.path.exists('/etc/xdg/menus/' + menu):
            print '/etc/xdg/menus/' + menu + ' Not found!'

       # write menu cache

        self.createFile(self.file_path)
        self.file = open(self.file_path, 'a')
        self.file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        self.file.write('<' + self.tag + '>\n')
        try:
            map(self.walk_menu,
                gmenu.lookup_tree(menu).root.get_contents())
        except:
            print 'ocurrio un problema'
        self.file.write('</' + self.tag + '>\n')
        self.file.close()

    def getMenu(self):

        # print self.file_path

        return self.file_path

    def walk_menu(self, entry):
        if entry.get_type() == gmenu.TYPE_DIRECTORY:
            self.file.write('<menu id="%s" label="%s" icon="%s">\n'
                            % (escape(entry.menu_id),
                            escape(entry.get_name()),
                            escape(entry.get_icon())))
            map(self.walk_menu, entry.get_contents())
            self.file.write('</menu>\n')
        elif entry.get_type() == gmenu.TYPE_ENTRY \
            and not entry.is_excluded:
            try:
                self.file.write('<item label="%s" icon="%s">\n'
                                % (escape(entry.get_name()),
                                escape(entry.get_icon())))
                command = re.sub(' [^ ]*%[fFuUdDnNickvm]', '',
                                 entry.get_exec())
                if entry.launch_in_terminal:
                    command = 'xterm -title "%s" -e %s' \
                        % (entry.get_name(), command)
                self.file.write('<action name="Execute">\n'
                                + '<command>%s</command></action>\n'
                                % escape(command))
                self.file.write('</item>\n')
            except:
                pass

          #    print "no se pudo cargar el item " + entry.get_name()

    def createFile(self, file_path):
        if not os.path.exists(self.cache_dir_path):
            os.system('mkdir %s' % self.cache_dir_path)
        file = open(file_path, 'w')
        file.close()
