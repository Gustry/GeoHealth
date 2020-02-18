# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autocorrelation.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from qgis.PyQt import QtCore, QtGui

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

class Ui_Autocorrelation(object):
    def setupUi(self, Autocorrelation):
        Autocorrelation.setObjectName(_fromUtf8("Autocorrelation"))
        Autocorrelation.setWindowModality(QtCore.Qt.NonModal)
        Autocorrelation.resize(674, 462)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Autocorrelation.sizePolicy().hasHeightForWidth())
        Autocorrelation.setSizePolicy(sizePolicy)
        Autocorrelation.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout = QtGui.QVBoxLayout(Autocorrelation)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Autocorrelation)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.cbx_aggregation_layer = QgsMapLayerComboBox(Autocorrelation)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_aggregation_layer.sizePolicy().hasHeightForWidth())
        self.cbx_aggregation_layer.setSizePolicy(sizePolicy)
        self.cbx_aggregation_layer.setObjectName(_fromUtf8("cbx_aggregation_layer"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbx_aggregation_layer)
        self.label_4 = QtGui.QLabel(Autocorrelation)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cbx_indicator_field = QgsFieldComboBox(Autocorrelation)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_indicator_field.sizePolicy().hasHeightForWidth())
        self.cbx_indicator_field.setSizePolicy(sizePolicy)
        self.cbx_indicator_field.setObjectName(_fromUtf8("cbx_indicator_field"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbx_indicator_field)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.le_output_filepath = QtGui.QLineEdit(Autocorrelation)
        self.le_output_filepath.setObjectName(_fromUtf8("le_output_filepath"))
        self.horizontalLayout_6.addWidget(self.le_output_filepath)
        self.button_browse = QtGui.QPushButton(Autocorrelation)
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.horizontalLayout_6.addWidget(self.button_browse)
        self.formLayout.setLayout(12, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_3 = QtGui.QLabel(Autocorrelation)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_3)
        self.cbx_contiguity = QtGui.QComboBox(Autocorrelation)
        self.cbx_contiguity.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_contiguity.sizePolicy().hasHeightForWidth())
        self.cbx_contiguity.setSizePolicy(sizePolicy)
        self.cbx_contiguity.setMinimumSize(QtCore.QSize(104, 0))
        self.cbx_contiguity.setObjectName(_fromUtf8("cbx_contiguity"))
        self.cbx_contiguity.addItem(_fromUtf8(""))
        self.cbx_contiguity.addItem(_fromUtf8(""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.cbx_contiguity)
        self.label_8 = QtGui.QLabel(Autocorrelation)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout.addLayout(self.formLayout)
        self.button_box_ok = QtGui.QDialogButtonBox(Autocorrelation)
        self.button_box_ok.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box_ok.setObjectName(_fromUtf8("button_box_ok"))
        self.verticalLayout.addWidget(self.button_box_ok)

        self.retranslateUi(Autocorrelation)
        QtCore.QObject.connect(self.cbx_aggregation_layer, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.cbx_indicator_field.setLayer)
        QtCore.QMetaObject.connectSlotsByName(Autocorrelation)

    def retranslateUi(self, Autocorrelation):
        Autocorrelation.setWindowTitle(_translate("Autocorrelation", "Autocorrelation", None))
        self.label.setText(_translate("Autocorrelation", "Layer", None))
        self.label_4.setText(_translate("Autocorrelation", "Field", None))
        self.le_output_filepath.setPlaceholderText(_translate("Autocorrelation", "Save to temporary file", None))
        self.button_browse.setText(_translate("Autocorrelation", "Browse", None))
        self.label_3.setText(_translate("Autocorrelation", "Contiguity", None))
        self.cbx_contiguity.setItemText(0, _translate("Autocorrelation", "Queen", None))
        self.cbx_contiguity.setItemText(1, _translate("Autocorrelation", "Rook", None))
        self.label_8.setText(_translate("Autocorrelation", "Output", None))

from qgis.gui import QgsFieldComboBox
from qgis.gui import QgsMapLayerComboBox
