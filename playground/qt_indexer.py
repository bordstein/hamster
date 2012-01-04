#!/usr/bin/env python

#from gevent import monkey; monkey.patch_socket()
from dbcloner import normalize

import u1db
import sys
import re
import imdb
import json
from whoosh_action.index import HamsterIndex
from PySide.QtCore import QRunnable, QObject, QThreadPool, QDirIterator, Signal, QThread
from PySide.QtGui import QApplication
import signal

# allow aborting via ctrl + c
signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerObject(QObject):
    finished = Signal(dict)
    finsig = Signal()

class Job(QRunnable): 
    def __init__(self, imdb_db, imdb_id): 
        QRunnable.__init__(self) 
        self.imdb_id = imdb_id 
        self.imdb_db = imdb_db
        self.obj = WorkerObject()

    def run(self): 
        print "fetching", self.imdb_id, "..."
        movie = self.imdb_db.get_movie(self.imdb_id)
        nm = normalize(movie)
        nm['_id'] = str(self.imdb_id)

        self.obj.finished.emit(nm)

    def autoDelete(self):
        return True
        

class Printer(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.index = HamsterIndex("/tmp/hamster.idx")
        self.db = u1db.open("/tmp/out.db", create=True)
    def slotPrint(self, movie):
        self.index.index_movie(movie)
        self.db.create_doc(json.dumps(movie), doc_id=movie["_id"])
        print movie['title'], "finished"
    def printFin(self):
        print "finished!"

class IndexThread (QThread):
    def __init__ (self, media_path, parent = None):
        QThread.__init__(self, parent)
        self.media_path = media_path

    def run(self):
        print "running"
        rex = re.compile(".*\[(\d{7})\]$")
        imdb_db = imdb.IMDb()
        index = HamsterIndex("/tmp/hamster.idx")
        tp = QThreadPool.globalInstance()
        printer = Printer()
        count = 0

        it = QDirIterator(self.media_path, QDirIterator.Subdirectories)
        while it.hasNext():
            dir = it.next()
            try:
                directory = unicode(dir)
                match = rex.match(directory)
                if match:
                    count += 1
                    imdb_id = match.group(1)
                    j = Job(imdb_db, imdb_id) 
                    j.obj.finished.connect(printer.slotPrint)
                    tp.start(j) 
            except:
                pass
        print count
        self.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    tp = QThreadPool.globalInstance()
    tp.setMaxThreadCount(8) 

    t = IndexThread("/media/DATA/media/movies/")
    t.finished.connect(app.quit)
    print "started"
    t.start()
    sys.exit(app.exec_())

