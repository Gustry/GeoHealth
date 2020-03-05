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

from builtins import str
from builtins import range
from tempfile import NamedTemporaryFile
from qgis.PyQt.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem, QMessageBox, QApplication
from qgis.PyQt.QtCore import QSize, QVariant, Qt, pyqtSignal
from qgis.PyQt.QtWidgets import QFileDialog

from qgis.utils import Qgis

from qgis.core import (\
    QgsField,\
    QgsGradientColorRamp,\
    QgsGraduatedSymbolRenderer,\
    QgsSymbol,\
    QgsVectorFileWriter,\
    QgsFeature,\
    QgsVectorLayer,\
    QgsProject,\
    QgsGeometry,\
    QgsMapLayerProxyModel, QgsFieldProxyModel, QgsWkbTypes)

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
from GeoPublicHealth.src.core.stats import Stats

from GeoPublicHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('analysis', 'composite_index.ui')

class CommonCompositeIndexDialog(QDialog):

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
        self.use_point_layer = None

    def setup_ui(self):
        # Connect slot.
        # noinspection PyUnresolvedReferences
        self.button_browse.clicked.connect(self.open_file_browser)
        self.command_link_button.clicked.connect(self.add_indicator)
        self.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_stats)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.hide)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)

        # Add items in symbology
        self.cbx_mode.addItem(
            'Quantile (equal count)', QgsGraduatedSymbolRenderer.Quantile)
        self.cbx_mode.addItem(
            'Natural breaks', QgsGraduatedSymbolRenderer.Jenks)
        self.cbx_mode.addItem(
            'Standard deviation', QgsGraduatedSymbolRenderer.StdDev)
        self.cbx_mode.addItem(
            'Pretty breaks', QgsGraduatedSymbolRenderer.Pretty)
        self.cbx_mode.addItem(
            'Equal interval', QgsGraduatedSymbolRenderer.EqualInterval)

        self.cbx_aggregation_layer.setFilters(QgsMapLayerProxyModel.PolygonLayer)

        self.cbx_list_indicators.itemDoubleClicked.connect(self.remove_item)

        self.cbx_indicator_field.setFilters(QgsFieldProxyModel.Numeric)
        self.cbx_indicator_field.setLayer(self.cbx_aggregation_layer.currentLayer())
        self.cbx_aggregation_layer.layerChanged.connect(self.cbx_indicator_field.setLayer)
        self.cbx_aggregation_layer.layerChanged.connect(self.reset_field_indicator)
        self.reset_field_indicator()

    def reset_field_indicator(self):
        self.cbx_indicator_field.setCurrentIndex(0)

    def remove_item(self):
        self.cbx_list_indicators.takeItem( self.cbx_list_indicators.currentRow())

    def add_indicator(self):
        present = False
        for index in range(self.cbx_list_indicators.count()):
            if self.cbx_list_indicators.item(index).text() == self.vector_indicator():
                present = True
        if not present:
            self.cbx_list_indicators.addItem(self.vector_indicator())

    def vector_indicator(self):
        return self.cbx_indicator_field.currentField() + " | " + self.vector_direction()

    def vector_direction(self):
        if self.radioButton_vector_positive.isChecked():
            return "+"
        else:
            return "-"

    def open_file_browser(self):
        output_file, __ = QFileDialog.getSaveFileName(
            self.parent, tr('Save shapefile'), filter='SHP (*.shp)')
        self.le_output_filepath.setText(output_file[0])

    def indicators_list(self):
        items = []
        for index in range(self.cbx_list_indicators.count()):
            items.append(self.cbx_list_indicators.item(index))
        return [i.text().split(" | ") for i in items]


    def run_stats(self):
        """Main function which do the process."""

        # Get the common fields.
        self.admin_layer = self.cbx_aggregation_layer.currentLayer()

        selected_indicators = self.indicators_list()

        if not self.name_field:
            self.name_field = self.le_new_column.placeholderText()

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

            if not self.use_point_layer and not self.use_area:
                if not self.cbx_list_indicators:
                    raise FieldException(field_1='List Indicators should not empty')

            # Output
            if not self.output_file_path:
                temp_file = NamedTemporaryFile(
                    delete=False,
                    suffix='-geopublichealth.shp')
                self.output_file_path = temp_file.name
                temp_file.flush()
                temp_file.close()

            admin_layer_provider = self.admin_layer.dataProvider()
            fields = self.admin_layer.fields()

            if admin_layer_provider.fields().indexFromName(self.name_field) != -1:
                raise FieldExistingException(field=self.name_field)

            for indicator_selected in selected_indicators:
                fields.append(QgsField("Z" + indicator_selected[0], QVariant.Double))

            fields.append(QgsField(self.name_field, QVariant.Double))

            file_writer = QgsVectorFileWriter(
                self.output_file_path,
                'utf-8',
                fields,
                QgsWkbTypes.Polygon,
                self.admin_layer.crs(),
                'ESRI Shapefile')

            count = self.admin_layer.featureCount()
            stats = {}

            for indicator_selected in selected_indicators:
                values = []
                indicator_selected_name = str(indicator_selected[0])

                for i, feature in enumerate(self.admin_layer.getFeatures()):
                    index = self.admin_layer.fields().indexFromName(indicator_selected_name)

                    if feature[index]:
                        value = float(feature[index])
                    else:
                        value = 0.0
                    values.append(value)

                stats[indicator_selected_name] = Stats(values)

            for i, feature in enumerate(self.admin_layer.getFeatures()):
                attributes = feature.attributes()

                composite_index_value = 0.0
                for indicator_selected in selected_indicators:
                    indicator_selected_name = str(indicator_selected[0])
                    index = self.admin_layer.fields().indexFromName(indicator_selected_name)

                    if feature[index]:
                        value = float(feature[index])
                    else:
                        value = 0.0

                    zscore = (value - stats[indicator_selected_name].average()) / stats[indicator_selected_name].standard_deviation()
                    attributes.append(float(zscore))



                    if indicator_selected[1] == '+':
                        composite_index_value -= zscore
                    else:
                        composite_index_value += zscore

                attributes.append(float(composite_index_value))
                new_feature = QgsFeature()
                new_geom = QgsGeometry(feature.geometry())
                new_feature.setAttributes(attributes)
                new_feature.setGeometry(new_geom)
                file_writer.addFeature(new_feature)

            del file_writer

            self.output_layer = QgsVectorLayer(
                self.output_file_path,
                self.name_field,
                'ogr')
            QgsProject.instance().addMapLayer(self.output_layer)

            if self.symbology.isChecked():
                self.add_symbology()

            self.signalStatus.emit(3, tr('Successful process'))

        except GeoPublicHealthException as e:
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)

        finally:
            self.button_box_ok.setDisabled(False)
            # noinspection PyArgumentList
            QApplication.restoreOverrideCursor()
            # noinspection PyArgumentList
            QApplication.processEvents()

    def draw_plot(self, data):
        """Function to draw the plot and display it in the canvas.

        :param data: The data to display
        :type data: list
        """
        ax = self.figure.add_subplot(111)

        ax.plot(data, '*-')
        ax.set_xlabel('Polygon')
        ax.set_ylabel(self.name_field)
        ax.grid()
        self.canvas.draw()

    def add_symbology(self):
        low_color = self.color_low_value.color()
        high_color = self.color_high_value.color()
        index = self.cbx_mode.currentIndex()
        mode = self.cbx_mode.itemData(index)
        classes = self.spinBox_classes.value()

        # Compute renderer
        # noinspection PyArgumentList
        symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.geometryType(QgsWkbTypes.Polygon))

        color_ramp = QgsGradientColorRamp(low_color, high_color)
        # noinspection PyArgumentList
        renderer = QgsGraduatedSymbolRenderer.createRenderer(
            self.output_layer,
            self.name_field,
            classes,
            mode,
            symbol,
            color_ramp)
        self.output_layer.setRenderer(renderer)

class CompositeIndexDialog(CommonCompositeIndexDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        CommonCompositeIndexDialog.__init__(self, parent)
        # noinspection PyArgumentList
        FORM_CLASS.setupUi(self, self)

        self.use_area = False
        self.use_point_layer = False

        self.setup_ui()

    def run_stats(self):
        """Main function which do the process."""
        CommonCompositeIndexDialog.run_stats(self)
