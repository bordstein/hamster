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


#!/usr/bin/python -d

from PySide import QtGui
import os
from pprint import pprint
from PySide.QtCore import Signal, Qt, QCoreApplication, QSettings, QByteArray
from moviehamster.gui.util import humanize_mins
from PySide.QtGui import QDesktopServices, QAbstractItemView, QPushButton, QShortcut, QKeySequence
from moviehamster.indexer import IndexThread
from moviehamster.hamsterdb.hamsterdb import HamsterDB
import moviehamster.log as L
from qtgui import Ui_MainWindow
from whooshresmodel import ResultViewModel

RICHTEXT_RATING = """<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">imdb</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">rating</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="
font-size:36pt; font-weight:600;">%s</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;">%s</p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">votes</p>"""

class GUI(QtGui.QMainWindow):
    shutmedown = Signal()
    def _init_config(self):
        QCoreApplication.setOrganizationName("Hamster Inc.")
        QCoreApplication.setApplicationName("Hamster")
        self.settings = QSettings()

    def _init_db(self):
        self.db_dir = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
            #TODO catch exception
        self.index_path = self.db_dir + '/' + 'hamster.idx'
        self.db_path = self.db_dir + '/' + 'hamster.db'
        self.user = os.environ['USERNAME']
        self.db = HamsterDB(self.user, self.index_path, self.db_path)
        #TODO ask username from user?

    def _init_shortcuts(self):
        shortcut = QShortcut(QKeySequence(self.tr("Alt+Left")), self, self.history.backward)
        shortcut = QShortcut(QKeySequence(self.tr("Alt+Right")), self, self.history.forward)

    def _init_movie_list(self):
        tv = self.ui.movieList
        tv.setShowGrid(False)
        results = self.db.list_all_movies()
        self.model = ResultViewModel(results, tv)
        tv.setModel(self.model)
        tv.resizeColumnsToContents()
        tv.verticalHeader().setVisible(False)
        tv.horizontalHeader().setStretchLastSection(True)
        tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        tv.doubleClicked.connect(self.history.overwrite_entry)
        tv.doubleClicked.connect(self._do_open_movie)

    def _do_open_movie(self, idx):
        imdb_id = self.model.getIdForRow(idx.row())
        self._open_movie(imdb_id)

    def _open_movie(self, imdb_id, nohist=False):
        movie = self.db.get_movie(imdb_id)

        plot_short = movie.get('plot outline', "")
        plot = movie.get('plot', [""])[0]
        genres = movie.get('genres', [""])
        cast = movie.get('cast', [""])
        countries = movie.get('countries', [""])
        runtime = movie.get('runtimes', [""])[0]
        # handle stuff like "USA:107" in runtime array
        try:
            if ":" in runtime:
                runtime = runtime.split(":")[1]
            runtime = humanize_mins(runtime)
        except:
            runtime = movie.get('runtimes', [""])[0] # reload
            print "could not humanize", runtime, "for", id
        imdb_rating = str(movie.get('rating', "-"))
        votes = movie.get('votes', "-")
        rating = RICHTEXT_RATING % (imdb_rating, votes)
        director = movie.get('director', ["-"])[0]["name"]
        title = movie['long imdb title']
        title = '<span style=" font-size:16pt; font-weight:600;"> '+ title + '</span>'

        self.ui.btn_director.setText(director)
        self.ui.l_length.setText(runtime)
        self.ui.l_genres.setText(', '.join(genres))
        self.ui.l_countries.setText(', '.join(countries))
        for actor in cast:
            actor_button = QPushButton(actor['name'])
            actor_button.clicked.connect(self._open_person)
            # TODO
            # actor_button.id = actor['id']
            self.ui.box_cast.addWidget(actor_button)
        self.ui.l_title.setText(title)
        self.ui.l_plot_short_3.setText(plot_short)
        self.ui.l_plot_3.setText(plot)
        self.ui.l_rating.setText(rating)
        cover_img = movie.get("_cover_", None)
        if cover_img:
            raw_img = QByteArray.fromBase64(cover_img.encode("UTF-8"))
            img = QtGui.QImage()
            img.loadFromData(raw_img)
            self.ui.l_img.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.ui.l_img.setText("-")

        self.ui.stackedWidget.setCurrentWidget(self.ui.movie_view)
        if not nohist:
            self.history.create_entry(imdb_id)

    def _open_person(self, person_id=None, nohist=False):
        if not person_id:
            person_id = '0000136'
            # TODO
            # person_id = self.sender().id
        #DOESNT WORK
        p = self.db.get_person('person_' + person_id)
        self.ui.l_person_name.setText(p['name'])
        self.ui.person_bio.setText(p['mini biography'][0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.person_view)
        if not nohist:
            self.history.create_entry(person_id)

    def _update_model(self, new_text):
        search_string = str(new_text)
        if search_string:
            titles = self.db.search(search_string)
        else:
            titles = self.db.list_all_movies()
        self.model.setResults(titles)

    def sync(self):
        if self.index_thread and self.index_thread.isRunning():
            self.index_thread.set_stopped()
        else:
            stop_icon = QtGui.QIcon()
            stop_icon.addPixmap(QtGui.QPixmap(":/icons/icons/process-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_sync.setIcon(stop_icon)
            movie_dir = self.settings.value("movie_dir")
            self.index_thread = IndexThread(movie_dir, self.user,
                    self.index_path, self.db_path)
            self.index_thread.finished.connect(self._indexer_closed)
            self.shutmedown.connect(self.index_thread.set_stopped,
                    Qt.QueuedConnection)
            self.index_thread.start()
            L.d("syncer started")

    def _open_library(self, filter=None, nohist=False):
        self.ui.filter.clear()
        if filter:
            self.ui.filter.setText(filter)
            self._update_model(filter)
        self.ui.stackedWidget.setCurrentWidget(self.ui.library_view)
        if not nohist:
            self.history.create_entry()

    def _indexer_closed(self):
        L.d("indexer finished")
        if self._shutdown_requested:
            self.close()
        else:
            refresh_icon = QtGui.QIcon()
            refresh_icon.addPixmap(QtGui.QPixmap(":/icons/icons/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_sync.setIcon(refresh_icon)


    def closeEvent(self, event):
        L.d("shutdown requested")
        L.d("hiding window")
        self.setVisible(False)
        if self.index_thread and self.index_thread.isRunning():
            event.ignore()
            L.d("setting quit")
            self._shutdown_requested = True
            self.index_thread.set_stopped()
        else:
            L.d("goodby")
            event.accept()

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.history = History(self)

        self._init_config()
        self._init_db()
        self._init_movie_list()

        self._init_shortcuts()

        self.index_thread = None
        self._shutdown_requested = False

        self.ui.filter.textChanged.connect(self._update_model)
        self.ui.button_sync.clicked.connect(self.sync)

        self.ui.btn_back.clicked.connect(self.history.backward)
        self.ui.btn_forward.clicked.connect(self.history.forward)
        self.ui.btn_library.clicked.connect(self._open_library)

        self._open_library()

class History(object):
    current = -1
    history = []

    def __init__(self, gui):
        self.gui = gui

    def backward(self):
        if 0 < self.current < len(self.history):
            self.history[self.current - 1][0](self.history[self.current - 1][1], nohist=True)
            self.current -= 1

    def forward(self):
        if 0 <= self.current < len(self.history) - 1:
            self.history[self.current + 1][0](self.history[self.current + 1][1], nohist=True)
            self.current += 1

    def create_entry(self, id=None, overwrite=False):
        L.d("CREATE HISTORY ENTRY")
        L.d("BEFORE:")
        L.d("CURRENT: %d" % self.current)
        for m,a in self.history:
            L.d(m.func_name + ' ' + a)
        idx = self.gui.ui.stackedWidget.currentIndex()
        if idx == 0:
            view = self.gui._open_library
            arg = self.gui.ui.filter.text()
        elif idx == 1:
            view = self.gui._open_person
            arg = id
        elif idx == 2:
            view = self.gui._open_movie
            arg = id

        if self.current < len(self.history) - 1:
            # avoid two library entries in a row
            if not overwrite:
                self.current += 1
            self.history.insert(self.current, (view, arg))
            self.history = self.history[:self.current + 1]
        else:
            if overwrite:
                self.history.pop(self.current)
            else:
                self.current += 1
            self.history.append((view, arg))

        L.d("AFTER:")
        L.d("CURRENT: %d" % self.current)
        for m,a in self.history:
            L.d(m.func_name + ' ' + a)
        L.d("*" * 78)

    def overwrite_entry(self):
        print 'called'
        self.create_entry(overwrite=True)

