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

from GeoHealth.ui.main import Ui_Dialog
from GeoHealth.gui.import_gui.open_csv import OpenCsv
from GeoHealth.gui.import_gui.raster import OpenRasterWidget
from GeoHealth.gui.analysis.main_blurring_dialog import MainBlurringDialog
from GeoHealth.gui.import_gui.open_shapefile import OpenShapefileWidget
from GeoHealth.gui.analysis.incidence_dialog import IncidenceDialog
from GeoHealth.gui.analysis.density_dialog import DensityDialog
from GeoHealth.gui.analysis.histogram_dialog import HistogramDialog
from GeoHealth.gui.export.csv import CsvExport
from GeoHealth.gui.about import AboutWidget
from GeoHealth.gui.wip import WipWidget


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
            11: OpenCsv(),
            12: OpenShapefileWidget(),
            13: OpenRasterWidget(),
            21: MainBlurringDialog(),
            22: IncidenceDialog(),
            23: DensityDialog(),
            24: HistogramDialog(),
            31: CsvExport(),
            41: AboutWidget(),
            100: WipWidget()
        }

        for content in self.content:
            self.stack.addWidget(self.content[content])

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
