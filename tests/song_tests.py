import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("House of the Rising Sun", "The Animals", "Classic Rock")

    def test_song_has_name(self):
        self.assertEqual("House of the Rising Sun", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("The Animals", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Classic Rock", self.song.genre)