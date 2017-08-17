import unittest
from app.customer import Application
from app.user import User


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.andela_app = Application()

    def test_user_create_account(self):
        self.andela_app.user_create_account('flavia', 'fmary@gmail.com',
                                            '0123456789')
        self.assertTrue(self.andela_app.users.__contains__('fmary@gmail.com'))

    def test_more_than_one_user_create_account(self):
        self.andela_app.user_create_account('flavia', 'fmary@gmail.com',
                                            '0123456789')
        self.andela_app.user_create_account('odette', 'oprincess@gmail.com',
                                            '12345682')
        self.andela_app.user_create_account('sammunan', 'smunan@gmail.com',
                                            'adbcnh')
        self.assertTrue(self.andela_app.users.__contains__('fmary@gmail.com'),
                        msg="User can not create account as first user")
        self.assertTrue(self.andela_app.users.__contains__(
                        'oprincess@gmail.com'), msg="User 2 can not create \
                        account")
        self.assertTrue(self.andela_app.users.__contains__('smunan@gmail.com'),
                        msg="User 3 can create account")

    def test_user_can_create_duplicate_account(self):
        self.andela_app.user_create_account('flavia', 'fmary@gmail.com',
                                            '0123456789')
        self.assertEqual(self.andela_app.user_create_account('flavia',
                         'fmary@gmail.com', '0123456789'),
                         "User already exists",
                         msg="User can create duplicate accounts")
                
    def test_non_user_login(self):
        self.assertEqual(self.andela_app.user_login('fmary@gmail.com',
                         '0123456789'), 'Invalid credentials or user does not exist')

    def test_existing_user_login(self):
        self.andela_app.users['fmary@gmail.com'] = User('flavia', 'fmary@gmail.com', '0123456789')
        self.assertEqual(self.andela_app.user_login('fmary@gmail.com', '0123456789'), 'User logged in')
