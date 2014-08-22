# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoHealthDialog
                                 A QGIS plugin
 GeoHealth
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
from incidence import Ui_Incidence
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

class NavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Next', 'Pan', 'Zoom', 'Save')]

class IncidenceDialog(QDialog, Ui_Incidence):
    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self)
        self.setupUi(self)
        
        #Connect
        self.comboBox_incidence_adminLayer.currentIndexChanged.connect(self.updateFields)
        self.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(self.runStats)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(self.hide)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)
        
    def updateFields(self):
        self.comboBox_incidence_populationField.clear()
        
        index = self.comboBox_incidence_adminLayer.currentIndex()
        adminLayer = self.comboBox_incidence_adminLayer.itemData(index)
        if not adminLayer:
            return False
        
        fields = adminLayer.dataProvider().fields()
        
        for item in fields:
            self.comboBox_incidence_populationField.addItem(item.name(),item)

    def fillComboboxLayer(self):
        self.comboBox_incidence_adminLayer.clear()
        self.comboBox_incidence_pointLayer.clear()
        self.comboBox_incidence_populationField.clear()

        for layer in iface.legendInterface().layers():
            if layer.type() == 0 :
                
                if layer.geometryType() == 0 :
                    self.comboBox_incidence_pointLayer.addItem(layer.name(),layer)
                
                if layer.geometryType() == 2 :
                    self.comboBox_incidence_adminLayer.addItem(layer.name(),layer)
                    
    def runStats(self):
        #Get the fields
        index = self.comboBox_incidence_adminLayer.currentIndex()
        adminLayer = self.comboBox_incidence_adminLayer.itemData(index)
        index = self.comboBox_incidence_pointLayer.currentIndex()
        pointLayer = self.comboBox_incidence_pointLayer.itemData(index)
        population = self.comboBox_incidence_populationField.currentText()
        self.nameField = self.lineEdit_incidence_columnName.text()
        ratio = self.comboBox_incidence_ratio.currentText()
        ratio = ratio.replace(" ","")
        
        try:
            
            if not adminLayer or not pointLayer:
                raise NoLayerProvidedException

            crsAdminLayer = adminLayer.crs()
            crsPointLayer = pointLayer.crs()
            if crsAdminLayer != crsPointLayer:
                raise DifferentCrsException(epsg1 = crsPointLayer.authid(), epsg2 = crsAdminLayer.authid())
            
            try :
                ratio = float(ratio)
            except ValueError:
                raise NotANumberException(suffix=ratio)
            
            useArea = self.radioButton_incidence_area.isChecked()
            addNbIntersections = self.checkBox_addNbIntersections.isChecked()
            
            indexPopulation = None
            if not useArea:
                indexPopulation = adminLayer.fieldNameIndex(population)
            
            adminLayerProvider = adminLayer.dataProvider()
            adminLayer.startEditing()
            adminLayerProvider.addAttributes([QgsField(self.nameField, QVariant.Double)])
            
            if addNbIntersections:
                adminLayerProvider.addAttributes([QgsField("nb_of_intersections", QVariant.Int)])
            
            adminLayer.updateFields()
            fields = adminLayer.pendingFields()
            nbFields = fields.count()
            
            numFieldIncidence = None
            numFieldIntersections = None        
            
            if addNbIntersections:
                numFieldIncidence = nbFields-2
                numFieldIntersections = nbFields-1
            else:
                numFieldIncidence = nbFields-1
            
            data = []
            
            for i,feature in enumerate(adminLayer.getFeatures()):
                attrs = feature.attributes()
                count = 0
                for f in pointLayer.getFeatures():
                    if f.geometry().intersects(feature.geometry()):
                        count += 1
                
                indice = None
                if useArea:
                    indice = float(count) / feature.geometry().area() * ratio
                else:
                    try :
                        population = float(attrs[indexPopulation])
                    except ValueError:
                        adminLayer.rollBack()
                        raise NotANumberException(suffix=attrs[indexPopulation])
                    indice = float(count) / population * ratio
                
                data.append(indice)
                adminLayer.changeAttributeValue(feature.id(), numFieldIncidence, indice)
                if addNbIntersections:
                    adminLayer.changeAttributeValue(feature.id(), numFieldIntersections, count)
            
            adminLayer.commitChanges()
            adminLayer.updateFields()
            
            if self.checkBox_incidence_runStats.isChecked():
            
                stats = Stats(data)
                
                itemsStats = []
                itemsStats.append("Count(point),%d"%pointLayer.featureCount())
                itemsStats.append("Count(polygon),%d"%adminLayer.featureCount())
                itemsStats.append("Min,%d"%stats.min())
                itemsStats.append("Average,%f"%stats.average())
                itemsStats.append("Max,%d"%stats.max())
                itemsStats.append("Median,%f"%stats.median())
                itemsStats.append("Range,%d"%stats.range())
                itemsStats.append("Variance,%f"%stats.variance())
                itemsStats.append("Standard deviation,%f"%stats.standardDeviation())
                
                self.tableWidget.clear()
                self.tableWidget.setColumnCount(2)
                self.tableWidget.setHorizontalHeaderLabels(['Parameters','Values'])
                self.tableWidget.setRowCount(len(itemsStats))
                
                for i,item in enumerate(itemsStats):
                    s = item.split(',')
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(s[0]))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(s[1]))
                self.tableWidget.resizeRowsToContents()
                
                self.drawPlot(data)
            
            else:
                self.hide()
        
        except GeoHealthException,e:
            self.messageBar.pushMessage(e.msg, level=e.level, duration=e.duration)
        
    def drawPlot(self,data):
        ax = self.figure.add_subplot(111)
        ax.hold(False)
        ax.plot(data, '*-')        
        ax.set_xlabel('Polygon')
        ax.set_ylabel(self.nameField)
        ax.grid()
        self.canvas.draw()