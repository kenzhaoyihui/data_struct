#!/usr/bin/env python3

"""Quick Sorting -- unstable"""

def quick_sort(alist, start, end):
    if start >= end:
        return
    mid_value = alist[start]
    #n = len(alist)

    low = start
    high = end

    while low < high:
        while high >= low and alist[high] >= mid_value:
            high -= 1

        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        
        alist[high] = alist[low]
    
    alist[low] = mid_value
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

def quick2_sort(alist):
    if (len(alist) < 2):
        return
    left = [x for x in alist[1:] if x < alist[0]]
    right = [x for x in alist[1:] if x >= alist[0]]

    quick2_sort(left)
    quick2_sort(right)
    alist[:] = left + [alist[0]] + right


if __name__ == "__main__":
    alist = [21, 33, 12, 45, 1, 100, 3, 0, 24, 45, 54, 23]
    alist1 = [21, 33, 12, 45, 1, 100, 3, 0, 24, 45, 54, 23]
    print (alist)
    quick_sort(alist, 0, len(alist)-1)
    print (alist)
    print "-----------------"
    print (alist1)
    quick2_sort(alist1)
    print (alist1)
    