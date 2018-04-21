#!/usr/bin/env python3

class Quene(object):
    def __init__(self):
        self._list = []

    def enquene(self, item):
        self._list.append(item)
        #self._list.insert(0, item)

    def dequene(self):
        return self._list.pop(0)
        #return self._list.pop()

    def is_empty(self):
        return not self._list

    def size(self):
        return len(self._list)

if __name__ == "__main__":
    s = Quene()
    s.enquene(1)
    s.enquene(2)
    s.enquene(3)
    print (s.is_empty())
    print (s.size())
    s.enquene(4)
    print (s.dequene())
    print (s.dequene())
    print (s.dequene())
    print (s.dequene())