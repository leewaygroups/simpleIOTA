
from lib.util import Util

utils = Util()

class Wallet():
    def __init__(self, seed):
        self.seed = seed
        self.addresses = {}
    
    def generate_address(self):
        address = utils.hash(str(self.seed)  + str(len(self.addresses)))
        self.addresses[address] = 0
        return address