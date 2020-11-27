import sqlite3
from flask import Flask, jsonify
from sqlite3 import Error

def add_task(item):
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("INSERT INTO todo(item) VALUES(?)", ["item"])
        curs.execute("COMMIT")
        return {"item": item}
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
        print(rows)
        return jsonify({'tasks': rows})
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def delete_task(item):
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute('DELETE FROM todo WHERE item=?', (item,))
        conn.commit()
        return {'item': item}
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()