"""
    1. Users create account
    2. Users can log in
    3. Users create, view, update and delete shopping lists.
    4. Users can add, update, view or delete items in a shopping list

"""

from flask import Flask, request, render_template, redirect, url_for, session
from user import User
from item import Item
from shopping_list import ShoppingList
app = Flask(__name__)
app.secret_key = 'abcdefghijklmn'
users = {}  # user[email]=user_object1


@app.route('/', methods=['POST', 'GET'])
def index():
    if 'email' in session:
        username = users[session['email']].username
        return redirect(url_for('user_view_shopping_lists',
                        loggedin_user=username))
    return redirect(url_for('user_create_account'))


@app.route('/register', methods=['POST', 'GET'])
def user_create_account(username=None, email=None, password=None):
    """Method for a user to register for an account"""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            if users.__contains__(email):
                print(users.keys())
                return render_template("registration.html",
                                       error_msg="User already exists")
            else:
                register_user = User(username, email, password)
                users[register_user.email] = register_user
                return redirect(url_for('user_login'))
        else:
            return render_template("registration.html",
                                   error_msg="Passwords do not match")
    return render_template('registration.html')


@app.route('/login', methods=['POST', 'GET'])
def user_login(email=None, password=None):
    """Method for a registered user to login"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        user_to_login = users.get(email, False)
        if user_to_login and user_to_login.login(email, password):
            session['email'] = email
            username = user_to_login.username
            return redirect(url_for('user_view_shopping_lists',
                            loggedin_user=username))
        else:
            return render_template("login.html",
                                   error_msg="Invalid credentials or user does \
                                   not exist")
    return render_template('login.html')


@app.route('/<loggedin_user>/shoppinglists')
def user_view_shopping_lists(loggedin_user):
    """Method to view user's shopping list"""
    if 'email' in session:
        user = users[session['email']]
        shopping_lists = user.view_shopping_lists()
        return render_template('view_shopping_lists.html',
                               shopping_lists=shopping_lists,
                               username=user.username, num=len(shopping_lists))
    return render_template('login.html')


@app.route('/<loggedin_user>/create', methods=['POST', 'GET'])
def user_create_shopping_list(loggedin_user):
    """Method for user to create shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    if request.method == 'POST':
        name = request.form['list_name']
        shopping_list = ShoppingList(name)
        user.create_shopping_list(shopping_list)
        return redirect(url_for('user_add_items_to_shopping_list',
                                num=len(user.shopping_lists)-1))
    return render_template('add_shopping_list.html', username=user.username)


@app.route('/<loggedin_user>/update/<list_no>', methods=['POST', 'GET'])
def user_update_shopping_list(loggedin_user, list_no):
    """Method for user to update shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    if request.method == 'POST':
        name = request.form['list_name']
        user.shopping_lists[int(list_no)].name = name
        return redirect(url_for('user_view_shopping_lists',
                                loggedin_user=user.username))
    return render_template('update_shopping_list.html',
                           username=user.username,
                           list_name=user.shopping_lists[int(list_no)].name)


@app.route('/shoppinglist/<num>', methods=['POST', 'GET'])
def user_add_items_to_shopping_list(num):
    """Method for user to add items to shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    if request.method == 'POST':
        item = request.form['item']
        qty = request.form['qty']
        user.shopping_lists[int(num)].add_item_to_shopping_list(Item(item, qty)
                                                                )
        return redirect(url_for('user_view_shopping_list_items',
                                num=num))
    return render_template('add_items.html', username=user.username)


@app.route('/shoppinglist/<num>/item/<item_id>/update',
           methods=['POST', 'GET'])
def user_update_items_in_shopping_list(num, item_id):
    """Method for user to add items to shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    shopping_list = user.shopping_lists[int(num)]
    item = shopping_list.items[int(item_id)]
    if request.method == 'POST':
        update_item = request.form['item']
        update_qty = request.form['qty']
        item.name = update_item
        item.quantity = update_qty
        return redirect(url_for('user_view_shopping_list_items',
                        num=num))
    return render_template('update_items.html',
                           username=user.username,
                           item=item.name,
                           quantity=item.quantity
                           )


@app.route('/<num>/delete')
def user_delete_shopping_list(num):
    """User can delete shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    try:
        user = users[session['email']]
        shopping_list = user.shopping_lists[int(num)]
        user.delete_shopping_list(shopping_list)
        return redirect(url_for('user_view_shopping_lists',
                        loggedin_user=user.username))
    except ValueError:
        return redirect(url_for('user_view_shopping_lists',
                        loggedin_user=user.username))


@app.route('/shoppinglist/items/<num>/')
def user_view_shopping_list_items(num):
    """Method to view items in shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    user = users[session['email']]
    items = user.shopping_lists[int(num)].view_shopping_list()
    return render_template('shopping_list.html', items=items,
                           shopping_list=user.shopping_lists[int(num)].name,
                           no_items=len(items), list_index=num,
                           username=user.username)


@app.route('/<list_index>/<item_index>/delete')
def delete_item_from_shopping_list(list_index, item_index):
    """User can delete item from shopping list"""
    if 'email' not in session:
        return render_template('login.html')
    try:
        user = users[session['email']]
        shopping_list = user.shopping_lists[int(list_index)]
        item = shopping_list.items[int(item_index)]
        shopping_list.delete_item_from_shopping_list(item)
        return redirect(url_for('user_view_shopping_list_items',
                                num=list_index))
    except ValueError:
        return redirect(url_for('user_view_shopping_list_items',
                                num=list_index))


@app.route('/logout')
def logout():
    """ remove the username from the session if it is there """
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
