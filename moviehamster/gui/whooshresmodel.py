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

from PySide.QtCore import QAbstractTableModel, Qt
from moviehamster.constants import *
 
class ResultViewModel(QAbstractTableModel): 
    def __init__(self, results, liststore, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.headerdata = ['Title', 'Year', 'Rating', 'Favorite', 'Watch Later']
        self.results = results
        self.lists = liststore
        #self.bookmark_list = self.lists.get_user_list("bookmark", failsave=True)
        #self.favourite_list = self.lists.get_user_list("favourite", failsave=True)
        #print self.bookmark_list
        #print self.favourite_list
 
    def rowCount(self, parent): 
        if self.results:
            return len(self.results)
        return 0
 
    def columnCount(self, parent): 
        return len(self.headerdata)

    def setResults(self, results):
        self.beginResetModel()
        self.results = results
        self.endResetModel()

    def getIdForRow(self, row):
        return self.results[row]["imdb_id"]

    def data(self, index, role): 
        if not index.isValid(): 
            return None
        elif role != Qt.DisplayRole: 
            return None
        elif self.results:
            if index.column() == MOVIELIST_COL_TITLE:
                return self.results[index.row()]["title"]
            elif index.column() == MOVIELIST_COL_YEAR:
                return self.results[index.row()]["year"]
            elif index.column() == MOVIELIST_COL_RATING:
                return str(self.results[index.row()]["rating"])
            elif index.column() == MOVIELIST_COL_FAVOURITE:
                imdb_id = self.results[index.row()]['imdb_id']
                if imdb_id in self.lists.get_favourites():
                    return True
                return False
            elif index.column() == MOVIELIST_COL_WATCHLATER:
                imdb_id = self.results[index.row()]['imdb_id']
                if imdb_id in self.lists.get_watchlater():
                    return True
                return False
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headerdata[col]
        return None
