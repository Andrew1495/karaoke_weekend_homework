import unittest
from src.room import Room
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("room 1", 5)
        self.room2 = Room("room 2", 3)


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