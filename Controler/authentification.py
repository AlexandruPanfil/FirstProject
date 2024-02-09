import hashlib
# from View.work_interface import enter_interface
import sqlite3
from View import work_interface
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
