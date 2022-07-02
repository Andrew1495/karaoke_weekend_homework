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
        self.room3 = Room("room 3", 1)
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

    def test_adding_items_to_menu(self):
        self.venue_1.add_item_menu(self.drink1)
        self.assertEqual(1, len(self.venue_1.menu))
        self.assertEqual("beer", self.venue_1.menu[0].name)

    def test_find_item_by_name(self):
        self.venue_1.add_item_menu(self.drink1)
        item = self.venue_1.find_item_buy_name(self.drink1.name)
        self.assertEqual(self.drink1, item)

    def test_cannot_find_item(self):
        item = self.venue_1.find_item_buy_name(self.food1.name)
        self.assertEqual(None, item)

    def test_adding_drink_to_customer(self):
        self.venue_1.add_item_menu(self.drink1)
        item = self.venue_1.find_item_buy_name(self.drink1.name)
        self.venue_1.add_item_to_guest(self.guest1, item)
        self.assertEqual(1, len(self.guest1.item_list))
        self.assertEqual("beer", self.guest1.item_list[0].name)
        self.assertEqual(49, self.venue_1.menu[0].quanity)

    def test_customer_paying(self):
        self.venue_1.add_item_menu(self.drink1)
        item = self.venue_1.find_item_buy_name(self.drink1.name)
        self.venue_1.add_item_to_guest(self.guest1, item)
        self.venue_1.customer_pay_tab(self.guest1)
        self.assertEqual(17.00, self.guest1.wallet)
        self.assertEqual(208.00, self.venue_1.till)
        self.assertEqual(49, self.venue_1.menu[0].quanity)


    def test_add_room_to_venue(self):
        self.venue_1.add_room(self.room1)
        self.assertEqual(1, len(self.venue_1.rooms))
        self.assertEqual("room 1", self.venue_1.rooms[0].name)


    def test_add_guest_to_room(self):
        self.venue_2.add_room(self.room3)
        self.room3.add_guest_room(self.guest1, self.venue_2)
        self.assertEqual("Bob", self.venue_2.rooms[0].guests[0].name)
        
    def test_remove_guest_from_room(self):
        self.venue_2.add_room(self.room3)
        self.room3.add_guest_room(self.guest1, self.venue_2)
        self.assertEqual("Bob", self.venue_2.rooms[0].guests[0].name)
        self.room3.remove_guest(self.guest1)
        self.assertEqual(0, len(self.venue_2.rooms[0].guests))

    def test_full_room_adding(self):
        self.venue_2.add_room(self.room3)
        self.room3.add_guest_room(self.guest1, self.venue_2)
        self.room3.add_guest_room(self.guest2, self.venue_2)
        self.assertEqual(1, len(self.venue_2.rooms[0].guests))

    def test_adding_max_rooms(self):
        self.venue_1.setting_up_rooms(5)
        self.assertEqual(10, len(self.venue_1.rooms))

    def test_adding_max_rooms_and_adding_customers(self):
        self.venue_1.setting_up_rooms(5)
        self.venue_1.rooms[0].add_guest_room(self.guest1, self.venue_1)
        self.venue_1.rooms[0].add_guest_room(self.guest2, self.venue_1)
        self.venue_1.rooms[0].add_guest_room(self.guest3, self.venue_1)
        self.assertEqual(3, len(self.venue_1.rooms[0].guests))


    def test_adding_customer_who_cant_afford(self):
        self.venue_1.setting_up_rooms(5)
        self.venue_1.rooms[0].add_guest_room(self.guest4, self.venue_1)
        self.assertEqual(0, len(self.venue_1.rooms[0].guests))

    def testing_customer_paying_for_room_and_items(self):
        self.venue_1.setting_up_rooms(5)
        self.venue_1.rooms[0].add_guest_room(self.guest1, self.venue_1)
        self.venue_1.add_item_menu(self.drink1)
        item = self.venue_1.find_item_buy_name(self.drink1.name)
        self.venue_1.add_item_to_guest(self.guest1, item)
        self.venue_1.customer_pay_tab(self.guest1)
        self.venue_1.rooms[0].remove_guest(self.guest1)
        self.assertEqual(17.00, self.guest1.wallet)
        self.assertEqual(208, self.venue_1.till)
        self.assertEqual(49, self.venue_1.menu[0].quanity)

    
