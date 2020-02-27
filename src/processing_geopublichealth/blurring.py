# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoPublicHealth
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

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QVariant, QSettings,QCoreApplication
from qgis.utils import Qgis
from qgis.core import QgsProcessing,QgsVectorFileWriter, QgsField, QgsProcessingAlgorithm,QgsProcessingUtils
#from processing.core.GeoAlgorithm import GeoAlgorithm
#from processing.core.parameters import (ParameterVector, ParameterNumber, ParameterBoolean)
from qgis.core import QgsProcessingParameterNumber,QgsProcessingParameterVectorLayer, QgsProcessingParameterBoolean,QgsProcessingOutputVectorLayer,QgsWkbTypes
#from processing.core.outputs import OutputVector
#from processing.tools.vector import dataobjects, features
#from processing.tools.vector import features


from GeoPublicHealth.src.core.blurring.blur import Blur
from GeoPublicHealth.src.core.blurring.layer_index import LayerIndex
from GeoPublicHealth.src.core.tools import tr
from GeoPublicHealth.src.utilities.resources import resource

class BlurringGeoAlgorithm(QgsProcessingAlgorithm):
#class BlurringGeoAlgorithm(GeoAlgorithm):
    """QGIS Processing"""


    OUTPUT_LAYER = 'OUTPUT_LAYER'
    INPUT_LAYER = 'INPUT_LAYER'
    RADIUS_FIELD = 'RADIUS_FIELD'
    RADIUS_EXPORT = 'RADIUS_EXPORT'
    CENTROID_EXPORT = 'CENTROID_EXPORT'
    DISTANCE_EXPORT = 'DISTANCE_EXPORT'
    ENVELOPE_LAYER = 'ENVELOPE_LAYER'

    def initAlgorithm(self,config):
        #self.name = "Blurring a point layer"
        #self.group = "Blurring a point layer"

        self.addParameter(QgsProcessingParameterVectorLayer(
            self.INPUT_LAYER,
            'Point layer',
            [QgsProcessing.TypeVectorPoint]),False)

        self.addParameter(QgsProcessingParameterNumber(
            self.RADIUS_FIELD,
            'Radius (maps unit)',
            0,
            999999999,
            500.00))

        self.addParameter(QgsProcessingParameterVectorLayer(
            self.ENVELOPE_LAYER,
            'Envelope layer',
            [QgsProcessing.TypeVectorPolygon],
            True))

        self.addParameter(QgsProcessingParameterBoolean(
            self.RADIUS_EXPORT,
            'Add the radius to the attribute table',
            False))

        self.addParameter(QgsProcessingParameterBoolean(
            self.CENTROID_EXPORT,
            'Add the centroid to the attribute table',
            False))

        self.addOutput(QgsProcessingOutputVectorLayer(
            self.OUTPUT_LAYER,
            'Output layer with selected features'))

    def help(self):
        return True, tr(
            'For more explanations, go to the vector\'s menu then "Blurring"'
            ' -> "Help"<br />')

    def icon(self):
        return QIcon(resource('blur.png'))
    def name(self):
        return "Blurring a point layer"
    def group(self):
        return "Blurring a point layer"
    def displayName(self):
        return self.tr(self.name())
    def createInstance(self):
        return BlurringGeoAlgorithm()
    def tr(self,string):
        return QCoreApplication.translate("BlurringGeoAlgorithm",string)
    def processAlgorithm(self, progress):

        # Get parameters
        input_filename = self.getParameterValue(self.INPUT_LAYER)
        radius = self.getParameterValue(self.RADIUS_FIELD)
        export_radius = self.getParameterValue(self.RADIUS_EXPORT)
        export_centroid = self.getParameterValue(self.CENTROID_EXPORT)
        envelope_layer_field = self.getParameterValue(self.ENVELOPE_LAYER)
        output = self.getOutputValue(self.OUTPUT_LAYER)

        #vector_layer = dataobjects.getObjectFromUri(input_filename)
        vector_layer=QgsProcessingUtils.mapLayerFromStrong(input_filename)

        # If we use a mask, envelope
        vector_layer_envelope_index = None
        if envelope_layer_field is not None:
            #vector_layer_envelope = dataobjects.getObjectFromUri(envelope_layer_field)
            vector_layer_envelope=QgsProcessingUtils.mapLayerFromStrong(envelope_layer_field)
            vector_layer_envelope_index = LayerIndex(vector_layer_envelope)

        settings = QSettings()
        system_encoding = settings.value('/UI/encoding', 'System')
        provider = vector_layer.dataProvider()
        fields = provider.fields()

        if export_radius:
            fields.append(QgsField(u"Radius", QVariant.Int))

        if export_centroid:
            fields.append(QgsField(u"X centroid", QVariant.Int))
            fields.append(QgsField(u"Y centroid", QVariant.Int))

        writer = QgsVectorFileWriter(
            output,
            system_encoding,
            fields,
            QgsWkbTypes.Polygon,
            provider.crs())

        # Creating a algorithm with all these parameters.
        algorithm = Blur(
            radius,
            vector_layer_envelope_index,
            export_radius,
            export_centroid)
        selection=vector_layer.selectedFeatures()
        #for feature in features(vector_layer):
        for feature in selection:
            feature = algorithm.blur(feature)
            writer.addFeature(feature)
