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
"""

from GeoHealth.geohealth.plugin import GeoHealthPlugin


def classFactory(iface):
    return GeoHealthPlugin(iface)
