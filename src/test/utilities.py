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

import inspect
import shutil
from os.path import exists, join, splitext, dirname, abspath, basename
from tempfile import mkdtemp

from qgis.core import QgsVectorLayer, QgsRasterLayer


def iface():
    """Helper method to get the iface for testing.

    :return: The QGIS interface.
    :rtype: QgsInterface
    """
    from qgis.utils import iface
    if iface is not None:
        return iface
    else:
        from qgis.testing.mocked import get_iface
        return get_iface()


def standard_data_path(*args):
    """Return the absolute path to the InaSAFE test data or directory path.

    .. versionadded:: 3.0

    :param args: List of path e.g. ['control', 'files',
        'test-error-message.txt'] or ['control', 'scenarios'] to get the path
        to scenarios dir.
    :type args: list

    :return: Absolute path to the test data or dir path.
    :rtype: str

    """
    path = dirname(__file__)
    path = abspath(join(path, 'data'))
    for item in args:
        path = abspath(join(path, item))

    return path


def load_local_vector_layer(test_file, **kwargs):
    """Return the test vector layer.

    See documentation of load_path_vector_layer

    :param test_file: The file to load in the data directory next to the file.
    :type test_file: str

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        clone_to_memory=True if you want to create a memory layer.

        with_keywords=False if you do not want keywords. "clone_to_memory" is
            required.

    :type kwargs: dict

    :return: The vector layer.
    :rtype: QgsVectorLayer

    .. versionadded:: 4.0
    """
    caller_path = inspect.getouterframes(inspect.currentframe())[1][1]
    path = join(dirname(caller_path), 'data', test_file)
    return load_path_vector_layer(path, **kwargs)


def load_test_vector_layer(*args, **kwargs):
    """Return the test vector layer.

    See documentation of load_path_vector_layer

    :param args: List of path e.g. ['exposure', 'buildings.shp'].
    :type args: list

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        clone_to_memory=True if you want to create a memory layer.

        with_keywords=False if you do not want keywords. "clone_to_memory" is
            required.

    :type kwargs: dict

    :return: The vector layer.
    :rtype: QgsVectorLayer

    .. versionadded:: 4.0
    """
    path = standard_data_path(*args)
    return load_path_vector_layer(path, **kwargs)


def load_path_vector_layer(path, **kwargs):
    """Return the test vector layer.

    :param path: Path to the vector layer.
    :type path: str

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        clone_to_memory=True if you want to create a memory layer.

        with_keywords=False if you do not want keywords. "clone_to_memory" is
            required.

    :type kwargs: dict

    :return: The vector layer.
    :rtype: QgsVectorLayer

    .. versionadded:: 4.0
    """
    if not exists(path):
        raise Exception('%s do not exist.' % path)

    name = splitext(basename(path))[0]
    extension = splitext(path)[1]

    extensions = [
        '.shp', '.shx', '.dbf', '.prj', '.gpkg', '.geojson', '.xml', '.qml']

    if kwargs.get('with_keywords'):
        if not kwargs.get('clone_to_memory'):
            raise Exception('with_keywords needs a clone_to_memory')

    if kwargs.get('clone', False):
        target_directory = mkdtemp()
        current_path = splitext(path)[0]
        path = join(target_directory, name + extension)

        for ext in extensions:
            src_path = current_path + ext
            if exists(src_path):
                target_path = join(target_directory, name + ext)
                shutil.copy2(src_path, target_path)

    if path.endswith('.csv'):
        layer = QgsVectorLayer(path, name, 'delimitedtext')
    else:
        layer = QgsVectorLayer(path, name, 'ogr')

    if not layer.isValid():
        raise Exception('{name} is not a valid layer : {path}'.format(
            name=name, path=path))

    return layer


def load_local_raster_layer(test_file, **kwargs):
    """Return the test raster layer.

    See documentation of load_path_raster_layer

    :param test_file: The file to load in the data directory next to the file.
    :type test_file: str

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        with_keywords=False if you do not want keywords. "clone" is
            required.

    :type kwargs: dict

    :return: The raster layer.
    :rtype: QgsRasterLayer

    .. versionadded:: 4.0
    """
    caller_path = inspect.getouterframes(inspect.currentframe())[1][1]
    path = join(dirname(caller_path), 'data', test_file)
    return load_path_raster_layer(path, **kwargs)


def load_test_raster_layer(*args, **kwargs):
    """Return the test raster layer.

    See documentation of load_path_raster_layer

    :param args: List of path e.g. ['exposure', 'population.asc]'.
    :type args: list

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        with_keywords=False if you do not want keywords. "clone" is
            required.

    :type kwargs: dict

    :return: The raster layer.
    :rtype: QgsRasterLayer

    .. versionadded:: 4.0
    """
    path = standard_data_path(*args)
    return load_path_raster_layer(path, **kwargs)


def load_path_raster_layer(path, **kwargs):
    """Return the test raster layer.

    :param path: Path to the raster layer.
    :type path: str

    :param kwargs: It can be :
        clone=True if you want to copy the layer first to a temporary file.

        with_keywords=False if you do not want keywords. "clone" is
            required.

    :return: The raster layer.
    :rtype: QgsRasterLayer

    .. versionadded:: 4.0
    """
    if not exists(path):
        raise Exception('%s do not exist.' % path)

    name = splitext(basename(path))[0]
    extension = splitext(path)[1]

    extensions = [
        '.tiff', '.tif', '.asc', '.xml', '.qml']

    if kwargs.get('with_keywords'):
        if not kwargs.get('clone'):
            raise Exception('with_keywords needs a clone')

    if not kwargs.get('with_keywords', True):
        index = extensions.index('.xml')
        extensions.pop(index)

    if kwargs.get('clone', False):
        target_directory = mkdtemp()
        current_path = splitext(path)[0]
        path = join(target_directory, name + extension)

        for ext in extensions:
            src_path = current_path + ext
            if exists(src_path):
                target_path = join(target_directory, name + ext)
                shutil.copy2(src_path, target_path)

    name = basename(path)
    layer = QgsRasterLayer(path, name)

    if not layer.isValid():
        raise Exception('%s is not a valid layer.' % name)

    return layer
