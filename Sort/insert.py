#!/usr/bin/env python3

""" Insert Sorting -- stable"""
def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        #i = j
        for i in range(j, 0, -1):
        #while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                #i -= 1
            else:
                break
    return alist

if __name__ == "__main__":
    alist = [43, 12, 34, 1, 97, 123, 22, 43]
    print (alist)
    insert_sort(alist)
    print (alist)