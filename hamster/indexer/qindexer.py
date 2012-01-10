#!/usr/bin/env python

#from gevent import monkey; monkey.patch_socket()
from hamster.util.dbcloner import normalize

import sys
import re
import imdb
import json
from PySide.QtCore import QRunnable, QObject, QThreadPool, QDirIterator, Signal, QThread, Qt, QTimer
from PySide.QtGui import QApplication
from hamster.util.files import get_user_index, get_user_db
import hamster.util.log as L
import signal

# allow aborting via ctrl + c
signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerObject(QObject):
    finished = Signal(dict)
    finsig = Signal()

class Job(QRunnable): 
    def __init__(self, imdb_db, imdb_id, stopvar): 
        QRunnable.__init__(self) 
        self.imdb_id = imdb_id 
        self.imdb_db = imdb_db
        self.obj = WorkerObject()
        self.thread = stopvar

    def run(self): 
        if self.thread.stopvar:
            # threadpool already stopped - do nothing
            return

        L.d( "fetching %s ..." % self.imdb_id)
        movie = self.imdb_db.get_movie(self.imdb_id)
        nm = normalize(movie)
        nm['_id'] = str(self.imdb_id)

        self.obj.finished.emit(nm)

    def autoDelete(self):
        return True
        

class IndexWriter(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.index = get_user_index()
        self.db = get_user_db()
    def index_movie(self, movie):
        self.index.index_movie(movie)
        self.db.create_doc(json.dumps(movie), doc_id=movie["_id"])
        L.d("%s finished" % movie['title'])

class IndexThread (QThread):
    def __init__ (self, media_path, parent = None):
        QThread.__init__(self, parent)
        self.media_path = media_path

    def run(self):
        L.d("running")
        self.stopvar = False
        rex = re.compile(".*\[(\d{7})\]$")
        imdb_db = imdb.IMDb()
        db = get_user_db()
        tp = QThreadPool.globalInstance()
        writer = IndexWriter()
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
                    movie = db.get_doc(imdb_id)
                    if movie:
                        L.d("%s already in db - skipping" % imdb_id)
                    else:
                        j = Job(imdb_db, imdb_id, self) 
                        j.obj.finished.connect(writer.index_movie,
                                Qt.QueuedConnection)
                        tp.start(j) 
            except:
                pass
        print count
        self.exec_()
    
    def set_stopped(self):
        L.d("setting stopvar")
        self.stopvar = True
        QTimer.singleShot(10, self._shutdown)

    def _shutdown(self):
        tp = QThreadPool.globalInstance()
        L.d("waiting for threadpool to be done...")
        tp.waitForDone()
        self.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    tp = QThreadPool.globalInstance()
    tp.setMaxThreadCount(8) 

    t = IndexThread("/media/DATA/media/movies/")
    t.start()
    sys.exit(app.exec_())

