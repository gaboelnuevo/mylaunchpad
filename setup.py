#!/usr/bin/python

import os, sys, glob, fnmatch
try: 
    from distutils.core import setup, Extension
    import distutils.command.install_data
    
except:
    print "DistUtils / SetupTools are required"
    sys.exit(1)

try:
    from DistUtilsExtra.command import *
except:
    print "DistUtils Extras is required"
    sys.exit(1)
    
          
setup(name="Launcher",  
          version="0.3",  
          description="Eyecandy Full Screen launcher script for openbox and other stand-alone window managers.",  
          author="Gabriel Sabillon",  
          author_email="gabrielsabillon@gmail.com",  
          url="https://github.com/gaboelnuevo/mylaunchpad",  
          license="GPL",  
          scripts=["data/mylaunchpad"],  
          packages=["appsmenu"], 
          data_files = [('/usr/share/icons', glob.glob('data/icons/*')),
                 ('/usr/share/applications', glob.glob('data/mylaunchpad-menu.desktop')), 
                 ('/etc', glob.glob('data/mylaunchpad.conf'))],
    
          cmdclass = { 'build' : build_extra.build_extra,
                       'build_i18n' :  build_i18n.build_i18n },

)  
