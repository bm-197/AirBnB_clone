#!/usr/bin/python3
"""Unittest for amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_name(self):
        inst = Amenity()
        self.assertTrue(isinstance(inst.name, str))
