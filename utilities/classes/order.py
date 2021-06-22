from utilities.db.db_manager import dbManager


class order:
    __user = None
    __address = None
    __supply_date = None
    __paid = None


    def __init__(self, user, address, supply_date, paid):
        self.__user = user
        self.__address = address
        self.__supply_date = supply_date
        self.__paid = paid


    def insert_to_order(self, user):
        query = "INSERT INTO orders(user) VALUES ('%s')" % (user)
        dbManager.commit(query)

    def update_order_details(self, user, address, date, paid):
        query = "UPDATE orders SET address='%s',supply_date='%s',paid='%s'  WHERE user = '%s'" % (address,date, paid, user)
        orders = dbManager.commit(query)
        return orders


