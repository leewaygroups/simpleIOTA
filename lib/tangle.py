
import json
import hashlib, binascii
from lib.util import Util
from lib.transaction import Transaction

utils = Util()

class Tangle(object):
    def __init__(self, *args):
        self.DAG = {}     
        root_transaction = Transaction('0000', 'root', 25000000000)        
        self.attach_transaction(root_transaction, ['root'])
    
    def str_join(self, *args):
        return ''.join(map(str, args))

    def attach_transaction(self, transaction, confirmed_transactions):
        if self.is_valid_transaction(transaction):
            transaction.key = utils.hash(self.str_join([
                transaction.time_stamp, 
                transaction.pow, 
                transaction.tnx['sender'],
                transaction.tnx['receiver'],
                transaction.tnx['value'] 
            ]))
            
            for trans in confirmed_transactions:
                transaction.pre_transactions.add(trans)

            self.DAG[transaction.key] = transaction
            return transaction

        return {'msg': 'invalid transaction. Attachment failed'}
    
    def is_valid_transaction(self, transaction):
        # TODO: implement transaction validation logic
        return True
        
        
        
    