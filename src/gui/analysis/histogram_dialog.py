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

from PyQt4.QtGui import QDialog, QDialogButtonBox
from PyQt4.QtCore import QSize, pyqtSignal
from matplotlib.backends.backend_qt4agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

<<<<<<< HEAD:src/gui/analysis/histogram_dialog.py
from GeoHealth.src.core.graph_toolbar import CustomNavigationToolbar
from GeoHealth.src.utilities.resources import get_ui_class

FORM_CLASS = get_ui_class('analysis', 'histogram.ui')
=======
from GeoPublicHealth.core.graph_toolbar import CustomNavigationToolbar
from GeoPublicHealth.ui.analysis.histogram import Ui_Histogram
>>>>>>> Change the files for the new name GeoPublicHealth:gui/analysis/histogram_dialog.py


class HistogramDialog(QDialog, FORM_CLASS):

    signalAskCloseWindow = pyqtSignal(int, name='signalAskCloseWindow')

    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # Connect slot.
        self.button_box.button(QDialogButtonBox.Ok).clicked.connect(
            self.draw_plot)
        self.button_box.button(QDialogButtonBox.Cancel).clicked.connect(
            self.hide)
        self.button_box.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)

        # Setup the graph.
        self.figure = Figure()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)
        self.layout_plot.addWidget(self.toolbar)
        self.layout_plot.addWidget(self.canvas)

    def draw_plot(self):
        """Function to draw the plot and display it in the canvas."""

        index = self.cbx_layer.currentIndex()
        layer = self.cbx_layer.itemData(index)
        render = layer.rendererV2()

        for ran in render.ranges():
            print "%f - %f: %s %s" % (
                ran.lowerValue(),
                ran.upperValue(),
                ran.label(),
                str(ran.symbol())
            )

        bar_list = self.ax.bar([1, 2, 3, 4], [1, 2, 3, 4])
        bar_list[0].set_color('r')
        bar_list[1].set_color('g')
        bar_list[2].set_color('b')

        self.canvas.draw()
