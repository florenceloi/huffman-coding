"""Main file to compress text files"""

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
    return priority_queue


# def create_char_code_map(priority_binary_tree):


##############################################################################
if __name__ == '__main__':

    char_frequency = create_char_freq_map('samples/example.txt')
    char_priority_queue = create_priority_queue(char_frequency)
    char_tree = create_priority_binary_tree(char_priority_queue)


##############################################################################
# Steps:

# - Generate Frequency Table
# - Put Singleton Trees in Priority Queue
# - Tree Creation
# - Code Retrieval --> NEED TO CONSTRUCT MAP USING SINGLE TRAVERSAL OF HUFFMAN CODE TREE
# - Compression
# - Decompression
