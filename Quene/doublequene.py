#!/usr/bin/env python3

class DoubleQuene(object):
    def __init__(self):
        self._list = []

    def add_front(self, item):
        #self._list.append(item)
        self._list.insert(0, item)

    def add_rear(self, item):
        self._list.append(item)

    def pop_front(self):
        return self._list.pop(0)

    def pop_rear(self):
        return self._list.pop()

    def is_empty(self):
        return not self._list

    def size(self):
        return len(self._list)

if __name__ == "__main__":
    pass