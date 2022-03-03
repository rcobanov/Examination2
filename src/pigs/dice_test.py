#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Instantiate an object and check its properties."""
        test_dice = dice.Dice()
        self.assertIsInstance(test_dice, dice.Dice)

    def testrolldice(self):
        """Roll the dice 25 times, verify the result"""
        test_dice = dice.Dice()
        expected = True
        for i in range(25):
            res = test_dice.roll()
            if expected != 1 <= res <= test_dice.faces:
                expected = False
                break
        self.assertTrue(expected)

if __name__ == '__main__':
    unittest.main()
