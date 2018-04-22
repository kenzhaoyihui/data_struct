#!/usr/bin/env python3

""" Merge Sorting -- unstable"""

def merge_sort(alist):
    """ di gui"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    #return merge(left, right)

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result += left[left_pointer:]
    result += right[right_pointer:]
    # Need to return a new list "result",
    # So should use `sorted = merge_sort(alist)`
    # `print (sorted)`
    return result


if __name__ == "__main__":
    alist = [34, 12, 45, 1, 23, 56, 99, 123, 22]
    print (alist)
    sorted = merge_sort(alist)
    print (sorted)

    # Execute process
    """
    merge_sort([43, 12, 45, 1, 23, 56, 99, 123, 22])
    left = merge_sort([43, 12, 45, 1])
        left = merge_sort([43, 12])
            left = merge_sort([43]) ==> left = [43]
            right = merge_sort([12]) ==> right = [12]
            result = [12, 43]
            return result
        right = merge_sort([45, 1])
            left = merge_sort([45])
            right = merge_sort([1])
            result = [1, 45]
            return result

        result = [1, 12, 43, 45]
        return result

    right = merge_sort([23, 56, 99, 123, 22])
        left = merge_sort([23, 56])
            left = merge_sort([23])
            right = merge_sort([56])
            result = [23, 56]
            return result
        right = merge_sort([99, 123, 22])
            left = merge_sort([99])
            right = merge_sort([123, 22])
                left = merge_sort([123])
                right = merge_sort([22])
                result = [22, 123]
                return result
            result = [22, 99, 123]
        result = [22, 23, 56, 99, 123]
        return result

    result = [1, 12, 22, 23, 43, 45, 56, 99, 123]
    return result
    """