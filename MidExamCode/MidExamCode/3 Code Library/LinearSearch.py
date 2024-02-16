#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Linear Search
# ---------------------------------------------------------------------------
# method:
#    1、lterative versions
#    2、Recursive versions
#
#############################################################################


def iterative_linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

 def recursive_linear_search(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recursive_linear_search(arr, l+1, r-1, x)
