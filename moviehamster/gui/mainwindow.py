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
from PySide.QtCore import Signal, Qt, QCoreApplication, QSettings
from PySide.QtGui import QDesktopServices, QAbstractItemView, QPushButton
from moviehamster import log
from moviehamster.gui.util import humanize_mins
from moviehamster.hamsterdb.hamsterdb import HamsterDB
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
    def _init_config(self):
        QCoreApplication.setOrganizationName("Hamster Inc.")
        QCoreApplication.setApplicationName("Hamster")
        self.settings = QSettings()

    def _init_db(self):
        self.db_dir = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
            #TODO catch exception
        self.db = HamsterDB(os.environ['USERNAME'], self.db_dir + '/' + 'hamster.idx',
        #TODO ask username from user?
                            self.db_dir + '/' + 'hamster.db',)

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
        tv.doubleClicked.connect(self._open_movie)

    def _open_movie(self, idx):
        imdb_id = self.model.getIdForRow(idx.row())
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
        director = movie.get('director', ["-"])[0]["name"]
        title = movie['long imdb title']
        title = '<span style=" font-size:16pt; font-weight:600;"> '+ title + '</span>'

        self.ui.btn_director.setText(director)
        self.ui.l_length.setText(runtime)
        self.ui.l_genres.setText(', '.join(genres))
        self.ui.l_countries.setText(', '.join(countries))
        self.ui.box_cast.addWidget(QPushButton('hallo'))
        self.ui.box_cast.addWidget(QPushButton('hallo2'))
        self.ui.box_cast.addWidget(QPushButton('hallo3'))
        self.ui.box_cast.addWidget(QPushButton('hallo3'))
        self.ui.box_cast.addWidget(QPushButton('hallo3'))
        self.ui.box_cast.addWidget(QPushButton('hallo3'))
        self.ui.stackedWidget.setCurrentWidget(self.ui.movie_view)

    def _update_model(self, new_text):
        search_string = str(new_text)
        if search_string:
            titles = self.db.search(search_string)
        else:
            titles = self.db.list_all_movies()
        self.model.setResults(titles)

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_config()
        self._init_db()
        self._init_movie_list()
        self.ui.stackedWidget.setCurrentWidget(self.ui.library_view)
        self.ui.filter.textChanged.connect(self._update_model)

