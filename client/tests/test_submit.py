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

    def test_submit(self):
        result = SAKo.submit('sako_dev', path_to_script, 'test', 'test1',
                             'ping')
        print result[-3:]
        self.assert_(result[-3:-1] == "OK")

if __name__ == "__main__":
    unittest.main()
