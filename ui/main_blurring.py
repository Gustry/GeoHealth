# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_blurring.ui'
#
# Created: Mon Oct 26 19:12:56 2015
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
        Form.resize(590, 562)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tab = QtGui.QTabWidget(Form)
        self.tab.setIconSize(QtCore.QSize(32, 32))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tab_blur = QtGui.QWidget()
        self.tab_blur.setObjectName(_fromUtf8("tab_blur"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_blur)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.blur = BlurWidget(self.tab_blur)
        self.blur.setObjectName(_fromUtf8("blur"))
        self.verticalLayout_5.addWidget(self.blur)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/blur.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_blur, icon, _fromUtf8(""))
        self.tab_stats = QtGui.QWidget()
        self.tab_stats.setObjectName(_fromUtf8("tab_stats"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_stats)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.statistics = StatsWidget(self.tab_stats)
        self.statistics.setObjectName(_fromUtf8("statistics"))
        self.verticalLayout_6.addWidget(self.statistics)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/GeoHealth/resources/sigma.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_stats, icon1, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tab)

        self.retranslateUi(Form)
        self.tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_blur), _translate("Form", "Blur", None))
        self.tab.setTabText(self.tab.indexOf(self.tab_stats), _translate("Form", "Stats", None))

from GeoHealth.gui.stats_dialog import StatsWidget
from GeoHealth.gui.blur_dialog import BlurWidget
from GeoHealth.resources import resources_rc
