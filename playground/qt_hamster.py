#!/usr/bin/python -d

import sys
from PyQt4 import QtCore, QtGui
from qtgui import Ui_MainWindow
from qtcustomia import MyTableModel
from resultviewmodel import ResultViewModel
from moviedb import MovieDB
import urllib

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        header = ['Movie']

        self.db = MovieDB("movies")
        tv = self.ui.tableView
        tv.setShowGrid(False)
        #model = MyTableModel(self.db, header, tv)
        titles = self.db.get_movie_titles()
        self.model = ResultViewModel(titles, header, tv)
        #model = QtGui.QStandardItemModel()
        #model.insertRow(0, [QtGui.QStandardItem("hallo")])
        #model.insertRow(0, [QtGui.QStandardItem("sadf")])
        #model.insertRow(0, [QtGui.QStandardItem("pfui")])
        #model.insertRow(0, [QtGui.QStandardItem("warum?")])
        #model.insertRow(0, [QtGui.QStandardItem("haeff")])
        tv.setModel(self.model)
        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)
        #print self.connect(tv,
        #    QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
        #    self.update_selection)
        print self.connect(tv,
            QtCore.SIGNAL("clicked(QModelIndex)"),
            self.setCurrentSelection)
        print self.connect(self.ui.search_bar,
            QtCore.SIGNAL("textChanged(QString)"),
            self.update_model)

    def update_model(self, new_text):
        #search_string = str(self.ui.search_bar.text())
        search_string = str(new_text)
        titles = self.db.get_movie_titles(search_string)
        self.model.setResultView(titles)

    def setCurrentSelection(self, item):
        print "clicked", item.row()
        #id, title = self.db.get_movie_id_title_for_position(item.row())
        id = self.model.getIdForRow(item.row())
        movie = self.db.get_movie(id)
        plot_short = movie.get('plot outline', "")
        plot = movie.get('plot', [""])[0]
        genres = movie.get('genres', [""])
        rating = str(movie.get('rating', "-"))
        director = movie.get('director', ["-"])[0]["name"]
        title = movie['long imdb title']
        self.ui.l_title.setText(title)
        self.ui.l_plot.setText(plot)
        self.ui.l_plot_short.setText(plot_short)
        self.ui.l_rating.setText(rating)
        self.ui.l_director.setText(director)
        self.ui.l_genres.setText(", ".join(genres))
        #url = movie.get('full-size cover url', None)
        url = movie.get('cover url', None)
        if url:
            filename, msg = urllib.urlretrieve(url)
            img = QtGui.QImage(filename)
            self.ui.l_img.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.ui.l_img.setText("-")

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())
