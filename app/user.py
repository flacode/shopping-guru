class User(object):
    """Class for user attributes and methods"""
    def __init__(self, username, email, password, shopping_lists=None):
        self.username = username
        self.email = email
        self.password = password
        self.shopping_lists = shopping_lists or []

    def login(self, email, password):
        """Method to handle user login"""
        if email == self.email and password == self.password:
            return True
        else:
            return False

    def create_shopping_list(self, shopping_list):
        """Method to create shopping list"""
        self.shopping_lists.append(shopping_list)

    def delete_shopping_list(self, shopping_list):
        """Method to delete shopping list"""
        self.shopping_lists.remove(shopping_list)

    def view_shopping_lists(self):
        """Method to view shopping lists"""
        return self.shopping_lists

