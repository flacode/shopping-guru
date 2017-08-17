import unittest
from app.shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    """Test cases for the shopping list class"""
    def setUp(self):
        self.my_list = ShoppingList('Flavia')

    def test_add_item_to_empty_shopping_list(self):
        """Test for add item to an empty list"""
        self.my_list.add_item_to_shopping_list('milk')
        self.assertEqual(self.my_list.items, ['milk'], msg='Method to add item to shopping \
        list does not add it')

    def test_add_item_to_non_empty_shopping_list(self):
        """Test for add item to a list with items"""
        self.my_list.items.append('sugar')
        self.my_list.add_item_to_shopping_list('coffee')
        self.assertEqual(self.my_list.items, ['sugar', 'coffee'], msg='Can not add \
        items to non empty list')

    def test_delete_item_that_is_not_in_the_shopping_list(self):
        """Delete Item that does not exist on in the shopping list"""
        self.assertRaises(ValueError, self.my_list.delete_item_from_shopping_list, 'bread')

    def test_delete_item_from_shopping_list(self):
        """Add Items to the shopping list and delete one of the items"""
        self.my_list.items.append('sugar')
        self.my_list.items.append('milk')
        self.my_list.items.append('coffee')
        self.my_list.delete_item_from_shopping_list('milk')
        self.assertEqual(self.my_list.items, ['sugar', 'coffee'], msg='Item was not deleted \
        from the list')

    def test_delete_item_from_empty_shopping_list(self):
        """Delete Item from empty shopping list"""
        self.assertRaises(ValueError,
                          self.my_list.delete_item_from_shopping_list, 'milk')

    def test_view_empty_shopping_list(self):
        """View empty shopping list"""
        self.assertEqual(self.my_list.view_shopping_list(), [],
                         msg="Can not display empty list")

    def test_view_non_empty_shopping_list(self):
        """View shopping list with items"""
        self.my_list.items.append('sugar')
        self.my_list.items.append('milk')
        self.my_list.items.append('coffee')
        self.assertEqual(self.my_list.view_shopping_list(),
                         ['sugar', 'milk', 'coffee'],
                         msg='Can not display list correctly')
