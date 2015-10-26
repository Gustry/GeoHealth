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
from os.path import splitext, basename
from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog
from qgis.core import QgsMapLayerRegistry, QgsVectorLayer

from GeoHealth.ui.open_shapefile import Ui_Form
from GeoHealth.core.tools import trans


class OpenShapefileWidget(QWidget, Ui_Form):

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenShapefileWidget, self).__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Open).clicked.connect(
            self.open_shapefile)
        # noinspection PyUnresolvedReferences
        self.bt_browse.clicked.connect(self.open_file_browser)

    def open_file_browser(self):
        # noinspection PyArgumentList
        shapefile = QFileDialog.getOpenFileName(
            parent=self.parent,
            caption=trans('Select shapefile'),
            filter='Shapefile (*.shp)')
        self.le_shapefile.setText(shapefile)

    def open_shapefile(self):
        path = self.le_shapefile.text()
        name = basename(splitext(path)[0])
        layer = QgsVectorLayer(path, name, 'ogr')
        # noinspection PyArgumentList
        QgsMapLayerRegistry.instance().addMapLayer(layer)
