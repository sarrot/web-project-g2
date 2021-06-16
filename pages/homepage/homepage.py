from flask import Blueprint, render_template, redirect, url_for, session, flash
from utilities.classes.plate import Plate


# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')



plate = Plate('a', 'a')
# Routes
@homepage.route('/homepage')
@homepage.route('/home')
@homepage.route('/')
def index():
    return render_template('homepage.html')


@homepage.route('/add_cart_family')
def add_to_cart_family():
    if session:
        plate = Plate('family', session['email'] )
        plate.insert_to_cart()
    else:
        flash("")
    return redirect(url_for('homepage.index'))

@homepage.route('/add_cart_double')
def add_to_cart2_double():
    if session:
        plate = Plate('double', session['email'])
        plate.insert_to_cart()
    return redirect(url_for('homepage.index'))

@homepage.route('/add_cart_exotic')
def add_to_cart_exotic():
    if session:
        plate = Plate('exotic', session['email'])
        plate.insert_to_cart()
    return redirect(url_for('homepage.index'))

@homepage.route('/add_cart_exciting')
def add_to_cart_exciting():
    if session:
        plate = Plate('exciting', session['email'])
        plate.insert_to_cart()
    return redirect(url_for('homepage.index'))

@homepage.route('/add_cart_hypnotist')
def add_to_cart_hypnotist():
    if session:
        plate = Plate('hypnotist', session['email'])
        plate.insert_to_cart()
    return redirect(url_for('homepage.index'))

@homepage.route('/add_cart_pampering')
def add_to_cart_pampering():
    if session:
        plate = Plate('pampering', session['email'])
        plate.insert_to_cart()
    return redirect(url_for('homepage.index'))


@homepage.route('/homepage/open_family')
def open_cart_family():
    return render_template('family.html')

@homepage.route('/homepage/open_double' )
def open_cart_double():
    return render_template('double.html')

@homepage.route('/homepage/open_exciting' )
def open_cart_exciting():
    return render_template('exciting.html')

@homepage.route('/homepage/open_exotic' )
def open_cart_exotic():
    return render_template('exotic.html')

@homepage.route('/homepage/open_hypnotist' )
def open_cart_hypnotist():
    return render_template('hypnotist.html')

@homepage.route('/homepage/open_pampering' )
def open_cart_pampering():
    return render_template('pampering.html')