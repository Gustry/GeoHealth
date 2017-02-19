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
import inspect
from os.path import abspath, dirname

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

    currentdir = dirname(abspath(inspect.getfile(inspect.currentframe())))
    parentdir = dirname(currentdir)
    print parentdir
    sys.path.insert(0, parentdir)
    for path in sys.path:
        print path
    help('modules')
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)


def test_package(package='src'):
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
