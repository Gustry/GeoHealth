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

from qgis.core import QGis, QgsFeatureRequest

from GeoHealth import *
from GeoHealth.ui.stats import Ui_Stats
from GeoHealth.core.tools import \
    trans, display_message_bar, get_last_input_path, set_last_input_path
import os
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar

#import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class StatsWidget(QWidget, Ui_Stats):
    
    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')
    
    def __init__(self, parent=None):
        super(StatsWidget, self).__init__()
        self.setupUi(self)

        self.label_progressStats.setText("")

        #Connect
        self.pushButton_saveTable.clicked.connect(self.saveTable)
        self.pushButton_saveYValues.clicked.connect(self.saveYValues)
        self.buttonBox_stats.button(QDialogButtonBox.Ok).clicked.connect(self.runStats)
        self.buttonBox_stats.button(QDialogButtonBox.Cancel).clicked.connect(self.signalAskCloseWindow.emit)
        
        # a figure instance to plot on
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)

    def fillComboxboxLayers(self):
        self.comboBox_blurredLayer.clear()
        self.comboBox_statsLayer.clear()

        for layer in iface.legendInterface().layers():
            if layer.type() == 0 :
                self.comboBox_statsLayer.addItem(layer.name(),layer)
                
                if layer.geometryType() == 2 :
                    self.comboBox_blurredLayer.addItem(layer.name(),layer)
    
    def runStats(self):
        self.progressBar_stats.setValue(0)
        self.label_progressStats.setText("")
        QApplication.processEvents()
        
        index = self.comboBox_blurredLayer.currentIndex()
        layerBlurred = self.comboBox_blurredLayer.itemData(index)
        
        index = self.comboBox_statsLayer.currentIndex()
        layerStats = self.comboBox_statsLayer.itemData(index)
        
        try:
            
            if not layerBlurred or not layerStats:
                raise NoLayerProvidedException
            
            crsLayerBlurred = layerBlurred.crs()
            crsLayerStats = layerStats.crs()
            if crsLayerBlurred != crsLayerStats:
                raise DifferentCrsException(epsg1 = crsLayerBlurred.authid(), epsg2 = crsLayerStats.authid())
            
            if layerBlurred == layerStats:
                raise NoLayerProvidedException
            
            if not layerBlurred or not layerStats:
                raise NoLayerProvidedException
            
            nbFeatureStats = layerStats.featureCount()
            nbFeatureBlurred = layerBlurred.featureCount()
            featuresStats = {}

            label_preparing = trans('Preparing index on the stats layer')
            label_creating = trans('Creating index on the stats layer')
            label_calculating = trans('Calculating')

            if QGis.QGIS_VERSION_INT < 20700:
                self.label_progressStats.setText('%s 1/3' % label_preparing)

                for i, feature in enumerate(layerStats.getFeatures()):
                    featuresStats[feature.id()] = feature
                    percent = int((i + 1) * 100 / nbFeatureStats)
                    self.progressBar_stats.setValue(percent)
                    QApplication.processEvents()

                self.label_progressStats.setText('%s 2/3' % label_creating)
                QApplication.processEvents()
                index = QgsSpatialIndex()
                for i, f in enumerate(layerStats.getFeatures()):
                    index.insertFeature(f)

                    percent = int((i + 1) * 100 / nbFeatureStats)
                    self.progressBar_stats.setValue(percent)
                    QApplication.processEvents()

                self.label_progressStats.setText('%s 3/3' % label_calculating)

            else:
                # If QGIS >= 2.7, we can speed up the spatial index.
                # From 1 min 15 to 7 seconds on my PC.
                self.label_progressStats.setText('%s 1/2' % label_creating)
                QApplication.processEvents()
                index = QgsSpatialIndex(layerStats.getFeatures())
                self.label_progressStats.setText('%s 2/2' % label_calculating)

            self.tab = []
            QApplication.processEvents()
            for i, feature in enumerate(layerBlurred.getFeatures()):
                count = 0
                ids = index.intersects(feature.geometry().boundingBox())
                for id in ids:
                    request = QgsFeatureRequest().setFilterFid(id)
                    f = layerStats.getFeatures(request).next()

                    if f.geometry().intersects(feature.geometry()):
                        count += 1
                self.tab.append(count)
                
                percent = int((i + 1) * 100 / nbFeatureBlurred)
                self.progressBar_stats.setValue(percent)
                QApplication.processEvents()
            
            stats = Stats(self.tab)
            
            itemsStats = []
            itemsStats.append("Count(blurred),%d"%nbFeatureBlurred)
            itemsStats.append("Count(stats),%d"%nbFeatureStats)
            itemsStats.append("Min,%d"%stats.min())
            itemsStats.append("Average,%f"%stats.average())
            itemsStats.append("Max,%d"%stats.max())
            itemsStats.append("Median,%f"%stats.median())
            itemsStats.append("Range,%d"%stats.range())
            itemsStats.append("Variance,%f"%stats.variance())
            itemsStats.append("Standard deviation,%f"%stats.standard_deviation())
            
            self.tableWidget.clear()
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(['Parameters','Values'])
            self.tableWidget.setRowCount(len(itemsStats))
            
            for i,item in enumerate(itemsStats):
                s = item.split(',')
                self.tableWidget.setItem(i, 0, QTableWidgetItem(s[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(s[1]))
            self.tableWidget.resizeRowsToContents()
            
            self.drawPlot(self.tab)
            
        except GeoHealthException,e:
            self.label_progressStats.setText("")
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)
            
    def saveTable(self):
        
        if not self.tableWidget.rowCount():
            return False
        
        csvString = "parameter,values\n"
        
        for i in range(self.tableWidget.rowCount()):
            itemParam = self.tableWidget.item(i,0) 
            itemValue = self.tableWidget.item(i,1)
            csvString += str(itemParam.text()) + "," + itemValue.text() + "\n"
            
        lastDir = get_last_input_path()
  
        outputFile = QFileDialog.getSaveFileName(parent=self,
                                                 caption=trans('Select file'),
                                                 directory=lastDir,
                                                 filter="CSV (*.csv)")
        if outputFile:
            path = os.path.dirname(outputFile)
            set_last_input_path(path)

            fh = open(outputFile,"w")
            fh.write(csvString)
            fh.close()
            return True
   
    def saveYValues(self):
        
        if not self.tableWidget.rowCount():
            return False
        
        csvString = "parameter,values\n"
        
        for value in self.tab:
            csvString += str(value) + "\n"
            
        lastDir = get_last_input_path()
        outputFile = QFileDialog.getSaveFileName(parent=self,
                                                 caption=trans('Select file'),
                                                 directory=lastDir,
                                                 filter="CSV (*.csv)")
        if outputFile:
            path = os.path.dirname(outputFile)
            set_last_input_path(path)

            fh = open(outputFile,"w")
            fh.write(csvString)
            fh.close()
            return True    

    def drawPlot(self,data):
        #Creating the plot        
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data, '*-')
        
        #ax.set_title('Number of intersections per entity')
        ax.set_xlabel('Blurred entity')
        ax.set_ylabel('Number of intersections')
        ax.grid()
        
        # refresh canvas
        self.canvas.draw()    

class NavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Next', 'Pan', 'Zoom', 'Save')]