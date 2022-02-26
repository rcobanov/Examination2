#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import bot


class TestBotClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Instantiate an object and check its properties."""
        test_bot = bot.Bot(0, 0, 1)
        self.assertIsInstance(test_bot, bot.Bot)

    def test_add_current_to_total_score(self):
        """Summarize total with the current score on this round."""
        test_bot = bot.Bot(12, 10, 2)
        test_bot.addCurrToTotal()
        self.assertEqual(test_bot.total_score, 22)

    def test_reset_current_score_to_zero(self):
        """Reset current score to zero."""
        test_bot = bot.Bot(12, 0, 2)
        test_bot.reset_current_score()
        self.assertEqual(test_bot.curr_round_score, 0)

    def test_number_of_rounds(self):
        """Test getNumberOfRounds method."""
        test_bot = bot.Bot(0, 0, 2)
        numberofRounds = test_bot.get_number_of_rounds(2)
        exp = 9
        self.assertEqual(numberofRounds, exp)


if __name__ == '__main__':
    unittest.main()
