#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import highscore
import player


class TestHighscoreClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Test initiating an object from the class."""
        test_hs = highscore.Highscore()
        self.assertIsInstance(test_hs, highscore.Highscore)

    def test_collect_score(self):
        """Test collect score."""
        test_player = player.Player("TESTER", 122, 122, 122, 122)
        filename = "highscore_test.txt"
        test_hs = highscore.Highscore()
        test_hs.collect_score(test_player.name, test_player.total_score,
                            test_player.longest_streak, filename)
        with open(filename, "r") as file:
            for line in file:
                name, total, streak = line.split(";")
                self.assertEqual(name, test_player.name)

    def test_score_board(self):
        """Test the scoreboard."""
        filename = "highscore_test.txt"
        test_hs = highscore.Highscore()
        test_hs.show_score_board(filename)


if __name__ == '__main__':
    unittest.main()
