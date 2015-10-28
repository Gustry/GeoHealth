# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_csv.ui'
#
# Created: Wed Oct 28 11:11:25 2015
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
        Form.resize(689, 538)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cbx_layer = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_layer.sizePolicy().hasHeightForWidth())
        self.cbx_layer.setSizePolicy(sizePolicy)
        self.cbx_layer.setObjectName(_fromUtf8("cbx_layer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbx_layer)
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
        self.mGroupBox = gui.QgsCollapsibleGroupBox(Form)
        self.mGroupBox.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mGroupBox.sizePolicy().hasHeightForWidth())
        self.mGroupBox.setSizePolicy(sizePolicy)
        self.mGroupBox.setCheckable(True)
        self.mGroupBox.setChecked(False)
        self.mGroupBox.setCollapsed(True)
        self.mGroupBox.setSaveCollapsedState(False)
        self.mGroupBox.setObjectName(_fromUtf8("mGroupBox"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.mGroupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(7, 36, 253, 50))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton = QtGui.QRadioButton(self.formLayoutWidget_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_4.addWidget(self.radioButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.radioButton_2 = QtGui.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.mGroupBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

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
        self.mGroupBox.setTitle(_translate("Form", "Export geometry", None))
        self.label_4.setText(_translate("Form", "Format", None))
        self.radioButton.setText(_translate("Form", "As XY", None))
        self.radioButton_2.setText(_translate("Form", "As YX", None))
        self.label_5.setText(_translate("Form", "CRS", None))

from qgis import gui
