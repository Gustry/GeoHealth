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

from PyQt4.QtGui import QIcon
from processing.core.AlgorithmProvider import AlgorithmProvider

from GeoPublicHealth.processing_geopublichealth.blurring import BlurringGeoAlgorithm


class Provider(AlgorithmProvider):
    """QGIS Processing"""

    def __init__(self):
        AlgorithmProvider.__init__(self)
    
        self.activate = True
    
        # Load algorithms
        self.alglist = [BlurringGeoAlgorithm()]
        for alg in self.alglist:
            alg.provider = self
    
    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)
    
    def unload(self):
        AlgorithmProvider.unload(self)
    
    def getName(self):
        return 'GeoPublicHealth'
    
    def getDescription(self):
        return 'GeoPublicHealth'
    
    def getIcon(self):
        return QIcon(':/plugins/GeoPublicHealth/resources/icon-32.png')
    
    def _loadAlgorithms(self):
        self.algs = self.alglist