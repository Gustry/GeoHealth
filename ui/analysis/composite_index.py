# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'composite_index.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Composite_Index(object):
    def setupUi(self, Composite_Index):
        Composite_Index.setObjectName(_fromUtf8("Composite_Index"))
        Composite_Index.resize(651, 695)
        self.verticalLayout = QtGui.QVBoxLayout(Composite_Index)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Composite_Index)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.cbx_aggregation_layer = QgsMapLayerComboBox(Composite_Index)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_aggregation_layer.sizePolicy().hasHeightForWidth())
        self.cbx_aggregation_layer.setSizePolicy(sizePolicy)
        self.cbx_aggregation_layer.setObjectName(_fromUtf8("cbx_aggregation_layer"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbx_aggregation_layer)
        self.label_4 = QtGui.QLabel(Composite_Index)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cbx_indicator_field = QgsFieldComboBox(Composite_Index)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_indicator_field.sizePolicy().hasHeightForWidth())
        self.cbx_indicator_field.setSizePolicy(sizePolicy)
        self.cbx_indicator_field.setObjectName(_fromUtf8("cbx_indicator_field"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbx_indicator_field)
        self.label_3 = QtGui.QLabel(Composite_Index)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_3)
        self.le_new_column = QtGui.QLineEdit(Composite_Index)
        self.le_new_column.setMaxLength(10)
        self.le_new_column.setObjectName(_fromUtf8("le_new_column"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.le_new_column)
        self.label_8 = QtGui.QLabel(Composite_Index)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.le_output_filepath = QtGui.QLineEdit(Composite_Index)
        self.le_output_filepath.setObjectName(_fromUtf8("le_output_filepath"))
        self.horizontalLayout_6.addWidget(self.le_output_filepath)
        self.button_browse = QtGui.QPushButton(Composite_Index)
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.horizontalLayout_6.addWidget(self.button_browse)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.symbology = QgsCollapsibleGroupBox(Composite_Index)
        self.symbology.setCheckable(True)
        self.symbology.setProperty("collapsed", False)
        self.symbology.setObjectName(_fromUtf8("symbology"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.symbology)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.symbology)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.color_low_value = QgsColorButtonV2(self.symbology)
        self.color_low_value.setProperty("color", QtGui.QColor(255, 246, 246))
        self.color_low_value.setObjectName(_fromUtf8("color_low_value"))
        self.horizontalLayout_3.addWidget(self.color_low_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.symbology)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.color_high_value = QgsColorButtonV2(self.symbology)
        self.color_high_value.setProperty("color", QtGui.QColor(202, 33, 36))
        self.color_high_value.setObjectName(_fromUtf8("color_high_value"))
        self.horizontalLayout_3.addWidget(self.color_high_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.symbology)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBox_classes = QtGui.QSpinBox(self.symbology)
        self.spinBox_classes.setMinimum(1)
        self.spinBox_classes.setProperty("value", 5)
        self.spinBox_classes.setObjectName(_fromUtf8("spinBox_classes"))
        self.horizontalLayout_4.addWidget(self.spinBox_classes)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.symbology)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.cbx_mode = QtGui.QComboBox(self.symbology)
        self.cbx_mode.setObjectName(_fromUtf8("cbx_mode"))
        self.horizontalLayout_4.addWidget(self.cbx_mode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.symbology)
        self.button_box_ok = QtGui.QDialogButtonBox(Composite_Index)
        self.button_box_ok.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box_ok.setObjectName(_fromUtf8("button_box_ok"))
        self.verticalLayout.addWidget(self.button_box_ok)

        self.retranslateUi(Composite_Index)
        QtCore.QObject.connect(self.cbx_aggregation_layer, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.cbx_indicator_field.setLayer)
        QtCore.QMetaObject.connectSlotsByName(Composite_Index)

    def retranslateUi(self, Composite_Index):
        Composite_Index.setWindowTitle(_translate("Composite_Index", "Incidence", None))
        self.label.setText(_translate("Composite_Index", "Layer", None))
        self.label_4.setText(_translate("Composite_Index", "Indicator field", None))
        self.label_3.setText(_translate("Composite_Index", "New column", None))
        self.le_new_column.setPlaceholderText(_translate("Composite_Index", "UHN", None))
        self.label_8.setText(_translate("Composite_Index", "Output", None))
        self.le_output_filepath.setPlaceholderText(_translate("Composite_Index", "Save to temporary file", None))
        self.button_browse.setText(_translate("Composite_Index", "Browse", None))
        self.symbology.setTitle(_translate("Composite_Index", "Add a symbology", None))
        self.label_9.setText(_translate("Composite_Index", "Low Priority", None))
        self.label_10.setText(_translate("Composite_Index", "High Priority", None))
        self.label_11.setText(_translate("Composite_Index", "Classes", None))
        self.label_12.setText(_translate("Composite_Index", "Mode", None))

from qgis.gui import QgsFieldComboBox
from qgis.gui import QgsMapLayerComboBox
from qgis.gui import QgsCollapsibleGroupBox
from qgis.gui import QgsColorButtonV2
