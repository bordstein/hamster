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
from PySide.QtCore import Signal, Qt, QCoreApplication, QSettings
from PySide.QtGui import QDesktopServices
from moviehamster.hamsterdb.hamsterdb import HamsterDB
from qtgui import Ui_MainWindow
from whooshresmodel import ResultViewModel

class GUI(QtGui.QMainWindow):
    def init_config(self):
        QCoreApplication.setOrganizationName("Hamster Inc.")
        QCoreApplication.setApplicationName("Hamster")
        self.settings = QSettings()

    def init_db(self):
        self.db_dir = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
            #TODO catch exception
        self.db = HamsterDB(self.db_dir + '/' + 'hamster.idx',
                            self.db_dir + '/' + 'hamster.db',)

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_config()

        self.init_db()

        tv = self.ui.movieList
        tv.setShowGrid(False)
        results = self.db.list_all_movies()
        self.model = ResultViewModel(results, tv)
        tv.setModel(self.model)
        tv.resizeColumnsToContents()

        tv.verticalHeader().setVisible(False)
        tv.horizontalHeader().setStretchLastSection(True)

