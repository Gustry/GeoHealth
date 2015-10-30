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

from tempfile import NamedTemporaryFile
from PyQt4.QtGui import \
    QDialog,\
    QDialogButtonBox,\
    QTableWidgetItem,\
    QApplication
from PyQt4.QtCore import QSize, QVariant, Qt, pyqtSignal
from PyQt4.QtGui import QFileDialog

from qgis.utils import iface, QGis
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

from GeoHealth.core.graph_toolbar import CustomNavigationToolbar
from GeoHealth.core.tools import display_message_bar, trans
from GeoHealth.core.exceptions import \
    GeoHealthException,\
    NoLayerProvidedException,\
    DifferentCrsException,\
    FieldExistingException,\
    NotANumberException
from GeoHealth.core.stats import Stats


class IncidenceDensityDialog(QDialog):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')

    def __init__(self, parent=None):
        """Constructor."""
        self.parent = parent
        QDialog.__init__(self, parent)
        self.name_field = None
        self.admin_layer = None
        self.figure = None
        self.canvas = None
        self.toolbar = None
        self.output_file_path = None
        self.output_layer = None

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
            'Equal interval', QgsGraduatedSymbolRendererV2.EqualInterval)
        self.cbx_mode.addItem(
            'Quantile (equal count)', QgsGraduatedSymbolRendererV2.Quantile)
        self.cbx_mode.addItem(
            'Natural breaks', QgsGraduatedSymbolRendererV2.Jenks)
        self.cbx_mode.addItem(
            'Standard deviation', QgsGraduatedSymbolRendererV2.StdDev)
        self.cbx_mode.addItem(
            'Pretty breaks', QgsGraduatedSymbolRendererV2.Pretty)

        # Setup the graph.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)

    def open_file_browser(self):
        output_file = QFileDialog.getSaveFileNameAndFilter(
            self.parent, trans('Save shapefile'), filter='SHP (*.shp)')
        self.le_output_filepath.setText(output_file[0])

    def fill_combobox_layer(self):
        """Fill combobox about layers."""
        self.cbx_case_layer.clear()
        self.cbx_aggregation_layer.clear()

        for layer in iface.legendInterface().layers():
            if layer.type() == 0:

                if layer.geometryType() == 0:
                    self.cbx_case_layer.addItem(
                        layer.name(), layer)

                if layer.geometryType() == 2:
                    self.cbx_aggregation_layer.addItem(
                        layer.name(), layer)

    def run_stats(self, use_area):
        """Main function which do the process."""

        # Get the fields.
        index = self.cbx_aggregation_layer.currentIndex()
        self.admin_layer = self.cbx_aggregation_layer.itemData(index)
        index = self.cbx_case_layer.currentIndex()
        point_layer = self.cbx_case_layer.itemData(index)
        self.name_field = self.le_new_column.text()

        if not self.name_field:
            self.name_field = self.le_new_column.placeholderText()

        ratio = self.cbx_ratio.currentText()
        ratio = ratio.replace(' ', '')
        self.output_file_path = self.le_output_filepath.text()

        try:

            self.button_box_ok.setDisabled(True)
            # noinspection PyArgumentList
            QApplication.setOverrideCursor(Qt.WaitCursor)
            # noinspection PyArgumentList
            QApplication.processEvents()

            if not self.admin_layer or not point_layer:
                raise NoLayerProvidedException

            crs_admin_layer = self.admin_layer.crs()
            crs_point_layer = point_layer.crs()
            if crs_admin_layer != crs_point_layer:
                raise DifferentCrsException(
                    epsg1=crs_point_layer.authid(),
                    epsg2=crs_admin_layer.authid())

            try:
                ratio = float(ratio)
            except ValueError:
                raise NotANumberException(suffix=ratio)

            add_nb_intersections = self.checkBox_addNbIntersections.isChecked()

            index_population = None
            if not use_area:
                population = self.cbx_population_field\
                    .currentText()
                index_population = self.admin_layer.fieldNameIndex(population)

            # Output
            if not self.output_file_path:
                temp_file = NamedTemporaryFile(
                    delete=False,
                    suffix='-geohealth.shp')
                self.output_file_path = temp_file.name
                temp_file.flush()
                temp_file.close()

            admin_layer_provider = self.admin_layer.dataProvider()
            fields = admin_layer_provider.fields()

            if admin_layer_provider.fieldNameIndex(self.name_field) != -1:
                raise FieldExistingException(field=self.name_field)

            fields.append(QgsField(self.name_field, QVariant.Double))

            if add_nb_intersections:
                fields.append(QgsField('nb_of_intersections', QVariant.Int))

            data = []

            file_writer = QgsVectorFileWriter(
                self.output_file_path,
                'utf-8',
                fields,
                QGis.WKBPolygon,
                self.admin_layer.crs(),
                'ESRI Shapefile')

            for i, feature in enumerate(self.admin_layer.getFeatures()):
                attributes = feature.attributes()
                count = 0
                for f in point_layer.getFeatures():
                    if f.geometry().intersects(feature.geometry()):
                        count += 1

                try:
                    if use_area:
                        area = feature.geometry().area()
                        value = float(count) / area * ratio
                    else:
                        try:
                            population = float(attributes[index_population])
                        except ValueError:
                            raise NotANumberException(
                                suffix=attributes[index_population])
                        value = float(count) / population * ratio

                except ZeroDivisionError:
                    value = None

                data.append(value)
                attributes.append(value)

                if add_nb_intersections:
                    attributes.append(count)

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
            QgsMapLayerRegistry.instance().addMapLayer(self.output_layer)

            if self.checkBox_incidence_runStats.isChecked():

                stats = Stats(data)

                items_stats = [
                    'Incidence null,%d' % stats.null_values(),
                    'Count(point),%d' % point_layer.featureCount(),
                    'Count(polygon),%d' % self.admin_layer.featureCount(),
                    'Min,%d' % stats.min(),
                    'Average,%f' % stats.average(),
                    'Max,%d' % stats.max(),
                    'Median,%f' % stats.median(),
                    'Range,%d' % stats.range(),
                    'Variance,%f' % stats.variance(),
                    'Standard deviation,%f' % stats.standard_deviation()
                ]

                self.tableWidget.clear()
                self.tableWidget.setColumnCount(2)
                labels = ['Parameters', 'Values']
                self.tableWidget.setHorizontalHeaderLabels(labels)
                self.tableWidget.setRowCount(len(items_stats))

                for i, item in enumerate(items_stats):
                    s = item.split(',')
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(s[0]))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(s[1]))
                self.tableWidget.resizeRowsToContents()

                self.draw_plot(data)

            else:
                self.hide()

            if self.symbology.isChecked():
                self.add_symbology()

        except GeoHealthException, e:
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
        ax.hold(False)
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
