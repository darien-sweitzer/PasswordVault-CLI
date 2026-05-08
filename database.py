# creating tables, inserting & retrieving passwords

import sqlite3

DB_NAME = 'passwords.db'

def connect_db():
    # connects to the SQLite database
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():

    # creates the passwords table if it doesn't exist
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
