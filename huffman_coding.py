"""Main file to compress text files"""

import sys
from Queue import PriorityQueue
from helpers import CustomOpen, CharTree

BYTE_LENGTH = 8


class Colors(object):

    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


class HuffmanCoding(object):

    def __init__(self, filename):
        self.original_file = filename
        self.compressed_file = filename.split('.')[0] + '_compressed.bin'
        self.decompressed_file = filename.split('.')[0] + '_decompressed.txt'
        self.char_frequency_dict = {}
        self.priority_queue = PriorityQueue()
        self.huffman_tree = None
        self.char_to_code_mapping = {}
        self.code_to_char_mapping = {}

    def create_char_frequency_map(self):

        with CustomOpen(self.original_file) as f:
            contents = f.read()
            for char in contents:
                value = self.char_frequency_dict.get(char, 0)
                self.char_frequency_dict[char] = value + 1

        print 'Character frequency mapping: {dict}\n'.format(dict=self.char_frequency_dict)

    def create_priority_queue(self):

        for char, frequency in self.char_frequency_dict.iteritems():
            self.priority_queue.put((frequency, CharTree(frequency, char)))

        print 'Character frequency priority queue mapping: {dict}\n'.format(dict=self.priority_queue)

    def create_priority_binary_tree(self):

        while self.priority_queue.qsize() > 1:
            print 'Current priority queue size: {num}'.format(num=self.priority_queue.qsize())
            tree_one = self.priority_queue.get()
            tree_two = self.priority_queue.get()
            total_freq = tree_one[0] + tree_two[0]
            print '\t-> total frequency: {freq}'.format(freq=total_freq)
            root = CharTree(total_freq, None, tree_one, tree_two)
            self.priority_queue.put((total_freq, root))

        print '\nFinal length of priority queue: {length}'.format(length=self.priority_queue.qsize())

        self.huffman_tree = self.priority_queue.get()[1]

    def create_char_code_map(self, huffman_tree, code):

        if huffman_tree.data[1] is not None:
            self.char_to_code_mapping[huffman_tree.data[1]] = code
        if huffman_tree.left is not None:
            self.create_char_code_map(huffman_tree.left[1], code + '0')
        if huffman_tree.right is not None:
            self.create_char_code_map(huffman_tree.right[1], code + '1')

        print 'Character to code mapping: {dict}\n'.format(dict=self.char_to_code_mapping)

    @staticmethod
    def add_padding(text):

        padding_length = BYTE_LENGTH - len(text) % BYTE_LENGTH
        padding_data = "{0:08b}".format(padding_length)
        padding = '0' * padding_length
        padded_text = padding_data + text + padding

        return padded_text

    @staticmethod
    def convert_string_to_byte_array(text):

        b = bytearray()

        for i in range(0, len(text), BYTE_LENGTH):
            byte = text[i:i+BYTE_LENGTH]
            b.append(int(byte, 2))

        return b

    def write_compressed_file(self):

        print Colors.OKBLUE + Colors.BOLD + 'COMPRESSING FILE...' + Colors.ENDC

        with CustomOpen(self.original_file) as input_file, CustomOpen(self.compressed_file, 'wb') as output_file:
            encoded_text = ''
            contents = input_file.read()

            for char in contents:
                encoded_text += self.char_to_code_mapping[char]
            padded_encoded_text = self.add_padding(encoded_text)
            bytes = self.convert_string_to_byte_array(padded_encoded_text)

            output_file.write(bytes)

        print Colors.OKGREEN + Colors.BOLD + 'FILE COMPRESSED' + Colors.ENDC

    def create_code_char_map(self):

        for char, code in self.char_to_code_mapping.iteritems():
            self.code_to_char_mapping[code] = char

        print '\nCode to character mapping: {dict}\n'.format(dict=self.code_to_char_mapping)

    @staticmethod
    def remove_padding(text):

        padded_data = text[:BYTE_LENGTH]
        extra_padding = int(padded_data, 2)

        encoded_text = text[BYTE_LENGTH:-1*extra_padding]

        return encoded_text

    def decode_text(self, text):

        current_code = ''
        decoded_text = ''

        for bit in text:
            current_code += bit
            if current_code in self.code_to_char_mapping:
                character = self.code_to_char_mapping[current_code]
                decoded_text += character
                current_code = ''

        return decoded_text

    def write_decompressed_file(self):

        print Colors.OKBLUE + Colors.BOLD + 'DECOMPRESSING FILE...' + Colors.ENDC

        with CustomOpen(self.compressed_file, 'rb') as input_file, CustomOpen(self.decompressed_file, 'w') as output_file:
            bit_string = ''

            byte = input_file.read(1)
            while byte != '':
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(BYTE_LENGTH, '0')  # convert to bits and remove '0b'
                bit_string += bits
                byte = input_file.read(1)   # read next byte

            encoded_text = self.remove_padding(bit_string)
            decoded_text = self.decode_text(encoded_text)

            output_file.write(decoded_text)

        print Colors.OKGREEN + Colors.BOLD + 'FILE DECOMPRESSED' + Colors.ENDC


##############################################################################
if __name__ == '__main__':

    input_file = sys.argv[1]        # This script assumes the input file is suffixed '.txt' with no extra periods.
    h = HuffmanCoding(input_file)

    # Compress text file
    h.create_char_frequency_map()
    h.create_priority_queue()
    h.create_priority_binary_tree()
    h.create_char_code_map(h.huffman_tree, '')
    h.write_compressed_file()

    # Decompress binary file
    h.create_code_char_map()
    h.write_decompressed_file()
