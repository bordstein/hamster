""" Qt - gevent event loop integration using a Qt IDLE timer
"""

import sys, itertools

from PyQt4 import QtCore, QtGui

import gevent

# Limit the IDLE handler's frequency while still allow for gevent
# to trigger a microthread anytime
IDLE_PERIOD = 0.01

class MainWindow(QtGui.QMainWindow):

    def __init__(self, application):

        QtGui.QMainWindow.__init__(self)

        self.application = application

        self.counter = itertools.count()

        self.resize(400, 100)
        self.setWindowTitle(u'Counting: -')

        self.button = QtGui.QPushButton(self)
        self.button.setText(u'Reset')
        self.button.clicked.connect(self.reset_counter)

        self.show()

    def counter_loop(self):

        while self.isVisible():
            self.setWindowTitle(u'Counting: %d' % self.counter.next())
            gevent.sleep(0.1)

    def reset_counter(self):

        self.counter = itertools.count()

    def run_application(self):

        # IDLE timer: on_idle is called whenever no Qt events left for processing
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_idle)
        self.timer.start(0)

        # Start counter
        gevent.spawn(self.counter_loop)

        # Start you application normally, but ensure that you stop the timer
        try:
            self.application.exec_()
        finally:
            self.timer.stop()

    def on_idle(self):

        # Cooperative yield, allow gevent to monitor file handles via libevent
        gevent.sleep(IDLE_PERIOD)

def main():

    application = QtGui.QApplication(sys.argv)
    main_window = MainWindow(application)
    main_window.run_application()

if __name__ == '__main__':
    main()
