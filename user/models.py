import hashlib
import uuid
from core.manager import store_db
from core.models import DBModel
import logging


# todo: logging


class User(DBModel):
    TABLE = "Users"
    PK = "u_id"
    #  todo: add user to db

    def __init__(self, name, lastname, username, password, phone_number=None):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.phone_number = phone_number
        self.password = password
        self.id = uuid.uuid1()
        store_db.insert(User, '(u_id, u_name, lastname, username, user_password, phonenumber)', (str(self.id), self.name, self.lastname, self.username, self.password, self.phone_number))
        logging.info(f"**user {self.username} with user id {self.id} created**")

    @staticmethod
    def encode_password(password):
        # encrypting password for more security
        password = password.encode('utf-8')
        return hashlib.md5(password).hexdigest()

    @staticmethod
    def check_password(password):
        # password must be at least 4 characters
        if len(password) > 3:
            return True
        else:
            logging.error("--invalid password--")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if User.check_password(password):
            self.__password = User.encode_password(password)

    @staticmethod
    def check_username(username):
        if len(username) != 0:
            for usr in store_db.read(User, "username"):
                if username == usr[0]:
                    logging.error("--invalid username--")
                    return False
            else:
                return True

    @classmethod
    def user_assign(cls, name, lastname, username, password, phone_number=None):
        if User.check_password(password) and User.check_username(username):
            return cls(name, lastname, username, password, phone_number)

    def edit_user(self, username, phonenumber):
        if User.check_username(username):
            self.username = username
            self.phone_number = phonenumber
            print(self)
        else:
            print("user name taken!")

    def change_password(self, prepass, newpass):
        if User.encode_password(prepass) == self.__password and User.check_password(newpass):
            self.__password = User.encode_password(newpass)
            print("**password changed successfully**")
        else:
            print("--try again--")

    @staticmethod
    def user_login(username:str, password:str):
        # first check user exist
        for usr in store_db.read(User):
            if username == usr[3]:
                logging.debug("valid username")
                # last check password
                if User.encode_password(password) == usr[4]:
                    logging.info("**login successfully**")
                    return usr
                else:
                    logging.error("--wrong password--")
        else:
            logging.error("--user does not exist--")

    def __str__(self):
        return f"user info ~> id = -{self.id}- username = -{self.username}- phone number = -{self.phone_number}-"

    def __repr__(self):
        return f"id: {self.id} username: {self.username}"
