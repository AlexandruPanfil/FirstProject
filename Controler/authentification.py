import hashlib
import sqlite3


def authentification():
    pass

def connect_db():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
    id integer PRIMARY KEY,
    user text NOT NULL, 
    pasword text NOT NULL, 
    admin text NOT NULL)""")
    db.close()

connect_db()
