# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys
import gevent

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from qtgui import Ui_MainWindow

IDLE_PERIOD = 0.01

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

def mainloop(app):
    while True:
        app.processEvents()
        while app.hasPendingEvents():
            app.processEvents()
            gevent.sleep()
        gevent.sleep(IDLE_PERIOD) # don't appear to get here but cooperate again

def testprint():
    print 'this is running'
    gevent.spawn_later(1, testprint)

def main():
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    #sys.exit(app.exec_())
    gevent.joinall([gevent.spawn(testprint), gevent.spawn(mainloop, app)])
    print 'done'
    

if __name__ == "__main__":
    main()
    
