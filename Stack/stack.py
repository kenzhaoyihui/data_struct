#!/usr/bin/env python3

class Stack(object):
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)
        #self._list.insert(0, item)

    def pop(self):
        return self._list.pop()
        #return self._list.pop(0)

    def peek(self):
        if self._list:
            return self._list[-1]
        else:
            return None

    def is_empty(self):
        return self._list == []

    def size(self):
        return len(self._list)

if __name__ == "__main__":
    s = Stack()
    print (s.is_empty())
    s.push(1)
    s.push(2)
    s.push(100)
    s.push(1000)
    print (s.is_empty())
    print (s.size())
    print (s.peek())  # 1000

    print (s.pop())
    print (s.peek()) # 100
    print (s.pop())
    print (s.peek()) # 2

