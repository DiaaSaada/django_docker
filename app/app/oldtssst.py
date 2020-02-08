from django.test import TestCase
from app.calc import add
from app.calc import subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """ Test that numbers are added"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Values are subtracted and returned"""
        self.assertEqual(subtract(9, 7), 2)
