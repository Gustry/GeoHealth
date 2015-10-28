# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_csv.ui'
#
# Created: Wed Oct 28 14:08:43 2015
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
        Form.resize(563, 358)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cbx_layer = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_layer.sizePolicy().hasHeightForWidth())
        self.cbx_layer.setSizePolicy(sizePolicy)
        self.cbx_layer.setObjectName(_fromUtf8("cbx_layer"))
        self.horizontalLayout.addWidget(self.cbx_layer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.tab_delimiter = QtGui.QRadioButton(Form)
        self.tab_delimiter.setChecked(True)
        self.tab_delimiter.setObjectName(_fromUtf8("tab_delimiter"))
        self.horizontalLayout_2.addWidget(self.tab_delimiter)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comma_delimiter = QtGui.QRadioButton(Form)
        self.comma_delimiter.setObjectName(_fromUtf8("comma_delimiter"))
        self.horizontalLayout_2.addWidget(self.comma_delimiter)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pipe_delimiter = QtGui.QRadioButton(Form)
        self.pipe_delimiter.setObjectName(_fromUtf8("pipe_delimiter"))
        self.horizontalLayout_2.addWidget(self.pipe_delimiter)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.semicolon_delimiter = QtGui.QRadioButton(Form)
        self.semicolon_delimiter.setObjectName(_fromUtf8("semicolon_delimiter"))
        self.horizontalLayout_2.addWidget(self.semicolon_delimiter)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.export_geometry = gui.QgsCollapsibleGroupBox(Form)
        self.export_geometry.setEnabled(False)
        self.export_geometry.setCheckable(True)
        self.export_geometry.setChecked(False)
        self.export_geometry.setCollapsed(True)
        self.export_geometry.setSaveCollapsedState(False)
        self.export_geometry.setObjectName(_fromUtf8("export_geometry"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.export_geometry)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.export_geometry)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.as_xy = QtGui.QRadioButton(self.export_geometry)
        self.as_xy.setChecked(True)
        self.as_xy.setObjectName(_fromUtf8("as_xy"))
        self.horizontalLayout_4.addWidget(self.as_xy)
        self.as_yx = QtGui.QRadioButton(self.export_geometry)
        self.as_yx.setObjectName(_fromUtf8("as_yx"))
        self.horizontalLayout_4.addWidget(self.as_yx)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.export_geometry)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
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
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)

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
        self.export_geometry.setTitle(_translate("Form", "Export geometry", None))
        self.label_4.setText(_translate("Form", "Format", None))
        self.as_xy.setText(_translate("Form", "As XY", None))
        self.as_yx.setText(_translate("Form", "As YX", None))
        self.label_2.setText(_translate("Form", "Output", None))
        self.bt_browse.setText(_translate("Form", "Browse", None))

from qgis import gui
