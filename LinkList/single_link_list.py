#!/usr/bin/env python3

class ListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

    # @property
    # def node_item(self):
    #     return self.item

    # @node_item.setter
    # def node_item(self, val):
    #     self.item = val

    # @property
    # def node_next(self):
    #     return self.next

    # @node_next.setter
    # def node_next(self, val):
    #     self.next = val

class SingleLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print cur.item
            cur = cur.next

    def add(self, item):
        """O(1)"""
        node = ListNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """O(n)"""
        node = ListNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = ListNode(item)
            count = 0
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                if pre == None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print ll.is_empty()
    print ll.length()

    print "----------"
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.add(2)
    ll.add(1)
    print ll.is_empty()
    print ll.length()
    print "----------"

    ll.travel()
    print "----------"
    print ll.search(3)
    print ll.search(6)

    print "----------"
    ll.insert(3, 100)
    ll.travel()
    print "----------"
    ll.remove(100)
    ll.travel()



