import sqlite3
import helper
import json
from flask import Flask, jsonify, request, Response
from sqlite3 import Error


app = Flask(__name__)


# default view
@app.route("/", methods=['GET'])
def hello():
    return jsonify({'message': 'Hello world!'})


# Create table
def create_tab():
    conn = None
    try:
        # conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect('mydatabase.db')
        conn.execute(
            "CREATE TABLE IF NOT EXISTS todo(ID INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, status TEXT NOT NULL)")
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
create_tab()


# Add item to list


@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req_data = request.get_json()
    new_item = req_data['item']

    # Add to list
    res_data = helper.add_task(item)

    # error response
    if res_data is None:
        response = Response("{'error': 'Item not added - " + new_item + "'}", status=400, mimetype='application/json')
        return response
    # return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


# Retrieve table
@app.route("/items/all", methods=['GET'])
def get_all_items():
    # Get items from the helper
    rows = helper.retrieve_rows()

    # Return response
    response = Response(json.dumps({'tasks': rows}), mimetype='application/json')
    return response


# Delete the task
@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    req_data = request.get_json()
    item = req_data['item']

    res_data = helper.delete_task(item)

    # Return error
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item + "}", status=400, mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


# Update task
@app.route('/item/update', methods=['PUT'])
def update_status():
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    res_data = helper.update_status(item, status)

    # Return error
    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item + ", " + status + "}", status=400,
                            mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(debug=True)
