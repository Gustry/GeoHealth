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

from numpy import median, average, var, std


class Stats(object):

    def __init__(self, figures):
        figures.sort()
        self.figures = figures
        self.null = len([x for x in self.figures if x is None])
        self.figures = self.figures[self.null:]
        self.nb_items = len(figures)

    def count(self):
        return self.nb_items

    def null_values(self):
        return self.null

    def min(self):
        return self.figures[0]

    def max(self):
        return self.figures[-1]

    def range(self):
        return self.max() - self.min()

    def average(self):
        return average(self.figures)

    def median(self):
        return median(self.figures)

    def variance(self):
        return var(self.figures)

    def standard_deviation(self):
        return std(self.figures)
