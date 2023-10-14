#!/usr/bin/python3
"""Unittest for class City"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    @classmethod
    def setUpClass(self):
        """setup  a inst for test"""
        self.inst = City()

    @classmethod
    def tearDownClass(self):
        """Delete created inst after test"""
        del self.inst

    def test_state_id(self):
        """Test state_id is a string"""
        self.assertTrue(isinstance(self.inst.state_id, str))

    def test_state_name(self):
        """Test state name is a string"""
        self.assertTrue(isinstance(self.inst.name, str))
