from os.path import join
from qgis.core import (
    QgsVectorLayer,
    QgsRectangle,
    QgsFeatureRequest,
    QGis,
    QgsFeature,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsField,
    QgsFeature,
)
from PyQt4.QtCore import QVariant, QPyNullVariant


from safe.common.utilities import unique_filename
from GeoPublicHealth.src.test.debug_helper import show_qgis_layer
from GeoPublicHealth.src.core.tools import create_memory_layer, create_spatial_index
from GeoPublicHealth.src.core.gis.reproject import reproject
from GeoPublicHealth.src.core.tools import copy_layer, remove_fields

from GeoPublicHealth.src.core.accessibility.network import Graph

import processing

path = '/Users/etienne/dev/python/GeoHealth/src/test/data'
roads = QgsVectorLayer(join(path, 'roads.geojson'), 'roads', 'ogr')
extent = QgsRectangle(335147, 6636000, 352384, 6650000)
cell_size = 5000
health_points = QgsVectorLayer(
    join(path, 'crossing.geojson'), 'health_points', 'ogr')
number_of_points = 3
id_field = 'osm_id'


def create_grid(size):
    """Create a polygonal grid using Processing.

    :param size: The cell size.
    :type size: int

    :return: The grid layer in memory.
    :rtype: QgsVectorLayer
    """
    output_filename = unique_filename(prefix='grid', suffix='.shp')

    result = processing.runalg(
        'qgis:vectorgrid',
        '336199.970553,352338.397991,7636164.67975,7648562.41208',
        size,  # X spacing
        size,  # Y spacing
        0,  # Output as polygons
        output_filename)

    layer = QgsVectorLayer(output_filename, 'grid', 'ogr')
    layer.setCrs(QgsCoordinateReferenceSystem(32740))

    remove_fields(layer, ['xmin', 'xmax', 'ymin', 'ymax'])

    # Make a copy in memory
    memory = create_memory_layer(
        'grid', layer.geometryType(), layer.crs(), layer.fields())
    copy_layer(layer, memory)

    print "NB cells : %s" % layer.featureCount()

    return memory


def intersect_grid_and_roads(grid, roads):
    """Create a subset of the grid."""

    grid.startEditing()
    grid.addAttribute(
        QgsField('has_road', QVariant.String, len=10, prec=0))
    intersection_index = grid.fieldNameIndex('has_road')

    spatial_index = create_spatial_index(roads)

    for cell in grid.getFeatures():
        geometry = cell.geometry()
        intersects = spatial_index.intersects(geometry.boundingBox())

        for i in intersects:
            request = QgsFeatureRequest().setFilterFid(i)
            road = next(roads.getFeatures(request))
            road_geometry = road.geometry()

            if geometry.intersects(road_geometry):
                has_intersection = True
                break
        else:
            has_intersection = False

        grid.changeAttributeValue(
            cell.id(), intersection_index, has_intersection)

    grid.commitChanges()
    return grid


def centroids(layer):
    """Create centroids."""
    centroids_layer = create_memory_layer(
        'centroids',
        QGis.Point,
        layer.crs(),
        layer.fields())

    centroids_layer.startEditing()

    for feature in layer.getFeatures():
        new_feature = QgsFeature(feature)
        new_feature.setGeometry(feature.geometry().centroid())
        centroids_layer.addFeature(new_feature)
    centroids_layer.commitChanges()
    return centroids_layer


def create_graph(network, centroid_layer, target_point_layer):
    """Create a graph based on a road network and some tied points."""
    tied_points = []
    for f in centroid_layer.getFeatures():
        tied_points.append(f.geometry().centroid().asPoint())
    for feature in target_point_layer.getFeatures():
        tied_points.append(feature.geometry().asPoint())

    graph = Graph(network, tied_points)
    return graph


def intersecting_blocks(line, destination, grid):
    """Function to fetch intersectings polygons from the grid."""
    dest_id_field = grid.fieldNameIndex('destination_id')
    request = QgsFeatureRequest()
    request.setFilterRect(line.boundingBox())
    request.setFilterExpression('"destination_id" is None')
    for feature in grid.getFeatures(request):
        if feature.geometry().intersects(line):
            grid.changeAttributeValue(feature.id(), dest_id_field, destination)


def assign_cost_to_cells(network_graph, source, destination, id_field):
    """Assign the nearest destination point from the source layer.

    :param network_graph: The network graph.
    :type network_graph: Graph

    :param source: Grid as a polygon vector layer
    :type source: QgsVectorLayer

    :param destination: The destination point layer.
    :type destination: QgsVectorLayer

    :param id_field: The ID field in the destination layer.
    :type id_field: basestring
    """
    spatial_index = create_spatial_index(destination)
    destination_features = {}
    for feature in destination.getFeatures():
        destination_features[feature.id()] = feature
    index_id_field = destination.fieldNameIndex(id_field)

    fields = [QgsField('distance', QVariant.Int)]
    routes = create_memory_layer(
        'routes', QGis.Line, destination.crs(), fields)
    routes.startEditing()

    source.startEditing()
    source.addAttribute(
        QgsField('destination_id', QVariant.Int, len=5, prec=0))
    dest_id_field = source.fieldNameIndex('destination_id')
    source.addAttribute(QgsField('distance', QVariant.Int, len=5, prec=0))
    distance_field = source.fieldNameIndex('distance')
    source.commitChanges()

    request = QgsFeatureRequest()
    request.setFilterExpression('"has_road" = \'true\'')
    # request.setLimit(20)  # Hack for now to speedup development
    i = 0
    for source_cell in source.getFeatures(request):
        source_geometry_point = source_cell.geometry().centroid().asPoint()
        desination_id = source_cell['destination_id']
        if desination_id is None or isinstance(desination_id, QPyNullVariant):
            source.startEditing()
            nearest_health_points = spatial_index.nearestNeighbor(
                source_geometry_point, 5)
            minimum_distance = None
            minimal_geom = None
            for health_point in nearest_health_points:
                try:
                    i += 1
                    p = destination_features[health_point].geometry().asPoint()
                    geom, distance, _ = network_graph.route(
                        source_geometry_point, p)
                except:
                    distance = -1

                if minimum_distance is None or (
                                minimum_distance > distance >= 0):
                    minimal_geom = geom
                    minimum_distance = distance

            if minimum_distance:
                feature = QgsFeature()
                feature.setGeometry(minimal_geom)
                feature.setAttributes([minimum_distance])
                routes.addFeatures([feature])

                index_id = destination_features[health_point][index_id_field]
                destination_value = index_id
            else:
                destination_value = '-1'
                minimum_distance = '-1'

            source.changeAttributeValue(
                source_cell.id(), dest_id_field, destination_value)
            source.changeAttributeValue(
                source_cell.id(), distance_field, minimum_distance)
            intersecting_blocks(minimal_geom, destination_value, grid)
            source.commitChanges()

        else:
            print 'speedup'
            geom, distance, _ = network_graph.route(
                source_geometry_point,
                destination_features[desination_id].geometry().asPoint())

    source.commitChanges()
    # source.commitErrors()
    routes.commitChanges()
    print 'Call : %s' % i
    return routes, source

if health_points.crs != roads.crs():
    health_points = reproject(health_points, roads.crs())

grid = create_grid(cell_size)
# show_qgis_layer(grid)
grid = intersect_grid_and_roads(grid, roads)
# show_qgis_layer(cells_without_roads)
# centroids_layer = centroids(cells_with_roads)
# show_qgis_layer(centroids_layer)
network = create_graph(roads, grid, health_points)
routes, grids = assign_cost_to_cells(network, grid, health_points, id_field)
show_qgis_layer(grids)
show_qgis_layer(routes)
show_qgis_layer(health_points)
