from flask import render_template, Blueprint, request, redirect, flash, session
from utilities.classes.choosenPlate import choosenPlate
from utilities.classes.plate import Plate

# selfAssembly blueprint definition
selfAssembly = Blueprint('selfAssembly', __name__, static_folder='static', static_url_path='/selfAssembly',
                         template_folder='templates')

# Routes
@selfAssembly.route('/selfAssembly')
def index():
    choosenplate = choosenPlate('a','a','a','a','a','a','a','a','a','a','a')
    base_plate_square = choosenplate.get_square_plate()
    base_plate_circle=choosenplate.get_circle_plate()
    # fruit_regular = choosenplate.get_fruit_regular()
    return render_template('selfAssembly.html', base_plate_square = base_plate_square, base_plate_circle=base_plate_circle )


@selfAssembly.route('/insert_self_to_cart/<final_price>/<fruit_list>')
def insert_self_to_cart(final_price, fruit_list):
    if session:
        choosenplate = choosenPlate('a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
        base_plate_square = choosenplate.get_square_plate()
        base_plate_circle = choosenplate.get_circle_plate()
        plate = Plate('self_assembly', session['email'],final_price)
        plate.insert_to_cart()
    else:
        flash("")

    return render_template('selfAssembly.html', base_plate_square = base_plate_square, base_plate_circle=base_plate_circle)


@selfAssembly.route('/calcPrice', methods=['get', 'post'])
def calcPrice():
    self_size = request.args.getlist('size')
    choosenplate = choosenPlate('a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
    if self_size:
        fruits = request.args.getlist('fruits')
        if fruits and len(fruits) < 9 :
            fruit_list = self_size
            fruits_price = 0
            for fr in fruits:
                fruit_list.append(fr)
                if len(fruit_list) <= len(fruits) + 1 :
                     fruits_price += choosenplate.get_fruit_price(fruit_list[len(fruit_list) - 1])  ##get fruits price

            while (len(fruit_list) < 9):
                fruit_list.append('0')

            size_price = choosenplate.get_size_price(self_size[0])  # get the base price for the plate
            final_price = size_price + fruits_price
            fruit_list.append(final_price)
            error =""
        else:
            error = "יש לבחור עד שמונה פירות"
            final_price = ""
            fruit_list = ""
    else:
        error = "בבקשה בחר מגש"
        final_price =""
        fruit_list =""
    base_plate_square = choosenplate.get_square_plate()
    base_plate_circle = choosenplate.get_circle_plate()
    return render_template('selfAssembly.html', final_price=final_price, base_plate_square = base_plate_square, base_plate_circle=base_plate_circle,fruit_list=fruit_list, error=error )
