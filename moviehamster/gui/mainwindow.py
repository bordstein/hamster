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


#!/usr/bin/python -d

from PySide import QtGui
import os
from PySide.QtCore import Signal, Qt, QCoreApplication, QSettings, QByteArray, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from moviehamster.gui.linkbutton import LinkButton
from moviehamster.gui.util import humanize_mins, os_open_file
from PySide.QtGui import QDesktopServices, QAbstractItemView, QShortcut, QKeySequence, QListWidgetItem
from moviehamster.indexer import IndexThread
from moviehamster.hamsterdb.hamsterdb import HamsterDB
import moviehamster.log as L
from moviehamster.constants import *
from qtgui import Ui_MainWindow
from whooshresmodel import ResultViewModel
from hamsterdelegate import HamsterDelegate
import getpass
from settings import Ui_SettingsDialog

RICHTEXT_RATING = """<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">imdb</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">rating</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="
font-size:36pt; font-weight:600;">%s</span></p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px;
margin-right:0px; -qt-block-indent:0; text-indent:0px;">%s</p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">votes</p>"""


class GUI(QtGui.QMainWindow):
    shutmedown = Signal()

    def _init_config(self):
        QCoreApplication.setOrganizationName("Hamster Inc.")
        QCoreApplication.setApplicationName("Hamster")
        self.settings = QSettings()

    def _init_db(self):
        self.db_dir = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)
            #TODO catch exception
        self.index_path = self.db_dir + '/' + 'hamster.idx'
        self.db_path = self.db_dir + '/' + 'hamster.db'
        self.user = getpass.getuser()
        self.db = HamsterDB(self.user, self.index_path, self.db_path)
        #TODO ask username from user?

    def open_settings(self):
        diag = Ui_SettingsDialog()
        diag.show()

    def _init_shortcuts(self):
        QShortcut(QKeySequence(self.tr("Alt+Left")), self, self.history.backward)
        QShortcut(QKeySequence(self.tr("Alt+Right")), self, self.history.forward)

    def _init_movie_list_buttons(self):
        self.db.lists._current_movie = None
        self.ui.button_movie_favourite.toggled.connect(self.db.lists.toggle_movie_in_list)
        self.ui.button_movie_watchlater.toggled.connect(self.db.lists.toggle_movie_in_list)

    def _init_movie_list(self):
        tv = self.ui.movieList
        tv.setShowGrid(False)
        results = self.db.list_all_movies()
        self.model = ResultViewModel(results, self.db.lists, tv)
        tv.setModel(self.model)
        tv.setMouseTracking(True)
        tv.setItemDelegate(HamsterDelegate(tv))
        tv.resizeColumnsToContents()
        tv.verticalHeader().setVisible(False)
        tv.horizontalHeader().setStretchLastSection(True)
        tv.verticalHeader().setDefaultSectionSize(24)
        tv.setSelectionBehavior(QAbstractItemView.SelectRows)
        tv.clicked.connect(self._table_clicked)
        self.ui.button_extended_options.toggled.connect(self._toggle_extended_options)

    def _table_clicked(self, idx):
        col = idx.column()
        row = idx.row()
        imdb_id = self.model.getIdForRow(row)
        if col == MOVIELIST_COL_TITLE:
            self.history.create_entry(overwrite=True)
            self._open_movie(imdb_id)
        elif col == MOVIELIST_COL_FAVOURITE:
            current_state = self.model.data(idx, Qt.DisplayRole)
            L.d("clicked on favorite, state is %s" % current_state)
            self.db.lists.toggle_movie_in_list(not current_state, imdb_id,
                    NAME_USER_LIST_FAVOURITES)
        elif col == MOVIELIST_COL_WATCHLATER:
            current_state = self.model.data(idx, Qt.DisplayRole)
            L.d("clicked on watchlater, state is %s" % current_state)
            self.db.lists.toggle_movie_in_list(not current_state, imdb_id,
                    NAME_USER_LIST_WATCHLATER)
        else:
            pass
            # TODO
            # handle star etc.

    def _open_movie(self, imdb_id, nohist=False):
        movie = self.db.get_movie(imdb_id)
        self.movie = movie
        plot_short = movie.get('plot outline', "")
        plot = movie.get('plot', [""])[0]
        genres = movie.get('genres', [""])
        countries = movie.get('countries', [""])
        runtime = movie.get('runtimes', [""])[0]
        final_runtime = None
        if ":" in runtime:
            runtimes = runtime.split(":")
            for r in runtimes:
                try:
                    final_runtime = humanize_mins(r)
                    break
                except:
                    pass
        else:
            final_runtime = humanize_mins(runtime)
        if not final_runtime:
            final_runtime = movie.get('runtimes', ["Not available"])[0]  # reload
            L.w("could not humanize " + runtime + " for " + str(imdb_id))
        imdb_rating = str(movie.get('rating', "-"))
        votes = movie.get('votes', "-")
        rating = RICHTEXT_RATING % (imdb_rating, votes)
        title = movie['long imdb title']
        title = '<span style=" font-size:16pt; font-weight:600;"> ' + title + '</span>'

        self.ui.l_length.setText(final_runtime)
        self.ui.l_genres.setText(', '.join(genres))
        self.ui.l_countries.setText(', '.join(countries))

        self.ui.box_director.clear()
        last = len(movie['director']) - 1
        for idx, director in enumerate(movie['director']):
            director_button = LinkButton(director['name'])
            director_button.clicked.connect(self._open_person)
            director_button.id = director['person_id']
            i = QListWidgetItem(director['name'], self.ui.box_director)
            # dirty hack to avoid having the LinkButton text above the QListWidgetItem which looks bold then
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            i.setForeground(brush)
            self.ui.box_director.setItemWidget(i, director_button)
            if not idx == last:
                QListWidgetItem('|', self.ui.box_cast)

        self.ui.box_cast.clear()
        last = len(movie['cast']) - 1
        for idx, actor in enumerate(movie['cast']):
            actor_button = LinkButton(actor['name'])
            actor_button.clicked.connect(self._open_person)
            actor_button.id = actor['person_id']
            i = QListWidgetItem(actor['name'], self.ui.box_cast)
            # dirty hack to avoid having the LinkButton text above the QListWidgetItem which looks bold then
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            i.setForeground(brush)
            self.ui.box_cast.setItemWidget(i, actor_button)
            if not idx == last:
                QListWidgetItem('|', self.ui.box_cast)

        self.ui.l_title.setText(title)
        self.ui.l_plot_short_3.setText(plot_short)
        self.ui.l_plot_3.setText(plot)
        self.ui.l_rating.setText(rating)
        cover_img = movie.get("_cover_", None)
        if cover_img:
            raw_img = QByteArray.fromBase64(cover_img.encode("UTF-8"))
            img = QtGui.QImage()
            img.loadFromData(raw_img)
            self.ui.l_img.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.ui.l_img.setText("-")

        # set toggle list buttons
        self.db.lists._current_movie = None  # avoid firing signals on setting buttons
        favourites = self.db.lists.get_favourites()
        movie_is_favourite = imdb_id in favourites
        self.ui.button_movie_favourite.setChecked(movie_is_favourite)
        self.ui.button_movie_favourite._movielist = NAME_USER_LIST_FAVOURITES

        watchlater = self.db.lists.get_watchlater()
        movie_is_watchlater = imdb_id in watchlater
        self.ui.button_movie_watchlater.setChecked(movie_is_watchlater)
        self.ui.button_movie_watchlater._movielist = NAME_USER_LIST_WATCHLATER

        self.db.lists._current_movie = imdb_id

        self.ui.stackedWidget.setCurrentWidget(self.ui.movie_view)
        if not nohist:
            self.history.create_entry(imdb_id)

        # enable/disable play button
        movie_base_dir = self.settings.value("movie_dir")
        movie_ok = os.path.exists(
                os.path.join(movie_base_dir,
                    self.movie['_meta_'][self.user]['movie_path']))
        self.ui.btn_play.setEnabled(movie_ok)

    def _open_person(self, person_id=None, nohist=False):
        if not person_id:
            person_id = self.sender().id
        p = self.db.get_person('person_' + person_id)
        name = '<span style=" font-size:16pt; font-weight:600;"> ' + p['name'] + '</span>'
        self.ui.l_person_name.setText(name)
        self.ui.person_bio.setText(p['mini biography'])
        self.ui.stackedWidget.setCurrentWidget(self.ui.person_view)
        head_shot = p.get("headshot", None)
        if head_shot:
            raw_img = QByteArray.fromBase64(head_shot.encode("UTF-8"))
            img = QtGui.QImage()
            img.loadFromData(raw_img)
            self.ui.l_headshot.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.ui.l_headshot.setText("-")
        if not nohist:
            self.history.create_entry(person_id)

    def _update_model(self, new_text):
        search_string = str(new_text)
        if search_string:
            titles = self.db.search(search_string)
        else:
            titles = self.db.list_all_movies()
        self.model.setResults(titles)

    def sync(self):
        if self.index_thread and self.index_thread.isRunning():
            self.index_thread.set_stopped()
        else:
            stop_icon = QtGui.QIcon()
            stop_icon.addPixmap(QtGui.QPixmap(":/icons/icons/process-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_sync.setIcon(stop_icon)
            movie_dir = self.settings.value("movie_dir")
            self.index_thread = IndexThread(movie_dir, self.user,
                    self.index_path, self.db_path)
            self.index_thread.finished.connect(self._indexer_closed)
            self.shutmedown.connect(self.index_thread.set_stopped,
                    Qt.QueuedConnection)
            self.index_thread.start()
            L.d("syncer started")

    def _open_library(self, filter=None, nohist=False):
        self.ui.filter.clear()
        if filter:
            self.ui.filter.setText(filter)
            self._update_model(filter)
        self.ui.stackedWidget.setCurrentWidget(self.ui.library_view)
        if not nohist:
            self.history.create_entry()

    def _indexer_closed(self):
        L.d("indexer finished")
        if self._shutdown_requested:
            self.close()
        else:
            refresh_icon = QtGui.QIcon()
            refresh_icon.addPixmap(QtGui.QPixmap(":/icons/icons/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.button_sync.setIcon(refresh_icon)

    def closeEvent(self, event):
        L.d("shutdown requested")
        L.d("hiding window")
        self.setVisible(False)
        if self.index_thread and self.index_thread.isRunning():
            event.ignore()
            L.d("setting quit")
            self._shutdown_requested = True
            self.index_thread.set_stopped()
        else:
            L.d("goodby")
            event.accept()

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.history = History(self)
        self.open_settings()

        self._init_config()
        self._init_db()
        self._init_movie_list()
        self._init_movie_list_buttons()

        self._init_shortcuts()

        self.index_thread = None
        self._shutdown_requested = False

        self.ui.filter.textChanged.connect(self._update_model)
        self.ui.button_sync.clicked.connect(self.sync)

        self.ui.btn_back.clicked.connect(self.history.backward)
        self.ui.btn_forward.clicked.connect(self.history.forward)
        self.ui.btn_library.clicked.connect(self._open_library)

        self._open_library()

        self.ui.btn_play.clicked.connect(self._play_movie)

    def _play_movie(self):
        movie_base_dir = self.settings.value("movie_dir")
        os_open_file(
                os.path.join(movie_base_dir,
                    self.movie['_meta_'][self.user]['movie_path']))


    def _toggle_extended_options(self, enabled):
        geometry = self.ui.widget_extended_options.size()
        if enabled:
            maxHeight = 30
            duration = 700
            self.ui.button_extended_options.setArrowType(Qt.UpArrow)
        else:
            maxHeight = 0
            duration = 700
            self.ui.button_extended_options.setArrowType(Qt.DownArrow)
        # IMPORTANT: avoid garbage collection of animation by making
        # it a object attribute (self.animation)
        self.animation = QPropertyAnimation(self.ui.widget_extended_options, "maximumHeight")
        self.animation.setDuration(duration)
        self.animation.setStartValue(geometry.height())
        self.animation.setEndValue(maxHeight)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)


class History(object):
    current = -1
    history = []

    def __init__(self, gui):
        self.gui = gui

    def backward(self):
        if 0 < self.current < len(self.history):
            self.history[self.current - 1][0](self.history[self.current - 1][1], nohist=True)
            self.current -= 1

    def forward(self):
        if 0 <= self.current < len(self.history) - 1:
            self.history[self.current + 1][0](self.history[self.current + 1][1], nohist=True)
            self.current += 1

    def create_entry(self, id=None, overwrite=False):
        idx = self.gui.ui.stackedWidget.currentIndex()
        if idx == 0:
            view = self.gui._open_library
            arg = self.gui.ui.filter.text()
        elif idx == 1:
            view = self.gui._open_person
            arg = id
        elif idx == 2:
            view = self.gui._open_movie
            arg = id

        if self.current < len(self.history) - 1:
            # avoid two library entries in a row
            if not overwrite:
                self.current += 1
            self.history.insert(self.current, (view, arg))
            self.history = self.history[:self.current + 1]
        else:
            if overwrite:
                self.history.pop(self.current)
            else:
                self.current += 1
            self.history.append((view, arg))

    def overwrite_entry(self):
        print 'called'
        self.create_entry(overwrite=True)
