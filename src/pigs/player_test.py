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
        test_player.reset_scores()
        exp = 0
        self.assertEqual(test_player.curr_round_score, exp)
        self.assertEqual(test_player.total_score, exp)
        self.assertEqual(test_player.rolls_made, exp)
        self.assertEqual(test_player.longest_streak, exp)
        self.assertEqual(test_player.fav_number, exp)

    def test_longest_streak(self):
        """Test so rolls made overwrites longest streak"""
        test_player = player.Player("TP", 12, 25, 4, 13)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.play_round(test_opponent, test_dice, "hold")
        self.assertEqual(test_player.longest_streak, 13)

    def test_player_rolls_one(self):
        """Testing functionality if player rolls 1"""
        test_player = player.Player("TP", 12, 10, 2, 5)
        test_dice = dice.Dice()
        exp = 0
        for i in range(30):
            test_player.player_roll(test_dice)
            if test_dice.this_roll == 1:
                break
        self.assertEqual(test_player.curr_round_score, exp)
        self.assertTrue(test_player.is_holding)

    def test_player_cheat_dice(self):
        """Testing functionality if player input rosebud"""
        test_player = player.Player("TP", 12, 10, 2, 5)
        test_dice = dice.Dice()
        test_player.is_cheating = True
        test_player.player_roll(test_dice)
        exp = test_dice.this_roll = 6
        self.assertTrue(exp)

    def test_values_after_player_round(self):
        """Testing values after one round from player_round"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.player_roll(test_dice)
        self.assertEqual(test_player.rolls_made, 1)
        #self.assertEqual(test_player.is_holding, True) Blir bara true om en etta rullas?
        self.assertTrue(0 <= test_player.curr_round_score <= 6)
        self.assertTrue(0 <= test_player.total_score <= 6)

    def test_player_quitting(self):
        """Testing so quit is true when player input quit"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.play_round(test_opponent, test_dice, "quit")
        self.assertTrue(test_player.is_quitting)

    def test_player_holding(self):
        """Testing so holding is true when player input hold"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.play_round(test_opponent, test_dice, "hold")
        self.assertTrue(test_player.is_holding)
        self.assertFalse(test_opponent.is_holding)

    def test_player_cheating(self):
        """Testing so cheat is true when player input cheat"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.play_round(test_opponent, test_dice, "rosebud")
        self.assertTrue(test_player.is_cheating)

    def test_player_restarting(self):
        """Testing so both players are reset if game is restarted"""
        test_player = player.Player("TP", 15, 15, 15, 15)
        test_opponent = player.Player("TO", 15, 15, 15, 15)
        exp = 0
        test_dice = dice.Dice()
        test_player.play_round(test_opponent, test_dice, "restart")
        self.assertEqual(test_player.curr_round_score, exp)
        self.assertEqual(test_player.total_score, exp)
        self.assertEqual(test_player.rolls_made, exp)
        self.assertEqual(test_player.longest_streak, exp)
        self.assertEqual(test_player.fav_number, exp)
        self.assertEqual(test_opponent.curr_round_score, exp)
        self.assertEqual(test_opponent.total_score, exp)
        self.assertEqual(test_opponent.rolls_made, exp)
        self.assertEqual(test_opponent.longest_streak, exp)
        self.assertEqual(test_opponent.fav_number, exp)

    def test_player_rolling(self):
        """Check that roll function works when input roll"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        test_player.play_round(test_opponent,test_dice, "roll")
        exp = test_dice.this_roll != 0
        self.assertTrue(exp)
        self.assertNotEqual(test_player.curr_round_score,0)

    def test_player_rolling_one(self):
        """Check that player holds when 1 is rolled when input roll"""
        test_player = player.Player("TP", 0, 0, 0, 0)
        test_opponent = player.Player("TO", 0, 0, 0, 0)
        test_dice = dice.Dice()
        for i in range(50):
            test_player.play_round(test_opponent,test_dice, "roll")
            if test_dice.this_roll == 1:
                self.assertTrue(test_player.is_holding)


if __name__ == '__main__':
    unittest.main()
