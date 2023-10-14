#!/usr/bin/python3
"""Unittest for user class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    @classmethod
    def setUpClass(self):
        """Setup inst for tests"""
        self.inst = User()

    @classmethod
    def tearDownClass(self):
        """Delete tests after tests"""
        del self.inst

    def test_name(self):
        """Test if user last name is public string"""
        self.assertTrue(isinstance(self.inst.last_name, str))

    def test_email(self):
        """Test if user email is public string"""
        self.assertTrue(isinstance(self.inst.email, str))

    def test_first_name(self):
        """Test if User first name is public string"""
        self.assertTrue(isinstance(self.inst.first_name, str))

    def test_password(self):
        """Test if passeword is public string"""
        self.assertTrue(isinstance(self.inst.password, str))
