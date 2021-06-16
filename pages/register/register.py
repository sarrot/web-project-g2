from flask import Blueprint, render_template, request ,redirect ,flash, url_for
from utilities.classes.user import User


# register blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')


# Routes
@register.route('/register')
def index():
    return render_template('register.html')

@register.route('/insert_user',methods=['POST'])
def insert():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    psw = request.form['psw']
    user = User(first_name,last_name,email, psw)
    user.insert_user()
    flash('(: נרשם בהצלחה ')
    register = "yes"
    return render_template('register.html', register= register)


