#!/usr/bin/python3
"""Unittest for review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.inst = Review()

    @classmethod
    def tearDownClass(self):
        del self.inst

    def test_user_id(self):
        self.assertTrue(isinstance(self.inst.user_id, str))

    def test_place_id(self):
        self.assertTrue(isinstance(self.inst.place_id, str))

    def test_text(self):
        self.assertTrue(isinstance(self.inst.text, str))
