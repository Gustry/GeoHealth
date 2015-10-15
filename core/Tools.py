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

from GeoHealth import *

class Tools:

    @staticmethod
    def getLastInputPath():
        settings = QSettings()
        return settings.value("LastInputPath")
    
    @staticmethod
    def setLastInputPath(lastDir):
        path = lastDir
        settings = QSettings()
        settings.setValue( "LastInputPath", str(path))
       
    @staticmethod
    def trans(msg):
        return QApplication.translate("GeoHealth",msg)
    
    @staticmethod
    def displayMessageBar(title = None, msg = None,level=QgsMessageBar.INFO,duration=5):
        if iface.Blurring_mainWindowDialog.isVisible():
            iface.Blurring_mainWindowDialog.messageBar.pushMessage(title, msg, level,duration)
        else:
            iface.messageBar().pushMessage(title, msg, level,duration)