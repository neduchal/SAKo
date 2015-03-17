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
        pass
        
    def test_find(self):
        dir = None
        try:
            dir = SAKo.directory(path_to_script)
        except:
            self.assert_(false)
        for i in range(dir.getCount()):
            filename = dir.getNext()
            if filename is not None :
                if filename == "test_directory.py":
                    self.assert_(true)
                    pass
        self.assert_(false)

    def test_previous(self):
        try:
            dir = SAKo.directory(path_to_script)
        except:
            self.assert_(false)
        dir.position = dir.getCount() - 1
        dir.getPrevious()
        self.assert_(dir.position ==  dir.getCount() - 2)
        
    def test_next(self):
        try:
            dir = SAKo.directory(path_to_script)
        except:
            self.assert_(false)
        dir.getNext()
        self.assert_(dir.position ==  1)
        
    def test_first(self):
        try:
            dir = SAKo.directory(path_to_script)
        except:
            self.assert_(false)
        filename = dir.getFirst()
        self.assert_(dir.filelist[0] ==  filename)
        
    def test_Last(self):
        try:
            dir = SAKo.directory(path_to_script)
        except:
            self.assert_(false)
        filename = dir.getLast()
        self.assert_(dir.filelist[dir.getCount() - 1] ==  filename)
        


if __name__ == "__main__":
    unittest.main()
