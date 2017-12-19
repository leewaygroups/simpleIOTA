
#import requests
from uuid import uuid4
from flask import Flask, jsonify, request

# custom classes
from node import Node
from tangle import Tangle


# Instantiate our Node
app = Flask(__name__)

''' 
    1. Generate a globally unique identifier for this node 
    2. Pass the identify to the node constructor to create a node instance
'''
node_key = str(uuid4()).replace('-', '')
_node = Node(node_key)

# Instantiate Tangle
tangle = Tangle()

@app.route('/node/register', methods=['POST'])
def register_new_node():
    values = request.get_json()
    return jsonify(values), 201
  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = { }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)