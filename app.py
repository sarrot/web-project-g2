from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## contact
from pages.contact.contact import contact
app.register_blueprint(contact)

## login
from pages.login.login import login
app.register_blueprint(login)

## selfAssembly
from pages.selfAssembly.selfAssembly import selfAssembly
app.register_blueprint(selfAssembly)

## register
from pages.register.register import register
app.register_blueprint(register)

## shoppingcart
from pages.shoppingcart.shoppingcart import shoppingcart
app.register_blueprint(shoppingcart)

## payment
from pages.payment.payment import payment
app.register_blueprint(payment)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
