import unittest
from src.karaoke_venue import Venue



class TestVenue(unittest.TestCase):
    

    def setUp(self):
        self.venue_1 = Venue("code clan karaoke", 200, 10)
        self.venue_2 = Venue("Karaoke place", 100, 4)


    def test_venue_has_name(self):
        self.assertEqual("code clan karaoke", self.venue_1.name)
        self.assertEqual("Karaoke place", self.venue_2.name)