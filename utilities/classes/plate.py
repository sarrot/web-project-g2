from utilities.db.db_manager import dbManager


class Plate:
    __plate_name = None
    __price = None
    __photo = None
    __hebrew_name = None
    __user =None


    def __init__(self,plate_name, user,price):
        self.__plate_name = plate_name
        self.__user = user
        self.__price = price

    def insert_to_cart(self):
        query = "INSERT INTO cart(plate_name, user,price) VALUES ('%s','%s','%s')" % (self.__plate_name, self.__user, self.__price)
        dbManager.commit(query)

    def delet_from_cart(self,user):
        query = "DELETE FROM cart WHERE user = '%s';" % user
        dbManager.commit(query)


    def delet_cart(self, plate_delete, user):
        query = "DELETE FROM cart WHERE (serial_number , user)  = ('%s', '%s');" % (plate_delete, user)
        dbManager.commit(query)

    def get_plate_table(self):
        query = "SELECT * FROM plates where plate_name != 'self_assembly'"
        return dbManager.fetch(query)



