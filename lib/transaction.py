
import time
from threading import Timer

class Transaction():
    def __init__(self, sender, receiver, value, *args):
        
        # state 0: hidden, state 1: revealed
        self.state = 0
        self.weight = 1
        self.pow = None
        self.key = None
        self.time_stamp = time.time()
        self.tnx = {
            'sender': sender,
            'receiver': receiver,
            'value': value 
        }

        '''
            1. pre-transactions: A ref collection of transactions confirmed by the issuing node to 
            attach a new transaction to tangle

            2. post_transactions" A ref collection of post transactions that confirmed this transaction              
        '''
        self.pre_transactions = set()
        # self.post_transactions = set()

        # switch transaction state to revealed after 50 secs.
        Timer(1, self.__reveal__, None)
    
    def height(self):
        pass

    def cummulative_weight(self):
        pass
    
    def __reveal__(self):
        transaction.state = 1
        print("Prince is here")

        