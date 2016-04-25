"""Utility file to create helper classes and functions"""

from collections import deque

class CustomOpen(object):

    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()


class CharTree(object):

    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    # def __repr__(self):
    #     nodes = deque()
    #     levels = deque()

    #     nodes.append(self)
    #     level = 1
    #     levels.append(level)
    #     print level, "(%s: %d)" % (self.char, self.freq)

    #     while len(nodes) > 0:
    #         node = nodes.popleft()
    #         level = levels.popleft()

    #         if node.left is not None:
    #             nodes.append(node.left)
    #             levels.append(level + 1)

    #         if node.right is not None:
    #             nodes.append(node.right)
    #             levels.append(level + 1)

    #         if len(levels) > 0 and levels[0] > level and levels[0] == levels[-1]:
    #             level += 1
    #             for item in nodes:
    #                 print level, "(%s: %d)" % (self.char, self.freq)

    def __cmp__(self, other):
        return cmp(self.freq, other.freq)
