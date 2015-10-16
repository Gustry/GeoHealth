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
from GeoHealth.ui.main_blurring import Ui_BlurringDialogBase
from os.path import join, dirname, abspath, isfile


class MainBlurringDialog(QDialog, Ui_BlurringDialogBase):

    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self)
        self.setupUi(self)

        #Connect
        self.blur.signalAskCloseWindow.connect(self.hide)
        self.statistics.signalAskCloseWindow.connect(self.hide)

        self.set_help_web_view()

    def set_help_web_view(self):
        """Set the help."""
        locale = QSettings().value("locale/userLocale")[0:2]
        locale += "."
        help_file_base = "main"
        helps = [help_file_base + locale + '.html', help_file_base + '.html']

        doc_path = join(dirname(dirname(abspath(__file__))), 'doc')
        for helpFileName in helps:
            help_file_path = join(doc_path, helpFileName)
            if isfile(help_file_path):
                self.webview.load(QUrl(help_file_path))
                break
        else:
            self.webview.setHtml("<h3>Help not available</h3>")

    def fill_combo_box_layers(self):
        self.statistics.fill_comboxbox_layers()
        self.blur.fill_comboxbox_layers()
