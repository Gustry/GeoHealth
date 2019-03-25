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
from PyQt4.QtGui import QFileDialog, QColor

from qgis.utils import QGis
from qgis.gui import \
    QgsMapLayerProxyModel,\
    QgsFieldProxyModel
from qgis.core import \
    QgsField,\
    QgsRendererCategoryV2,\
    QgsCategorizedSymbolRendererV2,\
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

from GeoPublicHealth.src.core.graph_toolbar import CustomNavigationToolbar
from GeoPublicHealth.src.core.tools import display_message_bar, tr
from GeoPublicHealth.src.core.exceptions import \
    GeoPublicHealthException,\
    NoLayerProvidedException,\
    DifferentCrsException,\
    FieldExistingException,\
    FieldException,\
    NotANumberException
from pysal import pysal
from GeoPublicHealth.src.core.stats import Stats
import processing 
from processing.tools.vector import VectorWriter
import numpy as np

from qgis.gui import QgsFieldComboBox
from qgis.gui import QgsMapLayerComboBox

from GeoPublicHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('analysis', 'autocorrelation.ui')

class CommonAutocorrelationDialog(QDialog):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')
    signalStatus = pyqtSignal(int, str, name='signalStatus')

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

        self.cbx_aggregation_layer.setFilters(QgsMapLayerProxyModel.PolygonLayer)


        self.cbx_indicator_field.setFilters(QgsFieldProxyModel.Numeric)
        self.cbx_indicator_field.setLayer(self.cbx_aggregation_layer.currentLayer())
        self.cbx_aggregation_layer.layerChanged.connect(self.cbx_indicator_field.setLayer)

        self.lisa = {
            1 : ("#b92815", "High - High"),
            2 : ("#3f70df", "Low - High"),
            3 : ("#aecbdd", "Low - Low"),
            4 : ("#e79e2c", "High - Low")
        }

    def open_file_browser(self):
        output_file = QFileDialog.getSaveFileNameAndFilter(
            self.parent, tr('Save shapefile'), filter='SHP (*.shp)')
        self.le_output_filepath.setText(output_file[0])

    def run_stats(self):
        """Main function which do the process."""

        # Get the common fields..currentField() 
        self.admin_layer = self.cbx_aggregation_layer.currentLayer()
        input_name =  self.admin_layer.name()
        field = self.cbx_indicator_field.currentField() 

        self.layer = processing.getObject(input_name)

        # Output.
        self.output_file_path = self.le_output_filepath.text()

        try:
            self.button_box_ok.setDisabled(True)
            # noinspection PyArgumentList
            QApplication.setOverrideCursor(Qt.WaitCursor)
            # noinspection PyArgumentList
            QApplication.processEvents()

            if not self.admin_layer:
                raise NoLayerProvidedException

            if not self.admin_layer and self.use_point_layer:
                raise NoLayerProvidedException

            crs_admin_layer = self.admin_layer.crs()

            # Output
            if not self.output_file_path:
                temp_file = NamedTemporaryFile(
                    delete=False,
                    suffix='-geopublichealth.shp')
                self.output_file_path = temp_file.name
                temp_file.flush()
                temp_file.close()

            admin_layer_provider = self.layer.dataProvider()
            fields = admin_layer_provider.fields()

            if admin_layer_provider.fieldNameIndex(self.name_field) != -1:
                raise FieldExistingException(field=self.name_field)

            fields.append(QgsField('LISA_P', QVariant.Double))
            fields.append(QgsField('LISA_Z', QVariant.Double))
            fields.append(QgsField('LISA_Q', QVariant.Int))
            fields.append(QgsField('LISA_I', QVariant.Double))
            fields.append(QgsField('LISA_C', QVariant.Double))

            file_writer = QgsVectorFileWriter(
                self.output_file_path,
                'utf-8',
                fields,
                QGis.WKBPolygon,
                self.admin_layer.crs(),
                'ESRI Shapefile')

            if self.cbx_contiguity.currentIndex()  == 0: # queen
                print 'INFO: Local Moran\'s using queen contiguity'
                w = pysal.queen_from_shapefile(self.admin_layer.source())
            else: # 1 for rook
                print 'INFO: Local Moran\'s using rook contiguity'
                w = pysal.rook_from_shapefile(self.admin_layer.source())

            f = pysal.open(self.admin_layer.source().replace('.shp','.dbf'))
            y = np.array(f.by_col[str(field)])
            lm = pysal.Moran_Local(y, w, transformation = "r", permutations = 999)

            sig_q = lm.q * (lm.p_sim <= 0.05) # could make significance level an option
            outFeat = QgsFeature()
            i = 0

            count = self.admin_layer.featureCount()

            for i, feature in enumerate(self.admin_layer.getFeatures()):
                attributes = feature.attributes()
                attributes.append(float(lm.p_sim[i]))
                attributes.append(float(lm.z_sim[i]))
                attributes.append(int(lm.q[i]))
                attributes.append(float(lm.Is[i]))
                attributes.append(int(sig_q[i]))
              
                new_feature = QgsFeature()
                new_geom = QgsGeometry(feature.geometry())
                new_feature.setAttributes(attributes)
                new_feature.setGeometry(new_geom)
                file_writer.addFeature(new_feature)

            del file_writer

            self.output_layer = QgsVectorLayer(
                self.output_file_path,
                "LISA Moran's I - " + field,
                'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(self.output_layer)


            self.add_symbology()

            self.signalStatus.emit(3, tr('Successful process'))

        except GeoPublicHealthException, e:
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)

        finally:
            self.button_box_ok.setDisabled(False)
            # noinspection PyArgumentList
            QApplication.restoreOverrideCursor()
            # noinspection PyArgumentList
            QApplication.processEvents()

    def add_symbology(self):
        categories = []
        for lisaCategory, (color, label) in self.lisa.items():
            sym = QgsSymbolV2.defaultSymbol(self.output_layer.geometryType())
            sym.setColor(QColor(color))
            category = QgsRendererCategoryV2(lisaCategory, sym, label)
            categories.append(category)

        self.newlayer = QgsVectorLayer(
            self.output_layer.source(),
            self.output_layer.name() + " significance test", 
            self.output_layer.providerType())
        QgsMapLayerRegistry.instance().addMapLayer(self.newlayer)

        # noinspection PyArgumentList
        renderer = QgsCategorizedSymbolRendererV2(
            'LISA_Q',
            categories)
        self.output_layer.setRendererV2(renderer)

        symbol = QgsSymbolV2.defaultSymbol(QGis.Polygon)

        color_ramp = QgsVectorGradientColorRampV2(QColor(0,0,0), QColor(255,0,0))
        # noinspection PyArgumentList
        renderer = QgsGraduatedSymbolRendererV2.createRenderer(
            self.newlayer,
            'LISA_C',
            4,
            QgsGraduatedSymbolRendererV2.Jenks,
            symbol,
            color_ramp)
        self.newlayer.setRendererV2(renderer)
        self.newlayer.setLayerTransparency(40)

class AutocorrelationDialog(CommonAutocorrelationDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        CommonAutocorrelationDialog.__init__(self, parent)
        # noinspection PyArgumentList
        FORM_CLASS.setupUi(self, self)

        self.use_area = False

        self.setup_ui()

    def run_stats(self):
        """Main function which do the process."""
        CommonAutocorrelationDialog.run_stats(self)
