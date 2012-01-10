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
 
class ResultViewModel(QAbstractTableModel): 
    def __init__(self, results, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        #self.arraydata = datain
        self.headerdata = headerdata
        self.results = results
 
    def rowCount(self, parent): 
        if self.results:
            return len(self.results)
        return 0
 
    def columnCount(self, parent): 
        #return len(self.arraydata[0]) 
        return 1

    def setResults(self, results):
        self.beginResetModel()
        self.results = results
        self.endResetModel()

    def getIdForRow(self, row):
        id = self.results[row]["imdb_id"]
        return id
 
    def data(self, index, role): 
        if not index.isValid(): 
            return None
        elif role != Qt.DisplayRole: 
            return None
        #return QVariant(self.arraydata[index.row()][index.column()]) 
        if self.results:
            title = self.results[index.row()]["title"]
            return title
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headerdata[col]
        return None
