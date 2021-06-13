from flask import Blueprint, render_template

# shoppingcart blueprint definition
shoppingcart = Blueprint('shoppingcart', __name__, static_folder='static', static_url_path='/shoppingcart', template_folder='templates')


# Routes
@shoppingcart.route('/shoppingcart')
def index():
    return render_template('shoppingcart.html')
