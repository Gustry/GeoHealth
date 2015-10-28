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

from PyQt4.QtGui import QDialog

from GeoHealth.ui.main_blurring import Ui_Form


class MainBlurringDialog(QDialog, Ui_Form):

    def __init__(self, parent=None):
        """Constructor."""
        self.parent = parent
        QDialog.__init__(self)
        self.setupUi(self)

        #Connect
        self.blur.signalAskCloseWindow.connect(self.hide)
        self.statistics.signalAskCloseWindow.connect(self.hide)

    def fill_combo_box_layers(self):
        self.statistics.fill_comboxbox_layers()
        self.blur.fill_comboxbox_layers()
