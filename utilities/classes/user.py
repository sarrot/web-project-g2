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
        query = "INSERT INTO users(first_name,last_name, email, password_user) VALUES ('%s','%s','%s', '%s')" % (self.__first_name, self.__last_name, self.__email, self.__password_user)
        dbManager.commit(query)

    def get_name(self, email, password):
        query = "SELECT first_name, password_user FROM users WHERE email = '%s'" %(email)
        result = dbManager.fetch(query)
        if password == result[0][1]:
            return result[0][0]
        return ""

