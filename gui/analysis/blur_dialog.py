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

from os.path import dirname, basename
from qgis.utils import iface, QGis
from qgis.gui import QgsMessageBar, QgsMapLayerProxyModel
from qgis.core import \
    QgsField,\
    QgsVectorFileWriter, \
    QgsMapLayerRegistry, \
    QgsVectorLayer

from PyQt4.QtGui import (
    QWidget, QDialogButtonBox, QFileDialog, QApplication)
from PyQt4.QtCore import pyqtSignal, QSettings, QVariant
from processing.tools.system import getTempFilenameInTempFolder

from GeoPublicHealth.core.blurring.layer_index import LayerIndex
from GeoPublicHealth.core.blurring.blur import Blur
from GeoPublicHealth.core.tools import \
    get_last_input_path, set_last_input_path, tr, display_message_bar
from GeoPublicHealth.core.exceptions import \
    GeoPublicHealthException, \
    NoLayerProvidedException,\
    NoFileNoDisplayException, \
    DifferentCrsException,\
    CreatingShapeFileException
<<<<<<< HEAD:src/gui/analysis/blur_dialog.py
from GeoHealth.src.utilities.resources import get_ui_class
=======
from GeoPublicHealth.ui.analysis.blur import Ui_Blur
>>>>>>> Change the files for the new name GeoPublicHealth:gui/analysis/blur_dialog.py

FORM_CLASS = get_ui_class('analysis', 'blur.ui')


class BlurWidget(QWidget, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(name='signalAskCloseWindow')

    def __init__(self, parent=None):
        self.parent = parent
        super(BlurWidget, self).__init__()
        self.setupUi(self)

        self.label_progress.setText('')
        self.checkBox_envelope.setChecked(False)
        self.comboBox_envelope.setEnabled(False)

        # noinspection PyUnresolvedReferences
        self.pushButton_browseFolder.clicked.connect(self.select_file)
        self.buttonBox_blur.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_blur)
        self.buttonBox_blur.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow)

        self.settings = QSettings()

        self.comboBox_layerToBlur.setFilters(QgsMapLayerProxyModel.PointLayer)
        self.comboBox_envelope.setFilters(QgsMapLayerProxyModel.PolygonLayer)

    def select_file(self):
        last_folder = get_last_input_path()
        # noinspection PyArgumentList
        output_file = QFileDialog.getSaveFileName(
            parent=self,
            caption=tr('Select file'),
            directory=last_folder,
            filter='Shapefiles (*.shp)')

        if output_file:
            self.lineEdit_outputFile.setText(output_file)
            path = dirname(output_file)
            set_last_input_path(path)
        else:
            self.lineEdit_outputFile.setText('')

    def run_blur(self):

        self.progressBar_blur.setValue(0)
        self.label_progress.setText('')

        # Get all the fields.
        layer_to_blur = self.comboBox_layerToBlur.currentLayer()
        radius = self.spinBox_radius.value()
        display = self.checkBox_addToMap.isChecked()
        selected_features_only = self.checkBox_selectedOnlyFeatures.isChecked()
        file_name = self.lineEdit_outputFile.text()
        export_radius = self.checkBox_exportRadius.isChecked()
        export_centroid = self.checkBox_exportCentroid.isChecked()

        if self.checkBox_envelope.isChecked():
            layer_envelope = self.comboBox_envelope.currentLayer()
        else:
            layer_envelope = None

        # Test values
        try:
            if not layer_to_blur:
                raise NoLayerProvidedException

            if not file_name and not display:
                raise NoFileNoDisplayException

            if layer_to_blur.crs().mapUnits() != 0:
                msg = tr('The projection of the map or of the layer is not '
                            'in meters. These parameters should be in meters.')
                display_message_bar(
                    msg, level=QgsMessageBar.WARNING, duration=5)

            if not file_name:
                file_name = getTempFilenameInTempFolder('blurring.shp')
                pass

            if layer_envelope:

                if layer_to_blur.crs() != layer_envelope.crs():
                    raise DifferentCrsException(
                        epsg1=layer_to_blur.crs().authid(),
                        epsg2=layer_envelope.crs().authid())

                self.label_progress.setText('Creating index ...')
                layer_envelope = LayerIndex(layer_envelope)
                self.progressBar_blur.setValue(0)

            self.label_progress.setText('Blurring ...')

            if selected_features_only:
                features = layer_to_blur.selectedFeatures()
                nb_features = layer_to_blur.selectedFeatureCount()
            else:
                features = layer_to_blur.getFeatures()
                nb_features = layer_to_blur.featureCount()

            # Fields
            fields = layer_to_blur.pendingFields()
            if export_radius:
                fields.append(QgsField(u"Radius", QVariant.Int))
            if export_centroid:
                fields.append(QgsField(u"X centroid", QVariant.Int))
                fields.append(QgsField(u"Y centroid", QVariant.Int))

            # Creating the output shapefile
            file_writer = QgsVectorFileWriter(
                file_name,
                'utf-8',
                fields,
                QGis.WKBPolygon,
                layer_to_blur.crs(),
                'ESRI Shapefile')

            if file_writer.hasError() != QgsVectorFileWriter.NoError:
                raise CreatingShapeFileException(suffix=file_writer.hasError())

            # Creating the algorithm with radius
            algo = Blur(radius, layer_envelope, export_radius, export_centroid)

            for j, feature in enumerate(features):
                feature = algo.blur(feature)
                file_writer.addFeature(feature)

                # Update progress bar
                percent = int((j + 1) * 100 / nb_features)
                self.progressBar_blur.setValue(percent)

            # Write all features in the file
            del file_writer

            if display:
                old_default_projection = self.settings.value(
                    '/Projections/defaultBehaviour')
                self.settings.setValue(
                    '/Projections/defaultBehaviour', 'useProject')

                layer_name = basename(file_name)
                new_layer = QgsVectorLayer(file_name, layer_name, 'ogr')
                new_layer.commitChanges()
                new_layer.clearCacheImage()
                # noinspection PyArgumentList
                QgsMapLayerRegistry.instance().addMapLayers([new_layer])

                self.settings.setValue(
                    '/Projections/defaultBehaviour', old_default_projection)

            msg = tr('Successful export in %s' % file_name)
            iface.messageBar().pushMessage(
                msg, level=QgsMessageBar.INFO, duration=5)

            self.signalAskCloseWindow.emit()

        except GeoPublicHealthException, e:
            self.label_progress.setText('')
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)

        finally:
            # noinspection PyArgumentList
            QApplication.restoreOverrideCursor()
            # noinspection PyArgumentList
            QApplication.processEvents()
