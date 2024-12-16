import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection(testing=False):
    if testing:
        # In-memory SQLite database for testing purposes
        return sqlite3.connect(":memory:")
    else:
        # Connect to the real database
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        return conn
