"""Main file to compress text files"""

from Queue import PriorityQueue
from helpers import CustomOpen, CharTree


def create_char_freq_map(filename):

    char_frequency = {}

    with CustomOpen(filename) as f:
        contents = f.read()
        for char in contents:
            value = char_frequency.get(char, 0)
            char_frequency[char] = value + 1

    return char_frequency


def create_priority_queue(char_dict):

    char_priority = PriorityQueue()

    for k, v in char_dict.iteritems():
        char_priority.put(CharTree(v, k))

    return char_priority


def create_priority_binary_tree(priority_queue):

    while priority_queue.qsize() > 1:
        print priority_queue.qsize()
        left = priority_queue.get()
        right = priority_queue.get()
        freq = left.freq + right.freq
        root = CharTree(freq, None, left, right)
        print "Combining %s (%d) and %s (%d) to add %d" % (left.char,
                                                           left.freq,
                                                           right.char,
                                                           right.freq,
                                                           root.freq)
        priority_queue.put(root)

    return priority_queue.get()


# def create_char_code_map(priority_binary_tree):


##############################################################################
if __name__ == '__main__':

    char_frequency = create_char_freq_map('samples/example.txt')
    char_priority = create_priority_queue(char_frequency)
    char_tree = create_priority_binary_tree(char_priority)

    print char_tree


##############################################################################
# Steps:

# - Generate Frequency Table
# - Put Singleton Trees in Priority Queue
# - Tree Creation   --> NEED TO FINISH __REPR__ FOR CHAR_TREE
# - Code Retrieval
# - Compression
# - Decompression
