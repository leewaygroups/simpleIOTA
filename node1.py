
import sys

#import requests
from uuid import uuid4
from flask import Flask, jsonify, request

# custom classes
from lib.node import Node
from lib.tangle import Tangle
from lib.wallet import Wallet
from lib.util import Util


# Instantiate our Node
# Instantiate Tangle
app = Flask(__name__)
utils = Util()

node = Node(utils.unique_gen())

@app.route('/node/register_neighbours', methods=['POST'])
def register_new_node():
    response = node.register_neighbours(request.get_json())
    return jsonify(response), 201

@app.route('/transactions/new', methods=['POST'])
def make_transaction():
    response = node.make_transaction(request.get_json())
    return jsonify(response), 201

@app.route('/wallet/balance', methods=['POST'])
def wallet_balance():
    return "wallets and balances of this node"

@app.route('/dag', methods=['GET'])
def full_chain():
    response = { }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001)