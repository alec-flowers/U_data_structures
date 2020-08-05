import unittest
from problem3 import huffman_encoding, huffman_decoding

class TestHuffman(unittest.TestCase):

    def test1(self):
        a_great_sentence = "Halleluja, Halleluja, Halleluja!"
        encoded_data, tree = huffman_encoding(a_great_sentence)
        decoded_data = huffman_decoding(encoded_data, tree)

        self.assertEqual(a_great_sentence, decoded_data)

if __name__ == '__main__':
    unittest.main()