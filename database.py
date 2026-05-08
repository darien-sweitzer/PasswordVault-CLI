# creating tables, inserting & retrieving passwords

import sqlite3
from encryption import encrypt_password, decrypt_password

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

def add_password(website, username, password):
    """
    Encrypts and stores a password entry.
    """

    encrypted_password = encrypt_password(password)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO passwords (website, username, password)
    VALUES (?, ?, ?)
    """, (website, username, encrypted_password))

    conn.commit()
    conn.close()


def get_passwords():
    """
    Retrieves and decrypts all stored passwords.
    """

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT website, username, password FROM passwords")

    rows = cursor.fetchall()

    conn.close()

    decrypted_rows = []

    for website, username, encrypted_password in rows:
        decrypted_password = decrypt_password(encrypted_password)

        decrypted_rows.append(
            (website, username, decrypted_password)
        )

    return decrypted_rows