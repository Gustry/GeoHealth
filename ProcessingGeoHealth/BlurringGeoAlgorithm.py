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

from GeoHealth import *
from GeoHealth.CoreGeoHealth.Blurring.BlurAlgo import *
from GeoHealth.CoreGeoHealth.Blurring.LayerIndex import *
from GeoHealth.ProcessingGeoHealth import *

"""QGIS Processing"""

class BlurringGeoAlgorithm(GeoAlgorithm):

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

        self.addParameter(ParameterVector(self.INPUT_LAYER, 'Point layer',[ParameterVector.VECTOR_TYPE_POINT], False))
        self.addParameter(ParameterNumber(self.RADIUS_FIELD, 'Radius (maps unit)',0,999999999,500.00))
        self.addParameter(ParameterVector(self.ENVELOPE_LAYER, 'Envelope layer',[ParameterVector.VECTOR_TYPE_POLYGON], True))
        self.addParameter(ParameterBoolean(self.RADIUS_EXPORT, 'Add the radius to the attribute table',False))
        self.addParameter(ParameterBoolean(self.CENTROID_EXPORT, 'Add the centroid to the attribute table',False))

        self.addOutput(OutputVector(self.OUTPUT_LAYER,'Output layer with selected features'))

    def help(self):
        return True, Tools.trans('For more explanations, go to the vector\'s menu then "Blurring" -> "Help"<br />')
    
    def getIcon(self):
        return QIcon(":/plugins/GeoHealth/resources/blur.png")

    def processAlgorithm(self, progress):

        #Get parameters
        inputFilename = self.getParameterValue(self.INPUT_LAYER)
        radius = self.getParameterValue(self.RADIUS_FIELD)
        exportRadius = self.getParameterValue(self.RADIUS_EXPORT)
        exportCentroid = self.getParameterValue(self.CENTROID_EXPORT)
        envelopeLayerField = self.getParameterValue(self.ENVELOPE_LAYER)
        output = self.getOutputValue(self.OUTPUT_LAYER)

        vectorLayer = dataobjects.getObjectFromUri(inputFilename)
        
        #If we use a mask, envelope
        vectorlayerEnvelopeIndex = None
        if envelopeLayerField != None:
            vectorLayerEnvelope = dataobjects.getObjectFromUri(envelopeLayerField)
            vectorlayerEnvelopeIndex = LayerIndex(vectorLayerEnvelope)

        settings = QSettings()
        systemEncoding = settings.value('/UI/encoding', 'System')
        provider = vectorLayer.dataProvider()
        fields = provider.fields()
        
        if exportRadius:
            fields.append(QgsField(u"Radius", QVariant.Int))
        
        if exportCentroid:
            fields.append(QgsField(u"X centroid", QVariant.Int))
            fields.append(QgsField(u"Y centroid", QVariant.Int))
        
        writer = QgsVectorFileWriter(output, systemEncoding,
                                     fields,
                                     QGis.WKBPolygon, provider.crs())
        
        #Creating a algorithm with all these paramaters
        algo = BlurAlgo(radius, vectorlayerEnvelopeIndex, exportRadius, exportCentroid)

        features = vector.features(vectorLayer)
        for feature in features:
            feature = algo.blur(feature)
            writer.addFeature(feature)