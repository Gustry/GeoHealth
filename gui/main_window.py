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

from PyQt4.QtGui import QDialog

from GeoHealth.doc.help import *
from GeoHealth.ui.main import Ui_Dialog
from GeoHealth.gui.import_gui.open_shapefile import OpenShapefileWidget
from GeoHealth.gui.import_gui.open_csv import OpenCsv
from GeoHealth.gui.import_gui.raster import OpenRasterWidget
from GeoHealth.gui.import_gui.open_xls_dbf import OpenXlsDbfFileWidget
from GeoHealth.gui.analysis.main_blurring_dialog import MainBlurringDialog
from GeoHealth.gui.analysis.incidence_dialog import IncidenceDialog
from GeoHealth.gui.analysis.density_dialog import DensityDialog
from GeoHealth.gui.analysis.histogram_dialog import HistogramDialog
from GeoHealth.gui.export.csv import CsvExport
from GeoHealth.gui.about import AboutWidget


class MainDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self)
        self.parent = parent
        self.setupUi(self)

        # noinspection PyUnresolvedReferences
        self.menu.clicked.connect(self.expand)
        # noinspection PyUnresolvedReferences
        self.menu.clicked.connect(self.display_content)

        self.content = {
            11: [OpenShapefileWidget(), help_open_shapefile()],
            12: [OpenRasterWidget(), help_open_raster()],
            13: [OpenXlsDbfFileWidget(), help_open_table()],
            14: [OpenCsv(), help_open_csv()],
            15: [OpenCsv(), help_open_xy()],
            21: [MainBlurringDialog(), help_blur()],
            22: [IncidenceDialog(), help_incidence()],
            23: [DensityDialog(), help_density()],
            24: [HistogramDialog()],
            31: [CsvExport(), help_attribute_table()],
            100: [AboutWidget()]
        }

        for content in self.content:
            self.stack.addWidget(self.content[content][0])

            try:
                self.content[content][0].signalAskCloseWindow.connect(
                    self.hide)
            except AttributeError:
                pass

        index = self.content.keys().index(100)
        self.stack.setCurrentIndex(index)
        self.help.hide()

    def expand(self, i):
        self.menu.setExpanded(i, not self.menu.isExpanded(i))

    def display_content(self):
        current_index = self.menu.currentIndex()
        parent = current_index.parent()
        if parent.row() == -1:
            tree_index = current_index.row() * 10 + 10
        else:
            tree_index = current_index.row() + 1 + parent.row() * 10 + 10

        if tree_index in self.content.keys():
            index = self.content.keys().index(tree_index)
        else:
            index = self.content.keys().index(100)

        self.stack.setCurrentIndex(index)
        try:
            self.help.setHtml(self.content[tree_index][1])
            self.help.show()
        except KeyError:
            self.help.hide()
        except IndexError:
            self.help.hide()

        # Try to refresh layers if needed
        widget = self.stack.currentWidget()
        try:
            widget.fill_combobox_layer()
        except AttributeError:
            pass
