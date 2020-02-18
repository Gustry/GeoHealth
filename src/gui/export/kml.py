# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoPublicHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
         copyright            : (C) 2014 by Etienne Trimaille, (C) 2017 by
        Rachel Gorée et Christophe Révillion
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


import codecs
from qgis.PyQt.QtWidgets import QWidget, QDialogButtonBox, QFileDialog
from qgis.PyQt.QtCore import pyqtSignal

from qgis.core import QgsMapLayerProxyModel
from qgis.core import QgsVectorFileWriter

from GeoPublicHealth.src.core.tools import tr
from GeoPublicHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('export', 'export_kml.ui')


class KmlExport(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

    def __init__(self, parent=None):
        self.parent = parent
        super(KmlExport, self).__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(
            self.save_kml)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)
        # noinspection PyUnresolvedReferences
        self.bt_browse.clicked.connect(self.open_file_browser)
        self.cbx_layer.setFilters(QgsMapLayerProxyModel.VectorLayer)

    def open_file_browser(self):
        # noinspection PyArgumentList
        output_file, __ = QFileDialog.getSaveFileName(
            parent=self.parent,
            caption=tr('Export as KML'),
            filter='KML (*.kml)')
        self.le_output.setText(output_file[0])

    def save_kml(self):
        path = self.le_output.text()
        layer = self.cbx_layer.currentLayer()
        QgsVectorFileWriter.writeAsVectorFormat(
            layer, path, 'utf-8', None, 'kml')
        self.signalStatus.emit(3, tr('Successful export to %s' % path))
