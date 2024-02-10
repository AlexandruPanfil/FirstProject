import hashlib
import sqlite3

def add_to_db_Users(tryis=1, user= None, password=None):
        hash_password = hashlib.md5(password.encode()).hexdigest()
        with sqlite3.connect("database.db") as db:
                cursor = db.cursor()
        cursor.execute("""SELECT max(id) FROM Users""")
        max_id = cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        for i in range(tryis):
                cursor.execute("""INSERT INTO Users(id, user, pasword)
                VALUES(?,?,?)""", (new_id, user, hash_password))
                # print(new_id, user, hash_password)

        db.commit()
        db.close()

def add_to_db_Products(name, price, quantity):
        with sqlite3.connect("database.db") as db:
                cursor = db.cursor()
        cursor.execute("SELECT max(id) FROM Products")
        max_id = cursor.fetchone()[0]
        print(max_id)
        new_id = 1 if max_id is None else max_id + 1
        print(new_id)
        cursor.execute("""INSERT INTO Products(id, name, price, quantity)
        VALUES(?,?,?,?)""", (new_id, name, price, quantity))

name_produs = "Mar"
pret_produs = 19.99
quantity_produs = 100

add_to_db_Products(name= name_produs, price=pret_produs, quantity=quantity_produs)