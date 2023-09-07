 
import hashlib  
import json  
from time import time  
  

class Block_chain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
  
        self.newBlock(previousHash = "set of people who owned the following product", the_proof = 100)  
  
    def newBlock(self, the_proof, previousHash = None):  
        the_block = { 
             
            'index': len(self.chain) + 1,  
            'timestamp': time(),  
            'transactions': self.pendingTransactions,  
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        self.pendingTransactions = []  
        self.chain.append(the_block)  
  
        return the_block  
  

    @property  
    def lastBlock(self):  
   
        return self.chain[-1]  
  

    def newTransaction(self, the_sender, the_recipient, the_amount):  
        the_transaction = {  
            'prev owner': the_sender,  
            'current owner': the_recipient,  
            'proof': the_amount  
        }  
        self.pendingTransactions.append(the_transaction)  
        return self.lastBlock['index'] + 1  
  
    def hash(self, the_block):  
        stringObject = json.dumps(the_block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        rawHash = hashlib.sha256(blockString)  
        hexHash = rawHash.hexdigest()  
  
        return hexHash  
  
block_chain = Block_chain() 
print(" \n")
transaction1 = block_chain.newTransaction("Satoshi", "Alex", '10 BTC')
print(" \n")
transaction2 = block_chain.newTransaction("Alex", "Satoshi", '2 BTC')  
print(" \n")
transaction3 = block_chain.newTransaction("Satoshi", "James", '10 BTC')  
print(" \n")
block_chain.newBlock(10123)  
print(" \n")
  
transaction4 = block_chain.newTransaction("Alex", "Lucy", '2 BTC')  
print(" \n")
transaction5 = block_chain.newTransaction("Lucy", "Justin", '1 BTC') 
print(" \n")
transaction6 = block_chain.newTransaction("Justin", "Alex", '1 BTC') 
print(" \n")
block_chain.newBlock(10384)  
print(" \n")
  
print("Genesis block: ", block_chain.chain)  