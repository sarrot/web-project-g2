from utilities.db.db_manager import dbManager


class choosenPlate:
    __self_size = None
    __fruit1 = None
    __fruit2 = None
    __fruit3 = None
    __fruit4 = None
    __fruit5 = None
    __fruit6 = None
    __fruit7 = None
    __fruit8 = None
    __total_price = None
    __user = None


    def __init__(self, self_size, fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7, fruit8, total_price, user):
        __self_size = self_size
        __fruit1 = fruit1
        __fruit2 = fruit2
        __fruit3 = fruit3
        __fruit4 = fruit4
        __fruit5 = fruit5
        __fruit6 = fruit6
        __fruit7 = fruit7
        __fruit8 = fruit8
        __total_price = total_price
        __user = user


    def get_size_price(self, plate_size):
        query = "SELECT plate_price FROM base_plate WHERE plate_size= '%s'" % plate_size
        result = dbManager.fetch(query)
        return result[0][0]


    def get_fruit_price(self, fruit_name):
        query = "SELECT fruit_price FROM fruit WHERE fruit_name = '%s'" % (fruit_name)
        result = dbManager.fetch(query)
        print(result[0][0])
        return result[0][0]

    def get_square_plate(self):
        query = "SELECT * FROM base_plate WHERE type = '%s'" % ('square')
        result = dbManager.fetch(query)
        return result

    def get_circle_plate(self):
        query = "SELECT * FROM base_plate WHERE type = '%s'" % ('circle')
        result = dbManager.fetch(query)
        return result

    def get_fruit_regular(self):
        query = "SELECT * FROM fruit WHERE type = '%s'" % ('regular')
        result = dbManager.fetch(query)
        return result

    def insert_self_cart(self, price, email):
        query = "INSERT INTO cart(plate_name, price,hebrew_name, photo, user) VALUES ('%s','%s','%s','%s','%s')" % ('self_assembly', price, 'מגש בהרכבה עצמית', '/selfAssembly/media/self_assm.jpg', email)
        dbManager.commit(query)

    def insert_to_self_plate(self, email):
        query = "INSERT INTO self_plate(self_size, self_fruit1, self_fruit2, self_fruit3, self_fruit4, self_fruit5, self_fruit6, self_fruit7, self_fruit8, self_price, user) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s' )" % (self.__self_size, self.__fruit1, self.__fruit2, self.__fruit3, self.__fruit4, self.__fruit5, self.__fruit6, self.__fruit7, self.__fruit8, self.__total_price, self.__user)
        dbManager.commit(query)

