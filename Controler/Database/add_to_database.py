import hashlib
import sqlite3

def add_to_db_Users(user= None, password=None):
        hash_password = hashlib.md5(password.encode()).hexdigest()
        with sqlite3.connect("database.db") as db:
                cursor = db.cursor()
        cursor.execute("""SELECT max(id) FROM Users""")
        max_id = cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        cursor.execute("""INSERT INTO Users(id, user, pasword)
        VALUES(?,?,?)""", (new_id, user, hash_password))
        db.commit()
        db.close()

def add_to_db_Products(name, price, quantity):
        with sqlite3.connect("database.db") as db:
                cursor = db.cursor()
        cursor.execute("SELECT max(id) FROM Products")
        max_id = cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        cursor.execute("""INSERT INTO Products(id, name, price, quantity)
        VALUES(?,?,?,?)""", (new_id, name, price, quantity))
        db.commit()
        db.close()

def get_from_db_Products():
        with sqlite3.connect("database.db") as db:
                cursor = db.cursor()
        cursor.execute("""SELECT * FROM Products""")
        # print(cursor.fetchall())
        for i in cursor.fetchall():
                print(i)
        db.close()



