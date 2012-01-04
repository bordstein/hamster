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
