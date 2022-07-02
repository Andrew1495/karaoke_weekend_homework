import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.karaoke_venue import Venue


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.venue_1 = Venue("code clan karaoke", 200, 10, 5.00)
        self.room1 = Room("room 1", 5)
        self.room2 = Room("room 2", 3)
        self.guest1 = Guest("Bob", 25.00, "Yellow Submarine")
        self.guest2 = Guest("Frank", 50.00, "Hey Jude")
        self.guest3 = Guest("Steve", 30.00, "Let It Be")
        self.song1 = Song("Yellow Submarine", "The Beetles")
        self.song2 = Song("Hey Jude", "The Beetles")





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
        self.room1.add_guest_room(self.guest1, self.venue_1)
        self.assertEqual("Bob", self.room1.guests[0].name)

    def test_remove_guest_from_room(self):
        self.room1.add_guest_room(self.guest1, self.venue_1)
        guest_remove = self.guest1
        self.room1.remove_guest(guest_remove)
        self.assertEqual(0, len(self.room1.guests))

    def test_add_song_to_room(self):
        self.room1.add_song_room(self.song1)
        self.assertEqual("Yellow Submarine", self.room1.songs[0].name)


    def test_remove_song_from_room(self):
        self.room1.add_song_room(self.song1)
        self.room1.remove_song(self.song1)
        self.assertEqual(0, len(self.room1.songs))

    def test_customer_fav_song(self):
        self.room1.add_song_room(self.song1)
        self.room1.add_guest_room(self.guest1, self.venue_1)
        reaction = self.guest1.has_fav_song(self.room1)
        self.assertEqual("wooooo", reaction)
        
