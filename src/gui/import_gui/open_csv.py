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

from qgis.PyQt.QtWidgets import QWidget, QMdiArea, QVBoxLayout
from qgis.PyQt.QtCore import pyqtSignal
from qgis.core import QgsProviderRegistry
from qgis.utils import iface


from GeoHealth.src.core.tools import tr


class OpenCsv(QWidget):

    signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenCsv, self).__init__()

        mdi_area = QMdiArea()

        # noinspection PyArgumentList
        dialog = QgsProviderRegistry.instance().createSelectionWidget('delimitedtext')
        dialog.setWindowTitle(tr('Open a CSV'))

        layout = QVBoxLayout(self)
        layout.addWidget(mdi_area)
        mdi_area.addSubWindow(dialog)

        dialog.addVectorLayer.connect(self.success)
        dialog.rejected.connect(self.signalAskCloseWindow.emit)

    def success(self, path, base_name, provider_key):
        iface.addVectorLayer(path, base_name, provider_key)
        self.signalStatus.emit(3, tr('Successful import'))
