# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moviehamster/gui/qtgui.ui'
#
# Created: Mon Jan 16 10:04:59 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 654)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(55,55,55);\n"
"    color: rgb(188, 203, 215);\n"
"}\n"
"\n"
"/* push buttons */\n"
"QPushButton:focus {\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"/* horizontal scroll bar */\n"
"QScrollBar:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     height: 15px;\n"
"     margin: 0px 20px 0 20px;\n"
" }\n"
" QScrollBar::handle:horizontal {\n"
"     background: white;\n"
"     min-width: 20px;\n"
" }\n"
" QScrollBar::add-line:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     width: 20px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"     border: 2px solid grey;\n"
"     background: #32CC99;\n"
"     width: 20px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"/* vertical scroll  bar */\n"
"  QScrollBar:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #32CC99;\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"  QScrollBar::handle:vertical {\n"
"      background: white;\n"
"      min-height: 20px;\n"
"  }\n"
"  QScrollBar::add-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #32CC99;\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"  QScrollBar::sub-line:vertical {\n"
"      border: 2px solid grey;\n"
"      background: #32CC99;\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"  QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"      border: 2px solid grey;\n"
"      width: 3px;\n"
"      height: 3px;\n"
"      background: white;\n"
"  }\n"
"\n"
"  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"\n"
"/* table view */\n"
"QTableView{\n"
"    font: 12pt \"Ubuntu\";\n"
"    color: rgb(188, 203, 215);\n"
"background-color: rgb(55,55,55);\n"
"     alternate-background-color: rgb(49, 49, 49);\n"
"     selection-background-color: rgb(0, 0, 127);\n"
" }\n"
"\n"
"/*  tab bar */\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     alignment: center;\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }")
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
        self.widget = QtGui.QWidget(self.library_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filter = QtGui.QLineEdit(self.widget)
        self.filter.setObjectName("filter")
        self.horizontalLayout_3.addWidget(self.filter)
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.verticalLayout.addWidget(self.widget)
        self.movieList = QtGui.QTableView(self.library_view)
        self.movieList.setStyleSheet("")
        self.movieList.setAlternatingRowColors(True)
        self.movieList.setObjectName("movieList")
        self.verticalLayout.addWidget(self.movieList)
        self.stackedWidget.addWidget(self.library_view)
        self.person_view = QtGui.QWidget()
        self.person_view.setObjectName("person_view")
        self.gridLayout_3 = QtGui.QGridLayout(self.person_view)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_headshot = QtGui.QLabel(self.person_view)
        self.l_headshot.setObjectName("l_headshot")
        self.gridLayout_3.addWidget(self.l_headshot, 0, 0, 1, 1)
        self.l_person_name = QtGui.QLabel(self.person_view)
        self.l_person_name.setObjectName("l_person_name")
        self.gridLayout_3.addWidget(self.l_person_name, 0, 1, 1, 1)
        self.person_bio = QtGui.QTextEdit(self.person_view)
        self.person_bio.setReadOnly(True)
        self.person_bio.setObjectName("person_bio")
        self.gridLayout_3.addWidget(self.person_bio, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.person_view)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3.addWidget(self.groupBox, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.person_view)
        self.movie_view = QtGui.QWidget()
        self.movie_view.setObjectName("movie_view")
        self.gridLayout_2 = QtGui.QGridLayout(self.movie_view)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.l_title = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title.sizePolicy().hasHeightForWidth())
        self.l_title.setSizePolicy(sizePolicy)
        self.l_title.setTextFormat(QtCore.Qt.RichText)
        self.l_title.setObjectName("l_title")
        self.gridLayout_2.addWidget(self.l_title, 0, 0, 1, 4)
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
        self.gridLayout_2.addWidget(self.l_img, 1, 0, 5, 1)
        self.label = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.l_rating = QtGui.QLabel(self.movie_view)
        self.l_rating.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_rating.setFrameShadow(QtGui.QFrame.Plain)
        self.l_rating.setMargin(3)
        self.l_rating.setObjectName("l_rating")
        self.gridLayout_2.addWidget(self.l_rating, 1, 3, 5, 1)
        self.label_9 = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.movie_view)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.movie_view)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.tabWidget, 6, 0, 1, 3)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
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
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 6, 3, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_4 = QtGui.QCheckBox(self.movie_view)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_10.addWidget(self.checkBox_4)
        self.pushButton_8 = QtGui.QPushButton(self.movie_view)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.pushButton_9 = QtGui.QPushButton(self.movie_view)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9)
        self.pushButton_10 = QtGui.QPushButton(self.movie_view)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_10.addWidget(self.pushButton_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 7, 0, 1, 4)
        self.btn_director = QtGui.QPushButton(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_director.sizePolicy().hasHeightForWidth())
        self.btn_director.setSizePolicy(sizePolicy)
        self.btn_director.setText("")
        self.btn_director.setObjectName("btn_director")
        self.gridLayout_2.addWidget(self.btn_director, 1, 2, 1, 1)
        self.l_length = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_length.sizePolicy().hasHeightForWidth())
        self.l_length.setSizePolicy(sizePolicy)
        self.l_length.setText("")
        self.l_length.setObjectName("l_length")
        self.gridLayout_2.addWidget(self.l_length, 2, 2, 1, 1)
        self.l_countries = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_countries.sizePolicy().hasHeightForWidth())
        self.l_countries.setSizePolicy(sizePolicy)
        self.l_countries.setText("")
        self.l_countries.setObjectName("l_countries")
        self.gridLayout_2.addWidget(self.l_countries, 3, 2, 1, 1)
        self.l_genres = QtGui.QLabel(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_genres.sizePolicy().hasHeightForWidth())
        self.l_genres.setSizePolicy(sizePolicy)
        self.l_genres.setText("")
        self.l_genres.setObjectName("l_genres")
        self.gridLayout_2.addWidget(self.l_genres, 4, 2, 1, 1)
        self.scrollable_box_cast = QtGui.QScrollArea(self.movie_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollable_box_cast.sizePolicy().hasHeightForWidth())
        self.scrollable_box_cast.setSizePolicy(sizePolicy)
        self.scrollable_box_cast.setWidgetResizable(True)
        self.scrollable_box_cast.setObjectName("scrollable_box_cast")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.box_cast = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.box_cast.setContentsMargins(3, 3, 3, 3)
        self.box_cast.setObjectName("box_cast")
        self.scrollable_box_cast.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollable_box_cast, 5, 2, 1, 1)
        self.stackedWidget.addWidget(self.movie_view)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon2)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)
        self.btn_forward = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_forward.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forward.setIcon(icon3)
        self.btn_forward.setObjectName("btn_forward")
        self.horizontalLayout.addWidget(self.btn_forward)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.button_sync = QtGui.QPushButton(self.dockWidgetContents)
        self.button_sync.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sync.setIcon(icon4)
        self.button_sync.setObjectName("button_sync")
        self.horizontalLayout.addWidget(self.button_sync)
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btn_library = QtGui.QPushButton(self.dockWidgetContents)
        self.btn_library.setObjectName("btn_library")
        self.verticalLayout_2.addWidget(self.btn_library)
        self.listView = QtGui.QListView(self.dockWidgetContents)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "director", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "actor", None, QtGui.QApplication.UnicodeUTF8))
        self.l_headshot.setText(QtGui.QApplication.translate("MainWindow", "HEADSHOT", None, QtGui.QApplication.UnicodeUTF8))
        self.l_person_name.setText(QtGui.QApplication.translate("MainWindow", "NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "OTHER STUFF", None, QtGui.QApplication.UnicodeUTF8))
        self.l_title.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">hier wär das movie</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
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
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "View later", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "Annex fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_library.setText(QtGui.QApplication.translate("MainWindow", "Library", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
