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

import math

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
        return sum(self.listStats) / self.nbItems
    
    def stat_variance(self) :
        mq = self.average()**2
        s = sum( [ x**2 for x in self.listStats ] )
        variance = s / self.nbItems - mq
        return variance

    def stat_ecart_type(self):
        variance = self.stat_variance()
        ecart_type = math.sqrt(variance)
        return ecart_type       