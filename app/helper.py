import sqlite3
from sqlite3 import Error

# status
PENDING = "pending"
COMPLETED = "completed"


def create_table():
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        conn.execute(
            "CREATE TABLE IF NOT EXISTS todo(ID INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, status TEXT NOT NULL)")
        conn.commit()
        return "success"

    except Error as e:
        print(e)
        return "error"
    finally:
        if conn:
            conn.close()


def add_task(item):
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo(item, status) VALUES(?,?)", (item, PENDING))
        conn.commit()
        return "success"
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def retrieve_rows():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("SELECT * from todo")
        rows = curs.fetchall()
        return rows
    except Error as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()

def retrieve_pending():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("SELECT * from todo WHERE status='pending'")
        rows = curs.fetchall()
        return rows
    except Error as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()

def delete_task(ID):
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute('DELETE FROM todo WHERE ID=?', [ID, ])
        curs.execute("COMMIT")
        return "success"
    except Error as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()


def update_status(ID, status):
    # check
    if (status.lower().strip() == 'pending'):
        status = PENDING
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None

    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute('UPDATE todo SET status=? WHERE ID=?', [status, ID])
        curs.execute("COMMIT")
        return "success"
    except Error as e:
        print(e)
        return None
    finally:
        if conn:
            conn.close()
