import hashlib
import datetime as date
import random

class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = date.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.private_key = self.generate_private_key()
        self.hash = self.calculate_hash()
        self.key1 = 0
        self.ogkey = self.private_key
        
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.private_key).encode('utf-8'))
        return sha.hexdigest()
    
    def generate_private_key(self):
        return random.randint(10000000, 99999999)
    

class Blockchain:
    def __init__(self):
        self.chain = [Block("First Block Data", "0")]
        
    def add_block(self, data):
        new_block = Block(data, self.chain[-1].hash)
        self.chain.append(new_block)
        return new_block.private_key
    
    def get_block_data(self, block_index, private_key):
        if self.chain[block_index].private_key == private_key:
            new_private_key = self.generate_private_key()
            self.chain[block_index].key1 = private_key
            #key2 = new_private_key
            self.chain[block_index].private_key = new_private_key
            return self.chain[block_index].data, new_private_key
        else:
            return None, None
        
    def check_new_private_key(self, block_index, previous_private_key):
        
        if self.chain[block_index].ogkey == previous_private_key:
            #self.chain[block_index].private_key = new_private_key
            return self.chain[block_index].private_key
        else:
            return None
        
    def generate_private_key(self):
        return random.randint(10000000, 99999999)
    

# Main program
blockchain = Blockchain()

while True:
    choice = input("\nEnter from following\n'1' Add Data to Blockchain\n'2' Access Data from Blockchain\n'3' Access the New Private Key\n'q' Quit Application: ")
    
    if choice == '1':
        new_data = input("Enter Name, Address, Contact Number separated by commas: ")
        private_key = blockchain.add_block(new_data)
        print("Private key:", private_key)
    elif choice == '2':
        block_index = int(input("Enter block index to access: "))
        private_key = int(input("Enter Private Key: "))
        block_data, new_private_key = blockchain.get_block_data(block_index, private_key)
        if block_data is not None:
            print("Block data:", block_data)
        else:
            print("Invalid Private Key.")
    elif choice == '3':
        block_index = int(input("Enter block index to generate new private key: "))
        previous_private_key = int(input("Enter Original User's Private Key: "))
        new_private_key = blockchain.check_new_private_key(block_index, previous_private_key)
        if new_private_key is not None:
            print("New private key:", new_private_key)
        else:
            print("Invalid previous Private Key.")
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please enter '1', '2', '3', or 'q'.")
