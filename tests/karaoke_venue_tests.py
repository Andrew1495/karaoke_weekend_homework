import unittest
from src.karaoke_venue import Venue
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.food_drink import FoodDrink



class TestVenue(unittest.TestCase):
    

    def setUp(self):
        self.venue_1 = Venue("code clan karaoke", 200, 10, 5.00)
        self.venue_2 = Venue("Karaoke place", 100, 1, 10.00)
        self.song1 = Song("Yellow Submarine", "The Beetles")
        self.song2 = Song("Hey Jude", "The Beetles")
        self.room1 = Room("room 1", 5)
        self.room2 = Room("room 2", 3)
        self.guest1 = Guest("Bob", 25.00, "Yellow Submarine")
        self.guest2 = Guest("Frank", 50.00, "Hey Jude")
        self.guest3 = Guest("Steve", 30.00, "Let It Be")
        self.guest4 = Guest("Tom", 0.00, "Hey Jude")
        self.drink1 = FoodDrink("beer", 3.00, 50)
        self.food1 = FoodDrink("burger", 5.00, 25)



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


    def test_customer_can_afford_item(self):
        can_afford = self.venue_1.guest_can_afford(self.guest1, self.drink1)
        self.assertEqual(True, can_afford)

    def test_customer_cannot_afford_item(self):
        can_afford = self.venue_1.guest_can_afford(self.guest4, self.drink1)
        self.assertEqual(False, can_afford)

