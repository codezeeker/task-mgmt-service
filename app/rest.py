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
@app.route('/create', methods=['GET'])
def create_table():
    result = helper.create_table()
    return Response("{'result': '" + result + "'}", status=200, mimetype='application/json')

# Add item to list
@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body
    req = request.get_json()
    item = req['item']
    ##### example debugging statement below
    print(req)
    # Add to list
    result = helper.add_task(item)

    # error response
    if result is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
        return response

    return Response("{'result': '" + result + "'}", status=200, mimetype='application/json')


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
    ID = req_data['ID']

    res_data = helper.delete_task(ID)

    # Return error
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + ID + "}", status=400, mimetype='application/json')
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
