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

from PyQt4.QtGui import QWidget, QMdiArea, QVBoxLayout
from qgis.core import QgsProviderRegistry


from GeoHealth.core.tools import trans


class OpenCsv(QWidget):

    def __init__(self, parent=None):
        self.parent = parent
        super(OpenCsv, self).__init__()

        mdi_area = QMdiArea()

        dialog = QgsProviderRegistry.instance().selectWidget('delimitedtext')
        dialog.setWindowTitle(trans('XY to map'))

        layout = QVBoxLayout(self)
        layout.addWidget(mdi_area)
        mdi_area.addSubWindow(dialog)
