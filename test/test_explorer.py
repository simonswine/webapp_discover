# -*- encoding: UTF8 -*-

__author__ = 'Christian Simon'

# init env
from test_setup import setup
setup()

import unittest
from webapp_discover.explorer import Explorer

expl = Explorer()

class FileTreeLengths(unittest.TestCase):
    """Testing the length of FileTree"""

    def setUp(self):
        self.path = self.init_tempdir()

    def tearDown(self):
        pass

    def init_tempdir(self):
        pass

    def test_recurse_inf(self):
        pass

    def test_recurse_zero(self):
        pass

    def test_recurse_two(self):
        pass



if __name__ == '__main__':
    unittest.main()