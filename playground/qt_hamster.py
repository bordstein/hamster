#!/usr/bin/python -d

import sys
from PyQt4 import QtCore, QtGui
from qtgui import Ui_MainWindow
from qtcustomia import MyTableModel

class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    header = ['Movie']

    tv = self.ui.tableView
    tv.setShowGrid(False)
    tv.setModel(MyTableModel(None, header, tv))
    # hide vertical header
    vh = tv.verticalHeader()
    vh.setVisible(False)

    # set horizontal header properties
    hh = tv.horizontalHeader()
    hh.setStretchLastSection(True)
    #QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.ui.textEdit.clear )
    #QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.add_entry)

#  def add_entry(self):
#    self.ui.lineEdit.selectAll()
#    self.ui.lineEdit.cut()
#    self.ui.textEdit.append("")
#    self.ui.textEdit.paste()

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
