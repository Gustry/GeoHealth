# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Blurring
                                 A QGIS plugin
 Blur a point layer
                             -------------------
        begin                : 2014-03-05
        copyright            : (C) 2014 by UMR Espace-Dev
        email                : etienne at trimaille dot eu
        contributor          : Etienne Trimaille
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

class Stats:

    def __init__(self,listStats):
        listStats.sort()
        self.listStats = listStats 
        self.nbItems = len(listStats)
    
    def count(self):
        return self.nbItems

    def min(self):
        return self.listStats[0]
    
    def max(self):
        return self.listStats[-1]
    
    def range(self):
        return self.max() - self.min()

    def average(self) :
        return average(self.listStats)

    def median(self):
        return median(self.listStats)

    def variance(self) :
        return var(self.listStats)

    def standardDeviation(self):
        return std(self.listStats)