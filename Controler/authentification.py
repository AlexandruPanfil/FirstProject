import hashlib
# from View.work_interface import enter_interface
import sqlite3
# from View import work_interface
# from Controler.Database import



def authentification(user, password):
    password = hashlib.md5(password.encode()).hexdigest()
    with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
        cursor = db.cursor()

    cursor.execute("""SELECT user, pasword FROM Users""")
    for i in cursor.fetchall():
        # print(i)
        if user and password in i:
            # print("True")
            return True
    db.close()
    # print("False")
    return False

def add_to_db_Users(user=None, password=None):
    hash_password = hashlib.md5(password.encode()).hexdigest()
    with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM Users")
    for i in cursor.fetchall():
        if user in i[1]:
            print("User already exist")
            return False
    cursor.execute("""SELECT max(id) FROM Users""")
    max_id = cursor.fetchone()[0]
    new_id = 1 if max_id is None else max_id + 1
    cursor.execute("""INSERT INTO Users(id, user, pasword)
    VALUES(?,?,?)""", (new_id, user, hash_password))
    db.commit()
    db.close()
    return True


def show_users_from_db_Users():
    with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT user FROM Users")
    print(cursor.fetchall())
    return cursor.fetchall()

# TODO Logic of deleting users
def delete_from_db_Users(user):
    with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT user FROM Users")
    ...    #NOT FINISHED


