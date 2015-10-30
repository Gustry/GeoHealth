# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Oct 30 12:31:51 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(994, 767)
        Dialog.setWindowTitle(_fromUtf8("GeoHealth"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.menu = QtGui.QTreeWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setStyleSheet(_fromUtf8("QTreeWidget{\n"
"    background-color: rgb(69, 69, 69);\n"
"    outline: 0;\n"
"}\n"
"QTreeWidget::item {\n"
"    color: white;\n"
"    padding: 3px;\n"
"}\n"
"QTreeWidget::item::selected {\n"
"    color: black;\n"
"    background-color: rgb(10, 10, 10);\n"
"    padding-right: 0px;\n"
"}\n"
"\n"
"QTreeView::branch { \n"
"    border-image: url(none.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children{\n"
"        background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTreeWidget::item:has-children\n"
"{\n"
"        background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTreeWidget::item:!has-children\n"
"{\n"
"        background-color: rgb(69, 69, 69);\n"
"}"))
        self.menu.setFrameShape(QtGui.QFrame.NoFrame)
        self.menu.setLineWidth(0)
        self.menu.setMidLineWidth(0)
        self.menu.setIconSize(QtCore.QSize(32, 32))
        self.menu.setAutoExpandDelay(1)
        self.menu.setIndentation(9)
        self.menu.setObjectName(_fromUtf8("menu"))
        item_0 = QtGui.QTreeWidgetItem(self.menu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/csv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/shp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon2)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/raster.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon3)
        item_0 = QtGui.QTreeWidgetItem(self.menu)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/gears.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon4)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/blur.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon5)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/incidence.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon6)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon6)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/histogram.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon7)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/sigma.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon8)
        item_0 = QtGui.QTreeWidgetItem(self.menu)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/export.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon9)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon1)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/kml.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon10)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon2)
        self.menu.header().setVisible(False)
        self.menu.header().setStretchLastSection(True)
        self.horizontalLayout_5.addWidget(self.menu)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.messageBar = gui.QgsMessageBar(Dialog)
        self.messageBar.setObjectName(_fromUtf8("messageBar"))
        self.verticalLayout_11.addWidget(self.messageBar)
        self.stack = QtGui.QStackedWidget(Dialog)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.verticalLayout_11.addWidget(self.stack)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.help = QtWebKit.QWebView(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMinimumSize(QtCore.QSize(200, 0))
        self.help.setObjectName(_fromUtf8("help"))
        self.horizontalLayout_2.addWidget(self.help)

        self.retranslateUi(Dialog)
        self.stack.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.menu.headerItem().setText(0, _translate("Dialog", "Menu", None))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        self.menu.topLevelItem(0).setText(0, _translate("Dialog", "Import", None))
        self.menu.topLevelItem(0).child(0).setText(0, _translate("Dialog", "CSV", None))
        self.menu.topLevelItem(0).child(1).setText(0, _translate("Dialog", "SHP", None))
        self.menu.topLevelItem(0).child(2).setText(0, _translate("Dialog", "Raster", None))
        self.menu.topLevelItem(1).setText(0, _translate("Dialog", "Analysis", None))
        self.menu.topLevelItem(1).child(0).setText(0, _translate("Dialog", "Blur", None))
        self.menu.topLevelItem(1).child(1).setText(0, _translate("Dialog", "Incidence", None))
        self.menu.topLevelItem(1).child(2).setText(0, _translate("Dialog", "Density", None))
        self.menu.topLevelItem(1).child(3).setText(0, _translate("Dialog", "Histogram", None))
        self.menu.topLevelItem(1).child(4).setText(0, _translate("Dialog", "Statistics", None))
        self.menu.topLevelItem(2).setText(0, _translate("Dialog", "Export", None))
        self.menu.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Attribute table", None))
        self.menu.topLevelItem(2).child(1).setText(0, _translate("Dialog", "KML", None))
        self.menu.topLevelItem(2).child(2).setText(0, _translate("Dialog", "SHP", None))
        self.menu.setSortingEnabled(__sortingEnabled)

from qgis import gui
from PyQt4 import QtWebKit
from GeoHealth.resources import resources_rc
