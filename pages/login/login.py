from flask import Blueprint, render_template, request, session, url_for, redirect, flash
from utilities.classes.user import User

# login blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


# Routes
@login.route('/login')
def index():
    return render_template('login.html')


@login.route('/connect',methods= ['POST'])
def connect():

    email = request.form['email']
    password = request.form['psw']
    user = User('a', 'a', 'a','a')  # no need to create new user
    first_name = user.get_name(email, password) # check if it's the correct password
    print(first_name)
    session['userName'] = first_name  # return user name from DB
    if first_name == "":
        flash('נכשל בהתחברות, בבקשה נסה שוב')
        return redirect('/login')
    return redirect('/')




@login.route('/logout')
def logout():
        session.pop('userName', None)
        return redirect(url_for('homepage.index'))

