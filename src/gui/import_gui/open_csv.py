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

from qgis.PyQt.QtWidgets import QWidget, QMdiArea, QVBoxLayout
from qgis.PyQt.QtCore import pyqtSignal
from qgis.core import QgsProviderRegistry
from qgis.utils import iface
from qgis.gui import QgisInterface,QgsGui

from GeoPublicHealth.src.core.tools import tr


class OpenCsv(QWidget):

    #signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')
    #signalStatus = pyqtSignal(int, str, name='signalStatus')
    signalAskCloseWindow = pyqtSignal()
    signalStatus = pyqtSignal(int, str)

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenCsv, self).__init__()

        mdi_area = QMdiArea()

        ##Crete popup and select

        # noinspection PyArgumentList
        dialog=QgsGui.providerGuiRegistry().sourceSelectProviders('delimitedtext')[0].createDataSourceWidget()
        #https://github.com/qgis/QGIS/commit/80b5b0aed0ef5fef51fcc757fd82043ea768770f
        #dialog = QgsProviderRegistry.instance().createSelectionWidget('delimitedtext')
        #dialog=iface.mainWindow()
        #dialog.setWindowTitle(tr('Open a CSV'))

        layout = QVBoxLayout(self)
        layout.addWidget(mdi_area)
        mdi_area.addSubWindow(dialog)

        #Got and error, addVectorLayer is under QgsInterfaces
        #self.success(str,str,str)
        #self.addVectorLayer.connect([str,str,str])
        dialog.addVectorLayer[str, str, str].connect(self.success)
        #dialog.rejected.connect(self.signalAskCloseWindow.emit)

    def success(self, path, base_name, provider_key):
        iface.addVectorLayer(path, base_name, provider_key)
        self.signalStatus.emit(3, tr('Successful import'))
