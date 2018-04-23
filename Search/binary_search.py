#!/usr/bin/env python3

def binary_search(alist, item):
    """Di Gui"""
    n = len(alist)
    if n > 0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_two(alist, item):
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last)//2
        
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ == "__main__":
    
    alist = [17, 27, 45, 67, 100, 123, 124]
    print (binary_search(alist, 67))
    print (binary_search_two(alist, 67))
    print (binary_search(alist, 10000))
    print (binary_search_two(alist, 1000))