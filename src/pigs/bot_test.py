#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import bot
import dice

class TestBotClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Instantiate an object and check its properties."""
        test_bot = bot.Bot(0, 0, 1)
        self.assertIsInstance(test_bot, bot.Bot)

    def test_add_current_to_total_score(self):
        """Summarize total with the current score on this round."""
        test_bot = bot.Bot(12, 10, 2)
        test_bot.add_curr_to_total()
        self.assertEqual(test_bot.total_score, 22)

    def test_reset_current_score_to_zero(self):
        """Reset current score to zero."""
        test_bot = bot.Bot(12, 0, 2)
        test_bot.reset_current_score()
        self.assertEqual(test_bot.curr_round_score, 0)

    def test_number_of_rounds(self):
        """Test get_number_of_rounds method."""
        test_bot = bot.Bot(0, 0, 2)
        number_of_rounds = test_bot.get_number_of_rounds(2)
        exp = 9
        self.assertEqual(number_of_rounds, exp)

    def test_reset_bot_values(self):
        """Test reset scores on bot."""
        test_bot = bot.Bot(2, 2, 2)
        test_bot.reset_scores()
        self.assertTrue(test_bot.curr_round_score == 0)
        self.assertTrue(test_bot.total_score == 0)

    # Skriv om testen, för ibland klarar botjäveln att samla poäng
    def test_easy_level_on_bot_round(self):
        """Testing the the easiest level on the bot."""
        test_bot = bot.Bot(0, 0, 1)
        test_dice = dice.Dice()
        test_bot.bot_round(test_dice)
        exp = 0
        self.assertEqual(test_bot.curr_round_score, exp)
        self.assertTrue(test_bot.total_score < 60)
        self.assertEqual(test_bot.level, 1)

    def test_hard_level_on_bot_round(self):
        """Testing the the hardest level on the bot."""
        test_bot = bot.Bot(0, 0, 3)
        test_dice = dice.Dice()
        test_bot.bot_round(test_dice)
        self.assertTrue(test_bot.curr_round_score == 0)
        self.assertTrue(test_bot.total_score < 30)
        self.assertEqual(test_bot.level, 3)


if __name__ == '__main__':
    unittest.main()
