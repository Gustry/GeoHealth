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

<<<<<<< HEAD:src/gui/analysis/incidence_dialog.py
from GeoHealth.src.gui.analysis.parent_incidence_density_dialog import (
    IncidenceDensityDialog)
from GeoHealth.src.utilities.resources import get_ui_class
=======
from GeoPublicHealth.ui.analysis.incidence import Ui_Incidence
from GeoPublicHealth.gui.analysis.parent_incidence_density_dialog import IncidenceDensityDialog
>>>>>>> Change the files for the new name GeoPublicHealth:gui/analysis/incidence_dialog.py

FORM_CLASS = get_ui_class('analysis', 'incidence.ui')


class IncidenceDialog(IncidenceDensityDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        IncidenceDensityDialog.__init__(self, parent)
        # noinspection PyArgumentList
        FORM_CLASS.setupUi(self, self)

        self.use_area = False
        self.use_point_layer = False

        self.setup_ui()

    def run_stats(self):
        """Main function which do the process."""
        IncidenceDensityDialog.run_stats(self)
