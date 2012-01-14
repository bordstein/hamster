# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hamster/gui/qtgui.ui'
#
# Created: Tue Jan 10 12:47:46 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 581)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.explorer = QtGui.QWidget()
        self.explorer.setObjectName("explorer")
        self.gridLayout = QtGui.QGridLayout(self.explorer)
        self.gridLayout.setObjectName("gridLayout")
        self.l_title = QtGui.QLabel(self.explorer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title.sizePolicy().hasHeightForWidth())
        self.l_title.setSizePolicy(sizePolicy)
        self.l_title.setTextFormat(QtCore.Qt.RichText)
        self.l_title.setObjectName("l_title")
        self.gridLayout.addWidget(self.l_title, 0, 0, 1, 4)
        self.l_img = QtGui.QLabel(self.explorer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_img.sizePolicy().hasHeightForWidth())
        self.l_img.setSizePolicy(sizePolicy)
        self.l_img.setMinimumSize(QtCore.QSize(140, 0))
        self.l_img.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.l_img.setBaseSize(QtCore.QSize(0, 0))
        self.l_img.setFrameShape(QtGui.QFrame.StyledPanel)
        self.l_img.setScaledContents(False)
        self.l_img.setAlignment(QtCore.Qt.AlignCenter)
        self.l_img.setMargin(4)
        self.l_img.setObjectName("l_img")
        self.gridLayout.addWidget(self.l_img, 1, 0, 5, 1)
        self.label = QtGui.QLabel(self.explorer)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.l_director = QtGui.QLineEdit(self.explorer)
        self.l_director.setReadOnly(True)
        self.l_director.setObjectName("l_director")
        self.gridLayout.addWidget(self.l_director, 1, 2, 1, 1)
        self.l_rating = QtGui.QLabel(self.explorer)
        self.l_rating.setFrameShape(QtGui.QFrame.NoFrame)
        self.l_rating.setFrameShadow(QtGui.QFrame.Plain)
        self.l_rating.setMargin(3)
        self.l_rating.setObjectName("l_rating")
        self.gridLayout.addWidget(self.l_rating, 1, 3, 5, 1)
        self.label_7 = QtGui.QLabel(self.explorer)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.l_runtime = QtGui.QLineEdit(self.explorer)
        self.l_runtime.setReadOnly(True)
        self.l_runtime.setObjectName("l_runtime")
        self.gridLayout.addWidget(self.l_runtime, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.explorer)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.l_countries = QtGui.QLineEdit(self.explorer)
        self.l_countries.setReadOnly(True)
        self.l_countries.setObjectName("l_countries")
        self.gridLayout.addWidget(self.l_countries, 3, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.explorer)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.l_genres = QtGui.QLineEdit(self.explorer)
        self.l_genres.setReadOnly(True)
        self.l_genres.setObjectName("l_genres")
        self.gridLayout.addWidget(self.l_genres, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.explorer)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.l_cast = QtGui.QLineEdit(self.explorer)
        self.l_cast.setReadOnly(True)
        self.l_cast.setObjectName("l_cast")
        self.gridLayout.addWidget(self.l_cast, 5, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.explorer)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/oxygen/32x32/actions/draw-triangle3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_6 = QtGui.QLabel(self.explorer)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton_2 = QtGui.QPushButton(self.explorer)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../usr/share/icons/oxygen/32x32/actions/draw-triangle4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_5 = QtGui.QLabel(self.explorer)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 6, 3, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtGui.QCheckBox(self.explorer)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.pushButton_5 = QtGui.QPushButton(self.explorer)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_4 = QtGui.QPushButton(self.explorer)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.explorer)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 4)
        self.tabWidget = QtGui.QTabWidget(self.explorer)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_plot_short = QtGui.QTextBrowser(self.tab)
        self.l_plot_short.setObjectName("l_plot_short")
        self.horizontalLayout.addWidget(self.l_plot_short)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_plot = QtGui.QTextBrowser(self.tab_2)
        self.l_plot.setObjectName("l_plot")
        self.horizontalLayout_2.addWidget(self.l_plot)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 6, 0, 1, 3)
        self.stackedWidget.addWidget(self.explorer)
        self.search = QtGui.QWidget()
        self.search.setObjectName("search")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.search)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.l_title_3 = QtGui.QLabel(self.search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title_3.sizePolicy().hasHeightForWidth())
        self.l_title_3.setSizePolicy(sizePolicy)
        self.l_title_3.setTextFormat(QtCore.Qt.RichText)
        self.l_title_3.setObjectName("l_title_3")
        self.verticalLayout_7.addWidget(self.l_title_3)
        self.tabWidget_3 = QtGui.QTabWidget(self.search)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy)
        self.tabWidget_3.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget_3.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtGui.QLabel(self.tab_9)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_9)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.pushButton_8 = QtGui.QPushButton(self.tab_9)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 4, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.tab_9)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_9)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 1, 1, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.tab_9)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 1, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_9)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.tab_9)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 4, 1, 1)
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtGui.QLabel(self.tab_10)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.tab_10)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 3)
        self.tabWidget_3.addTab(self.tab_10, "")
        self.verticalLayout_7.addWidget(self.tabWidget_3)
        self.tableWidget = QtGui.QTableWidget(self.search)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.stackedWidget.addWidget(self.search)
        self.lists = QtGui.QWidget()
        self.lists.setObjectName("lists")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.lists)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.l_title_2 = QtGui.QLabel(self.lists)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_title_2.sizePolicy().hasHeightForWidth())
        self.l_title_2.setSizePolicy(sizePolicy)
        self.l_title_2.setTextFormat(QtCore.Qt.RichText)
        self.l_title_2.setObjectName("l_title_2")
        self.verticalLayout_5.addWidget(self.l_title_2)
        self.tableView_2 = QtGui.QTableView(self.lists)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_5.addWidget(self.tableView_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_7 = QtGui.QPushButton(self.lists)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_6 = QtGui.QPushButton(self.lists)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.lists)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 30))
        self.menubar.setObjectName("menubar")
        self.menuSync = QtGui.QMenu(self.menubar)
        self.menuSync.setObjectName("menuSync")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget_2 = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget_2.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget_2.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_bar = QtGui.QLineEdit(self.tab_3)
        self.search_bar.setText("")
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout_2.addWidget(self.search_bar)
        self.tableView = QtGui.QTableView(self.tab_3)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.treeWidget_2 = QtGui.QTreeWidget(self.tab_4)
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget_2)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout_6.addWidget(self.treeWidget_2)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtGui.QTreeWidget(self.tab_6)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.horizontalLayout_4.addWidget(self.tabWidget_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_sync_now = QtGui.QAction(MainWindow)
        self.action_sync_now.setObjectName("action_sync_now")
        self.menuSync.addAction(self.action_sync_now)
        self.menubar.addAction(self.menuSync.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget_2, QtCore.SIGNAL("currentChanged(int)"), self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Movie Hamster", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Length:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Countries:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Genres:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Cast:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">+4</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">rating</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Already watched", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "View later", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Annex fetch", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Outline", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Comments", None, QtGui.QApplication.UnicodeUTF8))
        self.l_title_3.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Search for movies</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MainWindow", "Go!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("MainWindow", "Actor", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("MainWindow", "Director", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Min. Rating:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QtGui.QApplication.translate("MainWindow", "easy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MainWindow", "Go!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Use tags \"cast\", \"title\", \"plot\", \"rating\", and \"director\" to search for fields", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QtGui.QApplication.translate("MainWindow", "nice", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Cast", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Votes", None, QtGui.QApplication.UnicodeUTF8))
        self.l_title_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Name der Liste</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSync.setTitle(QtGui.QApplication.translate("MainWindow", "Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.search_bar.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Search...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Movie Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "By Genre", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Action", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Adventure", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "By Actor", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Johnny Depp", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Search Movies", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "List", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "My Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Watch later", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Loved", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Top Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Top unwatched", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Top imdb rated", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Recently upvoted", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Movie Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.action_sync_now.setText(QtGui.QApplication.translate("MainWindow", "Sync now", None, QtGui.QApplication.UnicodeUTF8))
