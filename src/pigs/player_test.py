#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def testObjectInitiating(self):
        """Instantiate an object and check its properties."""
        test_player = player.Player("TP", 0, 0, 0, 0, 0)
        self.assertIsInstance(test_player, player.Player)

    def testSetName(self):
        """Setting the name of the player."""
        test_player = player.Player("TP", 0, 0, 0, 0, 0)
        test_player.setName("player")
        self.assertEqual(test_player.name, "player")

    def testIsHoldingSetAsFalse(self):
        """Checking isHolding variable to be false."""
        test_player = player.Player("TP", 0, 0, 0, 0, 0)
        self.assertFalse(test_player.is_holding)

    def testAddCurrentToTotalScore(self):
        """Summarize total with the current score on this round."""
        test_player = player.Player("TP", 12, 10, 0, 0, 0)
        test_player.addCurrToTotal()
        self.assertEqual(test_player.total_score, 22)

    def testResetCurrentScoreToZero(self):
        """Reset current score to zero."""
        test_player = player.Player("TP", 12, 0, 0, 0, 0)
        test_player.resetCurrentScore()
        self.assertEqual(test_player.curr_round_score, 0)


if __name__ == '__main__':
    unittest.main()
