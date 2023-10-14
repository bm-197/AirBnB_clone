#!/usr/bin/python3
"""Unittest for user class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.inst = User()

    @classmethod
    def tearDownClass(self):
        del self.inst

    def test_name(self):
        self.assertTrue(isinstance(self.inst.last_name, str))

    def test_email(self):
        self.assertTrue(isinstance(self.inst.email, str))

    def test_first_name(self):
        self.assertTrue(isinstance(self.inst.first_name, str))

    def test_password(self):
        self.assertTrue(isinstance(self.inst.password, str))
