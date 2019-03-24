# -*- coding: utf-8 -*-
"""
/***************************************************************************

                               GeoPublicHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2016-02-17
        copyright            : (C) 2016 by ePublicHealth
        email                : manuel@epublichealth.co
        
        Based on the work of Geohealth                  
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
from PyQt4.QtCore import QFileInfo, pyqtSignal
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer, QgsProviderRegistry

from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog

from GeoPublicHealth.src.core.tools import tr
from GeoPublicHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('import_ui', 'open_raster.ui')


class OpenRasterWidget(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenRasterWidget, self).__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Open).clicked.connect(
            self.open_raster)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)
        # noinspection PyUnresolvedReferences
        self.bt_browse.clicked.connect(self.open_file_browser)

    def open_file_browser(self):

        # noinspection PyArgumentList
        raster_filter = QgsProviderRegistry.instance().fileRasterFilters()

        # noinspection PyArgumentList
        raster = QFileDialog.getOpenFileName(
            parent=self.parent,
            caption=tr('Select raster'),
            filter=raster_filter)
        self.le_shapefile.setText(raster)

    def open_raster(self):
        path = self.le_shapefile.text()

        file_info = QFileInfo(path)
        layer = QgsRasterLayer(path, file_info.baseName())

        # noinspection PyArgumentList
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        self.signalStatus.emit(3, tr('Successful import from %s' % path))
