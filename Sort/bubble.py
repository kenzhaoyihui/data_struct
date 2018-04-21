#!/usr/bin/env python3
""" Bubble Sorting -- stable"""

def bubble_sort(alist):
    #i 0~n-2 range(0, n-1) j=0
    #i 0~n-3 range(0, n-2) j=1
    #i 0~n-2-k  range(0, n-1-k)  j=k
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return
    return alist

if __name__ == "__main__":
    alist = [54, 26, 43, 93, 17, 1, 22, 100, 77]
    print alist
    bubble_sort(alist)
    print alist
