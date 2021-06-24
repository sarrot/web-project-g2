from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.classes.plate import Plate
from utilities.classes.user import User
from utilities.classes.order import order

# shoppingcart blueprint definition
shoppingcart = Blueprint('shoppingcart', __name__, static_folder='static', static_url_path='/shoppingcart',
                         template_folder='templates')

user = User('a', 'a', 'a', 'a')


# Routes
@shoppingcart.route('/shoppingcart')
def index():
    if session:
        cart = user.user_cart(session['email'])
    else:
        cart = ""
    return render_template('shoppingcart.html', cart=cart)


@shoppingcart.route('/shoppingcart/<delete_cart>')
def delete(delete_cart):
    plate = Plate('a', 'a', 0)
    if session:
        plate.delet_cart(delete_cart, session['email'])
        cart = user.user_cart(session['email'])
    else:
        cart = ""
    return render_template('shoppingcart.html', cart=cart)



@shoppingcart.route('/shoppingcart/updatePrice', methods=['get', 'post'])
def updatePrice():
    price = 0
    cart = user.user_cart(session['email'])
    price = user.user_final_price(session['email'])
    return render_template('shoppingcart.html', price=price, cart=cart)


@shoppingcart.route('/shoppingcart/payment')
def payment():
    price = user.user_final_price(session['email'])
    if price:
        order2 = order('a', 'a', 'a', 'FALSE')
        order2 = order2.insert_to_order(session['email'])
        return render_template('payment.html')
    else:
        error = "יש להוסיף פריטים לסל"
        return render_template('shoppingcart.html', error=error)
