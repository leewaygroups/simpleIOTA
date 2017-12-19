
import json
import hashlib, binascii
from transaction import Transaction


class Tangle(object):
    def __init__(self, *args):
        root_transaction = Transaction('0000', 'root', 25000000000)

        self.DAG = {}
        self.attach_transaction(root_transaction)
    
    def hash(transaction_string):
        return hashlib.sha256(transaction_string.encode()).hexdigest()
    
    def str_join(self, *args):
        return ''.join(map(str, args))

    def attach_transaction(self, transaction):
        if self.is_valid_transaction(transaction):
            transaction.key = hash(self.str_join([
                transaction.time_stamp, 
                transaction.pow, 
                transaction.tnx['sender'],
                transaction.tnx['receiver'],
                transaction.tnx['value'] 
            ]))
            self.DAG[transaction.key] = transaction
            return transaction

        return {'msg': 'invalid transaction. Attachment failed'}
    
    def is_valid_transaction(self, transaction):
        # TODO: implement transaction validation logic
        return True
        
        
        
    