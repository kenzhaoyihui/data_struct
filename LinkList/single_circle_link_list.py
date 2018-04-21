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

class SingleCirLinkList(object):
    def __init__(self, node=None):
        self._head = node
        # if node:
        #     node.next = node

    def is_empty(self):
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0

        cur = self._head
        count = 1

        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return 
        cur = self._head
        while cur.next != self._head:
            print cur.item
            cur = cur.next
        print (cur.item)

    def add(self, item):
        """O(1)"""
        node = ListNode(item)
        if self.is_empty():
            self._head = node
            node.next = node
            # node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node
            # cur.next = self._head

    def append(self, item):
        """O(n)"""
        node = ListNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

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
        if self.is_empty():
            return False 
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.item == item:
                #head node
                if cur == self._head:
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                    #self._head = cur.next
                else:
                    #middle node
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #exit the while
        if cur.item == item:
            if cur == self._head:
                self._head = None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False


if __name__ == "__main__":
    ll = SingleCirLinkList()
    print ll.is_empty()
    print ll.length()

    print "----------"
    ll.append(1)
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6

    ll.insert(-1, 9) # 9 8 1 2 3 4 5 6
    ll.travel()
    print "----------"
    ll.insert(3, 100)
    ll.travel() #9 8 1 100 2 3 4 5 6
    print "----------"
    ll.insert(10, 200) #9 8 1 100 2 3 4 5 6 200
    ll.travel()
    print "----------"
    ll.remove(100) # 9 8 1 2 3 4 5 6 200
    ll.travel()
    print "-----------"
    ll.remove(9) # 8 1 2 3 4 5 6 200
    ll.travel() #
    print "-----------"
    ll.remove(200) # 8 1 2 3 4 5 6
    ll.travel()
    #print ll.search(3)
    #print ll.search(6)

    print "----------"
    ll.insert(3, 100)
    ll.travel()
    print "----------"
    ll.remove(100)
    ll.travel()

    print ll.search(3)
    print ll.search(2000)