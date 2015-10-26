# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wip.ui'
#
# Created: Mon Oct 26 18:06:08 2015
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

class Ui_Wip(object):
    def setupUi(self, Wip):
        Wip.setObjectName(_fromUtf8("Wip"))
        Wip.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Wip)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Wip)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Wip)
        QtCore.QMetaObject.connectSlotsByName(Wip)

    def retranslateUi(self, Wip):
        Wip.setWindowTitle(_translate("Wip", "Form", None))
        self.label.setText(_translate("Wip", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ff0000;\">Work in progress</span></p></body></html>", None))

