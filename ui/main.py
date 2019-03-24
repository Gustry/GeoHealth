# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Dec 17 22:51:13 2015
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
        Dialog.setWindowTitle(_fromUtf8("GeoPublicHealth"))
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
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.page)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)
        self.stack.addWidget(self.page)
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
        self.stack.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.menu.headerItem().setText(0, _translate("Dialog", "Menu", None))

from qgis import gui
from PyQt4 import QtWebKit
