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

from PyQt4.QtGui import QIcon
from PyQt4.QtCore import QVariant
from qgis.utils import QGis
from qgis.core import QgsVectorFileWriter, QgsField

from GeoHealth.core.blurring.blur import Blur
from GeoHealth.core.blurring.layer_index import LayerIndex
from GeoHealth.core.tools import trans
from GeoHealth.processing_geohealth import *


class BlurringGeoAlgorithm(GeoAlgorithm):
    """QGIS Processing"""

    OUTPUT_LAYER = 'OUTPUT_LAYER'
    INPUT_LAYER = 'INPUT_LAYER'
    RADIUS_FIELD = 'RADIUS_FIELD'
    RADIUS_EXPORT = 'RADIUS_EXPORT'
    CENTROID_EXPORT = 'CENTROID_EXPORT'
    DISTANCE_EXPORT = 'DISTANCE_EXPORT'
    ENVELOPE_LAYER = 'ENVELOPE_LAYER'

    def defineCharacteristics(self):
        self.name = "Blurring a point layer"
        self.group = "Blurring a point layer"

        self.addParameter(ParameterVector(
            self.INPUT_LAYER,
            'Point layer',
            [ParameterVector.VECTOR_TYPE_POINT],
            False))

        self.addParameter(ParameterNumber(
            self.RADIUS_FIELD,
            'Radius (maps unit)',
            0,
            999999999,
            500.00))

        self.addParameter(ParameterVector(
            self.ENVELOPE_LAYER,
            'Envelope layer',
            [ParameterVector.VECTOR_TYPE_POLYGON],
            True))

        self.addParameter(ParameterBoolean(
            self.RADIUS_EXPORT,
            'Add the radius to the attribute table',
            False))

        self.addParameter(ParameterBoolean(
            self.CENTROID_EXPORT,
            'Add the centroid to the attribute table',
            False))

        self.addOutput(OutputVector(
            self.OUTPUT_LAYER,
            'Output layer with selected features'))

    def help(self):
        return True, trans(
            'For more explanations, go to the vector\'s menu then "Blurring"'
            ' -> "Help"<br />')
    
    def getIcon(self):
        return QIcon(':/plugins/GeoHealth/resources/blur.png')

    def processAlgorithm(self, progress):

        #Get parameters
        input_filename = self.getParameterValue(self.INPUT_LAYER)
        radius = self.getParameterValue(self.RADIUS_FIELD)
        export_radius = self.getParameterValue(self.RADIUS_EXPORT)
        export_centroid = self.getParameterValue(self.CENTROID_EXPORT)
        envelope_layer_field = self.getParameterValue(self.ENVELOPE_LAYER)
        output = self.getOutputValue(self.OUTPUT_LAYER)

        vector_layer = dataobjects.getObjectFromUri(input_filename)
        
        #If we use a mask, envelope
        vector_layer_envelope_index = None
        if envelope_layer_field is not None:
            vector_layer_envelope = dataobjects.getObjectFromUri(
                envelope_layer_field)
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
            QGis.WKBPolygon,
            provider.crs())
        
        # Creating a algorithm with all these parameters.
        algorithm = Blur(
            radius,
            vector_layer_envelope_index,
            export_radius,
            export_centroid)

        for feature in vector.features(vector_layer):
            feature = algorithm.blur(feature)
            writer.addFeature(feature)