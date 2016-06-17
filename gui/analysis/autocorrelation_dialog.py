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

from tempfile import NamedTemporaryFile
from PyQt4.QtGui import \
    QDialog,\
    QDialogButtonBox,\
    QTableWidgetItem,\
    QMessageBox,\
    QApplication
from PyQt4.QtCore import QSize, QVariant, Qt, pyqtSignal
from PyQt4.QtGui import QFileDialog

from qgis.utils import QGis
from qgis.gui import \
    QgsMapLayerProxyModel,\
    QgsFieldProxyModel
from qgis.core import \
    QgsField,\
    QgsVectorGradientColorRampV2,\
    QgsGraduatedSymbolRendererV2,\
    QgsSymbolV2,\
    QgsVectorFileWriter,\
    QgsFeature,\
    QgsVectorLayer,\
    QgsMapLayerRegistry,\
    QgsGeometry

from matplotlib.backends.backend_qt4agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from GeoPublicHealth.core.graph_toolbar import CustomNavigationToolbar
from GeoPublicHealth.core.tools import display_message_bar, tr
from GeoPublicHealth.core.exceptions import \
    GeoPublicHealthException,\
    NoLayerProvidedException,\
    DifferentCrsException,\
    FieldExistingException,\
    FieldException,\
    NotANumberException
from GeoPublicHealth.core.stats import Stats

from GeoPublicHealth.ui.analysis.autocorrelation import Ui_Autocorrelation

class CommonAutocorrelationDialog(QDialog):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')

    def __init__(self, parent=None):
        """Constructor.

        Base class for Incidence and Density dialogs.

        use_area : If you use the area of the polygon or the population field.
        use_point_layer : If you a point a layer, or a field in the polygon
         layer.
        """
        self.parent = parent
        QDialog.__init__(self, parent)
        self.name_field = None
        self.admin_layer = None
        self.figure = None
        self.canvas = None
        self.toolbar = None
        self.output_file_path = None
        self.output_layer = None

        # Settings
        self.use_area = None

    def setup_ui(self):
        # Connect slot.
        # noinspection PyUnresolvedReferences
        self.button_browse.clicked.connect(self.open_file_browser)

        self.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_stats)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.hide)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)

        # Add items in symbology
        self.cbx_mode.addItem(
            'Quantile (equal count)', QgsGraduatedSymbolRendererV2.Quantile)
        self.cbx_mode.addItem(
            'Natural breaks', QgsGraduatedSymbolRendererV2.Jenks)
        self.cbx_mode.addItem(
            'Standard deviation', QgsGraduatedSymbolRendererV2.StdDev)
        self.cbx_mode.addItem(
            'Pretty breaks', QgsGraduatedSymbolRendererV2.Pretty)
        self.cbx_mode.addItem(
            'Equal interval', QgsGraduatedSymbolRendererV2.EqualInterval)

        # Setup the graph.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)

        self.cbx_aggregation_layer.setFilters(QgsMapLayerProxyModel.PolygonLayer)


        self.cbx_indicator_field.setFilters(QgsFieldProxyModel.Numeric)
        self.cbx_indicator_field.setLayer(self.cbx_aggregation_layer.currentLayer())
        self.cbx_aggregation_layer.layerChanged.connect(self.cbx_indicator_field.setLayer)

    def open_file_browser(self):
        output_file = QFileDialog.getSaveFileNameAndFilter(
            self.parent, tr('Save shapefile'), filter='SHP (*.shp)')
        self.le_output_filepath.setText(output_file[0])

    def add_symbology(self):
        low_color = self.color_low_value.color()
        high_color = self.color_high_value.color()
        index = self.cbx_mode.currentIndex()
        mode = self.cbx_mode.itemData(index)
        classes = self.spinBox_classes.value()

        # Compute renderer
        # noinspection PyArgumentList
        symbol = QgsSymbolV2.defaultSymbol(QGis.Polygon)

        color_ramp = QgsVectorGradientColorRampV2(low_color, high_color)
        # noinspection PyArgumentList
        renderer = QgsGraduatedSymbolRendererV2.createRenderer(
            self.output_layer,
            self.name_field,
            classes,
            mode,
            symbol,
            color_ramp)
        self.output_layer.setRendererV2(renderer)

class AutocorrelationDialog(CommonAutocorrelationDialog, Ui_Autocorrelation):
    def __init__(self, parent=None):
        """Constructor."""
        CommonAutocorrelationDialog.__init__(self, parent)
        # noinspection PyArgumentList
        Ui_Autocorrelation.setupUi(self, self)

        self.use_area = False

        self.setup_ui()

    def run_stats(self):
        """Main function which do the process."""
        CommonAutocorrelationDialog.run_stats(self)
