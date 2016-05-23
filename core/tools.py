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

from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QApplication
from qgis.utils import iface
from qgis.gui import QgsMessageBar


def get_last_input_path():
    settings = QSettings()
    return settings.value('LastInputPath')


def set_last_input_path(directory):
    settings = QSettings()
    settings.setValue('LastInputPath', str(directory))


def tr(msg):
    # noinspection PyCallByClass,PyArgumentList
    return QApplication.translate('GeoPublicHealth', msg)


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
