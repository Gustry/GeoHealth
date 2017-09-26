# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtGui import (
    QWidget, QDialogButtonBox, QFileDialog, QApplication)
from PyQt4.QtCore import pyqtSignal, QSettings, QVariant

from GeoHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('analysis', 'accessibility.ui')


class AccessibilityWidget(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')

    def __init__(self, parent=None):
        self.parent = parent
        super(AccessibilityWidget, self).__init__()
        self.setupUi(self)
