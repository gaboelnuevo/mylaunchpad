MyLaunchpad
============

Eyecandy Full Screen launcher script for openbox and other stand-alone window managers.

Run with python and gtk/cairo

Author: Gabriel Sabillon

Contributors:

-Tsarev Nikita

-LoranKey

Credits:
  Based in oblogout interface code by Andrew Williams and Archbang script for openbox pipe menu


*Dependences:
  python-gmenu
  pygtk
  python-lxml
  python-cairo
  python-imaging
  python-distutils-extra

How to install:

	#python setup.py install

How to RUN:

 	 $mylaunchpad default

  or simply:
	
	 $mylaunchpad


  By default the app works with xdg-menu  «applications.menu» of gnome-menus
  
  How to Change xdg-menu (3 ways)
  
	You can link another xdg-menu for example lxde-menu with ln command:

		$sudo ln -s /etc/xdg/menus/lxde-applications.menu /etc/xdg/menus/applications.menu
	
	Edit your config file found in /etc/mylaunchpad.conf
	
	Add xdg-menu in [options]
	
		# Use custom menu like xfce-applications or lxde-applications
		xdg-menu = xfce-applications
		
	Or You can change the default menu with your favorite xdg-menu like xfce-applications or lxde-aplications
	just send another xdg-menu like a argument simple run:
  
  
    $mylaunchpad.py lxde-applications
  

How to add launcher to panel(tint2):
	If your panel is tint2 you only need add a line in your config file:
	
		launcher_item_app = /usr/share/applications/mylaunchpad-menu.desktop

	For light color panel you can edit the desktop file and change the icon to dark changing this line: 
		Icon=mylaunchpad-menu.png 
	whith:
		Icon=mylaunchpad-menu-dark.png 
		 
