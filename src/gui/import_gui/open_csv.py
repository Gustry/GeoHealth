# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoPublicHealth
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

from PyQt4.QtGui import QWidget, QMdiArea, QVBoxLayout
from PyQt4.QtCore import pyqtSignal
from qgis.core import QgsProviderRegistry
from qgis.utils import iface


<<<<<<< HEAD:src/gui/import_gui/open_csv.py
from GeoHealth.src.core.tools import tr
=======
from GeoPublicHealth.core.tools import tr
>>>>>>> Change the files for the new name GeoPublicHealth:gui/import_gui/open_csv.py


class OpenCsv(QWidget):

    signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenCsv, self).__init__()

        mdi_area = QMdiArea()

        # noinspection PyArgumentList
        dialog = QgsProviderRegistry.instance().selectWidget('delimitedtext')
        dialog.setWindowTitle(tr('Open a CSV'))

        layout = QVBoxLayout(self)
        layout.addWidget(mdi_area)
        mdi_area.addSubWindow(dialog)

        dialog.addVectorLayer[str, str, str].connect(self.success)
        dialog.rejected.connect(self.signalAskCloseWindow.emit)

    def success(self, path, base_name, provider_key):
        iface.addVectorLayer(path, base_name, provider_key)
        self.signalStatus.emit(3, tr('Successful import'))
