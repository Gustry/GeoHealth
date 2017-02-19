# coding=utf-8
"""
Test Suite for GeoHealth.

Contact : etienne at kartoza dot com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

import sys
import unittest
import qgis

from osgeo import gdal

__author__ = 'etiennetrimaille'
__revision__ = '$Format:%H$'
__date__ = '14/06/2016'


def _run_tests(test_suite, package_name):
    """Core function to test a test suite."""
    count = test_suite.countTestCases()
    print '########'
    print '%s tests has been discovered in %s' % (count, package_name)
    print 'Python GDAL : %s' % gdal.VersionInfo('VERSION_NUM')
    print '########'
    for path in sys.path:
        print path
    help('modules')
    for dist in __import__('pkg_resources').working_set:
        print dist.project_name.replace('Python', '')
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)


def test_package(package='geohealth'):
    """Test package.
    This function is called by travis without arguments.

    :param package: The package to test.
    :type package: str
    """
    test_loader = unittest.defaultTestLoader
    try:
        test_suite = test_loader.discover(package)
    except ImportError:
        test_suite = unittest.TestSuite()
    _run_tests(test_suite, package)


if __name__ == '__main__':
    test_package()
