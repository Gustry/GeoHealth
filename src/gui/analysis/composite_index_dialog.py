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

from GeoPublicHealth.src.gui.analysis.parent_incidence_density_dialog import (
    IncidenceDensityDialog)

from qgis.core import QgsRendererRangeV2LabelFormat, QgsMessageLog, QgsFeature, QgsField, QgsStyleV2, QgsVectorGradientColorRampV2, QgsVectorLayer, QgsMapLayerRegistry, QgsGraduatedSymbolRendererV2, QgsSymbolV2,  QgsRendererRangeV2


from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import (QProgressBar, QPushButton, QDialog,
                         QSizePolicy, QGridLayout, QDialogButtonBox)

from tempfile import NamedTemporaryFile
from PyQt4.QtGui import \
    QDialog,\
    QDialogButtonBox,\
    QTableWidgetItem,\
    QApplication
from PyQt4.QtCore import QSize, QVariant, Qt, pyqtSignal
from PyQt4.QtGui import QFileDialog

from qgis.utils import QGis
from qgis.gui import QgsMapLayerProxyModel
from qgis.core import \
    QgsField,\
    QgsVectorGradientColorRampV2,\
    QgsGraduatedSymbolRendererV2,\
    QgsSymbolV2,\
    QgsVectorFileWriter,\
    QgsFeature,\
    QgsVectorLayer,\
    QgsMapLayerRegistry,\
    QgsGeometry

from matplotlib.backends.backend_qt4agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from GeoPublicHealth.src.core.graph_toolbar import CustomNavigationToolbar
from GeoPublicHealth.src.core.tools import display_message_bar, tr
from GeoPublicHealth.src.core.exceptions import \
    GeoPublicHealthException,\
    NoLayerProvidedException,\
    DifferentCrsException,\
    FieldExistingException,\
    FieldException,\
    NotANumberException
from GeoPublicHealth.src.core.stats import Stats

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Composite_Index(object):
    def setupUi(self, Composite_Index):
        Composite_Index.setObjectName(_fromUtf8("Composite_Index"))
        Composite_Index.resize(814, 754)
        self.verticalLayout = QtGui.QVBoxLayout(Composite_Index)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Composite_Index)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.cbx_aggregation_layer = QgsMapLayerComboBox(Composite_Index)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_aggregation_layer.sizePolicy().hasHeightForWidth())
        self.cbx_aggregation_layer.setSizePolicy(sizePolicy)
        self.cbx_aggregation_layer.setObjectName(_fromUtf8("cbx_aggregation_layer"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbx_aggregation_layer)
        self.label_4 = QtGui.QLabel(Composite_Index)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cbx_indicator_field = QgsFieldComboBox(Composite_Index)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbx_indicator_field.sizePolicy().hasHeightForWidth())
        self.cbx_indicator_field.setSizePolicy(sizePolicy)
        self.cbx_indicator_field.setObjectName(_fromUtf8("cbx_indicator_field"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbx_indicator_field)
        self.label_3 = QtGui.QLabel(Composite_Index)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_8 = QtGui.QLabel(Composite_Index)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.le_output_filepath = QtGui.QLineEdit(Composite_Index)
        self.le_output_filepath.setObjectName(_fromUtf8("le_output_filepath"))
        self.horizontalLayout_6.addWidget(self.le_output_filepath)
        self.button_browse = QtGui.QPushButton(Composite_Index)
        self.button_browse.setObjectName(_fromUtf8("button_browse"))
        self.horizontalLayout_6.addWidget(self.button_browse)
        self.formLayout.setLayout(12, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout.setLayout(13, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.radioButton_vector_positive = QtGui.QRadioButton(Composite_Index)
        self.radioButton_vector_positive.setChecked(True)
        self.radioButton_vector_positive.setObjectName(_fromUtf8("radioButton_vector_positive"))
        self.buttonGroup_2 = QtGui.QButtonGroup(Composite_Index)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_vector_positive)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.radioButton_vector_positive)
        self.radioButton_vector_negative = QtGui.QRadioButton(Composite_Index)
        self.radioButton_vector_negative.setObjectName(_fromUtf8("radioButton_vector_negative"))
        self.buttonGroup_2.addButton(self.radioButton_vector_negative)
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.radioButton_vector_negative)
        self.le_new_column = QtGui.QLineEdit(Composite_Index)
        self.le_new_column.setMaxLength(10)
        self.le_new_column.setObjectName(_fromUtf8("le_new_column"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.le_new_column)
        self.cbx_list_indicators = QtGui.QListWidget(Composite_Index)
        self.cbx_list_indicators.setObjectName(_fromUtf8("cbx_list_indicators"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.cbx_list_indicators)
        self.command_link_button = QtGui.QCommandLinkButton(Composite_Index)
        self.command_link_button.setObjectName(_fromUtf8("command_link_button"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.command_link_button)
        self.label_2 = QtGui.QLabel(Composite_Index)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.symbology = QgsCollapsibleGroupBox(Composite_Index)
        self.symbology.setCheckable(True)
        self.symbology.setProperty("collapsed", False)
        self.symbology.setObjectName(_fromUtf8("symbology"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.symbology)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.symbology)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.color_low_value = QgsColorButtonV2(self.symbology)
        self.color_low_value.setProperty("color", QtGui.QColor(50, 164, 46))
        self.color_low_value.setObjectName(_fromUtf8("color_low_value"))
        self.horizontalLayout_3.addWidget(self.color_low_value)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_10 = QtGui.QLabel(self.symbology)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.color_high_value = QgsColorButtonV2(self.symbology)
        self.color_high_value.setProperty("color", QtGui.QColor(202, 33, 36))
        self.color_high_value.setObjectName(_fromUtf8("color_high_value"))
        self.horizontalLayout_3.addWidget(self.color_high_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(self.symbology)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.spinBox_classes = QtGui.QSpinBox(self.symbology)
        self.spinBox_classes.setMinimum(1)
        self.spinBox_classes.setProperty("value", 5)
        self.spinBox_classes.setObjectName(_fromUtf8("spinBox_classes"))
        self.horizontalLayout_4.addWidget(self.spinBox_classes)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.symbology)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.cbx_mode = QtGui.QComboBox(self.symbology)
        self.cbx_mode.setObjectName(_fromUtf8("cbx_mode"))
        self.horizontalLayout_4.addWidget(self.cbx_mode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.symbology)
        self.button_box_ok = QtGui.QDialogButtonBox(Composite_Index)
        self.button_box_ok.setOrientation(QtCore.Qt.Horizontal)
        self.button_box_ok.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box_ok.setObjectName(_fromUtf8("button_box_ok"))
        self.verticalLayout.addWidget(self.button_box_ok)

        self.retranslateUi(Composite_Index)
        QtCore.QObject.connect(self.cbx_aggregation_layer, QtCore.SIGNAL(_fromUtf8("layerChanged(QgsMapLayer*)")), self.cbx_indicator_field.setLayer)
        QtCore.QMetaObject.connectSlotsByName(Composite_Index)

    def retranslateUi(self, Composite_Index):
        Composite_Index.setWindowTitle(_translate("Composite_Index", "Incidence", None))
        self.label.setText(_translate("Composite_Index", "Layer", None))
        self.label_4.setText(_translate("Composite_Index", "Indicator field", None))
        self.label_3.setText(_translate("Composite_Index", "Composite Index", None))
        self.label_8.setText(_translate("Composite_Index", "Output", None))
        self.le_output_filepath.setPlaceholderText(_translate("Composite_Index", "Save to temporary file", None))
        self.button_browse.setText(_translate("Composite_Index", "Browse", None))
        self.radioButton_vector_positive.setText(_translate("Composite_Index", "Higher the value of the indicator better the conditions for the population", None))
        self.radioButton_vector_negative.setText(_translate("Composite_Index", "Higher the value of the indicator worse the conditions for the population", None))
        self.le_new_column.setPlaceholderText(_translate("Composite_Index", "UHN", None))
        self.command_link_button.setText(_translate("Composite_Index", "Add to Index", None))
        self.label_2.setText(_translate("Composite_Index", "For removing and Indicator Click Twice in the one you want to remove", None))
        self.symbology.setTitle(_translate("Composite_Index", "Add a symbology", None))
        self.label_9.setText(_translate("Composite_Index", "Low Priority", None))
        self.label_10.setText(_translate("Composite_Index", "High Priority", None))
        self.label_11.setText(_translate("Composite_Index", "Classes", None))
        self.label_12.setText(_translate("Composite_Index", "Mode", None))

from qgis.gui import QgsFieldComboBox
from qgis.gui import QgsMapLayerComboBox
from qgis.gui import QgsCollapsibleGroupBox
from qgis.gui import QgsColorButtonV2


class CompositeIndexDialog(IncidenceDensityDialog, Ui_Composite_Index):
    def __init__(self, parent=None):
        """Constructor."""
        IncidenceDensityDialog.__init__(self, parent)
        # noinspection PyArgumentList
        Ui_Composite_Index.setupUi(self, self)

        self.use_area = True
        self.use_point_layer = False

        self.setup_ui()

    def setup_ui(self):
        # Connect slot.
        # noinspection PyUnresolvedReferences
        self.button_browse.clicked.connect(self.open_file_browser)
        self.button_box_ok.button(QDialogButtonBox.Ok).clicked.connect(
            self.run_stats)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.hide)
        self.button_box_ok.button(QDialogButtonBox.Cancel).clicked.connect(
            self.signalAskCloseWindow.emit)

        # Add items in symbology
        self.cbx_mode.addItem(
            'Equal interval', QgsGraduatedSymbolRendererV2.EqualInterval)
        self.cbx_mode.addItem(
            'Quantile (equal count)', QgsGraduatedSymbolRendererV2.Quantile)
        self.cbx_mode.addItem(
            'Natural breaks', QgsGraduatedSymbolRendererV2.Jenks)
        self.cbx_mode.addItem(
            'Standard deviation', QgsGraduatedSymbolRendererV2.StdDev)
        self.cbx_mode.addItem(
            'Pretty breaks', QgsGraduatedSymbolRendererV2.Pretty)

        # Setup the graph.
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(QSize(300, 0))
        self.toolbar = CustomNavigationToolbar(self.canvas, self)

        self.cbx_aggregation_layer.setFilters(
            QgsMapLayerProxyModel.PolygonLayer)

        if self.use_point_layer:
            self.cbx_case_layer.setFilters(QgsMapLayerProxyModel.PointLayer)

        if not self.use_area:
            self.cbx_population_field.setLayer(
                self.cbx_aggregation_layer.currentLayer())
            self.cbx_aggregation_layer.layerChanged.connect(
                self.cbx_population_field.setLayer)
            self.cbx_aggregation_layer.layerChanged.connect(
                self.reset_field_population)
            self.reset_field_population()

        self.cbx_list_indicators.itemDoubleClicked.connect(self.remove_item) 


    def reset_field_population(self):
        self.cbx_population_field.setCurrentIndex(0)

    def remove_item(self):
        self.cbx_list_indicators.takeItem( self.cbx_list_indicators.currentRow())

    def add_indicator(self):
        present = False
        for index in range(self.cbx_list_indicators.count()):
            if self.cbx_list_indicators.item(index).text() == self.vector_indicator():
                present = True
        if not present:
            self.cbx_list_indicators.addItem(self.vector_indicator())

    def vector_indicator(self):
        return self.cbx_indicator_field.currentField() + " " + self.vector_direction()

    def vector_direction(self):
        if self.radioButton_vector_positive.isChecked():
            return "+"
        else:
            return "-"

    def open_file_browser(self):
        output_file = QFileDialog.getSaveFileNameAndFilter(
            self.parent, tr('Save shapefile'), filter='SHP (*.shp)')
        self.le_output_filepath.setText(output_file[0])

    def indicators_list(self):
        items = []
        for index in xrange(self.cbx_list_indicators.count()):
            items.append(self.cbx_list_indicators.item(index))
        return [[i.text()[:-2], i.text()[-1]] for i in items]

    def run_stats(self):
        """Main function which do the process."""

        # Get the common fields.
        self.admin_layer = self.cbx_aggregation_layer.currentLayer()

        if self.use_point_layer:
            # If we use a point layer.
            point_layer = self.cbx_case_layer.currentLayer()
        else:
            # If we use a column with number of case.
            case_column = self.cbx_case_field.currentField()
            index_case = self.admin_layer.fieldNameIndex(case_column)

        selected_indicators = self.indicators_list()

        if not self.use_area:
            # If we don't use density.
            population = self.cbx_population_field.currentField()
            index_population = self.admin_layer.fieldNameIndex(population)

        if not self.name_field:
            self.name_field = self.le_new_column.placeholderText()

        # Add new column.
        add_nb_intersections = self.checkBox_addNbIntersections.isChecked()

        # Ratio
        ratio = self.cbx_ratio.currentText()
        ratio = ratio.replace(' ', '')

        # Output.
        self.output_file_path = self.le_output_filepath.text()

        try:
            self.button_box_ok.setDisabled(True)
            # noinspection PyArgumentList
            QApplication.setOverrideCursor(Qt.WaitCursor)
            # noinspection PyArgumentList
            QApplication.processEvents()

            if not self.admin_layer:
                raise NoLayerProvidedException

            if not self.admin_layer and self.use_point_layer:
                raise NoLayerProvidedException

            crs_admin_layer = self.admin_layer.crs()

            if self.use_point_layer:
                crs_point_layer = point_layer.crs()
                if crs_admin_layer != crs_point_layer:
                    raise DifferentCrsException(
                        epsg1=crs_point_layer.authid(),
                        epsg2=crs_admin_layer.authid())

            if not self.use_point_layer and not self.use_area:
                if not self.cbx_list_indicators:
                    raise FieldException(field_1='List Indicators should not empty')

            # Output
            if not self.output_file_path:
                temp_file = NamedTemporaryFile(
                    delete=False,
                    suffix='-geopublichealth.shp')
                self.output_file_path = temp_file.name
                temp_file.flush()
                temp_file.close()

            admin_layer_provider = self.admin_layer.dataProvider()
            fields = admin_layer_provider.fields()

            if admin_layer_provider.fieldNameIndex(self.name_field) != -1:
                raise FieldExistingException(field=self.name_field)

            for indicator_selected in selected_indicators:
                fields.append(QgsField("Z" + indicator_selected[0], QVariant.Double))
            fields.append(QgsField(self.name_field, QVariant.Double))


            file_writer = QgsVectorFileWriter(
                self.output_file_path,
                'utf-8',
                fields,
                QGis.WKBPolygon,
                self.admin_layer.crs(),
                'ESRI Shapefile')

            count = self.admin_layer.featureCount()
            stats = {}
            for indicator_selected in selected_indicators:
                values = []
                indicator_selected_name = str(indicator_selected[0])

                for i, feature in enumerate(self.admin_layer.getFeatures()):
                    index = self.admin_layer.fieldNameIndex(indicator_selected_name)

                    if feature[index]:
                        value = float(feature[index])
                    else:
                        value = 0.0
                    values.append(value)

                stats[indicator_selected_name] = Stats(values)

            for i, feature in enumerate(self.admin_layer.getFeatures()):
                attributes = feature.attributes()
                
                composite_index_value = 0.0
                for indicator_selected in selected_indicators:
                    indicator_selected_name = str(indicator_selected[0])
                    index = self.admin_layer.fieldNameIndex(indicator_selected_name)

                    if feature[index]:
                        value = float(feature[index])
                    else:
                        value = 0.0

                    zscore = (value - stats[indicator_selected_name].average()) / stats[indicator_selected_name].standard_deviation()
                    attributes.append(float(zscore))

                    #msgBox = QMessageBox()
                    #msgBox.setText("indicator_selected: " + str(indicator_selected) + " value: " + str(value) + " stats[indicator_selected_name].average(): " + str(stats[indicator_selected_name].average()) + " zscore: " + str(zscore))
                    #msgBox.exec_()

                    if indicator_selected[1] == '+':
                        composite_index_value -= zscore
                    else:
                        composite_index_value += zscore

                attributes.append(float(composite_index_value))
                new_feature = QgsFeature()
                new_geom = QgsGeometry(feature.geometry())
                new_feature.setAttributes(attributes)
                new_feature.setGeometry(new_geom)
                file_writer.addFeature(new_feature)
                
            del file_writer

            self.output_layer = QgsVectorLayer(
                self.output_file_path,
                self.name_field,
                'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(self.output_layer)

            if self.symbology.isChecked():
                self.add_symbology()

            self.signalStatus.emit(3, tr('Successful process'))

        except GeoPublicHealthException, e:
            display_message_bar(msg=e.msg, level=e.level, duration=e.duration)

        finally:
            self.button_box_ok.setDisabled(False)
            # noinspection PyArgumentList
            QApplication.restoreOverrideCursor()
            # noinspection PyArgumentList
            QApplication.processEvents()
