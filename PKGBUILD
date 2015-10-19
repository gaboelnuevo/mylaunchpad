# Maintainer: Gabriel Sabillon
# Contributors: Tsarev Nikita, LoranKey

# Set the following variable to true to use category icons instead of names
category_icons=false


pkgname=mylaunchpad-git
_pkgname_simple=mylaunchpad
pkgdesc="Eyecandy Full Screen launcher script for openbox and other stand-alone window managers"
pkgrel=1
pkgver=r78.57d57f5

pkgver() {
   cd "$srcdir/$_pkgname_simple"
   printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

arch=('any')
url="https://github.com/gaboelnuevo/mylaunchpad"
license=('GPL')
depends=('python2' 'python2-lxml' 'pygtk' 'cairo' 'python2-cairo' 'python2-imaging' 'gnome-menus2')
makedepends=('git')
optdepends=()
provides=('mylaunchpad')
md5sums=('SKIP')
backup=('etc/mylaunchpad.conf')

source=('mylaunchpad::git+http://github.com/gaboelnuevo/mylaunchpad')

package() {
    cd "$srcdir/$_pkgname_simple"
    if [ "$category_icons" = true ]; then
        git checkout category-icons
    fi
    python2 setup.py install --root ${pkgdir}
}
