import sqlite3
from flask import Flask, jsonify
from sqlite3 import Error

app = Flask(__name__)


#test
@app.route("/", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})



# Create table
@app.route("/view", methods=['GET'])
def create_db():
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS todo (item TEXT)")
        curs.execute("INSERT INTO todo(item) VALUES(?)", [])
        curs.execute("COMMIT")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



# Retrieve table
@app.route("/view", methods=['GET'])
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


# Update the table
@app.route("/new", methods=['GET'])
def update_task():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("")
        return jsonify({'tasks': rows})
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Delete the task based on index
@app.route("/new", methods=['GET'])
def delete_task():
    conn = None
    try:
        conn = sqlite3.connect('mydatabase.db')
        curs = conn.cursor()
        curs.execute("")
        return jsonify({'tasks': rows})
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



if __name__ == '__main__':
    app.run(debug=True)