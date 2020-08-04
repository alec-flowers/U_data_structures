import hashlib
from time import gmtime, strftime

class Block():

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = strftime("%Y-%m-%d %H:%M:%S", timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.block_header = str(self.timestamp) + str(self.data) + str(self.previous_hash) 

        self.hash = self._calc_hash()

    def _calc_hash(self):

        sha = hashlib.sha256()

        hash_str = self.block_header.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def __repr__(self):
        s = '---------\n'
        s += 'i = {}\n'.format(self.index)
        s += 'Data: {}\n'.format(self.data)
        s += 'Time: {}\n'.format(self.timestamp)
        s += 'Hash: {}\n'.format(self.hash)
        s += 'P Hash: {}\n\n'.format(self.previous_hash)
        return s

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListBlock():
    def __init__(self):
        first = self.create_first_block()
        self.head = first

    def create_first_block(self):
        first_block =  Block(0, gmtime(),'',0)
        nfirst_block = Node(first_block)

        print('---First Block created---')
        return nfirst_block

    def get_head(self):
        return self.head

    def add_block(self, value):
        temp = self.head
        last_block = temp.value
        new_block = Node(Block(last_block.index+1,gmtime(),value,last_block.hash))

        self.head = new_block
        self.head.next = temp

        print('Added block index: {}'.format(last_block.index+1))
    
    def __repr__(self):
        s = ''
        node = self.head
        while node:
            s += node.value.__repr__()
            node = node.next
        return s

blockchain = LinkedListBlock()
blockchain.add_block('Hello')
blockchain.add_block('My')
blockchain.add_block('Name')
blockchain.add_block('is')

print(blockchain)




