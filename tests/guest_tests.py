import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 50)
        self.room = Room("Room A", 10, 4)


    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_wallet_decrease(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(40, self.guest.wallet)