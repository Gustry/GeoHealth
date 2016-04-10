# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_csv.ui'
#
# Created: Sun Apr 10 15:43:44 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(577, 333)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tab_delimiter = QtGui.QRadioButton(Form)
        self.tab_delimiter.setChecked(True)
        self.tab_delimiter.setObjectName(_fromUtf8("tab_delimiter"))
        self.horizontalLayout_2.addWidget(self.tab_delimiter)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comma_delimiter = QtGui.QRadioButton(Form)
        self.comma_delimiter.setObjectName(_fromUtf8("comma_delimiter"))
        self.horizontalLayout_2.addWidget(self.comma_delimiter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pipe_delimiter = QtGui.QRadioButton(Form)
        self.pipe_delimiter.setObjectName(_fromUtf8("pipe_delimiter"))
        self.horizontalLayout_2.addWidget(self.pipe_delimiter)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.semicolon_delimiter = QtGui.QRadioButton(Form)
        self.semicolon_delimiter.setObjectName(_fromUtf8("semicolon_delimiter"))
        self.horizontalLayout_2.addWidget(self.semicolon_delimiter)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.le_output = QtGui.QLineEdit(Form)
        self.le_output.setInputMask(_fromUtf8(""))
        self.le_output.setText(_fromUtf8(""))
        self.le_output.setReadOnly(True)
        self.le_output.setPlaceholderText(_fromUtf8(""))
        self.le_output.setObjectName(_fromUtf8("le_output"))
        self.horizontalLayout_3.addWidget(self.le_output)
        self.bt_browse = QtGui.QPushButton(Form)
        self.bt_browse.setObjectName(_fromUtf8("bt_browse"))
        self.horizontalLayout_3.addWidget(self.bt_browse)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.cbx_layer = QgsMapLayerComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_layer.sizePolicy().hasHeightForWidth())
        self.cbx_layer.setSizePolicy(sizePolicy)
        self.cbx_layer.setObjectName(_fromUtf8("cbx_layer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbx_layer)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem3 = QtGui.QSpacerItem(20, 189, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_3.setText(_translate("Form", "Layer", None))
        self.label.setText(_translate("Form", "Delimiter", None))
        self.tab_delimiter.setText(_translate("Form", "tab", None))
        self.comma_delimiter.setText(_translate("Form", "comma", None))
        self.pipe_delimiter.setText(_translate("Form", "pipe", None))
        self.semicolon_delimiter.setText(_translate("Form", "semicolon", None))
        self.label_2.setText(_translate("Form", "Output", None))
        self.bt_browse.setText(_translate("Form", "Browse", None))

from qgis.gui import QgsMapLayerComboBox
