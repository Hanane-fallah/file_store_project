from user.models import User
from core.manager import store_db
import datetime
from file.models import File
import logging


def signup():
    global user
    name = input("enter your name:")
    lastname = input("enter your lastname:")
    username = input("enter your username:")
    password = input("enter your password:")
    phonenumber = input("enter your phonenumber(optional):")
    user = User.user_assign(name, lastname, username, password, phonenumber)
    sub()


def login():
    global user
    username = input("enter your username:")
    password = input("enter your password:")
    user = User.user_login(username, password)
    if user:
        sub()


def sub():
    from routes import sub_router
    sub_router.generate()


def info():
    print(user)


def edit():
    username = input("enter your new username:")
    phonenumber = input("enter your new phone number:")
    User.edit_user(username, phonenumber)


def upload():
    p_id = store_db.create()
    file = input("enter file path:")
    upload_date = datetime.date.today()
    modify_date = datetime.date.today()
    show_name = input("enter show name of your file:")
    description = input("any description:")
    seller_id = input("enter your id:")
    user_id = (store_db.getid(User, "username", user[3]))[0][0]

    if user_id == seller_id:
        File(p_id, file, upload_date, modify_date, seller_id, show_name, description)
        logging.info("*** file uploaded ***")
    else:
        logging.error('wrong ID')


def shop():
    files = store_db.read(File, 'showname, description, id, file, comment')
    for file in files:
        print('-- ', file[0], ' : ', file[1], ' id ~>', file[2], 'comments : ', file[4])


def buy():
    p_id = input("enter file id:")
    for file in store_db.read(File, 'id, file'):
        if file[0] == p_id:
            logging.info("*** Purchase  Done ***")
            print(file[1])
    else:
        logging.error("file does not exists")


def comment(num):
    if num == 0:
        p_id = input("enter product id:")
        name = input("enter your name:")
        comment = name + " : " + input("type your comment")

    else:
        p_id = input("enter product id:")
        # cm = input("type your comment")
        comment = user[3] + ' : ' + input("type your comment")

    for file in store_db.read(File, 'id, comment'):
        print(file)
        if file[0] == p_id:
            qstring = "UPDATE products SET comment = array_append(comment ," + comment.__repr__() + ") where id = " + p_id.__repr__() + ";"
            store_db.cur.execute(qstring)
    
