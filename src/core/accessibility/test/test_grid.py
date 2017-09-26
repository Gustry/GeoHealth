import unittest

from qgis.core import QgsRectangle, QgsCoordinateReferenceSystem
from qgis.testing.mocked import get_iface
from qgis.utils import iface

from GeoHealth.src.core.accessibility.create_grid import create_grid

if iface:
    APP = iface
else:
    APP = get_iface()


class TestTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_grid(self):

        extent = QgsRectangle(0, 0, 4, 4)
        size = 1
        crs = QgsCoordinateReferenceSystem(3857)
        print crs.authid()
        self.assertTrue(crs.isValid())
        layer = create_grid(extent, 2, crs)
        print layer.featureCount()
        print "TOTO"
