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
try:
    from matplotlib.backends.backend_qt4agg import \
        NavigationToolbar2QTAgg as NavigationToolbar
except ImportError:
    from matplotlib.backends.backend_qt4agg import \
        NavigationToolbar2Qt as NavigationToolbar


class CustomNavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Next', 'Pan', 'Zoom', 'Save')]
