#!/usr/bin/env python

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

from moviehamster.hamsterdb.util import normalize

import sys
import re
import imdb
from PySide.QtCore import QRunnable, QObject, QThreadPool, QDirIterator, Signal, QThread, Qt, QTimer
from PySide.QtGui import QApplication
from moviehamster.hamsterdb.hamsterdb import HamsterDB
from downloader import DownloadManager
import moviehamster.log as L
import signal

# allow aborting via ctrl + c
signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerObject(QObject):
    finished = Signal(dict, str)
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

        self.obj.finished.emit(nm, str(self.imdb_id))

    def autoDelete(self):
        return True
        

class IndexWriter(QObject):
    def __init__(self, user, index_path, u1db_path):
        QObject.__init__(self)
        self.db = HamsterDB(user, index_path, u1db_path)
        self.buffer = {}
        self.downloader = DownloadManager()
        self.downloader.dl_finished.connect(self._download_success)
        self.downloader.dl_failed.connect(self._download_failed)

    def _save_to_db(self, imdb_id):
        movie = self.buffer.pop(imdb_id)
        self.db.save_movie(movie, imdb_id)
        L.d("%s finished" % movie['title'])

    def _download_success(self, imdb_id, base64_image):
        movie = self.buffer[imdb_id]
        movie['_cover_'] = base64_image
        self._save_to_db(imdb_id)

    def _download_failed(self, imdb_id):
        L.w("downloading cover for %s failed" % imdb_id)
        self._save_to_db(imdb_id)

    def index_movie(self, movie, imdb_id):
        self.buffer[imdb_id] = movie
        url = movie.get('cover url', None)
        if url:
            L.d("downloading cover from %s.." % url)
            self.downloader.download_cover(imdb_id, url)
        else:
            self._save_to_db(imdb_id)

class IndexThread (QThread):
    def __init__ (self, media_path, user, index_path, u1db_path, parent = None):
        QThread.__init__(self, parent)
        self.media_path = media_path
        self.user = user
        self.index_path = index_path
        self.u1db_path = u1db_path

    def run(self):
        L.d("running")
        self.stopvar = False
        rex = re.compile(".*\[(\d{7})\]$")
        # initialize HamsterDB in this thread to avoid sqlite problems
        db = HamsterDB(self.user, self.index_path, self.u1db_path)
        imdb_db = imdb.IMDb()
        tp = QThreadPool.globalInstance()
        writer = IndexWriter(self.user, self.index_path, self.u1db_path)
        total_movie_count = 0
        available_movie_count = 0

        it = QDirIterator(self.media_path, QDirIterator.Subdirectories)
        while it.hasNext():
            dir = it.next()
            try:
                directory = unicode(dir)
                match = rex.match(directory)
                if match:
                    total_movie_count += 1
                    imdb_id = match.group(1)
                    already_in_db = db.has_movie(imdb_id)
                    if already_in_db:
                        available_movie_count += 1
                        L.d("%s already in db - skipping" % imdb_id)
                    else:
                        j = Job(imdb_db, imdb_id, self) 
                        j.obj.finished.connect(writer.index_movie,
                                Qt.QueuedConnection)
                        tp.start(j) 
            except:
                pass
        L.d("%i/%i movies available" % (available_movie_count, total_movie_count))
        if available_movie_count == total_movie_count:
            L.d("all movies are already in sync")
            self.set_stopped()
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

    t = IndexThread("/path/to/movies/", "user",
    "/path/to/hamster.idx",
    "/path/to/hamster.db")
    t.start()
    sys.exit(app.exec_())

