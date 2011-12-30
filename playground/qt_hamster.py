#!/usr/bin/python -d

import sys
from PyQt4 import QtCore, QtGui
from qtgui import Ui_MainWindow
from qtcustomia import MyTableModel
from moviedb import MovieDB
import urllib

RICHTEXT_BIG = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:14pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;
-qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:600;">%s</span></p></body></html>"""

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
        director = movie.get('director', ["-"])[0]["name"]
        title = movie['long imdb title']
        self.ui.l_title.setText(RICHTEXT_BIG % title)
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
