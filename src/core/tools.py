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

from uuid import uuid4
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QApplication
from qgis.utils import iface
from qgis.gui import QgsMessageBar
from qgis.core import QgsVectorLayer, QGis


def create_memory_layer(
        layer_name, geometry, coordinate_reference_system=None, fields=None):
    """Create a vector memory layer.

    :param layer_name: The name of the layer.
    :type layer_name: str

    :param geometry: The geometry of the layer.
    :rtype geometry: QGis.WkbType

    :param coordinate_reference_system: The CRS of the memory layer.
    :type coordinate_reference_system: QgsCoordinateReferenceSystem

    :param fields: Fields of the vector layer. Default to None.
    :type fields: QgsFields

    :return: The memory layer.
    :rtype: QgsVectorLayer
    """

    if geometry == QGis.Point:
        type_string = 'MultiPoint'
    elif geometry == QGis.Line:
        type_string = 'MultiLineString'
    elif geometry == QGis.Polygon:
        type_string = 'MultiPolygon'
    elif geometry == QGis.NoGeometry:
        type_string = 'none'
    else:
        raise Exception(
            'Layer is whether Point nor Line nor Polygon, I got %s' % geometry)

    uri = '%s?index=yes&uuid=%s' % (type_string, str(uuid4()))
    if coordinate_reference_system:
        crs = coordinate_reference_system.authid().lower()
        uri += '&crs=%s' % crs
    memory_layer = QgsVectorLayer(uri, layer_name, 'memory')
    memory_layer.keywords = {
        'inasafe_fields': {}
    }

    if fields:
        data_provider = memory_layer.dataProvider()
        data_provider.addAttributes(fields)
        memory_layer.updateFields()

    return memory_layer


def get_last_input_path():
    settings = QSettings()
    return settings.value('LastInputPath')


def set_last_input_path(directory):
    settings = QSettings()
    settings.setValue('LastInputPath', str(directory))


def tr(msg):
    # noinspection PyCallByClass,PyArgumentList
    return QApplication.translate('GeoHealth', msg)


def display_message_bar(
        title=None, msg=None, level=QgsMessageBar.INFO, duration=5):

    try:
        if iface.Blurring_mainWindowDialog.isVisible():
            iface.Blurring_mainWindowDialog.messageBar.pushMessage(
                title, msg, level, duration)
        else:
            iface.messageBar().pushMessage(title, msg, level, duration)
    except AttributeError:
        iface.messageBar().pushMessage(title, msg, level, duration)
