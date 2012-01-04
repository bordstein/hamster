#!/usr/bin/env python

#from gevent import monkey; monkey.patch_socket()
from dbcloner import normalize

import u1db
import sys
import re
import imdb
import json
from whoosh_action.index import HamsterIndex
from PySide.QtCore import QRunnable, QObject, QThreadPool, QDirIterator, Signal
from PySide.QtGui import QApplication
import signal

# allow aborting via ctrl + c
signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerObject(QObject):
    finished = Signal(dict)
    finsig = Signal()

class Job(QRunnable): 
    def __init__(self, imdb_id): 
        QRunnable.__init__(self) 
        self.imdb_id = imdb_id 
        self.obj = WorkerObject()

    def run(self): 
        print "fetching", self.imdb_id, "..."
        movie = imdb_db.get_movie(self.imdb_id)
        nm = normalize(movie)
        #db.create_doc(json.dumps(nm), doc_id=imdb_id)
        nm['_id'] = str(self.imdb_id)
        #db.save(nm)
        #index.index_movie(nm)
        #movie_json = json.dumps(nm)
        self.obj.finished.emit(nm)
        #self.obj.finsig.emit()
        #m.index(nm)

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

def cb_dir(directory):
    match = rex.match(directory)
    if match:
        imdb_id = match.group(1)
        j = Job(imdb_id) 
        j.obj.finished.connect(printer.slotPrint)
        #j.obj.finsig.connect(printer.printFin)
        tp.start(j) 

rex = re.compile(".*\[(\d{7})\]$")
imdb_db = imdb.IMDb()
index = HamsterIndex("/tmp/hamster.idx")

app = QApplication(sys.argv) 

tp = QThreadPool.globalInstance()
tp.setMaxThreadCount(6) 

printer = Printer()

media_path = "/media/DATA/media/movies/"
it = QDirIterator(media_path, QDirIterator.Subdirectories)
while it.hasNext():
    dir = it.next()
    try:
        dir = unicode(dir)
        cb_dir(dir)
    except:
        pass

#os.path.walk("/media/DATA/media/movies/", counter, "secret message")
#print count
sys.exit(app.exec_())
