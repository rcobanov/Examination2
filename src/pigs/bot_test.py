#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import bot


class TestBotClass(unittest.TestCase):
    """Test the class."""

    def testObjectInitiating(self):
        """Instantiate an object and check its properties."""
        testBot = bot.Bot(0, 0, 1)
        self.assertIsInstance(testBot, bot.Bot)

    def testAddCurrentToTotalScore(self):
        """Summarize total with the current score on this round."""
        testBot = bot.Bot(12, 10, 2)
        testBot.addCurrToTotal()
        self.assertEqual(testBot.totalScore, 22)

    def testResetCurrentScoreToZero(self):
        """Reset current score to zero."""
        testBot = bot.Bot(12, 0, 2)
        testBot.resetCurrentScore()
        self.assertEqual(testBot.currRoundScore, 0)

    def testNumberOfrounds(self):
        """Test getNumberOfRounds method."""
        testBot = bot.Bot(0, 0, 2)
        numberofRounds = testBot.getNumberOfRounds(2)
        exp = 9
        self.assertEqual(numberofRounds, exp)


if __name__ == '__main__':
    unittest.main()
