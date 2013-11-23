# -*- encoding: UTF8 -*-

__author__ = 'Christian Simon'

# init env
from test_setup import setup
setup()

import unittest

from webapp_discover.file_tree import FileTree


sample_list = [
    './index.php',
    './license.txt',
    './readme.html',
    './test123/readme.html',
    './test123/readme.txt',
]


class FileTreeBasics(unittest.TestCase):
    """Basic Tests of FileTree"""


    def test_creation(self):
        """Create from path list"""
        ft = FileTree(sample_list)

    def test_compare(self):
        """Compare two identical FileTree"""

        ft1 = FileTree(sample_list)
        ft2 = FileTree(sample_list)

        self.assertEqual(ft1, ft2)

    def test_compare_realtive(self):
        """Compare two identical FileTrees, with and without relative path"""

        ft1 = FileTree(sample_list)
        ft2 = FileTree([i.replace('./', '') for i in sample_list])

        self.assertEqual(ft1, ft2)


class FileTreeLengths(unittest.TestCase):
    """Testing the length of FileTree"""

    def setUp(self):
        self.ft = FileTree(sample_list)

    def test_check_length(self):
        """Test counting entries"""

        # Compare length
        self.assertEqual(len(sample_list), len(self.ft))

    def test_check_length_remove_subtree(self):
        """Test length after remove"""

        len_remove = FileTree.dict_count(self.ft.dict['test123'])

        del self.ft.dict['test123']

        # Compare length
        self.assertEqual(len(sample_list) - len_remove, len(self.ft))

    def test_zero_length(self):
        """Test empty file tree"""

        ft0 = FileTree([])

        self.assertEqual(0, len(ft0))


if __name__ == '__main__':
    unittest.main()

