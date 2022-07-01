import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Bob", 25.00, "Yellow submarine")
        self.guest2 = Guest("Frank", 50.00, "Hey Jude")



    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest1.name)
        self.assertEqual("Frank", self.guest2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(25.00, self.guest1.wallet)
        self.assertEqual(50.00, self.guest2.wallet)


    
    def test_guest_has_fav_song(self):
        self.assertEqual("Yellow submarine", self.guest1.fav_song)
        self.assertEqual("Hey Jude", self.guest2.fav_song)