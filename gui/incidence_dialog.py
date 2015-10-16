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

from PyQt4.QtGui import QDialog, QDialogButtonBox, QTableWidgetItem
from PyQt4.QtCore import QSize, QVariant

from qgis.utils import iface
from qgis.core import QgsField

from matplotlib.backends.backend_qt4agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import \
    NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from GeoHealth.core.tools import display_message_bar
from GeoHealth.core.exceptions import \
    GeoHealthException,\
    NoLayerProvidedException,\
    DifferentCrsException,\
    NotANumberException
from GeoHealth.core.stats import Stats
from GeoHealth.ui.incidence import Ui_Incidence


class CustomNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Next', 'Pan', 'Zoom', 'Save')]


class IncidenceDialog(QDialog, Ui_Incidence):
    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.name_field = None

        # Connect slot.
        # noinspection PyUnresolvedReferences
        self.comboBox_incidence_adminLayer.currentIndexChanged.connect(
            self.update_fields)
        self.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_stats)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.hide)

        # Setup the graph.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)

    def update_fields(self):
        """Update the combobox about the population field."""
        self.comboBox_incidence_populationField.clear()

        index = self.comboBox_incidence_adminLayer.currentIndex()
        admin_layer = self.comboBox_incidence_adminLayer.itemData(index)
        if not admin_layer:
            return False

        fields = admin_layer.dataProvider().fields()

        for item in fields:
            self.comboBox_incidence_populationField.addItem(item.name(), item)

    def fill_combobox_layer(self):
        """Fill combobox about layers."""
        self.comboBox_incidence_adminLayer.clear()
        self.comboBox_incidence_pointLayer.clear()
        self.comboBox_incidence_populationField.clear()

        for layer in iface.legendInterface().layers():
            if layer.type() == 0:

                if layer.geometryType() == 0:
                    self.comboBox_incidence_pointLayer.addItem(
                        layer.name(), layer)

                if layer.geometryType() == 2:
                    self.comboBox_incidence_adminLayer.addItem(
                        layer.name(), layer)

    def run_stats(self):
        """Main function which do the process."""

        # Get the fields.
        index = self.comboBox_incidence_adminLayer.currentIndex()
        admin_layer = self.comboBox_incidence_adminLayer.itemData(index)
        index = self.comboBox_incidence_pointLayer.currentIndex()
        point_layer = self.comboBox_incidence_pointLayer.itemData(index)
        population = self.comboBox_incidence_populationField.currentText()
        self.name_field = self.lineEdit_incidence_columnName.text()
        ratio = self.comboBox_incidence_ratio.currentText()
        ratio = ratio.replace(' ', '')

        try:

            if not admin_layer or not point_layer:
                raise NoLayerProvidedException

            crs_admin_layer = admin_layer.crs()
            crs_point_layer = point_layer.crs()
            if crs_admin_layer != crs_point_layer:
                raise DifferentCrsException(
                    epsg1=crs_point_layer.authid(),
                    epsg2=crs_admin_layer.authid())

            try:
                ratio = float(ratio)
            except ValueError:
                raise NotANumberException(suffix=ratio)

            use_area = self.radioButton_incidence_area.isChecked()
            add_nb_intersections = self.checkBox_addNbIntersections.isChecked()

            index_population = None
            if not use_area:
                index_population = admin_layer.fieldNameIndex(population)

            admin_layer_provider = admin_layer.dataProvider()
            admin_layer.startEditing()
            attributes = [QgsField(self.name_field, QVariant.Double)]
            admin_layer_provider.addAttributes(attributes)

            if add_nb_intersections:
                attributes = [QgsField('nb_of_intersections', QVariant.Int)]
                admin_layer_provider.addAttributes(attributes)

            admin_layer.updateFields()
            fields = admin_layer.pendingFields()
            nb_fields = fields.count()

            id_field_intersections = None

            if add_nb_intersections:
                id_field_incidence = nb_fields - 2
                id_field_intersections = nb_fields - 1
            else:
                id_field_incidence = nb_fields - 1

            data = []

            for i, feature in enumerate(admin_layer.getFeatures()):
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
                            admin_layer.rollBack()
                            raise NotANumberException(
                                suffix=attributes[index_population])
                        value = float(count) / population * ratio

                except ZeroDivisionError:
                    value = None

                data.append(value)
                admin_layer.changeAttributeValue(
                    feature.id(), id_field_incidence, value)

                if add_nb_intersections:
                    admin_layer.changeAttributeValue(
                        feature.id(), id_field_intersections, count)

            admin_layer.commitChanges()
            admin_layer.updateFields()

            if self.checkBox_incidence_runStats.isChecked():

                stats = Stats(data)

                items_stats = [
                    'Incidence null,%d' % stats.null_values(),
                    'Count(point),%d' % point_layer.featureCount(),
                    'Count(polygon),%d' % admin_layer.featureCount(),
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
