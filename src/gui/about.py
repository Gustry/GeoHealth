# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoPublicHealth
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

from qgis.PyQt.QtWidgets import QWidget
from qgis.PyQt.QtGui import QPixmap
from GeoPublicHealth.src.utilities.resources import get_ui_class, resource

FORM_CLASS = get_ui_class('default', 'about.ui')


class AboutWidget(QWidget, FORM_CLASS):

    def __init__(self, parent=None):
        self.parent = parent
        super(AboutWidget, self).__init__()
        self.setupUi(self)

        self.logo_geopublichealth.setPixmap(QPixmap(resource('icon-100.png')))
        self.logo_ird.setPixmap(QPixmap(resource('logo_ird.png')))
        self.logo_umr.setPixmap(QPixmap(resource('espace-dev.png')))
