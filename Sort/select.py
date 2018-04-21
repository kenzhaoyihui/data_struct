#!/usr/bin/env python3

""" Selection Sorting -- unstable"""

def select_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min = j
        for i in range(j+1, n):
            if alist[min] > alist[i]:
                min = i
        alist[j], alist[min] = alist[min], alist[j]
    
    return alist

if __name__ == "__main__":
    alist = [12, 34, 1, 43, 22, 100, 4]
    print alist
    select_sort(alist)
    print alist