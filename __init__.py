# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoPublicHealth
                                 A QGIS plugin
 GeoPublicHealth
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

<<<<<<< HEAD
from GeoHealth.src.plugin import GeoHealthPlugin


def classFactory(iface):
    return GeoHealthPlugin(iface)
=======
from geopublichealth import GeoPublicHealth


def classFactory(iface):

    return GeoPublicHealth(iface)
>>>>>>> Change the files for the new name GeoPublicHealth
