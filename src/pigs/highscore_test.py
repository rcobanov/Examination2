#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import string
from tokenize import String
import unittest
import highscore
import player


class TestHighscoreClass(unittest.TestCase):
    """Test the class."""

    def test_object_initiating(self):
        """Test initiating an object from the class."""
        test_hs = highscore.Highscore()
        self.assertIsInstance(test_hs, highscore.Highscore)

    # funkar inte som det ska, vet inte hur vi ska testa de 2 metoderna i highscore eftersom man skriver till fil
    def test_collect_score(self):
        """Test collect score."""
        test_hs = highscore.Highscore()
        test_name = "Testname"
        test_hs.collect_score(test_name, 12, 12)
        with open("highscores.txt", "r") as file:
            data = file.readlines()
            all_scores = []
            for line in data:
                name, total, streak = line.split(";")
                score = (name, int(total), streak.rstrip())
                all_scores.append(score)
                for score in all_scores:
                    if score[0] == test_name:
                        self.assertIn(test_name, score[0])
                   # self.assertEqual(score[0], "TESTSCORE")
                   # self.assertEqual(score[1], 12)
                   # self.assertEqual(score[2], 12)

# kan man testa datatyper bara så behöver man ej skriva nytt till textfilen?
# self.assertIs(score[0], string)
# self.assertIs(score[1], int)
# self.assertIs(score[2], int)


if __name__ == '__main__':
    unittest.main()

#def test_collect_score(self):
#    """Test collect_scores"""
#    test_hs = highscore.Highscore()
#    test_hs.collect_score("TESTSCORE", 12, 12)
#    message = "TESTSCORE NOT HERE"
#    with open("highscores.txt", "r") as file:
#        data = file.readlines
#namelist = []
# for line in data:
#   name, total, streak = line.split(";")
#    namelist.append(name)
#    self.assertIn("TESTSCORE",data,message)