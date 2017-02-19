# coding=utf-8

import unittest
import os
from subprocess import Popen, PIPE


class TestPep8(unittest.TestCase):

    def test_pep8(self):
        """Test if the code is PEP8 compliant."""

        if os.environ.get('ON_TRAVIS', False):
            root = './'
        else:
            root = '../../'

        command = ['make', 'pep8']
        output = Popen(command, stdout=PIPE, cwd=root).communicate()[0]

        # make pep8 produces some extra lines by default.
        default_number_lines = 5
        lines = len(output.splitlines()) - default_number_lines

        message = 'Hey mate, go back to your keyboard :)'
        self.assertEquals(lines, 0, message)
