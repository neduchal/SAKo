#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "neduchal"
__date__ = "$17.3.2015 13:37:46$"

import unittest
import os.path

path_to_script = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path_to_script, "../"))

import SAKo

class TestSAKoDirectoryClass(unittest.TestCase):
    
    def setUp(self):
        self.dir = SAKo.directory("./")
        
    def test_getFirst(self):
        filename = self.dir.getFirst()
        self.assert_(os.path.basename(filename) == "test.py")
  
    def test_getLast(self):
        filename = self.dir.getLast()
        self.assert_(os.path.basename(filename) == "test.py")        
        
    def test_getCount(self):
        count = self.dir.getCount()
        self.assert_(count == 1)             

if __name__ == "__main__":
    print "Hello World"
