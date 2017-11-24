import unittest
from block import *
from blockchain import *

class TestBlock(unittest.TestCase):
    def test_has_valid_index(self):
        block_1 = Block(0, time.time(), 'Block 1', '0')
        block_2 = Block(0, time.time(), 'Block 2', '0')
        block_3 = Block(1, time.time(), 'Block 3', '0')
        block_4 = Block(2, time.time(), 'Block 4', '0')

        self.assertEqual(False, block_2.has_valid_index(block_1))
        self.assertEqual(True, block_3.has_valid_index(block_1))
        self.assertEqual(True, block_3.has_valid_index(block_2))
        self.assertEqual(False, block_4.has_valid_index(block_2))

    def test_has_valid_previous_hash(self):
        block_1 = Block(0, time.time(), 'Block 1', '0')
        block_2 = Block(1, time.time(), 'Block 2', block_1.hash)
        block_3 = Block(2, time.time(), 'Block 3', block_1.hash)

        self.assertEqual(True, block_2.has_valid_previous_hash(block_1))
        self.assertEqual(False, block_3.has_valid_previous_hash(block_2))

    def test_hash_valid_hash(self):
        block_1 = Block(0, time.time(), 'Block 1', '0')
        block_2 = Block(1, time.time(), 'Block 2', '0')
        block_2.hash = '0'

        self.assertEqual(True, block_1.has_valid_hash())
        self.assertEqual(False, block_2.has_valid_hash())

class TestBlockchain(unittest.TestCase):
    def test_latest_block(self):
        new_chain = Blockchain()
        new_chain.generate_next_block('Next Block')

        self.assertEqual(new_chain.blockchains[-1], new_chain.get_latest_block())

    def test_generate_genesis_block(self):
        new_chain = Blockchain()
        genesis_block = new_chain.blockchains[0]

        self.assertEqual(0, genesis_block.index)
        self.assertEqual('0', genesis_block.previous_hash)

    def test_generate_next_block(self):
        new_chain = Blockchain()
        new_chain.generate_next_block('Block 1')
        new_chain.generate_next_block('Block 2')
        block_1 = new_chain.blockchains[1]
        block_2 = new_chain.blockchains[2]

        self.assertEqual(1, block_1.index)
        self.assertEqual('Block 1', block_1.data)
        self.assertEqual(True, block_2.has_valid_index(block_1))
        self.assertEqual(True, block_2.has_valid_previous_hash(block_1))
        self.assertEqual(True, block_2.has_valid_hash())

    def test_verify_new_block(self):
        new_chain = Blockchain()
        new_chain.generate_next_block('Block 1')
        block_1 = new_chain.blockchains[1]
        block_2 = Block(2, time.time(), 'Block 2', block_1.hash)
        block_3 = Block(3, time.time(), 'Block 3', block_2.hash)
        block_4 = Block(3, time.time(), 'Block 4', block_3.hash)
        block_5 = Block(4, time.time(), 'Block 4', block_1.hash)
        block_6 = Block(4, time.time(), 'Block 4', block_3.hash)
        block_6.hash = '0'

        self.assertEqual(True, new_chain.verify_new_block(block_2))
        self.assertEqual(True, new_chain.verify_new_block(block_3))
        self.assertEqual(False, new_chain.verify_new_block(block_4))
        self.assertEqual(False, new_chain.verify_new_block(block_5))
        self.assertEqual(False, new_chain.verify_new_block(block_6))

if __name__ == '__main__':
    unittest.main()