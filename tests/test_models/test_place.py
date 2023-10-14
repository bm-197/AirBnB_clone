#!/usr/bin/python3
"""Unittest for place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.inst = Place()

    @classmethod
    def tearDownClass(self):
        del self.inst

    def test_string_values(self):
        self.assertTrue(isinstance(self.inst.city_id, str))
        self.assertTrue(isinstance(self.inst.user_id, str))
        self.assertTrue(isinstance(self.inst.name, str))
        self.assertTrue(isinstance(self.inst.description, str))

    def test_number_values(self):
        self.assertTrue(isinstance(self.inst.number_rooms, int))
        self.assertTrue(isinstance(self.inst.number_bathrooms, int))
        self.assertTrue(isinstance(self.inst.max_guest, int))
        self.assertTrue(isinstance(self.inst.price_by_night, int))
        self.assertTrue(isinstance(self.inst.latitude, float))
        self.assertTrue(isinstance(self.inst.longitude, float))

    def test_amenities_id(self):
        self.assertTrue(isinstance(self.inst.amenity_ids, list))
