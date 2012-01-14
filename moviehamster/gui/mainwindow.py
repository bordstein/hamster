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
from PySide.QtGui import QDesktopServices, QAbstractItemView
from moviehamster.hamsterdb.hamsterdb import HamsterDB
from qtgui import Ui_MainWindow
from whooshresmodel import ResultViewModel

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
        m = self.db.get_movie(imdb_id)
        pprint(m)
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

        self.ui.filter.textChanged.connect(self._update_model)

