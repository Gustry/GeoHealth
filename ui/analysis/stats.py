# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created: Sun Apr 10 16:51:01 2016
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

class Ui_Stats(object):
    def setupUi(self, Stats):
        Stats.setObjectName(_fromUtf8("Stats"))
        Stats.resize(820, 728)
        Stats.setWindowTitle(_fromUtf8("Form"))
        self.verticalLayout = QtGui.QVBoxLayout(Stats)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.comboBox_blurredLayer = QgsMapLayerComboBox(Stats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_blurredLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_blurredLayer.setSizePolicy(sizePolicy)
        self.comboBox_blurredLayer.setObjectName(_fromUtf8("comboBox_blurredLayer"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox_blurredLayer)
        self.label = QtGui.QLabel(Stats)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox_statsLayer = QgsMapLayerComboBox(Stats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_statsLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_statsLayer.setSizePolicy(sizePolicy)
        self.comboBox_statsLayer.setObjectName(_fromUtf8("comboBox_statsLayer"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBox_statsLayer)
        self.label_2 = QtGui.QLabel(Stats)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_progressStats = QtGui.QLabel(Stats)
        self.label_progressStats.setText(_fromUtf8("progress"))
        self.label_progressStats.setObjectName(_fromUtf8("label_progressStats"))
        self.verticalLayout.addWidget(self.label_progressStats)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBar_stats = QtGui.QProgressBar(Stats)
        self.progressBar_stats.setProperty("value", 0)
        self.progressBar_stats.setObjectName(_fromUtf8("progressBar_stats"))
        self.horizontalLayout_2.addWidget(self.progressBar_stats)
        self.buttonBox_stats = QtGui.QDialogButtonBox(Stats)
        self.buttonBox_stats.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox_stats.setCenterButtons(False)
        self.buttonBox_stats.setObjectName(_fromUtf8("buttonBox_stats"))
        self.horizontalLayout_2.addWidget(self.buttonBox_stats)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Stats)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_saveTable = QtGui.QPushButton(Stats)
        self.pushButton_saveTable.setObjectName(_fromUtf8("pushButton_saveTable"))
        self.horizontalLayout_3.addWidget(self.pushButton_saveTable)
        self.pushButton_saveYValues = QtGui.QPushButton(Stats)
        self.pushButton_saveYValues.setObjectName(_fromUtf8("pushButton_saveYValues"))
        self.horizontalLayout_3.addWidget(self.pushButton_saveYValues)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidget = QtGui.QTableWidget(Stats)
        self.tableWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.layout_plot = QtGui.QVBoxLayout()
        self.layout_plot.setObjectName(_fromUtf8("layout_plot"))
        self.horizontalLayout.addLayout(self.layout_plot)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Stats)
        QtCore.QMetaObject.connectSlotsByName(Stats)

    def retranslateUi(self, Stats):
        self.label.setText(_translate("Stats", "Blurred layer", None))
        self.label_2.setText(_translate("Stats", "Stats layer", None))
        self.pushButton_saveTable.setText(_translate("Stats", "Save table", None))
        self.pushButton_saveYValues.setText(_translate("Stats", "Save Y values", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Stats", "Parameter", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Stats", "Value", None))

from qgis.gui import QgsMapLayerComboBox
from GeoPublicHealth.resources import resources_rc
