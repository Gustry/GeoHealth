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

from qgis.gui import QgsMapLayerProxyModel

from GeoHealth.core.tools import tr
from geohealth.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('export', 'export_csv.ui')


class CsvExport(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

    def __init__(self, parent=None):
        self.parent = parent
        super(CsvExport, self).__init__()
        self.setupUi(self)

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

        self.cbx_layer.setFilters(QgsMapLayerProxyModel.VectorLayer)

    def open_file_browser(self):
        # noinspection PyArgumentList
        output_file = QFileDialog.getSaveFileNameAndFilter(
            parent=self.parent,
            caption=tr('Export as CSV'),
            filter='CSV (*.csv)')
        self.le_output.setText(output_file[0])

    def save_csv(self):
        path = self.le_output.text()
        layer = self.cbx_layer.currentLayer()

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

        header = u'%s\n' % delimiter.join(fields)
        csv_file.write(header)

        for feature in layer.getFeatures():
            attributes = feature.attributes()
            line = u'%s\n' % delimiter.join([unicode(i) for i in attributes])
            csv_file.write(line)

        csv_file.close()

        self.signalStatus.emit(3, tr('Successful export to %s' % path))
