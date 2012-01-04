#!/usr/bin/python -d

import sys
from PySide import QtGui
from qtgui import Ui_MainWindow
import u1db
import json
from whooshresmodel import ResultViewModel
from indexer.hamsterindex import HamsterIndex
from util.strings import humanize_mins
from indexer.qindexer import IndexThread
import urllib

RICHTEXT_RATING = """<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">imdb</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">rating</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="
font-size:36pt; font-weight:600;">%s</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;">%s</p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">votes</p>"""

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        header = ['Movie']

        #self.db = MovieDB("movies")
        tv = self.ui.tableView
        tv.setShowGrid(False)
        #model = MyTableModel(self.db, header, tv)
        #titles = self.db.get_movie_titles()
        self.index = HamsterIndex("/media/DATA/hamster/hamster.idx")
        self.db = u1db.open("/media/DATA/hamster/hamster.db", create=True)
        results = self.index.list_all()
        self.model = ResultViewModel(results, header, tv)
        #model = QtGui.QStandardItemModel()
        #model.insertRow(0, [QtGui.QStandardItem("hallo")])
        #model.insertRow(0, [QtGui.QStandardItem("sadf")])
        #model.insertRow(0, [QtGui.QStandardItem("pfui")])
        #model.insertRow(0, [QtGui.QStandardItem("warum?")])
        #model.insertRow(0, [QtGui.QStandardItem("haeff")])
        tv.setModel(self.model)
        selectionModel = tv.selectionModel()
        # hide vertical header
        vh = tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(True)
        #print self.connect(tv,
        #    QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
        #    self.update_selection)
        #print self.connect(tv,
        #    QtCore.SIGNAL("clicked(QModelIndex)"),
        #    self.setCurrentSelection)
        #tv.clicked.connect(self.setCurrentSelection)
        selectionModel.selectionChanged.connect(self.setCurrentSelection)
        self.ui.search_bar.textChanged.connect(self.update_model)
        self.ui.action_sync_now.triggered.connect(self.sync)

    def sync(self):
        #self.t = IndexThread("/media/DATA/media/movies/")
        self.t = IndexThread("/tmp/mv/")
        print self.t.finished.connect(self.sync_finished)
        self.t.start()
        print "started"

    def sync_finished(self):
        print "\nsync finished"

    def update_model(self, new_text):
        search_string = str(new_text)
        if search_string:
            titles = self.index.query("'%s'" % new_text)
        else:
            titles = self.index.list_all()
        self.model.setResults(titles)

    def setCurrentSelection(self, newSelection, oldSelection):
        indexes = newSelection.at(0).indexes()
        if not len(indexes) == 1:
            return
        item = indexes[0]
        id = self.model.getIdForRow(item.row())
        movie_doc = self.db.get_doc(id)
        movie = json.loads(movie_doc.content)
        plot_short = movie.get('plot outline', "")
        plot = movie.get('plot', [""])[0]
        genres = movie.get('genres', [""])
        cast = movie.get('cast', [""])
        countries = movie.get('countries', [""])
        runtime = movie.get('runtimes', [""])[0]
        # handle stuff like "USA:107" in runtime array
        try:
            if ":" in runtime:
                runtime = runtime.split(":")[1]
            runtime = humanize_mins(runtime)
        except:
            runtime = movie.get('runtimes', [""])[0] # reload
            print "could not humanize", runtime, "for", id
        imdb_rating = str(movie.get('rating', "-"))
        votes = movie.get('votes', "-")
        rating = RICHTEXT_RATING % (imdb_rating, votes)
        director = movie.get('director', ["-"])[0]["name"]
        title = movie['long imdb title']
        title = '<span style=" font-size:16pt; font-weight:600;"> '+ title + '</span>'
        self.ui.l_title.setText(title)
        self.ui.l_plot.setText(plot)
        self.ui.l_plot_short.setText(plot_short)
        self.ui.l_rating.setText(rating)
        self.ui.l_director.setText(director)
        self.ui.l_runtime.setText(runtime)
        self.ui.l_genres.setText(", ".join(genres))
        self.ui.l_genres.setCursorPosition(0)
        self.ui.l_countries.setText(", ".join(countries))
        self.ui.l_countries.setCursorPosition(0)
        cast = [c['name'] for c in cast]
        self.ui.l_cast.setText(", ".join(cast[:4]))
        self.ui.l_cast.setCursorPosition(0)
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
