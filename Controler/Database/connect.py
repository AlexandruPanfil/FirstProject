import sqlite3

def connect_db():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    id integer PRIMARY KEY,
    user text NOT NULL, 
    pasword text NOT NULL, 
    admin text)""")
    db.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
    id integer PRIMARY KEY,
    name text NOT NULL,
    price real NOT NULL,
    quantity integer NOT NULL
    )""")
    db.commit()

    # cursor.execute("""SELECT user, pasword FROM Users """)
    # for i in cursor.fetchall():
    #     print(i)

    db.close()

connect_db()
