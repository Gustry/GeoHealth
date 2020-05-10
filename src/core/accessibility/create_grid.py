# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2016-11-20
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

from PyQt4.QtCore import QVariant

from qgis.core import (
    QGis,
    QgsVectorLayer,
    QgsCoordinateReferenceSystem,
    QgsPoint,
    QgsFields,
    QgsField,
    QgsFeature,
    QgsGeometry,
)

from GeoHealth.src.core.tools import create_memory_layer


def create_grid(extent, space, crs):
    """Create a grid polygon.

    :param extent: The extend where to create the grid.
    :type extent: QgsRectangle

    :param space: The X and Y size.
    :type space: float

    :param crs: The CRS of the new grid.
    :type crs: QgsCoordinateReferenceSystem

    :return: THe vector grid.
    :rtype: QgsVectorLayer
    """

    fields = QgsFields()
    fields.append(QgsField('id', QVariant.Int, '', 10, 0))
    fields.append(QgsField('xmin', QVariant.Double, '', 24, 15))
    fields.append(QgsField('xmax', QVariant.Double, '', 24, 15))
    fields.append(QgsField('ymin', QVariant.Double, '', 24, 15))
    fields.append(QgsField('ymax', QVariant.Double, '', 24, 15))

    writer = create_memory_layer('grid', QGis.Polygon, crs, fields)
    writer.startEditing()

    feat = QgsFeature()
    feat.initAttributes(len(fields))
    feat.setFields(fields)
    geom = QgsGeometry()
    id_polygon = 0

    count = 0
    y = extent.yMaximum()
    while y >= extent.yMinimum():
        x = extent.xMinimum()
        while x <= extent.xMaximum():
            polygon = [
                [
                    QgsPoint(x, y),
                    QgsPoint(x + space, y),
                    QgsPoint(x + space, y - space),
                    QgsPoint(x, y - space),
                    QgsPoint(x, y)
                ]
            ]
            feat.setGeometry(geom.fromPolygon(polygon))
            feat.setAttribute(0, id_polygon)
            feat.setAttribute(1, x)
            feat.setAttribute(2, x + space)
            feat.setAttribute(3, y - space)
            feat.setAttribute(4, y)
            writer.addFeature(feat)
            id_polygon += 1
            x += space
        y -= space
        count += 1

    writer.commitChanges()

    return writer
