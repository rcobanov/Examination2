#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dice


class TestDiceClass(unittest.TestCase): 

    def testroll(self):
        testdice = dice.Dice()
        res = testdice.roll()
        expected = 1 <= res <= testdice.faces
        self.assertTrue(expected)


if __name__ == '__main__':
    unittest.main()
