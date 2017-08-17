class Item(object):
    """Class for the Items in a shopping list"""
    def __init__(self, name, quantity, bought_from, status=None):
        self.name = name
        self.quantity = quantity
        self.bought_from = bought_from
        self.status = status

