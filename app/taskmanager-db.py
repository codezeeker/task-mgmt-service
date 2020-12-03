import sqlite3

PENDING = "pending"

def create_tab():
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        conn.execute("CREATE TABLE IF NOT EXISTS todo(ID INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, status TEXT NOT NULL)")
        conn.commit()

    finally:
        if conn:
            conn.close()

while True:
    create_tab()
    break