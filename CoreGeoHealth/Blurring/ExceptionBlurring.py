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

from Blurring import *

"""
QApplication.translate doesn't work in contructor's parameters
"""

class BlurringException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        GeoAlgorithmExecutionException.__init__(self,msg)    
        self.level = QgsMessageBar.CRITICAL
        self.duration = 7

class NoLayerProvidedException(BlurringException):
    def __init__(self, msg=None):
        if not msg:
            msg = Tools.trans(u"No layer was provided.")
        BlurringException.__init__(self,msg)
        
class NoFileNoDisplayException(BlurringException):
    def __init__(self, msg=None):
        if not msg:
            msg = Tools.trans(u'No file provided, "add resultat to canvas" required')
        BlurringException.__init__(self,msg)

class CreatingShapeFileException(BlurringException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = Tools.trans(u'No file provided, "add resultat to canvas" required')
        if suffix:
            msg += suffix
        BlurringException.__init__(self,msg)

class PointOutsideEnvelopeException(BlurringException):
    def __init__(self, msg=None, number=None):
        if not msg:
            msg = Tools.trans(u'Point number %d is outside the envelope.' %number)
        BlurringException.__init__(self,msg)

class DifferentCrsException(BlurringException):
    def __init__(self, msg=None, epsg1=None, epsg2=None):
        if not msg:
            msg = Tools.trans(u"It's not the same projection system : %s != %s" %(epsg1,epsg2))
        BlurringException.__init__(self,msg)
