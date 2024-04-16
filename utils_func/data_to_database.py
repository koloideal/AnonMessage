import sqlite3
from sqlite3.dbapi2 import Connection, Cursor


def to_database(from_user_ip: str, to_user_username: str, date: str) -> None:

    connection: Connection = sqlite3.connect('secret_data/database.db')

    cursor: Cursor = connection.cursor()

    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS data_of_messages(from_user_ip TEXT, 
                                                to_user_username TEXT,
                                                datetime DATETIME)
    
    """)

    connection.commit()

    cursor.execute("""
    
    INSERT INTO data_of_messages VALUES (?, ?, ?)
    
    """, (from_user_ip, to_user_username, date))

    connection.commit()

    connection.close()
