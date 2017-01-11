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

from qgis.PyQt.QtGui import QIcon
from processing.core.AlgorithmProvider import AlgorithmProvider

from GeoHealth.geohealth.processing_geohealth.blurring import (
    BlurringGeoAlgorithm)
from GeoHealth.geohealth.utilities.resources import resource


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
        return 'GeoHealth'

    def getDescription(self):
        return 'GeoHealth'

    def getIcon(self):
        return QIcon(resource('icon-32.png'))

    def _loadAlgorithms(self):
        self.algs = self.alglist
