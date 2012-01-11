#############################################################################
##  Hamster - Nice and friendly movie collection manager
##  Copyright (C) 2012 Christoph Meinhart, Michael Seiwald
##  
##  This file is part of Hamster.
##  
##  Hamster is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License along
##  with this program; if not, write to the Free Software Foundation, Inc.,
##  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
## 
#############################################################################

from distutils.core import setup

INSTALL_REQUIRES = ['u1db', 'whoosh', 'imdbpy']

PYSIDE_URL = 'http://developer.qt.nokia.com/wiki/PySideDownloads'

PYSIDE_WARNING = '''
\nWARNING: hamster requires PySide to be installed\n
Please install PySide from %s
                 ''' % PYSIDE_URL

CLASSIFIERS = """Development Status :: 2 - Pre-Alpha
        Intended Audience :: End Users/Desktop
        License :: OSI Approved :: GNU General Public License (GPL)
        Programming Language :: Python
        Topic :: Multimedia :: Video
        Operating System :: Microsoft :: Windows
        Operating System :: MacOS :: MacOS X
        Operating System :: Unix"""

try:
    __import__('PySide')
except ImportError:
    print(PYSIDE_WARNING)

setup(
    name='hamster',
    maintainer='hamster dev group',
    maintainer_email="hamster@nurio.at",
    version='0.1dev',
    packages=['moviehamster'],
    license='GPLv2',
    platforms=['any'],
    description='Hamster - Nice and friendly movie collection manager',
    long_description=open('README.md').read(),
    url='https://github.com/nurio/hamster',
    download_url='https://github.com/nurio/hamster',
    classifiers = filter(None, CLASSIFIERS.split("\n")),
    install_requires=INSTALL_REQUIRES,
    scripts=['bin/hamster']
)
