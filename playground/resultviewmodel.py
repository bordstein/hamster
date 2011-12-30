import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import couchdb
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    couch = couchdb.Server()
    db = couch['movies']
    string = "Star"
    rv = db.view("_design/test/_view/title", startkey=string, endkey=string + "\u9999")
    w.tm.setResultView(rv)
    print w.tm.getIdForRow(2)
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        # create table
        self.get_table_data()
        table = self.createTable() 
         
        # layout
        layout = QVBoxLayout()
        layout.addWidget(table) 
        self.setLayout(layout) 

    def get_table_data(self):
        #stdouterr = os.popen4("ls -la /")[1].read()
        #lines = stdouterr.splitlines()
        #lines = lines[5:]
        #lines = lines[:-2]
        #self.tabledata = [re.split(r"\s+", line, 4)
        #             for line in lines]
        pass

    def createTable(self):
        import couchdb
        couch = couchdb.Server()
        db = couch['movies']
        rv = db.view("_design/test/_view/title")

        # create the view
        tv = QTableView()

        # set the table model
        header = ['title']
        self.tm = ResultViewModel(rv, header, self) 
        tv.setModel(self.tm)

        # set the minimum size
        tv.setMinimumSize(400, 300)

        # hide grid
        tv.setShowGrid(False)

        # set the font
        font = QFont("Courier New", 8)
        tv.setFont(font)

        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        tv.resizeColumnsToContents()

        # set row height
        #nrows = len(self.tabledata)
        #for row in xrange(nrows):
        #    tv.setRowHeight(row, 18)

        # enable sorting
        #tv.setSortingEnabled(True)

        return tv
 
class ResultViewModel(QAbstractTableModel): 
    def __init__(self, resultView, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        #self.arraydata = datain
        self.headerdata = headerdata
        self.resultView = resultView
 
    def rowCount(self, parent): 
        if self.resultView:
            return len(self.resultView.rows)
        return 0
 
    def columnCount(self, parent): 
        #return len(self.arraydata[0]) 
        return 1

    def setResultView(self, rv):
        self.beginResetModel()
        self.resultView = rv
        self.endResetModel()

    def getIdForRow(self, row):
        id = self.resultView.rows[row].id
        return id
 
    def data(self, index, role): 
        if not index.isValid(): 
            return QVariant() 
        elif role != Qt.DisplayRole: 
            return QVariant() 
        #return QVariant(self.arraydata[index.row()][index.column()]) 
        if self.resultView:
            title = self.resultView.rows[index.row()].key
            return QVariant(title)
        return QVariant()

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

if __name__ == "__main__": 
    main()
