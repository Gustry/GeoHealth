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
#from qgis.core import QgsProcessingProvider
from qgis.core import QgsProcessingProvider

from GeoPublicHealth.src.processing_geopublichealth.blurring import (
    BlurringGeoAlgorithm)
from GeoPublicHealth.src.utilities.resources import resource

class Provider(QgsProcessingProvider):
#class Provider(QgsProcessingProvider):
    """QGIS Processing"""

    def __init__(self):
        QgsProcessingProvider.__init__(self)

        self.activate = True

        # Load algorithms
        self.alglist = [BlurringGeoAlgorithm()]
        for alg in self.alglist:
            alg.provider = self

    def initializeSettings(self):
        QgsProcessingProvider.initializeSettings(self)

    def unload(self):
        #QgsProcessingProvider.unload(self)
        pass
    def loadAlgorithms(self):
        self.addAlgorithm(BlurringGeoAlgorithm())

    def id(self):
        return 'GeoPublicHealth'

    def getName(self):
        return 'GeoPublicHealth'

    def getDescription(self):
        return 'GeoPublicHealth'

    def getIcon(self):
        return QIcon(resource('icon-32.png'))

    def _loadAlgorithms(self):
        self.algs = self.alglist
