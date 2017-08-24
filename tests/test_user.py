import unittest
from app.user import User

class TestUser(unittest.TestCase):
    """Tests for the User class"""
    def setUp(self):
        self.flavia = User('fnshemerirwe', 'fnshemerirwe@gmail.com',
                           '1234567890')

    def test_login_with_correct_credentials(self):
        """User can login with correct credentails correct"""
        self.assertTrue(self.flavia.login('fnshemerirwe@gmail.com',
                        '1234567890'))

    def test_login_with_incorrect_email_correct_password(self):
        """User login is rejected  with incorrect email."""
        self.assertFalse(self.flavia.login('flagh@gdjj.com', '1234567890'), msg="User\
         can login with incorrect email")

    def test_login_with_correct_email_incorrect_password(self):
        """User login is rejected is rejected with incorrect password"""
        self.assertFalse(self.flavia.login('fnshemerirwe@gmail.com', '5236912'), msg="User\
        can login with incorrect password")

    def test_login_with_incorrect_credentials(self):
        """User login is rejected is rejected with incorrect credentials"""
        self.assertFalse(self.flavia.login('fnsheme@gmail.com', '5236912'), msg="User\
        can login with incorrect credentials")

    def test_create_shopping_list(self):
        """User can create a shopping list"""
        self.flavia.create_shopping_list('monday')
        self.assertEqual(self.flavia.shopping_lists, ['monday'], msg="User can not \
        create a new shopping list")

    def test_create_shopping_list_with_non_empty_shopping_lists(self):
        """User can create shopping lists even with extising shopping lists"""
        self.flavia.shopping_lists.append('monday')
        self.flavia.shopping_lists.append('tuesday')
        self.flavia.create_shopping_list('wednesday')
        self.assertEqual(self.flavia.shopping_lists, ['monday', 'tuesday',
                         'wednesday'], msg="User can not create a new shopping \
                         list after creating a previous one")

    def test_delete_shopping_list_from_empty_shopping_lists(self):
        """User can not delete shopping list without creating any shopping list"""
        self.assertRaises(ValueError, self.flavia.delete_shopping_list,
                          'monday')

    def test_delete_shopping_list_from_shopping_lists(self):
        """User can delete any created shopping list"""
        self.flavia.shopping_lists.append('monday')
        self.flavia.shopping_lists.append('tuesday')
        self.flavia.delete_shopping_list('monday')
        self.assertEqual(self.flavia.shopping_lists, ['tuesday'], msg="User can not delete a shopping list \
                         that is in shopping list")

    def test_delete_non_existing_shopping_list_from_shopping_lists(self):
        """User can not delete a shoping list he did not create"""
        self.flavia.shopping_lists.append('monday')
        self.flavia.shopping_lists.append('tuesday')
        self.assertRaises(ValueError, self.flavia.delete_shopping_list,
                          'wednesday')

    def test_view_empty_shopping_lists(self):
        """User View empty shopping lists"""
        self.assertEqual(self.flavia.view_shopping_lists(), [],
                         msg="Can not display empty shopping list")

    def test_view_shopping_lists_created(self):
        """User can view all shopping lists created"""
        self.flavia.shopping_lists.append('monday')
        self.flavia.shopping_lists.append('tuesday')
        self.flavia.shopping_lists.append('wednesday')
        self.flavia.shopping_lists.append('thursday')
        self.assertEqual(self.flavia.view_shopping_lists(),
                         ['monday', 'tuesday', 'wednesday', 'thursday'],
                         msg='Can not display shopping lists correctly')


