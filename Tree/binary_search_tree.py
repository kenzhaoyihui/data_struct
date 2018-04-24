#!/usr/bin/env python3

""" Binary Search Tree"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinarySearchTree(object):
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    def insert(self, data):
        flag, node, parent = self.search(self.root, self.root, data)
        # flag is false, mean that the parent haven't child
        if flag is False:
            new_node = Node(data)
            if data > parent.data:
                parent.rchild = new_node
            else:
                parent.lchild = new_node
    
    def delete(self, root, data):
        flag, node, parent = self.search(root, root, data)
        if flag is False:
            print ("No this key")
        else:
            if node.lchild is None:
                if node == parent.lchild:
                    parent.lchild = node.rchild
                else:
                    parent.rchild = node.rchild
                del parent

            elif node.rchild is None:
                if node == parent.lchild:
                    parent.lchild = node.lchild
                else:
                    parent.rchild = node.lchild
                del parent
            # lchild and rchild is not None
            else:
                # find the later node
                pre = node.rchild
                if pre.lchild is None:
                   node.data = pre.data
                   node.rchild = pre.rchild
                   del pre
                else:
                    # 找最后一个没有左孩子的叶子结点
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    node.data = next.data
                    pre.lchild = next.rchild
                    del next

    def preOrderTravel(self, node):
        if node is None:
            return
        print (node.data, end=" ")
        self.preOrderTravel(node.lchild)
        self.preOrderTravel(node.rchild)

    def inOrderTravel(self, node):
        if node is None:
            return
        self.inOrderTravel(node.lchild)
        print (node.data, end=" ")
        self.inOrderTravel(node.rchild)

    def postOrderTravel(self, node):
        if node is None:
            return
        self.postOrderTravel(node.lchild)
        self.postOrderTravel(node.rchild)
        print (node.data, end=" ")


if __name__ == "__main__":
    node_list = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BinarySearchTree(node_list)
    print ("--------------------")
    bst.preOrderTravel(bst.root)
    print ("\n")
    bst.inOrderTravel(bst.root)
    print ("\n")
    bst.postOrderTravel(bst.root)
    print ("\n")
    print ("------------------")
    
    bst.delete(bst.root, 49)
    print ("\n")
    bst.preOrderTravel(bst.root)
    print ("\n")
    bst.inOrderTravel(bst.root)
    print ("\n")
    bst.postOrderTravel(bst.root)
    print ("\n")
    print ("-----------------")