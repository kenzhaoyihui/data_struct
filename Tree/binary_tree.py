#!/usr/bin/env python3

""" Binary Tree"""

class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        quene = [self.root]
        while quene:
            cur_node = quene.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                quene.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                quene.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        quene = [self.root]

        while quene:
            cur_node = quene.pop(0)
            print (cur_node.item, end=" ")

            if cur_node.lchild is not None:
                quene.append(cur_node.lchild)
            if cur_node.rchild is not None:
                quene.append(cur_node.rchild)

    def pre_order(self, node):
        if node is None:
            return
        print (node.item, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.lchild)
        print (node.item, end=" ")
        self.in_order(node.rchild)

    def last_order(self, node):
        if node is None:
            return
        self.last_order(node.lchild)
        self.last_order(node.rchild)
        print (node.item, end=" ")

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print ("\n")
    tree.pre_order(tree.root)
    print ("\n")
    tree.in_order(tree.root)
    print ("\n")
    tree.last_order(tree.root)
    print ("\n")