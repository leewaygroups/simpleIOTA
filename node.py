
from util import Util     
from wallet import Wallet
from transaction import Transaction

utils = Util()

class Node():
    def __init__(self, seed, *args):
        self.id = seed
        self.public_id
        self.wallets = {}
        self.tangle = self.sync_neighbour()

    def add_wallet(self):
        wallet_seed = utils.hash(str(self.seed)  + str(len(self.wallets)))
        self.wallets[wallet_seed] = Wallet(wallet_seed)
        return wallet_seed

    def make_transaction(self, wallet_id, receiver, value):
        '''
            1. Pick at least two transactions in Tangle to confirm
            2. Check picked transactions for conflict
            3. Approve non conflicting transactions
            4. Perform proof of work
            5. Send transaction to tangle 
        ''' 
        wallet = self.wallets[wallet_id] 
        if wallet != None:
            confirmed_transactions = self.confirm_transactions()
            proof_of_work = proof_of_work()

            if len(confirmed_transactions) > 2 and is_valid_pow(proof_of_work):
                new_transaction  = Transaction(
                    wallet.generate_address(), 
                    proof_of_work,
                    receiver,
                    value
                )
                return self.tangle.attach_transaction(new_transaction)

        return None
             
    def confirm_transactions(self):
        '''
            Even when a node is not making any transactions, it must participate 
            in confirming transactions in the network. A lazy node risks being dropped by its neighbour  
        '''
    
    def sync_neighbour(self):
        #TODO: search for neighbour and return a Tangle
        pass


        