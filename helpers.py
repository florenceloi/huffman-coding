"""Utility file to create helper classes and functions"""

from collections import deque


class CustomOpen(object):

    def __init__(self, filename, mode='r'):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()


class CharTree(object):

    def __init__(self, freq, char, left=None, right=None):
        self.data = (freq, char)
        self.left = left
        self.right = right

    def __cmp__(self, other):
        return cmp(self.data[0], other.data[0])
