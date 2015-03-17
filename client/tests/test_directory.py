#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "neduchal"
__date__ = "$17.3.2015 13:37:46$"

import unittest
import os.path
import sys

path_to_script = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path_to_script, "../"))

import SAKo


class TestSAKoDirectoryClass(unittest.TestCase):

    def setUp(self):
        self.dir = SAKo.directory(path_to_script)

    def test_getFirst(self):
        filename = self.dir.getFirst()
        print os.path.basename(filename)
        self.assert_(os.path.basename(filename) == "test_directory.py")

    def test_getLast(self):
        filename = self.dir.getLast()
        print os.path.basename(filename)
        self.assert_(os.path.basename(filename) == "test_directory.py")

    def test_getCount(self):
        count = self.dir.getCount()
        print count
        self.assert_(count == 1)

if __name__ == "__main__":
    unittest.main()
