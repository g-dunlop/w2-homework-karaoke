import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room A")
        self.guest = Guest("Bob")
        self.song = Song("House of the Rising Sun", "The Animals", "Classic Rock")

    def test_room_has_name(self):
        self.assertEqual("Room A", self.room.name)

    def test_can_add_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))