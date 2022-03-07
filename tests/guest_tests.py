import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 50, "House of the Rising Sun")
        self.room = Room("Room A", 10, 4)
        self.song = Song("House of the Rising Sun", "The Animals", "Classic Rock")
        self.song_2 = Song("Barbie Girl", "Aqua", "pop")


    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("House of the Rising Sun", self.guest.favourite_song)

    def test_guest_has_volume(self):
        self.assertEqual(0, self.guest.volume)

    def test_increase_volume(self):
        self.guest.increase_volume()
        self.assertEqual(25, self.guest.volume)

    def test_guest_wallet_decrease(self):
        self.guest.pay_fee(self.room)
        self.assertEqual(40, self.guest.wallet)

    def test_react_to_song_whoo(self):
        self.guest.react_to_song(self.song)
        self.assertEqual("whoo", self.guest.react_to_song(self.song))

    def test_react_to_song_meh(self):
        self.guest.react_to_song(self.song_2)
        self.assertEqual("meh", self.guest.react_to_song(self.song_2))
