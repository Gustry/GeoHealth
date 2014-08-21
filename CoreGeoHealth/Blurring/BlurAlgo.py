# -*- coding: utf-8 -*-
"""
/***************************************************************************
Blurring
A QGIS plugin
Blurring data
-------------------
begin : 2014-03-11
copyright : (C) 2014 by TER Géomatique UM2
email : ter-floutage@googlegroups.com
***************************************************************************/

/***************************************************************************
* *
* This program is free software; you can redistribute it and/or modify *
* it under the terms of the GNU General Public License as published by *
* the Free Software Foundation; either version 2 of the License, or *
* (at your option) any later version. *
* *
***************************************************************************/
"""

from Blurring import *
import random, math
from math import sqrt

"""Blurring's algorithm"""

class BlurAlgo:
    
    @staticmethod
    def randomPointAroundGeomPoint(point,radius):
        """Creating a random point"""
        teta = math.pi*random.uniform(0, 2)
        r = random.randint(0,radius)
        randomX = point.asPoint().x()+ (r * math.cos(teta))
        randomY = point.asPoint().y()+ (r * math.sin(teta))
        return QgsGeometry.fromPoint(QgsPoint(randomX, randomY)) 
    
    def __init__(self,radius, polygonEnvelope,addRadiusToAttributes, addCentroidToAttributes):
        self.__radius = radius
        self.__polygonEnvelope = polygonEnvelope
        self.__addRadiusToAttributes = addRadiusToAttributes
        self.__addCentroidToAttributes = addCentroidToAttributes
 
    
    def blur(self, feature):
        geom = feature.geometry()
        attrs = feature.attributes()
        pointAleaGeom = None
        
        #If we use a mask
        if self.__polygonEnvelope != None:
            
            #We have to be sure that every intial point intersect the layer
            if not self.__polygonEnvelope.contains(geom):
                raise PointOutsideEnvelopeException(number=feature.id())
            
            radius = self.__radius
            i = 0
            while True:
                pointAleaGeom = BlurAlgo.randomPointAroundGeomPoint(geom, radius)
                if self.__polygonEnvelope.contains(pointAleaGeom):
                    break
                else:
                    i +=1
                    #after i increment, we reduce the first buffer
                    if i == 100:
                        radius = int(radius * 0.5)
                    elif i == 150:
                        radius = int(radius * 0.5)
                    elif i == 200:
                        radius = int(radius * 0.5)
                    elif i >= 250:
                        radius = 0
                        break
        else:
            pointAleaGeom = BlurAlgo.randomPointAroundGeomPoint(geom, self.__radius)
        
        """Creating the second buffer"""
        bufferGeom = pointAleaGeom.buffer(self.__radius,20)
        bufferFeature = QgsFeature()
        bufferFeature.setGeometry(bufferGeom)
        
        if self.__addRadiusToAttributes:
            attrs.append(self.__radius)
        if self.__addCentroidToAttributes:
            attrs.append(int(bufferGeom.centroid().asPoint().x()))
            attrs.append(int(bufferGeom.centroid().asPoint().y()))

        bufferFeature.setAttributes(attrs)
        return bufferFeature 