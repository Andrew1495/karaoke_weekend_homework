import unittest
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("room 1", 5)
        self.room2 = Room("room 2", 3)
        self.guest1 = Guest("Bob", 25.00, "Yellow Submarine")
        self.guest2 = Guest("Frank", 50.00, "Hey Jude")
        self.guest3 = Guest("Steve", 30.00, "Let It Be")
        self.group = Group()
        self.group.add_to_group(self.guest1)
        self.group.add_to_group(self.guest2)
        self.group.add_to_group(self.guest3)




    def test_room_names(self):
        self.assertEqual("room 1", self.room1.name)
        self.assertEqual("room 2", self.room2.name)

    def test_room_capacity(self):
        self.assertEqual(5, self.room1.room_capacity)
        self.assertEqual(3, self.room2.room_capacity)

    def test_room_no_songs(self):
        self.assertEqual(0, len(self.room1.songs))
        self.assertEqual(0, len(self.room2.songs))

    def test_no_guests_in_room(self):
        self.assertEqual(0, len(self.room1.guests))
        self.assertEqual(0, len(self.room2.guests))

    def test_add_guest_to_room(self):
        self.room1.add_guest_room(self.guest1)
        self.assertEqual("Bob", self.room1.guests[0].name)

