
import time
from threading import Timer

class Transaction():
    def __init__(self, sending_addr, receiving_addr, value, *args):
        
        # state 0: hidden, state 1: revealed
        self.state = 0
        self.weight = 1
        self.key = None
        self.pow = None
        self.time_stamp = time.time()
        self.tnx = {
            'sending_addr': sending_addr,
            'receiving_addr': receiving_addr,
            'value': value 
        }

        '''
            1. pre-transactions: A ref collection of transactions confirmed by the issuing node to 
            attach a new transaction to tangle

            2. post_transactions" A ref collection of post transactions that confirmed this transaction              
        '''
        self.pre_transactions = set()
        # self.post_transactions = set()
    
    def height(self):
        pass

    def cummulative_weight(self):
        pass

        