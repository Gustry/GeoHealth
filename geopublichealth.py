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

from os.path import dirname, join, exists

from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QIcon, QAction
from processing.core.Processing import Processing

from GeoPublicHealth.src.gui.main_window import MainDialog
from GeoPublicHealth.processing_geopublichealth.provider import Provider


class GeoPublicHealth:

    def __init__(self, iface):

        self.iface = iface
        self.plugin_dir = dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = join(
            self.plugin_dir,
            'i18n',
            'GeoPublicHealth_{}.qm'.format(locale))

        if exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
                QCoreApplication.installTranslator(self.translator)

        self.plugin_menu = None
        self.geopublichealth_menu = None
        self.main_action = None
        self.xy_action = None
        self.blur_action = None
        self.incidence_action = None
        self.density_action = None
        self.histogram_action = None

        #Add to processing
        self.provider = Provider()
        Processing.addProvider(self.provider, True)

    def initGui(self):

        self.plugin_menu = self.iface.pluginMenu()

        # Main window
        icon = QIcon(':/plugins/GeoPublicHealth/resources/icon-32.png')
        self.main_action = QAction(icon, 'GeoPublicHealth', self.iface.mainWindow())
        self.plugin_menu.addAction(self.main_action)
        # noinspection PyUnresolvedReferences
        self.main_action.triggered.connect(self.open_main_window)

    def unload(self):
        self.plugin_menu.removeAction(self.main_action)
        Processing.removeProvider(self.provider)

    @staticmethod
    def open_main_window():
        dialog = MainDialog()
        dialog.show()
        dialog.exec_()
