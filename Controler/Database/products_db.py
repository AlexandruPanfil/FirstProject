import sqlite3

def add_to_db_Products(name, price, quantity, bar_code):
        with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
                cursor = db.cursor()
        cursor.execute("SELECT max(id) FROM Products")
        max_id = cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        # print(new_id, name, price, quantity, bar_code)
        cursor.execute("""INSERT INTO Products(id, name, price, quantity,  bar_code)
        VALUES(?,?,?,?,?)""", (new_id, name, price, quantity, bar_code))
        db.commit()
        db.close()

def get_from_db_Products(bar_code):
        with sqlite3.connect("D:\FirstProject\Controler\Database\database.db") as db:
                cursor = db.cursor()
        cursor.execute("""SELECT * FROM Products""")
        # print(cursor.fetchall())
        for i in cursor.fetchall():
                # print(i)
                if i[4] == bar_code:
                        # print(type(i[4]))
                        return i
        db.close()

add_to_db_Products("Discount 10", 10, 999, 999998)


