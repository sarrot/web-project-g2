from utilities.db.db_manager import dbManager


class Plate:
    __plate_name = None
    __price = None
    __photo = None
    __hebrew_name = None
    __user =None


    def __init__(self,plate_name, user):
        self.__plate_name = plate_name
        # self.__price = price
        # self.__photo = photo
        # self.__hebrew_name = hebrew_name
        self.__user = user

    def insert_to_cart(self):
        query = "INSERT INTO cart(plate_name, user) VALUES ('%s','%s')" % (self.__plate_name, self.__user)
        dbManager.commit(query)

    def delet_from_cart(self):
        query = "DELETE FROM cart WHERE plate_name = '%s';" % self.__plate_name
        dbManager.commit(query)

    def update_quantity(self, quantity, plate_name):
        query = "UPDATE cart SET quantity= '%s' WHERE plate_name = '%s'" % (quantity, plate_name)
        dbManager.commit(query)

    def get_plate_name(self):
        query = "SELECT * FROM cart WHERE plate_name = '%s'" % (self.__plate_name)
        return dbManager.fetch(query)

    def get_cart_table(self):
        query = "SELECT * FROM cart"
        query_result = dbManager.fetch(query)
        return query_result

    def delet_cart(self, plate_delete, user):
        query = "DELETE FROM cart WHERE (plate_name , user)  = ('%s', '%s');" % (plate_delete, user)
        dbManager.commit(query)

    def get_plate_table(self):
        query = "SELECT * FROM plates "
        return dbManager.fetch(query)


