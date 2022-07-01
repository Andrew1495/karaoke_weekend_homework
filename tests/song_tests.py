import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Yellow Submarine", "The Beetles")
        self.song2 = Song("Hey Jude", "The Beetles")


    def test_song_has_name(self):
        self.assertEqual("yellow Submarine", self.song1.name)
        self.assertEqual("Hey Jude", self.song2.name)

    def test_song_artist(self):
        self.assertEqual("The Beetles", self.song1.artist)
        self.assertEqual("The Beetles", self.song2.artist)