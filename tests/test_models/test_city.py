#!/usr/bin/python3
"""Unittest for class City"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.inst = City()

    @classmethod
    def tearDownClass(self):
        del self.inst

    def test_state_id(self):
        self.assertTrue(isinstance(self.inst.state_id, str))

    def test_state_name(self):
        self.assertTrue(isinstance(self.inst.name, str))
