#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os.path
import sys
import SAKo


class TestSAKo(unittest.TestCase):
    """
        Test klientskych funkci
    """

    def setUp(self):
        self.path_to_script = os.path.dirname(os.path.abspath(__file__))
        pass

    def test_SAKo(self):
        os.system('python ' + self.path_to_script + '/SAKo.py -d ' +
                  self.path_to_script +
                  '/example -l test -p test1 -a sako_dev -t ping > test.txt')
        p_f = open('test.txt', 'r')
        text = p_f.read()[-4:-2]
        print text
        self.assert_(text == "OK")
        p_f.close()

    def test_identity(self):
        sys.stdin = open(self.path_to_script + '/tests/identity.txt', 'r')
        result = SAKo.create_identification_file('identity')
        self.assert_(result == 1)

    def test_submit(self):
        result = SAKo.submit('sako_dev', self.path_to_script + '/example',
                             'test', 'test1', 'ping')

        self.assert_(result[-3:-1] == "OK")

if __name__ == "__main__":
    unittest.main()
