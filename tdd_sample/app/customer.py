"""
    1. Users create account
    2. Users can log in
    3. Users create, view, update and delete shopping lists. 
    4. Users can add, update, view or delete items in a shopping list

"""

from shopping_list import ShoppingList
from user import User
from flask import Flask, request, render_template
app = Flask(__name__)


def user_create_account(username, email, password):
    user = User(username, email, password)
    if users.__contains__(user.email):
        return "User already exists"
    users[user.email] = user


@app.route('/login', methods=['POST', 'GET'])
def user_login(email=None, password=None):
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        user = users.get(email, False)
        if user and user.login(email, password):
            return "User logged in"
        else:
            return "Invalid credentials or user does not exist"
    else:
        return render_template('login.html')


def user_create_shopping_list(user, name_of_shopping_list):
    user.create_shopping_list(name_of_shopping_list)


def user_view_shopping_lists(user):
    return user.view_shopping_lists()


def user_delete_shopping_list(user, name_of_shopping_list):
    try:
        user.delete_shopping_list(name_of_shopping_list)
    except ValueError:
        return "Shopping list not deleted"


def user_add_items_to_shopping_list(user, name_of_shopping_list, item):
    user.shopping_lists[name_of_shopping_list].add_item_to_shopping_list(item)


def user_view_shopping_list_items(user, name_of_shopping_list):
    return user.shopping_lists[name_of_shopping_list].view_shopping_list()


def delete_item_from_shopping_list(user, name_of_shopping_list, item):
    try:
        user.shopping_lists[name_of_shopping_list].delete_item_from_shopping_list(item)
    except ValueError:
        return "Item not deleted from shopping list"

if __name__ == '__main__':
    users = {}
    app.run(debug=True)
