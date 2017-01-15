# coding=utf-8
"""
InaSAFE Disaster risk assessment tool by AusAid - **Clipper test suite.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

import unittest

from tempfile import mkdtemp
from os.path import join

from PyQt4.QtCore import QDir

from GeoHealth.geohealth.test.utilities import iface, load_test_vector_layer
from GeoHealth.geohealth.datastore.folder import Folder

iface()


class TestFolder(unittest.TestCase):
    """Test the folder datastore."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_folder_datastore(self):
        """Test if we can store shapefiles."""
        path = QDir(mkdtemp())
        data_store = Folder(path)
        self.assertTrue(data_store.is_writable())

        path = mkdtemp()
        data_store = Folder(path)

        # We do not have any layer yet.
        self.assertEqual(len(data_store.layers()), 0)

        # Let's add a vector layer.
        layer = load_test_vector_layer('roads.geojson')
        vector_layer_name = 'flood_test'

        result = data_store.add_layer(layer, vector_layer_name)
        self.assertTrue(result[0])
        self.assertEqual(result[1], vector_layer_name)

        # We try to add the layer twice with the same name.
        result = data_store.add_layer(layer, vector_layer_name)
        self.assertFalse(result[0])

        # We have imported one layer.
        self.assertEqual(len(data_store.layers()), 1)

        # Check if we have the correct URI.
        # self.assertIsNone(data_store.layer_uri(layer_name))
        expected = join(path, vector_layer_name + '.shp')
        self.assertEqual(data_store.layer_uri(vector_layer_name), expected)

        # This layer do not exist
        self.assertIsNone(data_store.layer_uri('fake_layer'))


if __name__ == '__main__':
    unittest.main()
