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

from GeoHealth.ui.incidence import Ui_Incidence
from GeoHealth.gui.incidence_density_dialog import IncidenceDensityDialog


class IncidenceDialog(IncidenceDensityDialog, Ui_Incidence):
    def __init__(self, parent=None):
        """Constructor."""
        IncidenceDensityDialog.__init__(self, parent)
        Ui_Incidence.setupUi(self, self)

        self.setup_ui()
        self.fill_combobox_layer()
        self.update_fields()

        # Connect slot.
        # noinspection PyUnresolvedReferences
        self.cbx_aggregation_layer.currentIndexChanged.connect(
            self.update_fields)

    def update_fields(self):
        """Update the combobox about the population field."""
        self.cbx_population_field.clear()

        index = self.cbx_aggregation_layer.currentIndex()
        admin_layer = self.cbx_aggregation_layer.itemData(index)
        if not admin_layer:
            return False

        fields = admin_layer.dataProvider().fields()

        for item in fields:
            self.cbx_population_field.addItem(item.name(), item)

    def run_stats(self):
        """Main function which do the process."""
        IncidenceDensityDialog.run_stats(self, use_area=False)
