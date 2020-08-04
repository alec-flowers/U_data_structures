import sys
import heapq

class Node():
    def __init__(self, frequency):
        self.value = None
        self.frequency = frequency
        self.left = None
        self.right = None

    def set_left(self,left_value):
        self.left = left_value

    def set_right(self, right_value):
        self.right = right_value
    
    def set_value(self,value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def get_frequency(self):
        return self.frequency

    def __repr__(self):
        return "Node(freq: {}, value: {})".format(self.get_frequency(),self.get_value())
    
    def __lt__(self, other):
        return self.get_frequency() < other.get_frequency()

def get_frequeny(message):
    '''
    Returns frequency of lettters in a given string.
    Input: message (string) - string
    Return: frequency_dict (dict) - dictionary with keys being letters and value being frequency in string
    '''
    frequency_dict = dict()
    for letter in message:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1
    
    return frequency_dict

def tree_to_data(root):
    '''
    
    Input:
    Return: code_dict (dict) - 
    '''
    code_dict = {}
    bits = ''

    def traverse(root,bits):
        'Recursive function that traverses huffman tree to return bit values for each final node'

        if root.left == None and root.right == None:
            code_dict[root.value] = bits
            return
        else:
            traverse(root.left, bits+'0')
            traverse(root.right, bits+'1')

    traverse(root,bits)

    return code_dict

def huffman_encoding(message):
    
    frequency_dict = get_frequeny(message)

    #create heap
    heap = []
    for letter, freq in frequency_dict.items():
        node = Node(freq)
        node.set_value(letter)
        heapq.heappush(heap, node)

    #build huffman tree
    while len(heap) > 1:

        small = heapq.heappop(heap)
        next_small = heapq.heappop(heap)

        interior_node = Node(small.get_frequency()+next_small.get_frequency())
        interior_node.set_left(small)
        interior_node.set_right(next_small)

        heapq.heappush(heap, interior_node)

    tree = heap[0]
    letter_to_binary = tree_to_data(tree)
    encoded_data = ''

    for letter in message:
        encoded_data += letter_to_binary[letter]

    return encoded_data, tree

def huffman_decoding(encoded_data, tree):
    
    node = tree
    decoded_data = ''
    index = 0

    while index < len(encoded_data):

        if encoded_data[index] == '0':
            node = node.left
        else:
            node = node.right

        if (node.left == None) & (node.right == None):
            decoded_data += node.get_value()
            node = tree
        
        index+=1

    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "Halleluja, Halleluja, Halleluja!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))