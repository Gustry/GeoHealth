# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoHealth
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from GeoHealth_dialog import GeoHealthDialog
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from Stats import Stats

import os.path

class NavigationToolbar(NavigationToolbar):
    toolitems = [t for t in NavigationToolbar.toolitems if
                 t[0] in ('Home', 'Back', 'Next', 'Pan', 'Zoom', 'Save')]

class GeoHealth:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'GeoHealth_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = GeoHealthDialog()

        # Declare instance attributes
        self.action = None
        
        #Connect
        self.dlg.comboBox_incidence_adminLayer.currentIndexChanged.connect(self.updateFields)
        self.dlg.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(self.runStats)
        self.dlg.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(self.dlg.hide)
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = NavigationToolbar(self.canvas, self.dlg)
        self.dlg.layout_plot.addWidget(self.toolbar)
        self.dlg.layout_plot.addWidget(self.canvas)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/GeoHealth/resources/icon.png"),
            u"GeoHealth",
            self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(
            u"&GeoHealth",
            self.action)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu(
            u"&GeoHealth",
            self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Run method that performs all the real work"""
        
        self.fillComboboxLayer()
        
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        self.dlg.exec_()

    def updateFields(self):
        self.dlg.comboBox_incidence_populationField.clear()
        
        index = self.dlg.comboBox_incidence_adminLayer.currentIndex()
        adminLayer = self.dlg.comboBox_incidence_adminLayer.itemData(index)
        if not adminLayer:
            return False
        
        fields = adminLayer.dataProvider().fields()
        
        for item in fields:
            self.dlg.comboBox_incidence_populationField.addItem(item.name(),item)

    def fillComboboxLayer(self):
        self.dlg.comboBox_incidence_adminLayer.clear()
        self.dlg.comboBox_incidence_pointLayer.clear()
        self.dlg.comboBox_incidence_populationField.clear()

        for layer in self.iface.legendInterface().layers():
            if layer.type() == 0 :
                
                if layer.geometryType() == 0 :
                    self.dlg.comboBox_incidence_pointLayer.addItem(layer.name(),layer)
                
                if layer.geometryType() == 2 :
                    self.dlg.comboBox_incidence_adminLayer.addItem(layer.name(),layer)
                    
    def runStats(self):
        #Get the fields
        index = self.dlg.comboBox_incidence_adminLayer.currentIndex()
        adminLayer = self.dlg.comboBox_incidence_adminLayer.itemData(index)
        index = self.dlg.comboBox_incidence_pointLayer.currentIndex()
        pointLayer = self.dlg.comboBox_incidence_pointLayer.itemData(index)
        population = self.dlg.comboBox_incidence_populationField.currentText()
        self.nameField = self.dlg.lineEdit_incidence_columnName.text()
        ratio = self.dlg.comboBox_incidence_ratio.currentText()
        ratio = ratio.replace(" ","")
        
        try :
            ratio = float(ratio)
        except ValueError:
            return False
        
        useArea = self.dlg.radioButton_incidence_area.isChecked()
        addNbIntersections = self.dlg.checkBox_addNbIntersections.isChecked()
        
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
                    return False
                indice = float(count) / population * ratio
            
            data.append(indice)
            adminLayer.changeAttributeValue(feature.id(), numFieldIncidence, indice)
            if addNbIntersections:
                adminLayer.changeAttributeValue(feature.id(), numFieldIntersections, count)
        
        adminLayer.commitChanges()
        adminLayer.updateFields()
        
        stats = Stats(data)
        
        itemsStats = []
        itemsStats.append("Count(point),%d"%pointLayer.featureCount())
        itemsStats.append("Count(polygon),%d"%adminLayer.featureCount())
        itemsStats.append("Min,%d"%stats.min())
        itemsStats.append("Average,%f"%stats.average())
        itemsStats.append("Max,%d"%stats.max())
        itemsStats.append("Range,%d"%stats.range())
        itemsStats.append("Variance,%f"%stats.stat_variance())
        itemsStats.append("Ecart type,%f"%stats.stat_ecart_type())
        
        self.dlg.tableWidget.clear()
        self.dlg.tableWidget.setColumnCount(2)
        self.dlg.tableWidget.setHorizontalHeaderLabels(['Parameters','Values'])
        self.dlg.tableWidget.setRowCount(len(itemsStats))
        
        for i,item in enumerate(itemsStats):
            s = item.split(',')
            self.dlg.tableWidget.setItem(i, 0, QTableWidgetItem(s[0]))
            self.dlg.tableWidget.setItem(i, 1, QTableWidgetItem(s[1]))
        self.dlg.tableWidget.resizeRowsToContents()
        
        self.drawPlot(data)
        
    def drawPlot(self,data):
        #Creating the plot        
        # create an axis
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data, '*-')
        
        #ax.set_title('Number of intersections per entity')
        ax.set_xlabel('Polygon')
        ax.set_ylabel(self.nameField)
        ax.grid()
        
        # refresh canvas
        self.canvas.draw()