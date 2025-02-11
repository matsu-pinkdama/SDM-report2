#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        def test_sample1 (self):
                self.assertEqual (-1, calc(0.9,0.9))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0.9,10))

        def test_sample3 (self):
                self.assertEqual (-1, calc(10,0.9))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0,0))

        def test_sample5 (self):
                self.assertEqual (-1, calc(0,10))

        def test_sample6 (self):
                self.assertEqual (-1, calc(10,0))
        
        def test_sample7 (self):
                self.assertEqual (1, calc(1,1))

        def test_sample8 (self):
                self.assertEqual (10, calc(1,10))

        def test_sample9 (self):
                self.assertEqual (10, calc(10,1))

        def test_sample10 (self):
                self.assertEqual (-1, calc(1.1,10))

        def test_sample11 (self):
                self.assertEqual (-1, calc(10,1.1))

        def test_sample12 (self):
                self.assertEqual (-1, calc(1.1,1.1))

        def test_sample13 (self):
                self.assertEqual (9990, calc(999,10))

        def test_sample14 (self):
                self.assertEqual (9990, calc(10,999))

        def test_sample15 (self):
                self.assertEqual (998001, calc(999,999))
        
        def test_sample16 (self):
                self.assertEqual (-1, calc(998.9,998.9))

        def test_sample17 (self):
                self.assertEqual (-1, calc(998.9,10))

        def test_sample18 (self):
                self.assertEqual (-1, calc(10,998.9))

        def test_sample19 (self):
                self.assertEqual (-1, calc(1000,10))

        def test_sample20 (self):
                self.assertEqual (-1, calc(10,1000))

        def test_sample21 (self):
                self.assertEqual (-1, calc(1000,1000))

        def test_sample22 (self):
                self.assertEqual (-1, calc(999.9,10))

        def test_sample23 (self):
                self.assertEqual (-1, calc(10,999.9))

        def test_sample24 (self):
                self.assertEqual (-1, calc(999.9,999.9))
        
        def test_sample25 (self):
                self.assertEqual (-1, calc('A',10))

        def test_sample26 (self):
                self.assertEqual (-1, calc(10,'B'))

        def test_sample27 (self):
                self.assertEqual (-1, calc('A','B'))

