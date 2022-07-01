import unittest
from src.karaoke_venue import Venue



class TestVenue(unittest.TestCase):
    

    def setUp(self):
        self.venue_1 = Venue("code clan karaoke", 200, 10)
        self.venue_2 = Venue("Karaoke place", 100, 4)


    def test_venue_has_name(self):
        self.assertEqual("code clan karaoke", self.venue_1.name)
        self.assertEqual("Karaoke place", self.venue_2.name)


    def test_venue_holds_money(self):
        self.assertEqual(200, self.venue_1.till)
        self.assertEqual(100, self.venue_2.till)

    def test_venue_room_count(self):
        self.assertEqual(10, self.venue_1.amount_of_rooms)
        self.assertEqual(4, self.venue_2.amount_of_rooms)