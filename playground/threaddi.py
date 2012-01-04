import sys 
import os 
import time 

from PyQt4 import QtCore, QtGui 

class Job(QtCore.QRunnable): 
    def __init__(self, name): 
        QtCore.QRunnable.__init__(self) 
        self._name = name 

    def run(self): 
        time.sleep(3) 
        print self._name 


if __name__ == "__main__": 

    app = QtGui.QApplication(sys.argv) 

    QtCore.QThreadPool.globalInstance().setMaxThreadCount(5) 

    for i in range(5): 
        j = Job("Job-" + str(i)) 
        QtCore.QThreadPool.globalInstance().start(j, i) 

    app.exec_() 
