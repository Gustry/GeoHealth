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

from qgis.gui import QgsMessageBar
from processing.core.GeoAlgorithmExecutionException import \
    GeoAlgorithmExecutionException

from GeoPublicHealth.src.core.tools import tr

# QApplication.translate doesn't work in constructor's parameters.


class GeoPublicHealthException(GeoAlgorithmExecutionException):
    def __init__(self, msg=None):
        GeoAlgorithmExecutionException.__init__(self, msg)
        self.level = QgsMessageBar.CRITICAL
        self.duration = 7


class NoLayerProvidedException(GeoPublicHealthException):
    def __init__(self, msg=None):
        if not msg:
            msg = tr(u'No layer was provided.')
        GeoPublicHealthException.__init__(self, msg)


class NoFileNoDisplayException(GeoPublicHealthException):
    def __init__(self, msg=None):
        if not msg:
            msg = tr(u'No file provided, "add result to canvas" required')
        GeoPublicHealthException.__init__(self, msg)


class CreatingShapeFileException(GeoPublicHealthException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = tr(u'Error while creating the shapefile')
        if suffix:
            msg += suffix
        GeoPublicHealthException.__init__(self, msg)


class PointOutsideEnvelopeException(GeoPublicHealthException):
    def __init__(self, msg=None, number=None):
        if not msg:
            msg = tr(u'Point number %d is outside the envelope.' % number)
        GeoPublicHealthException.__init__(self, msg)


class DifferentCrsException(GeoPublicHealthException):
    def __init__(self, msg=None, epsg1=None, epsg2=None):
        if not msg:
            msg = tr(u'It\'s not the same projection system : %s != %s' %
                     (epsg1, epsg2))
        GeoPublicHealthException.__init__(self, msg)


class FieldExistingException(GeoPublicHealthException):
    def __init__(self, msg=None, field=None):
        if not msg:
            msg = tr(u'The field %s already exists in the layer.' % field)
        GeoPublicHealthException.__init__(self, msg)


class NotANumberException(GeoPublicHealthException):
    def __init__(self, msg=None, suffix=None):
        if not msg:
            msg = tr(u'It\'s not a number')
        if suffix:
            msg += " : %s" % suffix
        GeoPublicHealthException.__init__(self, msg)


class FieldException(GeoPublicHealthException):
    def __init__(self, msg=None, field_1=None, field_2=None):
        if not msg:
            msg = tr(u'Fields are not different')
        if field_1 and field_2:
            msg += " : %s and %s " % (field_1, field_2)
        GeoPublicHealthException.__init__(self, msg)
