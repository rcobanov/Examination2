#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def testObjectInitiating(self):
        """Instantiate an object and check its properties."""
        testPlayer = player.Player("TP", 0, 0, 0, 0, 0)
        self.assertIsInstance(testPlayer, player.Player)

    def testSetName(self):
        """Setting the name of the player"""
        testPlayer = player.Player("TP", 0, 0, 0, 0, 0)
        testPlayer.setName("player")
        self.assertEqual(testPlayer.name, "player")

    def testIsHoldingSetAsFalse(self):
        """Checking isHolding variable to be false"""
        testPlayer = player.Player("TP", 0, 0, 0, 0, 0)
        self.assertFalse(testPlayer.isHolding)

    def testAddCurrentToTotalScore(self):
        """Summarize total with the current score on this round"""
        testPlayer = player.Player("TP", 12, 10, 0, 0, 0)
        testPlayer.addCurrToTotal()
        self.assertEqual(testPlayer.totalScore, 22)

    def testResetCurrentScoreToZero(self):
        """Reset current score to zero"""
        testPlayer = player.Player("TP", 12, 0, 0, 0, 0)
        testPlayer.resetCurrentScore()
        self.assertEqual(testPlayer.currRoundScore, 0)

if __name__ == '__main__':
    unittest.main()
