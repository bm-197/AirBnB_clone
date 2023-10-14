#!/usr/bin/python3
"""Unittest for state class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state_name(self):
        inst = State()
        self.assertTrue(isinstance(inst.name, str))
