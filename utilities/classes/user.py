from utilities.db.db_manager import dbManager


class User:
    __first_name = None
    __last_name = None
    __email = None
    __password_user = None


    def __init__(self,first_name, last_name,email,password_user):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password_user = password_user

    def insert_user(self):
        query = "INSERT INTO users(first_name,last_name, email, password_user) VALUES ('%s','%s','%s', '%s')" % (self.__first_name, self.__last_name, self.__email
                                                                                                                 , self.__password_user)
        dbManager.commit(query)

    def get_name(self, email, password):
        query = "SELECT first_name, password_user FROM users WHERE email = '%s'" %(email)
        result = dbManager.fetch(query)
        if password == result[0][1]:
            return result[0][0]
        return ""

    def get_email(self, email):
        query = "SELECT email FROM users WHERE email = '%s'" %(email)
        result = dbManager.fetch(query)
        if result:
            return False
        else:
            return True

    def user_cart(self, user):
        query = "SELECT c.serial_number ,p.plate_name, p.price,c.price as self_price, p.hebrew_name, p.photo FROM  cart c join plates p on c.plate_name = p.plate_name  WHERE user = '%s'" %(user)
        cart = dbManager.fetch(query)
        return cart


    def user_final_price(self, user):
        query = "SELECT  (SUM(p.price)+SUM(c.price)) as total_price FROM cart c join plates p on c.plate_name = p.plate_name  WHERE user = '%s'" %(user)
        price = dbManager.fetch(query)
        return price[0][0]