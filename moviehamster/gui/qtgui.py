# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moviehamster/gui/qtgui.ui'
#
# Created: Thu Feb  2 10:43:18 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 654)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.library_view = QtGui.QWidget()
        self.library_view.setObjectName("library_view")
        self.verticalLayout = QtGui.QVBoxLayout(self.library_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_search = QtGui.QFrame(self.library_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_search.setObjectName("frame_search")
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_search)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.filter = QtGui.QLineEdit(self.frame_search)
        self.filter.setObjectName("filter")
        self.gridLayout_4.addWidget(self.filter, 0, 0, 1, 1)
        self.button_extended_options = QtGui.QToolButton(self.frame_search)
        self.button_extended_options.setCheckable(True)
        self.button_extended_options.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.button_extended_options.setArrowType(QtCore.Qt.DownArrow)
        self.button_extended_options.setObjectName("button_extended_options")
        self.gridLayout_4.addWidget(self.button_extended_options, 0, 1, 1, 1)
        self.widget_extended_options = QtGui.QWidget(self.frame_search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_extended_options.sizePolicy().hasHeightForWidth())
        self.widget_extended_options.setSizePolicy(sizePolicy)
        self.widget_extended_options.setMaximumSize(QtCore.QSize(16777215, 0))
        self.widget_extended_options.setObjectName("widget_extended_options")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_extended_options)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.checkBox_3 = QtGui.QCheckBox(self.widget_extended_options)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.checkBox_2 = QtGui.QCheckBox(self.widget_extended_options)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.widget_extended_options)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.label_5 = QtGui.QLabel(self.widget_extended_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.widget_extended_options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)
        self.gridLayout_4.addWidget(self.widget_extended_options, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_search)
        self.movieList = QtGui.QTableView(self.library_view)
        self.movieList.setAlternatingRowColors(True)
        self.movieList.setObjectName("movieList")
        self.verticalLayout.addWidget(self.movieList)
        self.stackedWidget.addWidget(self.library_view)
        self.person_view = QtGui.QWidget()
        self.person_view.setObjectName("person_view")
        self.gridLayout_3 = QtGui.QGridLayout(self.person_view)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtGui.QWidget(self.person_view)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_headshot = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_headshot.sizePolicy().hasHeightForWidth())
        self.l_headshot.setSizePolicy(sizePolicy)
        self.l_headshot.setMinimumSize(QtCore.QSize(98, 140))
        self.l_headshot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.l_headshot.setMargin(4)
        self.l_headshot.setObjectName("l_headshot")
        self.verticalLayout_5.addWidget(self.l_headshot)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_3 = QtGui.QWidget(self.person_view)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.l_person_name = QtGui.QLabel(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_person_name.sizePolicy().hasHeightForWidth())
        self.l_person_name.setSizePolicy(sizePolicy)
        self.l_person_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.l_person_name.setObjectName("l_person_name")
        self.verticalLayout_6.addWidget(self.l_person_name)
        self.person_bio = QtGui.QTextEdit(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.person_bio.sizePolicy().hasHeightForWidth())
        self.person_bio.setSizePolicy(sizePolicy)
        self.person_bio.setMinimumSize(QtCore.QSize(0, 0))
        self.person_bio.setBaseSize(QtCore.QSize(0, 0))
        self.person_bio.setReadOnly(True)
        self.person_bio.setObjectName("person_bio")
        self.verticalLayout_6.addWidget(self.person_bio)
        self.groupBox = QtGui.QGroupBox(self.widget_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6.addWidget(self.groupBox)
        self.gridLayout_3.addWidget(self.widget_3, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.person_view)
        self.movie_view = QtGui.QWidget()
        self.movie_view.setObjectName("movie_view")
        self.gridLayout_2 = QtGui.QGridLayout(self.movie_view)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_img = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_img.sizePolicy().hasHeightForWidth())
        self.l_img.setSizePolicy(sizePolicy)
        self.l_img.setMinimumSize(QtCore.QSize(200, 300))
        self.l_img.setMaximumSize(QtCore.QSize(200, 300))
        self.l_img.setBaseSize(QtCore.QSize(200, 300))
        self.l_img.setFrameShape(QtGui.QFrame.StyledPanel)
        self.l_img.setScaledContents(True)
        self.l_img.setAlignment(QtCore.Qt.AlignCenter)
        self.l_img.setMargin(4)
        self.l_img.setObjectName("l_img")
        self.gridLayout_2.addWidget(self.l_img, 2, 0, 5, 1)
        self.label = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.l_rating = QtGui.QLabel(self.movie_view)
        self.l_rating.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_rating.setFrameShadow(QtGui.QFrame.Plain)
        self.l_rating.setMargin(3)
        self.l_rating.setObjectName("l_rating")
        self.gridLayout_2.addWidget(self.l_rating, 2, 3, 5, 1)
        self.label_9 = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.movie_view)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.movie_view)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 6, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.movie_view)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.l_plot_short_3 = QtGui.QTextBrowser(self.tab_7)
        self.l_plot_short_3.setObjectName("l_plot_short_3")
        self.horizontalLayout_8.addWidget(self.l_plot_short_3)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.l_plot_3 = QtGui.QTextBrowser(self.tab_8)
        self.l_plot_3.setObjectName("l_plot_3")
        self.horizontalLayout_9.addWidget(self.l_plot_3)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.gridLayout_2.addWidget(self.tabWidget, 7, 0, 1, 3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton_6 = QtGui.QPushButton(self.movie_view)
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/draw-triangle3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.label_7 = QtGui.QLabel(self.movie_view)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.pushButton_7 = QtGui.QPushButton(self.movie_view)
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/draw-triangle4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.label_8 = QtGui.QLabel(self.movie_view)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 7, 3, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_4 = QtGui.QCheckBox(self.movie_view)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_10.addWidget(self.checkBox_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.pushButton_9 = QtGui.QPushButton(self.movie_view)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.btn_play = QtGui.QPushButton(self.movie_view)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_10.addWidget(self.btn_play)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 8, 0, 1, 4)
        self.l_length = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_length.sizePolicy().hasHeightForWidth())
        self.l_length.setSizePolicy(sizePolicy)
        self.l_length.setText("")
        self.l_length.setObjectName("l_length")
        self.gridLayout_2.addWidget(self.l_length, 3, 2, 1, 1)
        self.l_countries = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_countries.sizePolicy().hasHeightForWidth())
        self.l_countries.setSizePolicy(sizePolicy)
        self.l_countries.setText("")
        self.l_countries.setObjectName("l_countries")
        self.gridLayout_2.addWidget(self.l_countries, 4, 2, 1, 1)
        self.l_genres = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_genres.sizePolicy().hasHeightForWidth())
        self.l_genres.setSizePolicy(sizePolicy)
        self.l_genres.setText("")
        self.l_genres.setObjectName("l_genres")
        self.gridLayout_2.addWidget(self.l_genres, 5, 2, 1, 1)
        self.box_cast = QtGui.QListWidget(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_cast.sizePolicy().hasHeightForWidth())
        self.box_cast.setSizePolicy(sizePolicy)
        self.box_cast.setFlow(QtGui.QListView.LeftToRight)
        self.box_cast.setProperty("isWrapping", True)
        self.box_cast.setObjectName("box_cast")
        self.gridLayout_2.addWidget(self.box_cast, 6, 2, 1, 1)
        self.box_director = QtGui.QListWidget(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_director.sizePolicy().hasHeightForWidth())
        self.box_director.setSizePolicy(sizePolicy)
        self.box_director.setFlow(QtGui.QListView.LeftToRight)
        self.box_director.setProperty("isWrapping", True)
        self.box_director.setObjectName("box_director")
        self.gridLayout_2.addWidget(self.box_director, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_movie_favourite = QtGui.QPushButton(self.movie_view)
        self.button_movie_favourite.setCursor(QtCore.Qt.PointingHandCursor)
        self.button_movie_favourite.setStyleSheet("*{\n"
"border: none;\n"
"outline: none;\n"
"  margin: 0 0px 0 0px;\n"
"}")
        self.button_movie_favourite.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/favorite_disabled"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/favorite_enabled"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button_movie_favourite.setIcon(icon2)
        self.button_movie_favourite.setCheckable(True)
        self.button_movie_favourite.setChecked(False)
        self.button_movie_favourite.setObjectName("button_movie_favourite")
        self.horizontalLayout_2.addWidget(self.button_movie_favourite)
        self.button_movie_watchlater = QtGui.QPushButton(self.movie_view)
        self.button_movie_watchlater.setCursor(QtCore.Qt.PointingHandCursor)
        self.button_movie_watchlater.setStyleSheet("*{\n"
"border: none;\n"
"outline: none;\n"
"  margin: 0 0px 0 0px;\n"
"}")
        self.button_movie_watchlater.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/clock_disabled"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/clock_enabled"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button_movie_watchlater.setIcon(icon3)
        self.button_movie_watchlater.setCheckable(True)
        self.button_movie_watchlater.setObjectName("button_movie_watchlater")
        self.horizontalLayout_2.addWidget(self.button_movie_watchlater)
        self.l_title = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title.sizePolicy().hasHeightForWidth())
        self.l_title.setSizePolicy(sizePolicy)
        self.l_title.setTextFormat(QtCore.Qt.RichText)
        self.l_title.setObjectName("l_title")
        self.horizontalLayout_2.addWidget(self.l_title)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 4)
        self.stackedWidget.addWidget(self.movie_view)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setStyleSheet("QPushButton{\n"
"text-align:left;\n"
"padding:5 3 5 3px;\n"
"}")
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_back = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_back.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon4)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.btn_forward = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_forward.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forward.setIcon(icon5)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.button_sync = QtGui.QPushButton(self.dockWidgetContents)
        self.button_sync.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sync.setIcon(icon6)
        self.button_sync.setObjectName("button_sync")
        self.horizontalLayout.addWidget(self.button_sync)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_library = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_library.setStyleSheet("")
        self.btn_library.setObjectName("btn_library")
        self.verticalLayout_2.addWidget(self.btn_library)
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.dockWidgetContents)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/favorite_enabled"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon8)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_4.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/clock_enabled"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.toolButton = QtGui.QToolButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setCheckable(True)
        self.toolButton.setChecked(True)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.toolButton)
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.toolButton_2 = QtGui.QToolButton(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(True)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setArrowType(QtCore.Qt.UpArrow)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.toolButton_2)
        self.listWidget_2 = QtGui.QListWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget_2.setObjectName("listWidget_2")
        QtGui.QListWidgetItem(self.listWidget_2)
        self.verticalLayout_2.addWidget(self.listWidget_2)
        spacerItem7 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL("clicked(bool)"), self.listWidget.setVisible)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL("clicked(bool)"), self.listWidget_2.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_extended_options.setText(QtGui.QApplication.translate("MainWindow", "Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "title", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "actor", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "director", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Min. rating:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_headshot.setText(QtGui.QApplication.translate("MainWindow", "HEADSHOT", None, QtGui.QApplication.UnicodeUTF8))
        self.l_person_name.setText(QtGui.QApplication.translate("MainWindow", "NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "OTHER STUFF", None, QtGui.QApplication.UnicodeUTF8))
        self.l_img.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Director:", None, QtGui.QApplication.UnicodeUTF8))
        self.l_rating.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">imdb</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">-</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">ratings</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Countries:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Genres:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Cast:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QtGui.QApplication.translate("MainWindow", "Outline", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QtGui.QApplication.translate("MainWindow", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">+4</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">rating</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "Already watched", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "Annex fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_play.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.l_title.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">hier wär das movie</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_library.setText(QtGui.QApplication.translate("MainWindow", "Library", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Manage Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Favourites", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Watch Later", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "My Lists", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "Favourites", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "Subscribed Lists", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.item(0).setText(QtGui.QApplication.translate("MainWindow", "Favourites", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

import icons_rc
