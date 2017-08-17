class ShoppingList(object):
    """Class with methods for a shopping list"""

    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []

    def add_item_to_shopping_list(self, item):
        """add a single item to shopping list"""
        self.items.append(item)

    def delete_item_from_shopping_list(self, item):
        """Delete item form shopping list"""
        if len(self.items) > 0 and item in self.items:
            self.items.remove(item)
        else:
            raise ValueError

    def view_shopping_list(self):
        """View the entire list"""
        return self.items
