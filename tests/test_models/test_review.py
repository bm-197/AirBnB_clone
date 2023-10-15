#!/usr/bin/python3
"""Unittest for review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for review class"""
    @classmethod
    def setUpClass(self):
        """Set up inst for tests"""
        self.inst = Review()

    @classmethod
    def tearDownClass(self):
        """Delete instance after tests"""
        del self.inst

    def test_user_id(self):
        """Test if user_id is a public string"""
        self.assertTrue(isinstance(self.inst.user_id, str))

    def test_place_id(self):
        """Test if place_id is a public string"""
        self.assertTrue(isinstance(self.inst.place_id, str))

    def test_text(self):
        """Test if review text is a public string"""
        self.assertTrue(isinstance(self.inst.text, str))
