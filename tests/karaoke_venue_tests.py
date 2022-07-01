import unittest
from src.karaoke_venue import Venue
from src.guest import Guest



class TestVenue(unittest.TestCase):
    

    def setUp(self):
        self.venue_1 = Venue("code clan karaoke", 200, 10)
        self.venue_2 = Venue("Karaoke place", 100, 1)


    def test_venue_has_name(self):
        self.assertEqual("code clan karaoke", self.venue_1.name)
        self.assertEqual("Karaoke place", self.venue_2.name)


    def test_venue_holds_money(self):
        self.assertEqual(200, self.venue_1.till)
        self.assertEqual(100, self.venue_2.till)

    def test_venue_room_count(self):
        self.assertEqual(10, self.venue_1.amount_of_rooms)
        self.assertEqual(1, self.venue_2.amount_of_rooms)


    def test_venue_room_count(self):
        self.assertEqual(0, len(self.venue_1.rooms))
        self.assertEqual([], self.venue_2.rooms)


    def test_is_rooms_avaible(self):
        rooms_avaible = self.venue_1.is_rooms_avaible()
        self.assertEqual(True, rooms_avaible)
    
    def test_is_not_room_avaible(self):
        rooms_avaible = self.venue_2.is_rooms_avaible()
        self.assertEqual(True, rooms_avaible)