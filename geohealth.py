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
from ui.incidence_dialog import IncidenceDialog
from ui.main_blurring_dialog import MainBlurringDialog
from GeoHealth.ProcessingGeoHealth.GeoHealthAlgorithmProvider import GeoHealthAlgorithmProvider
from processing.core.Processing import Processing


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
        self.provider = GeoHealthAlgorithmProvider()
        Processing.addProvider(self.provider, True)

    def initGui(self):
        
        self.geohealth_menu = QMenu(Tools.trans("&GeoHealth"))
        
        self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.geohealth_menu)

        #Blur
        icon = QIcon(":/plugins/GeoHealth/resources/blur.png")
        self.blur_action = QAction(icon,Tools.trans("Blurring"),self.iface.mainWindow())
        self.geohealth_menu.addAction(self.blur_action)
        self.blur_action.triggered.connect(self.openBlurring)
        
        #Incidence
        icon = QIcon(":/plugins/GeoHealth/resources/incidence.png")
        self.incidence_action = QAction(icon,Tools.trans("Incidence - Density"),self.iface.mainWindow())
        self.geohealth_menu.addAction(self.incidence_action)
        self.incidence_action.triggered.connect(self.openIncidence)

    def unload(self):
        self.iface.mainWindow().menuBar().removeAction(self.geohealth_menu.menuAction())
        Processing.removeProvider(self.provider)
        
    def openIncidence(self):
        dialog = IncidenceDialog(self.iface)
        dialog.fillComboboxLayer()
        dialog.show()
        dialog.exec_()
        
    def openBlurring(self):
        iface.Blurring_mainWindowDialog = MainBlurringDialog(self.iface)
        iface.Blurring_mainWindowDialog.fillComboxboxLayers()
        iface.Blurring_mainWindowDialog.show()
        iface.Blurring_mainWindowDialog.exec_()