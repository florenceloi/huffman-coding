"""Main file to compress text files"""

import sys
from Queue import PriorityQueue
from helpers import CustomOpen, CharTree


def create_char_freq_map(filename):

    char_frequency_dict = {}

    with CustomOpen(filename) as f:
        contents = f.read()
        for char in contents:
            value = char_frequency_dict.get(char, 0)
            char_frequency_dict[char] = value + 1

    return char_frequency_dict


def create_priority_queue(char_dict):

    char_priority_queue_dict = PriorityQueue()

    for char, frequency in char_dict.iteritems():
        char_priority_queue_dict.put((frequency, CharTree(frequency, char)))

    return char_priority_queue_dict


def create_priority_binary_tree(priority_queue):

    while priority_queue.qsize() > 1:
        print 'Current priority queue size: {num}'.format(num=priority_queue.qsize())
        tree_one = priority_queue.get()
        tree_two = priority_queue.get()
        total_freq = tree_one[0] + tree_two[0]
        print '\t-> total frequency: {freq}'.format(freq=total_freq)
        root = CharTree(total_freq, None, tree_one, tree_two)
        priority_queue.put((total_freq, root))

    print '\nFinal length of priority queue: {length}'.format(length=priority_queue.qsize())
    return priority_queue.get()


def create_char_code_map(huffman_tree, mapping, code):

    if huffman_tree.data[1] is not None:
        mapping[huffman_tree.data[1]] = code
    if huffman_tree.left is not None:
        create_char_code_map(huffman_tree.left[1], mapping, code+'0')
    if huffman_tree.right is not None:
        create_char_code_map(huffman_tree.right[1], mapping, code+'1')

    return mapping


def write_compressed_file(filename, char_code_mapping):

    output = ''
    output_filename = filename.split('.')[0] + '_compressed.' + filename.split('.')[1]

    with CustomOpen(filename) as f:
        contents = f.read()
        for char in contents:
            output += char_code_mapping[char]

    print output

    with CustomOpen(output_filename, 'wb') as f:
        f.write(output)


##############################################################################
if __name__ == '__main__':

    input_file = sys.argv[1]
    char_frequency = create_char_freq_map(input_file)
    print char_frequency
    char_priority_queue = create_priority_queue(char_frequency)
    total_freq, char_tree = create_priority_binary_tree(char_priority_queue)
    print '\nTotal characters: {freq} \nCharacter tree: {tree}\n'.format(freq=total_freq, tree=char_tree)
    char_code_mapping = create_char_code_map(char_tree, {}, '')
    print char_code_mapping
    write_compressed_file(input_file, char_code_mapping)


##############################################################################
# Steps:

# - Generate Frequency Table
# - Put Singleton Trees in Priority Queue
# - Tree Creation
# - Code Retrieval
# - Compression --> ON THIS STEP
# - Decompression
