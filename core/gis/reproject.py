# coding=utf-8

"""Reproject a vector layer to a specific CRS."""

from qgis.core import QgsCoordinateTransform, QgsFeature

from GeoHealth.src.core.tools import create_memory_layer


def reproject(layer, output_crs):
    """Reproject a vector layer to a specific CRS.

    Issue https://github.com/inasafe/inasafe/issues/3183

    :param layer: The layer to reproject.
    :type layer: QgsVectorLayer

    :param output_crs: The destination CRS.
    :type output_crs: QgsCoordinateReferenceSystem

    :return: Reprojected memory layer.
    :rtype: QgsVectorLayer
    """
    input_crs = layer.crs()
    input_fields = layer.fields()

    reprojected = create_memory_layer(
        'reprojected', layer.geometryType(), output_crs, input_fields)
    reprojected.startEditing()

    crs_transform = QgsCoordinateTransform(input_crs, output_crs)

    out_feature = QgsFeature()

    for feature in layer.getFeatures():
        geom = feature.geometry()
        geom.transform(crs_transform)
        out_feature.setGeometry(geom)
        out_feature.setAttributes(feature.attributes())
        reprojected.addFeature(out_feature)

    reprojected.commitChanges()
    return reprojected
