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
        return result[0][0]

    def get_square_plate(self):
        query = "SELECT * FROM base_plate WHERE type = '%s'" % ('square')
        result = dbManager.fetch(query)
        return result

    def get_circle_plate(self):
        query = "SELECT * FROM base_plate WHERE type = '%s'" % ('circle')
        result = dbManager.fetch(query)
        return result




