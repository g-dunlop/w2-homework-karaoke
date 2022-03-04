import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room A", 10, 4)
        self.guest = Guest("Bob", 50)
        self.guest_2 = Guest("Joni", 25)
        self.guest_3 = Guest("Jimi", 35)
        self.guest_4 = Guest("Mick", 80)
        self.guest_5 = Guest("Bon", 5)

        self.song = Song("House of the Rising Sun", "The Animals", "Classic Rock")

    def test_room_has_name(self):
        self.assertEqual("Room A", self.room.name)

    def test_room_has_price(self):
        self.assertEqual(10, self.room.price)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_can_check_out_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_space_for_guest(self):
        self.room.check_room_has_space(self.room.guests, self.room.capacity)
        self.assertEqual(True, self.room.check_room_has_space(self.room.guests, self.room.capacity))

    def test_room_is_already_full(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_3)
        self.room.add_guest(self.guest_4)
        self.room.check_room_has_space(self.room.guests, self.room.capacity)
        self.assertEqual(False, self.room.check_room_has_space(self.room.guests, self.room.capacity) )

    def test_guest_has_enough_money(self):
        self.room.check_funds(self.guest)
        self.assertEqual(True,self.room.check_funds(self.guest))

    def test_guest_does_not_have_enough_money(self):
        self.room.check_funds(self.guest_5)
        self.assertEqual(False, self.room.check_funds(self.guest_5))
        

