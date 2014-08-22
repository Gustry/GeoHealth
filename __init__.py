# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoHealth
                                 A QGIS plugin
 GeoHealth
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
 This script initializes the plugin, making it known to QGIS.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
from CoreGeoHealth.Tools import *
from CoreGeoHealth.Stats import *
from processing.core.GeoAlgorithmExecutionException import GeoAlgorithmExecutionException
from CoreGeoHealth.ExceptionGeoHealth import *


import os.path
import resources_rc

def classFactory(iface):
        
    from geohealth import GeoHealth
    return GeoHealth(iface)