from shopping_list import ShoppingList


flavia_list = ShoppingList()  # create shopping list
print('Shopping list created: {}'.format(flavia_list.view_shopping_list()))
flavia_list.add_item_to_shopping_list('milk')  # add first item to the shopping list
print('Item added to shopping list: {}'.format(flavia_list.view_shopping_list()))
flavia_list.add_item_to_shopping_list('coffee')  # update shopping list
print('Shopping list updated: {}'.format(flavia_list.view_shopping_list()))
flavia_list.add_item_to_shopping_list('sugar')  # update shopping list
print('Shopping list updated: {}'.format(flavia_list.view_shopping_list()))
flavia_list.delete_item_from_shopping_list('coffee')  # delete item from shopping list
print('Item deleted from the list: {}'.format(flavia_list.view_shopping_list()))
