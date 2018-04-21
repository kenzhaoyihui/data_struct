#!/usr/bin/env python3
""" Shell Sorting -- unstable"""

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while(gap >= 1):
        for j in range(gap, n):
            
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

if __name__ == "__main__":
    alist = [45, 12, 34, 97, 66, 1, 100, 33]
    print (alist)
    shell_sort(alist)
    print (alist)