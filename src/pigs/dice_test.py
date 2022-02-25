#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    def testroll(self):
        """Rool a dice and check if value is in bounds."""
        test_dice = dice.Dice()
        res = test_dice.roll()
        expected = 1 <= res <= test_dice.faces
        self.assertTrue(expected)


if __name__ == '__main__':
    unittest.main()
