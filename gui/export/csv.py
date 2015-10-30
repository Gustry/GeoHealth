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

import codecs
from PyQt4.QtGui import QWidget, QDialogButtonBox, QFileDialog
from PyQt4.QtCore import pyqtSignal

from qgis.utils import iface
from qgis.core import QgsMapLayer

from GeoHealth.ui.export.export_csv import Ui_Form
from GeoHealth.core.tools import trans


class CsvExport(QWidget, Ui_Form):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')

    def __init__(self, parent=None):
        self.parent = parent
        super(CsvExport, self).__init__()
        self.setupUi(self)
        self.fill_combobox_layer()

        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(
            self.save_csv)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)
        # noinspection PyUnresolvedReferences
        self.bt_browse.clicked.connect(self.open_file_browser)

        self.delimiters = {
            'tab': '    ',
            'pipe': '|',
            'comma': ',',
            'semicolon': ';'
        }

    def fill_combobox_layer(self):
        """Fill combobox about layers."""
        self.cbx_layer.clear()

        for layer in iface.legendInterface().layers():
            if layer.type() == QgsMapLayer.VectorLayer:
                self.cbx_layer.addItem(layer.name(), layer)

    def open_file_browser(self):
        # noinspection PyArgumentList
        output_file = QFileDialog.getSaveFileNameAndFilter(
            parent=self.parent,
            caption=trans('Export as CSV'),
            filter='CSV (*.csv)')
        self.le_output.setText(output_file[0])

    def save_csv(self):
        path = self.le_output.text()
        index = self.cbx_layer.currentIndex()
        layer = self.cbx_layer.itemData(index)
        export_geom = self.export_geometry.isChecked()

        if self.tab_delimiter.isChecked():
            delimiter = self.delimiters['tab']
        elif self.pipe_delimiter.isChecked():
            delimiter = self.delimiters['pipe']
        elif self.semicolon_delimiter.isChecked():
            delimiter = self.delimiters['semicolon']
        else:
            delimiter = self.delimiters['comma']

        csv_file = codecs.open(path, 'w', 'utf-8')

        provider = layer.dataProvider()
        fields = provider.fieldNameMap()

        if export_geom:
            if self.as_xy.isChecked():
                fields.append('X')
                fields.append('Y')
            else:
                fields.append('Y')
                fields.append('X')

        header = u'%s\n' % delimiter.join(fields)
        csv_file.write(header)

        for feature in layer.getFeatures():
            attributes = feature.attributes()
            # Todo Add geometry not finished
            line = u'%s\n' % delimiter.join(attributes)
            csv_file.write(line)

        csv_file.close()
