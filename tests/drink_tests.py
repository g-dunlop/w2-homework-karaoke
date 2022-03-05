import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Vodka", 2)
        self.drink_2 = Drink("Whiskey", 2)

    def test_drink_has_name(self):
        self.assertEqual("Vodka", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(2, self.drink_1.price)