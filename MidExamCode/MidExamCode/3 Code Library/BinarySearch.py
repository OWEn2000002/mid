#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Binary Search
# ---------------------------------------------------------------------------
# method:
#    1、lterative versions
#    2、Recursive versions
#
#############################################################################

# 1) iterative version of binary_search
def iterative_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# 2) recursive version of binary_search
def recursive_binary_search(arr, low, high, x):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return recursive_binary_search(arr, mid + 1, high, x)
        else:
            return recursive_binary_search(arr, low, mid - 1, x)
    else:
        return -1
