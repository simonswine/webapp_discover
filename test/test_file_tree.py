# -*- encoding: UTF8 -*-

__author__ = 'Christian Simon'

# init env
from test_setup import setup
setup()

import unittest
import tempfile
import shutil
import os

from webapp_discover.file_tree import FileTree


sample_list = [
    './index.php',
    './license.txt',
    './readme.html',
    './test123/readme.html',
    './test123/readme.txt',
]

def touch(fname, times=None):
    # Check if dir exists
    dir_path = os.path.dirname(fname)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


    # Create file  (or modify its times)
    with open(fname, 'a'):
        os.utime(fname, times)

def create_file_in_path(path, list):
    for i in list:
            touch(os.path.join(path,i))

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


class FileTreeChecks(unittest.TestCase):
    """Testing the check of FileTree"""

    def setUp(self):

        # Create filetree
        self.ft = FileTree(sample_list)

        # Create sample path
        self.path = tempfile.mkdtemp()


    def tearDown(self):

        # Delete sample path
        shutil.rmtree(self.path)


    def test_check_first2(self):
        """Test sample against a dir with 2 matching files"""
        count = 2
        create_file_in_path(self.path,sample_list[:count])
        self.assertEqual(float(count)/float(len(sample_list)), self.ft.check(self.path,ratio=0))

    def test_check_all(self):
        """Test sample against a dir with all matching files"""
        create_file_in_path(self.path,sample_list)
        self.assertEqual(1,self.ft.check(self.path,ratio=0))

    def test_check_none(self):
        """Test sample against a dir with no matching files"""
        self.assertEqual(0,self.ft.check(self.path,ratio=0))


if __name__ == '__main__':
    unittest.main()

