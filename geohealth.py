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

from os.path import dirname, join, exists
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QMenu, QIcon, QAction
from qgis.utils import iface
from processing.core.Processing import Processing

from GeoHealth.core.tools import trans
from GeoHealth.gui.incidence_dialog import IncidenceDialog
from GeoHealth.gui.main_blurring_dialog import MainBlurringDialog
from GeoHealth.gui.histogram_dialog import HistogramDialog
from GeoHealth.processing_geohealth.provider import Provider


class GeoHealth:

    def __init__(self, iface):

        self.iface = iface
        self.plugin_dir = dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = join(
            self.plugin_dir,
            'i18n',
            'GeoHealth_{}.qm'.format(locale))

        if exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                # noinspection PyCallByClass
                QCoreApplication.installTranslator(self.translator)

        self.plugin_menu = None
        self.geohealth_menu = None
        self.blur_action = None
        self.incidence_action = None
        self.histogram_action = None

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
        self.blur_action = QAction(
            icon, trans("Blurring"), self.iface.mainWindow())
        self.geohealth_menu.addAction(self.blur_action)
        # noinspection PyUnresolvedReferences
        self.blur_action.triggered.connect(self.open_blurring_window)

        # Incidence
        icon = QIcon(":/plugins/GeoHealth/resources/incidence.png")
        self.incidence_action = QAction(
            icon, trans("Incidence - Density"), self.iface.mainWindow())
        self.geohealth_menu.addAction(self.incidence_action)
        # noinspection PyUnresolvedReferences
        self.incidence_action.triggered.connect(self.open_incidence_window)

        # Histogram
        icon = QIcon(":/plugins/GeoHealth/resources/histogram.png")
        self.histogram_action = QAction(
            icon, trans('Histogram'), self.iface.mainWindow())
        self.geohealth_menu.addAction(self.histogram_action)
        # noinspection PyUnresolvedReferences
        self.histogram_action.triggered.connect(self.open_histogram_window)

    def unload(self):
        self.iface.removePluginMenu(trans("Blurring"), self.blur_action)
        self.iface.removePluginMenu(
            trans("Incidence - Density"), self.incidence_action)
        Processing.removeProvider(self.provider)

    @staticmethod
    def open_incidence_window():
        dialog = IncidenceDialog()
        dialog.fill_combobox_layer()
        dialog.show()
        dialog.exec_()

    @staticmethod
    def open_blurring_window():
        # Todo, fix iface in display_message_bar
        iface.Blurring_mainWindowDialog = MainBlurringDialog()
        iface.Blurring_mainWindowDialog.fill_combo_box_layers()
        iface.Blurring_mainWindowDialog.show()
        iface.Blurring_mainWindowDialog.exec_()

    @staticmethod
    def open_histogram_window():
        dialog = HistogramDialog()
        dialog.show()
        dialog.exec_()
