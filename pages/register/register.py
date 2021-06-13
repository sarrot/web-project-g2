from flask import Blueprint, render_template, request ,redirect ,flash, url_for
from utilities.db.db_manager import dbManager


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
    dbManager.insert_user(first_name,last_name,email,psw)
    # flash('user added to DB')
    return redirect(url_for('register.index'))

