#!/usr/bin/python -d

import sys
from PyQt4 import QtCore, QtGui
from qtgui import Ui_MainWindow
from qtcustomia import MyTableModel
from moviedb import MovieDB

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        header = ['Movie']

        self.db = MovieDB("movies")
        tv = self.ui.tableView
        tv.setShowGrid(False)
        model = MyTableModel(self.db, header, tv)
        #model = QtGui.QStandardItemModel()
        #model.insertRow(0, [QtGui.QStandardItem("hallo")])
        #model.insertRow(0, [QtGui.QStandardItem("sadf")])
        #model.insertRow(0, [QtGui.QStandardItem("pfui")])
        #model.insertRow(0, [QtGui.QStandardItem("warum?")])
        #model.insertRow(0, [QtGui.QStandardItem("haeff")])
        tv.setModel(model)
        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)
        print tv.selectionModel()
        #print self.connect(tv,
        #    QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
        #    self.update_selection)
        print self.connect(tv,
            QtCore.SIGNAL("clicked(QModelIndex)"),
            self.setCurrentSelection)

    def setCurrentSelection(self, item):
        print "clicked", item.row()
        id, title = self.db.get_movie_id_title_for_position(item.row())
        movie = self.db.get_movie(id)
        plot_short = movie.get('plot outline', "")
        plot = movie.get('plot', [""])[0]
        genres = movie.get('genres', [""])
        rating = str(movie.get('rating', "-"))
        self.ui.l_title.setText(movie['title'])
        self.ui.l_plot.setText(plot)
        self.ui.l_plot_short.setText(plot_short)
        self.ui.l_rating.setText(rating)
        self.ui.l_genres.setText(", ".join(genres))

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
