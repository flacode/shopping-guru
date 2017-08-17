import unittest
from app.item import Item


class TestItem(unittest.TestCase):
    """Tests for Item class"""
    def setUp(self):
        self.my_item = Item('milk', 5, 'Quality supermarket')
