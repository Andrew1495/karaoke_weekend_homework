import unittest
from src.food_drink import FoodDrink

class TestFoodDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = FoodDrink("beer", 3.00, 50)
        self.food1 = FoodDrink("burger", 5.00, 25)

    def test_food_and_drink_name(self):
        self.assertEqual("beer", self.drink1.name)
        self.assertEqual("burger", self.food1.name)

    def test_food_and_drink_price(self):
        self.assertEqual(3.00, self.drink1.price)
        self.assertEqual(5.00, self.food1.price)

    def test_stock_amount(self):
        self.assertEqual(50, self.drink1.quanity)
        self.assertEqual(25, self.food1.quanity)
    