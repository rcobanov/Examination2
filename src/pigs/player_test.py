#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import player
import dice


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Instantiate an object and check its properties."""
        test_player = player.Player("TP", 0, 0, 0, 0)
        self.assertIsInstance(test_player, player.Player)

    def test_set_name(self):
        """Setting the name of the player."""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_player.set_name("player")
        self.assertEqual(test_player.name, "player")

    def test_is_holding_set_as_false(self):
        """Checking isHolding variable to be false."""
        test_player = player.Player("TP", 0, 0, 0, 0)
        self.assertFalse(test_player.is_holding)

    def test_add_current_to_total_score(self):
        """Summarize total with the current score on this round."""
        test_player = player.Player("TP", 12, 10, 0, 0)
        test_player.add_curr_to_total()
        self.assertEqual(test_player.total_score, 22)

    def test_reset_current_score_to_zero(self):
        """Reset current score to zero."""
        test_player = player.Player("TP", 12, 0, 0, 0)
        test_player.reset_current_score()
        self.assertEqual(test_player.curr_round_score, 0)

    def reset_all_values_on_player_to_zero(self):
        """Reset all variables on test_player to zero"""
        test_player = player.Player("TP", 12, 10, 2, 5)
        test_player.reset_player()
        exp = 0
        self.assertEqual(test_player.curr_round_score, exp)
        self.assertEqual(test_player.total_score, exp)
        self.assertEqual(test_player.rolls_made, exp)
        self.assertEqual(test_player.longest_streak, exp)

    def test_values_after_player_round(self):
        """Testing values after one round from player_round"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.player_round(test_dice)
        self.assertEqual(test_player.rolls_made, 1)
        self.assertEqual(test_player.is_holding, True)
        self.assertTrue(0 <= test_player.curr_round_score <= 6)
        self.assertTrue(0 <= test_player.total_score <= 6)


if __name__ == '__main__':
    unittest.main()
