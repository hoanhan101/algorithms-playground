import time
from block import Block
from datetime import datetime

class Blockchain():
    def __init__(self):
        self.blockchains = []
        self.create_genesis_block()

    def get_latest_block(self):
        return self.blockchains[-1]

    def generate_next_block(self, data):
        index = len(self.blockchains)
        timestamp = time.time()
        previous_hash = self.get_latest_block().hash

        new_block = Block(index, timestamp, data, previous_hash)
        self.blockchains.append(new_block)

    def create_genesis_block(self):
        index = 0
        timestamp = time.time()
        data = 'First Block'
        previous_hash = '0'
        genesis_block = Block(index, timestamp, data, previous_hash)
        self.blockchains.append(genesis_block)

    def verify_new_block(self, new_block):
        previous_block = self.get_latest_block()

        if not new_block.has_valid_index(previous_block):
            print('Invalid index')
            return False
        if not new_block.has_valid_previous_hash(previous_block):
            print('Invalid previous hash')
            return False
        if not new_block.has_valid_hash():
            print('Invalid hash')
            return False

        self.blockchains.append(new_block)
        return True