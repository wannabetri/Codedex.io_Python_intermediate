import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('espresso'), 2.50)
        self.assertEqual(self.menu.get_price('latte'), 2.75)
        self.assertEqual(self.menu.get_price('cappuccino'), 3.20)
        self.assertEqual(self.menu.get_price('americano'), 2.70)

    def test_menu(self):
        menu = CoffeeMenu()
        self.assertEqual(menu.menu['espresso'], 2.50)
        self.assertEqual(menu.menu['latte'], 2.75)
        self.assertEqual(menu.menu['cappuccino'], 3.20)
        self.assertEqual(menu.menu['americano'], 2.70)

    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('mocha'))
        self.assertIsNone(self.menu.get_price('frappuccino'))
        self.assertIsNone(self.menu.get_price('macchiato'))
    
    def test_get_price_invalid_item(self):  
        self.assertIsNone(self.menu.get_price(''))
        self.assertIsNone(self.menu.get_price(' '))

    def test_add_item(self):
        self.menu.add_item('mocha', 3.50)
        self.assertEqual(self.menu.get_price('mocha'), 3.50)
        self.menu.add_item('frappuccino', 4.00)
        self.assertEqual(self.menu.get_price('frappuccino'), 4.00)
        self.menu.add_item('macchiato', 3.25)
        self.assertEqual(self.menu.get_price('macchiato'), 3.25)

if __name__ == '__main__':
    unittest.main()