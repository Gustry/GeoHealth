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

from processing.core.Processing import Processing

from GeoHealth import *
from GeoHealth.core.tools import trans
from GeoHealth.gui.incidence_dialog import IncidenceDialog
from GeoHealth.gui.main_blurring_dialog import MainBlurringDialog
from GeoHealth.processing_geohealth.provider import Provider


class GeoHealth:

    def __init__(self, iface):

        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeoHealth_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        #Add to processing
        self.provider = Provider()
        Processing.addProvider(self.provider, True)

    def initGui(self):

        # Setup the menu.
        self.geohealth_menu = QMenu(trans("&GeoHealth"))
        self.geohealth_menu.setIcon(
            QIcon(':/plugins/GeoHealth/resources/icon.png'))
        self.plugin_menu = self.iface.pluginMenu()
        self.plugin_menu.addMenu(self.geohealth_menu)

        # Blur
        icon = QIcon(":/plugins/GeoHealth/resources/blur.png")
        self.blur_action = QAction(icon, trans("Blurring"), self.iface.mainWindow())
        self.geohealth_menu.addAction(self.blur_action)
        self.blur_action.triggered.connect(self.open_blurring_window)

        # Incidence
        icon = QIcon(":/plugins/GeoHealth/resources/incidence.png")
        self.incidence_action = QAction(icon, trans("Incidence - Density"), self.iface.mainWindow())
        self.geohealth_menu.addAction(self.incidence_action)
        self.incidence_action.triggered.connect(self.open_incidence_window)

    def unload(self):
        self.iface.removePluginMenu(trans("Blurring"), self.blur_action)
        self.iface.removePluginMenu(trans("Incidence - Density"), self.incidence_action)
        Processing.removeProvider(self.provider)

    def open_incidence_window(self):
        dialog = IncidenceDialog()
        dialog.fill_combobox_layer()
        dialog.show()
        dialog.exec_()

    def open_blurring_window(self):
        iface.Blurring_mainWindowDialog = MainBlurringDialog()
        iface.Blurring_mainWindowDialog.fill_combo_box_layers()
        iface.Blurring_mainWindowDialog.show()
        iface.Blurring_mainWindowDialog.exec_()
