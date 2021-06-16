from flask import Blueprint, render_template, request, redirect, url_for, session
from utilities.classes.plate import Plate
from utilities.classes.user import User

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
        cart=""
    return render_template('shoppingcart.html', cart=cart)


@shoppingcart.route('/shoppingcart/<delete_cart>')
def delete(delete_cart):
    plate = Plate('a', 'a')
    if session:
        plate.delet_cart(delete_cart, session['email'])
        cart = user.user_cart(session['email'])
    else:
        cart = ""
    return render_template('shoppingcart.html', cart=cart)


@shoppingcart.route('/shoppingcart/updateAmount/<plate_name>')
def updateAmount(plate_name):
    value = request.form['value']
    Plate.update_quantity(value, plate_name)
    return render_template('shoppingcart.html')


@shoppingcart.route('/shoppingcart/updatePrice', methods=['get', 'post'])
def updatePrice():
    amounts = request.form.get('value')
    price = 0
    cart = user.user_cart(session['email'])
    price = user.user_final_price(session['email'])
    return render_template('shoppingcart.html', price=price, cart=cart, amounts=amounts)


@shoppingcart.route('/shoppingcart/payment')
def payment():
    return redirect(url_for('payment.index'))
