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

from os.path import dirname
from qgis.core import QGis, QgsFeatureRequest, QgsSpatialIndex
from qgis.gui import QgsMapLayerProxyModel

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import \
    FigureCanvasQTAgg as FigureCanvas
from qgis.PyQt.QtGui import \
    QWidget, QDialogButtonBox, QApplication, QTableWidgetItem, QFileDialog
from qgis.PyQt.QtCore import pyqtSignal, QSize

from geohealth.core.graph_toolbar import CustomNavigationToolbar
from geohealth.core.stats import Stats
from geohealth.core.tools import \
    tr, display_message_bar, get_last_input_path, set_last_input_path
from geohealth.core.exceptions import \
    GeoHealthException, NoLayerProvidedException, DifferentCrsException
from geohealth.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('analysis', 'stats.ui')


class StatsWidget(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')

    def __init__(self, parent=None):
        self.parent = parent
        super(StatsWidget, self).__init__()
        self.setupUi(self)

        self.label_progressStats.setText('')

        # Connect
        # noinspection PyUnresolvedReferences
        self.pushButton_saveTable.clicked.connect(self.save_table)
        # noinspection PyUnresolvedReferences
        self.pushButton_saveYValues.clicked.connect(self.save_y_values)
        self.buttonBox_stats.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_stats)
        self.buttonBox_stats.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)

        # a figure instance to plot on
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)

        self.tab = []

        self.comboBox_blurredLayer.setFilters(
            QgsMapLayerProxyModel.PolygonLayer)
        self.comboBox_statsLayer.setFilters(
            QgsMapLayerProxyModel.PolygonLayer)

    def run_stats(self):
        self.progressBar_stats.setValue(0)
        self.label_progressStats.setText('')
        # noinspection PyArgumentList
        QApplication.processEvents()

        blurred_layer = self.comboBox_blurredLayer.currentLayer()
        stats_layer = self.comboBox_statsLayer.currentLayer()

        try:

            if not blurred_layer or not stats_layer:
                raise NoLayerProvidedException

            crs_blurred_layer = blurred_layer.crs()
            crs_stats_layer = stats_layer.crs()

            if crs_blurred_layer != crs_stats_layer:
                raise DifferentCrsException(
                    epsg1=crs_blurred_layer.authid(),
                    epsg2=crs_stats_layer.authid())

            if blurred_layer == stats_layer:
                raise NoLayerProvidedException

            if not blurred_layer or not stats_layer:
                raise NoLayerProvidedException

            nb_feature_stats = stats_layer.featureCount()
            nb_feature_blurred = blurred_layer.featureCount()
            features_stats = {}

            label_preparing = tr('Preparing index on the stats layer')
            label_creating = tr('Creating index on the stats layer')
            label_calculating = tr('Calculating')

            if QGis.QGIS_VERSION_INT < 20700:
                self.label_progressStats.setText('%s 1/3' % label_preparing)

                for i, feature in enumerate(stats_layer.getFeatures()):
                    features_stats[feature.id()] = feature
                    percent = int((i + 1) * 100 / nb_feature_stats)
                    self.progressBar_stats.setValue(percent)
                    # noinspection PyArgumentList
                    QApplication.processEvents()

                self.label_progressStats.setText('%s 2/3' % label_creating)
                # noinspection PyArgumentList
                QApplication.processEvents()
                index = QgsSpatialIndex()
                for i, f in enumerate(stats_layer.getFeatures()):
                    index.insertFeature(f)

                    percent = int((i + 1) * 100 / nb_feature_stats)
                    self.progressBar_stats.setValue(percent)
                    # noinspection PyArgumentList
                    QApplication.processEvents()

                self.label_progressStats.setText('%s 3/3' % label_calculating)

            else:
                # If QGIS >= 2.7, we can speed up the spatial index.
                # From 1 min 15 to 7 seconds on my PC.
                self.label_progressStats.setText('%s 1/2' % label_creating)
                # noinspection PyArgumentList
                QApplication.processEvents()
                index = QgsSpatialIndex(stats_layer.getFeatures())
                self.label_progressStats.setText('%s 2/2' % label_calculating)

            # noinspection PyArgumentList
            QApplication.processEvents()
            self.tab = []
            for i, feature in enumerate(blurred_layer.getFeatures()):
                count = 0
                ids = index.intersects(feature.geometry().boundingBox())
                for unique_id in ids:
                    request = QgsFeatureRequest().setFilterFid(unique_id)
                    f = stats_layer.getFeatures(request).next()

                    if f.geometry().intersects(feature.geometry()):
                        count += 1
                self.tab.append(count)

                percent = int((i + 1) * 100 / nb_feature_blurred)
                self.progressBar_stats.setValue(percent)
                # noinspection PyArgumentList
                QApplication.processEvents()

            stats = Stats(self.tab)

            items_stats = [
                'Count(blurred),%d' % nb_feature_blurred,
                'Count(stats),%d' % nb_feature_stats,
                'Min,%d' % stats.min(),
                'Average,%f' % stats.average(),
                'Max,%d' % stats.max(), 'Median,%f' % stats.median(),
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

            self.draw_plot(self.tab)

        except GeoHealthException, e:
            self.label_progressStats.setText('')
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)

    def save_table(self):

        if not self.tableWidget.rowCount():
            return False

        csv_string = 'parameter,values\n'

        for i in range(self.tableWidget.rowCount()):
            item_param = self.tableWidget.item(i, 0)
            item_value = self.tableWidget.item(i, 1)
            csv_string += \
                str(item_param.text()) + ',' + item_value.text() + '\n'

        last_directory = get_last_input_path()

        # noinspection PyArgumentList
        output_file = QFileDialog.getSaveFileName(
            parent=self,
            caption=tr('Select file'),
            directory=last_directory,
            filter='CSV (*.csv)')

        if output_file:
            path = dirname(output_file)
            set_last_input_path(path)

            fh = open(output_file, 'w')
            fh.write(csv_string)
            fh.close()
            return True

    def save_y_values(self):

        if not self.tableWidget.rowCount():
            return False

        csv_string = 'parameter,values\n'

        for value in self.tab:
            csv_string += str(value) + '\n'

        last_directory = get_last_input_path()
        # noinspection PyArgumentList
        output_file = QFileDialog.getSaveFileName(
            parent=self,
            caption=tr('Select file'),
            directory=last_directory,
            filter='CSV (*.csv)')

        if output_file:
            path = dirname(output_file)
            set_last_input_path(path)

            fh = open(output_file, 'w')
            fh.write(csv_string)
            fh.close()
            return True

    def draw_plot(self, data):
        # Creating the plot
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data, '*-')

        # ax.set_title('Number of intersections per entity')
        ax.set_xlabel('Blurred entity')
        ax.set_ylabel('Number of intersections')
        ax.grid()

        # refresh canvas
        self.canvas.draw()
