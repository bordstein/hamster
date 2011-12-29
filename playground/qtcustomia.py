from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
import couchdb
import sys
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
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
        # create the view
        tv = QTableView()

        # set the table model
        header = ['date', 'time', '', 'size', 'filename']
        #tm = MyTableModel(self.tabledata, header, self) 
        tm = MyTableModel(None, header, self) 
        tv.setModel(tm)

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
        #tv.resizeColumnsToContents()

        # set row height
        #nrows = len(self.tabledata)
        #for row in xrange(nrows):
        #    tv.setRowHeight(row, 18)

        # enable sorting
        #tv.setSortingEnabled(True)

        return tv
 
class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, parent=None, *args): 
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        #self.arraydata = datain
        self.headerdata = headerdata

        couch = couchdb.Server()
        self.db = couch['movies']
        vr = self.db.view("_design/mv/_view/count")
        self.rowcount = vr.rows[0].value

 
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
        print "asking row", index.row()
        vr = self.db.view("_design/test/_view/title", skip=index.row(), limit=1)
        return QVariant(vr.rows[0].key)

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
