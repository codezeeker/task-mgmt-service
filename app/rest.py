import sqlite3
from flask import Flask, jsonify
from sqlite3 import Error

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


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

if __name__ == '__main__':
    app.run(debug=True)