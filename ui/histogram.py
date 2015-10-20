# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'histogram.ui'
#
# Created: Tue Oct 20 11:16:09 2015
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

class Ui_Histogram(object):
    def setupUi(self, Histogram):
        Histogram.setObjectName(_fromUtf8("Histogram"))
        Histogram.resize(606, 553)
        self.verticalLayout = QtGui.QVBoxLayout(Histogram)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Histogram)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.cbx_layer = QtGui.QComboBox(Histogram)
        self.cbx_layer.setObjectName(_fromUtf8("cbx_layer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbx_layer)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_box = QtGui.QDialogButtonBox(Histogram)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.verticalLayout.addWidget(self.button_box)
        self.layout_plot = QtGui.QVBoxLayout()
        self.layout_plot.setObjectName(_fromUtf8("layout_plot"))
        self.verticalLayout.addLayout(self.layout_plot)

        self.retranslateUi(Histogram)
        QtCore.QMetaObject.connectSlotsByName(Histogram)

    def retranslateUi(self, Histogram):
        Histogram.setWindowTitle(_translate("Histogram", "Histogram", None))
        self.label.setText(_translate("Histogram", "Layer", None))

