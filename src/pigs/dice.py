#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This class can create a dice object.

That can be rolled and get a value between 1-6.
"""

import random


class Dice():
    """The dice class."""

    faces = 6

    def __init__(self):
        """Initiate a dice object."""
        random.seed()
        self.this_roll = 0

    def roll(self):
        """Roll the dice."""
        roll = random.randint(1, self.faces)
        self.this_roll = roll
        return roll
