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

    def interior(self):
        return self.value is None

    def __repr__(self):
        return "Node(freq: {}, value: {})".format(self.get_frequency(),self.get_value())
    
    def __lt__(self, other):
        return self.get_frequency() < other.get_frequency()

def get_frequency(message):
    '''
    Returns frequency of lettters in a given string.
    Input: message (string) - string
    Output: frequency_dict (dict) - dictionary with keys being letters and value being frequency in string
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
    Encode data using the huffman tree. 
    Input: root (Node) - huffman tree to traverse
    Return: code_dict (dict) - encoded data using huffman tree
    '''
    code_dict = {}
    bits = ''

    def traverse(root,bits):
        'Recursive function that traverses huffman tree to return bit values for each final node'

        if not root.interior():
            code_dict[root.value] = bits
            return 
        else:
            if root.left != None:
                traverse(root.left, bits+'0')
            if root.right != None:
                traverse(root.right, bits+'1')

    traverse(root,bits)

    return code_dict

def huffman_encoding(message):
    'Take a message, create a huffman tree, and encode the data'
    assert isinstance(message, str)
    assert len(message)>0
    frequency_dict = get_frequency(message)
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

    if not heap[0].interior():
        print('a')
        interior_node = Node(heap[0].get_frequency())
        interior_node.set_left(heap[0])
        interior_node.set_right(Node(None))
        tree = interior_node
    
    letter_to_binary = tree_to_data(tree)
    encoded_data = ''

    for letter in message:
        encoded_data += letter_to_binary[letter]

    return encoded_data, tree


def huffman_decoding(encoded_data, tree):
    'Decode data using huffman tree'

    node = tree
    decoded_data = ''
    index = 0
    while index < len(encoded_data):
        
        if encoded_data[index] == '0':
            node = node.left
        else:
            node = node.right

        if not node.interior():
            decoded_data += node.get_value()
            node = tree
        
        index += 1
        
    return decoded_data

if __name__ == "__main__":
    
    #Test1   
    print('-- Test 1 --') 
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

    #Test2
    print('-- Test 2 --')
    sentence2 = ' '
    print('Message: {}'.format(sentence2))
    encoded_data2, tree2 = huffman_encoding(sentence2)

    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    print('Decoded Data: '.format(decoded_data2))

    #Test3 
    print('-- Test 3 --')
    sentence3 = '1asdflk234r0iwqer0wqelrqwenk;jf[qwe9   0rqweorlqlwetnroqe[w0qweqweerj;E\][\[\wefw'
    print('Message: {}'.format(sentence3))
    encoded_data3, tree3 = huffman_encoding(sentence3)

    decoded_data3 = huffman_decoding(encoded_data3, tree3)
    print('Decoded Data: {}'.format(decoded_data3))

    #Test4
    print('-- Test 4 --')
    sentence4 = 'AAA'
    print('Message: {}'.format(sentence4))
    encoded_data4, tree4 = huffman_encoding(sentence4)

    decoded_data4 = huffman_decoding(encoded_data4, tree4)
    print('Decoded Data: {}'.format(decoded_data4))