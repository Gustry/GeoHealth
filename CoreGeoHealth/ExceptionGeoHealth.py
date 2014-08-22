# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickOSM
                                 A QGIS plugin
 OSM's Overpass API frontend
                             -------------------
        begin                : 2014-06-11
        copyright            : (C) 2014 by 3Liz
        email                : info at 3liz dot com
        contributor          : Etienne Trimaille
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

"""
QApplication.translate doesn't work in contructor's parameters
"""

class GeoHealthException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        GeoAlgorithmExecutionException.__init__(self,msg)    
        self.level = QgsMessageBar.CRITICAL
        self.duration = 7

class NoLayerProvidedException(GeoHealthException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u"No layer was provided.")
        GeoHealthException.__init__(self,msg)
        
class NoFileNoDisplayException(GeoHealthException):
    def __init__(self, msg=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u'No file provided, "add resultat to canvas" required')
        GeoHealthException.__init__(self,msg)

class CreatingShapeFileException(GeoHealthException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u'Error while creating the shapefile')
        if suffix:
            msg += suffix
        GeoHealthException.__init__(self,msg)

class PointOutsideEnvelopeException(GeoHealthException):
    def __init__(self, msg=None, number=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u'Point number %d is outside the envelope.' %number)
        GeoHealthException.__init__(self,msg)

class DifferentCrsException(GeoHealthException):
    def __init__(self, msg=None, epsg1=None, epsg2=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u"It's not the same projection system : %s != %s" %(epsg1,epsg2))
        GeoHealthException.__init__(self,msg)

class NotANumberException(GeoHealthException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = QApplication.translate("GeoHealth",u"It's not a number")
        if suffix:
            msg += " : %s"%suffix
        GeoHealthException.__init__(self,msg)

