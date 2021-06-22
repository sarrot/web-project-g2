from flask import Blueprint, render_template, request, session, redirect,url_for ,flash
from utilities.classes.order import order
from utilities.classes.plate import Plate
# payment blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['post','get'])
def index():
    address = request.form['address']
    date = request.form['dateS']
    paid = 1
    order2 = order('a', 'a', 'a', 'FALSE')
    order2 = order2.update_order_details(session['email'], address, date, paid)
    flash('(: הזמנתך בוצעה בהצלחה')
    succcess = "yes"
    plate = Plate('a', 'a', 0)
    cart = plate.delet_from_cart(session['email'])
    return render_template('payment.html', order2=order2, succcess=succcess,cart=cart)



