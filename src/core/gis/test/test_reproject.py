# coding=utf-8

import unittest

from qgis.core import QgsCoordinateReferenceSystem

from GeoHealth.src.test.utilities import iface, load_test_vector_layer
from GeoHealth.src.core.gis.reproject import reproject

iface()

__copyright__ = "Copyright 2016, The InaSAFE Project"
__license__ = "GPL version 3"
__email__ = "info@inasafe.org"
__revision__ = '$Format:%H$'


class TestReprojectVector(unittest.TestCase):

    """Test Reproject Vector Layer."""

    def test_reproject_vector(self):
        """Test we can reproject a vector layer."""
        layer = load_test_vector_layer('roads.geojson')

        output_crs = QgsCoordinateReferenceSystem(3857)

        reprojected = reproject(layer=layer, output_crs=output_crs)

        self.assertEqual(reprojected.crs(), output_crs)
        self.assertEqual(
            reprojected.featureCount(), layer.featureCount())
