
from random import randint
from lib.util import Util     
from lib.wallet import Wallet
from lib.transaction import Transaction
from lib.tangle import Tangle

utils = Util()

class Node():
    def __init__(self, seed, *args):
        self.seed = seed
        self.wallet = Wallet(utils.hash(str(self.seed)))
        self.neighbours = set()
        self.tangle = Tangle()

    def proof_of_work(self, str_input):
        proof = 0
        while self.is_valid_proof(str_input, proof) is False:
            proof +=1
        return proof

    def is_valid_proof(self, str_input, proof):
        result = utils.hash(str_input + str(proof))
        return result.count("00") >= 2 and result[-4:]=="0000"        

    def select_tips(self):
        available_transactions = []
        selected_transactions = []

        for key in self.tangle.DAG:
            _transaction = self.tangle.DAG[key]
            if _transaction.status == 1:
                available_transactions.append(_transaction)

        for i in range(2):
            selected_transactions.append(available_transactions[randint(0, len(available_transactions)-1)]['key'])

        return selected_transactions
    
    def make_transaction(self, receiver_addr, value):
        '''
            1. Pick at least two transactions in Tangle to confirm
            2. Check picked transactions for conflict
            3. Approve non conflicting transactions
            4. Perform proof of work
            5. Send transaction to tangle 
        ''' 
        confirmed_transactions = self.confirm_transactions()
        proof_of_work = proof_of_work(''.join(confirmed_transactions))

        if len(confirmed_transactions) >= 2:
            new_transaction  = Transaction(
                self.wallet.generate_address(),
                receiver_addr,
                proof_of_work,                   
                value
            )
            return self.tangle.attach_transaction(new_transaction, confirmed_transactions)

        return None

    def confirm_transactions(self):
        '''
            Even when a node is not making any transactions, it must participate 
            in confirming transactions in the network. A lazy node risks being dropped by its neighbour 

            Different approches to picking transactions to confirm>
            1. Randomly pick any N visible transactions 

            2. Pick r.N/n transactions. 
            r=rate of new transaction attachment to Tangle. 
            N=number of visible transactions.
            n=number of neighbour nodes.

            we will pick the naive one. 
            TODO: check the validity of the PoW of selected transactions
        '''

        ''' 
            Select tips and assume the transactions are non-conflicting.             
        '''

        return self.select_tips()
        



    
    def sync_neighbour(self):
        #TODO: search for neighbour and return a Tangle
        pass

    def register_neighbours(self, neighbours):
        for ip in neighbours:
            self.neighbours.add(neighbours[ip])
        return None;
        


        