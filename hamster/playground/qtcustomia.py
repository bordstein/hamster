from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

class MyTableModel(QAbstractTableModel): 
    def __init__(self, db, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        #self.arraydata = datain
        self.headerdata = headerdata

        self.db = db
        self.rowcount = self.db.get_total_movies()

 
    def rowCount(self, parent): 
        #return len(self.arraydata) 
        return self.rowcount
 
    def columnCount(self, parent): 
        #return len(self.arraydata[0]) 
        return 1
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        #return QVariant(self.arraydata[index.row()][index.column()]) 
        #print "asking row", index.row()
        id, title = self.db.get_movie_id_title_for_position(index.row())
        return QVariant(title)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

#    def sort(self, Ncol, order):
#        """Sort table by given column number.
#        """
#        self.emit(SIGNAL("layoutAboutToBeChanged()"))
#        #self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))        
#        #if order == Qt.DescendingOrder:
#        #    self.arraydata.reverse()
#        self.emit(SIGNAL("layoutChanged()"))

if __name__ == "__main__": 
    main()
