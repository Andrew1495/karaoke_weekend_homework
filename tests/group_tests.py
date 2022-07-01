import unittest

from src.group import Group
from src.guest import Guest

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Bob", 25.00, "Yellow Submarine")
        self.guest2 = Guest("Frank", 50.00, "Hey Jude")
        self.guest3 = Guest("Steve", 30.00, "Let It Be")
        self.group = Group()

    def test_adding_guests_to_group(self):
        self.group.add_to_group(self.guest1)
        self.assertEqual("Bob", self.group.group[0].name)

    def test_adding_multi_guests_to_group(self):
        self.group.add_to_group(self.guest2)
        self.group.add_to_group(self.guest3)
        self.assertEqual("Frank", self.group.group[0].name)
        self.assertEqual("Steve", self.group.group[1].name)

    def test_remove_guest_from_group(self):
        self.group.add_to_group(self.guest1)
        self.group.remove_from_group(self.guest1)
        self.assertEqual(0, len(self.group.group))
    