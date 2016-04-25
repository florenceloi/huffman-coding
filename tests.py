import unittest
from Queue import PriorityQueue

from helpers import CustomOpen
from huffman_coding import create_char_freq_map, create_priority_queue


class CompressionTestCase(unittest.TestCase):

    def setUp(self):
        self.char_freq_dict = create_char_freq_map('WarAndPeace.txt')
        self.char_priority = create_priority_queue(self.char_freq_dict)

    def test_create_char_freq_map(self):
        self.assertIsInstance(self.char_freq_dict, dict)
        self.assertEqual(self.char_freq_dict, {'\n': 65334, '!': 3923,
            ' ': 515617, '#': 1, '"': 17968, '%': 1, '$': 2, "'": 7524,
            ')': 670, '(': 670, '*': 298, '-': 6034, ',': 39886, '/': 29,
            '.': 30804, '1': 359, '0': 170, '3': 58, '2': 138, '5': 51,
            '4': 23, '7': 39, '6': 55, '9': 35, '8': 174, ';': 1145, ':': 997,
            '=': 2, '?': 3136, 'A': 6209, '@': 2, 'C': 1769, 'B': 3589,
            'E': 1868, 'D': 2015, 'G': 1300, 'F': 1939, 'I': 7400, 'H': 4010,
            'K': 1186, 'J': 308, 'M': 3267, 'L': 707, 'O': 1597, 'N': 3602,
            'Q': 35, 'P': 6152, 'S': 2978, 'R': 2688, 'U': 277, 'T': 6439,
            'W': 2884, 'V': 934, 'Y': 1265, 'X': 349, '[': 1, 'Z': 108, ']': 1,
            'a': 199220, 'c': 59485, 'b': 31054, 'e': 312952, 'd': 116261,
            'g': 50019, 'f': 52948, 'i': 166345, 'h': 163020, 'k': 19230,
            'j': 2266, 'm': 58375, 'l': 95809, 'o': 191235, 'n': 180552,
            'q': 2295, 'p': 39014, 's': 159902, 'r': 145365, 'u': 65148,
            't': 219581, 'w': 56317, 'v': 25967, 'y': 44999, 'x': 3711,
            'z': 2280})

    def test_create_priority_queue(self):
        self.assertIsInstance(self.char_priority, PriorityQueue)
        self.assertFalse(self.char_priority.empty())

###############################################################################

if __name__ == '__main__':
    unittest.main()
