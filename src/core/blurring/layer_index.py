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

from qgis.core import QgsSpatialIndex, QgsFeatureRequest, QgsGeometry, QGis


class LayerIndex(object):
    """Check an intersection between a QgsGeometry and a QgsVectorLayer."""

    def __init__(self, layer):
        self.__layer = layer

        if QGis.QGIS_VERSION_INT >= 20700:
            self.__index = QgsSpatialIndex(layer.getFeatures())
        else:
            self.__index = QgsSpatialIndex()
            for ft in layer.getFeatures():
                self.__index.insertFeature(ft)

    def contains(self, point):
        """Return true if the point intersects the layer."""
        intersects = self.__index.intersects(point.boundingBox())
        for i in intersects:
            request = QgsFeatureRequest().setFilterFid(i)
            feat = self.__layer.getFeatures(request).next()
            if point.intersects(QgsGeometry(feat.geometry())):
                return True
        return False

    def count_intersection(self, buffer_geom, nb):
        """Return true if the buffer intersects enough entities."""
        count = 0
        intersects = self.__index.intersects(buffer_geom.boundingBox())
        for i in intersects:
            request = QgsFeatureRequest().setFilterFid(i)
            feat = self.__layer.getFeatures(request).next()

            if buffer_geom.intersects(QgsGeometry(feat.geometry())):
                count += 1
                if count >= nb:
                    return True
        return False
