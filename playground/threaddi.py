import sys 
import time 

from PyQt4.QtCore import QRunnable, QObject, pyqtSignal, QThreadPool
from PyQt4.QtGui import QApplication

class WorkerObject(QObject):
    finished = pyqtSignal(str)

class Job(QRunnable): 
    def __init__(self, name): 
        QRunnable.__init__(self) 
        self._name = name 
        self.obj = WorkerObject()

    def run(self): 
        time.sleep(1) 
        self.obj.finished.emit(self._name)
        print "ok"

class Printer(QObject):
    def slotPrint(self, name):
        print name, "finished"


if __name__ == "__main__": 

    app = QApplication(sys.argv) 

    tp = QThreadPool.globalInstance()
    tp.setMaxThreadCount(5) 

    printer = Printer()

    for i in range(6): 
        j = Job("Job-" + str(i)) 
        print j.obj.finished.connect(printer.slotPrint)
        tp.start(j, i) 

    print "waiting..."
    #tp.waitForDone()
    print "done"
    #app.quit()
    print "bye"
    #sys.exit()

    sys.exit(app.exec_())
