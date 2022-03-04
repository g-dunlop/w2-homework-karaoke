import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob")

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)