import sqlite3
from flask import Flask, jsonify
from sqlite3 import Error

# status
PENDING = "pending"
COMPLETED = "completed"


def add_task(item):
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO todo(item, status) VALUES(?,?)", (item, PENDING))
        curs.execute("COMMIT")
        return {"item": item, "status": PENDING}
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
    finally:
        if conn:
            conn.close()

def delete_task(item):
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute('DELETE FROM todo WHERE item=?', (item,))
        curs.execute("COMMIT")
        return {'item': item}
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def update_status(item, status):
    #check
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
        curs.execute('update items set status=? where item=?', (status, item))
        curs.execute("COMMIT")
        return {item: status}
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()