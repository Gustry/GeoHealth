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

from random import uniform
from math import pi, cos, sin

from qgis.core import QgsFeature, QgsGeometry, QgsPoint

from GeoPublicHealth.core.exceptions import PointOutsideEnvelopeException


# noinspection PyArgumentList
class Blur(object):
    """Blurring algorithm."""

    @staticmethod
    def random_point_around_geom_point(point, radius):
        """Creating a random point."""
        teta = pi * uniform(0, 2)
        r = uniform(0, radius)
        random_x = point.asPoint().x() + (r * cos(teta))
        random_y = point.asPoint().y() + (r * sin(teta))
        # noinspection PyCallByClass,PyTypeChecker
        return QgsGeometry.fromPoint(QgsPoint(random_x, random_y))

    def __init__(
            self,
            radius,
            polygon_envelope,
            add_radius_to_attributes,
            add_centroid_to_attributes):
        self.__radius = radius
        self.__polygon_envelope = polygon_envelope
        self.__add_radius_to_attributes = add_radius_to_attributes
        self.__add_centroid_to_attributes = add_centroid_to_attributes

    def blur(self, feature):
        geom = feature.geometry()
        attributes = feature.attributes()
        random_point = None

        # If we use a mask
        if self.__polygon_envelope is not None:

            # We have to be sure that every initial point intersect the layer
            if not self.__polygon_envelope.contains(geom):
                raise PointOutsideEnvelopeException(number=feature.id())

            radius = self.__radius
            i = 0
            while True:
                random_point = Blur.random_point_around_geom_point(
                    geom, radius)
                if self.__polygon_envelope.contains(random_point):
                    break
                else:
                    i += 1
                    # After i increment, we reduce the first buffer
                    if i == 100:
                        radius = int(radius * 0.5)
                    elif i == 150:
                        radius = int(radius * 0.5)
                    elif i == 200:
                        radius = int(radius * 0.5)
                    elif i >= 250:
                        radius = 0

        else:
            random_point = Blur.random_point_around_geom_point(
                geom, self.__radius)

        # Creating the second buffer.
        buffer_geom = random_point.buffer(self.__radius, 20)
        buffer_feature = QgsFeature()
        buffer_feature.setGeometry(buffer_geom)

        if self.__add_radius_to_attributes:
            attributes.append(self.__radius)
        if self.__add_centroid_to_attributes:
            attributes.append(int(buffer_geom.centroid().asPoint().x()))
            attributes.append(int(buffer_geom.centroid().asPoint().y()))

        buffer_feature.setAttributes(attributes)
        return buffer_feature
