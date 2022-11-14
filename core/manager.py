import psycopg2
import psycopg2.extras
from core.models import DBModel
from psycopg2._psycopg import connection, cursor
import uuid
import logging

logging.basicConfig(
    level=logging.DEBUG,  # set logging level debug to check functions work
    format="{asctime} -{name:<10} -{levelname:<16} -{message}", style="{",
    handlers=[
        logging.FileHandler("database.log"),  # log file
        logging.StreamHandler()
    ]
)

DB_CONNECTION = {
    "user": "postgres",
    "password": "hana7988",
    "host": "localhost",
    "port": "5432",
    "database": "store_database"
}


class DBManager:
    HOST = DB_CONNECTION["host"]
    USER = DB_CONNECTION["user"]
    PORT = DB_CONNECTION["port"]
    PASSWORD = DB_CONNECTION["password"]

    def __init__(self, database, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password

        self.conn: connection = \
            psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port, password=password)
        self.conn.autocommit = True
        self.cur = self.__get_cursor()
        logging.debug(f"{self.database} connected")

    def __del__(self):
        self.conn.close()  # Close the connection on delete
        logging.debug("connection closed")
        self.__get_cursor().close()
        logging.debug("cursur closed")

    def __get_cursor(self) -> cursor:
        return self.conn.cursor()


    @staticmethod
    def create() -> int:
        """
            make id for created model instance from table
        """
        return uuid.uuid1().int

    def read(self, model_instance: DBModel, col="*") -> DBModel:  # get
        """
            returns all instances of the model , attributes can be specified in 'col' arg
        """
        qstring = 'SELECT ' + col + ' from ' + model_instance.TABLE + ';'
        self.cur.execute(qstring)
        return self.cur.fetchall()

    def insert(self, model_instance: DBModel, args, vals) -> None:
        """
            update instance in db table by get all model_instance attrs
        """
        qstring = "INSERT INTO " + model_instance.TABLE + args + " VALUES (" + "%s, "*(len(args.split(","))-1) + "%s)"
        self.cur.execute(qstring, vals)

    def getid(self, model_instance: DBModel, arg, val):
        """
            get instance info with search in attributes
        """
        qstring = "select * from " + model_instance.TABLE + " where " + arg + " = '" + val + "'"
        self.cur.execute(qstring)
        return self.cur.fetchall()

    def delete(self, model_instance: DBModel) -> None:
        """
            delete instance method
        """

    def update(self):
        """
            update instance attributes
        """



store_db = DBManager("store_database")
