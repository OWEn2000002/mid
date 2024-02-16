#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Sorting Algorithms using Link List
# ---------------------------------------------------------------------------
#    1) Selection Sort
#    2) Insertion Sort
#    3) Quick Sort
#    4) IMerge Sort
#
#############################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1）Selection Sort for Linked List
def selection_sort_linked_list(head):
    current = head
    while current:
        min_node = current
        next_node = current.next
        while next_node:
            if next_node.data < min_node.data:
                min_node = next_node
            next_node = next_node.next
        current.data, min_node.data = min_node.data, current.data
        current = current.next
    return head

# 2）Insertion Sort for Linked List
def insertion_sort_linked_list(head):
    dummy = Node(0)
    dummy.next = head
    prev_sorted = dummy
    current = head
    while current:
        if current.next and current.next.data < current.data:
            while prev_sorted.next and prev_sorted.next.data < current.next.data:
                prev_sorted = prev_sorted.next
            temp = prev_sorted.next
            prev_sorted.next = current.next
            current.next = current.next.next
            prev_sorted.next.next = temp
            prev_sorted = dummy
        else:
            current = current.next
    return dummy.next

# 3）Quick Sort for Linked List
def quick_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    pivot = head
    greater_head = None
    equal_head = None
    smaller_head = None
    current = head.next
    while current:
        next_node = current.next
        if current.data < pivot.data:
            current.next = smaller_head
            smaller_head = current
        elif current.data == pivot.data:
            current.next = equal_head
            equal_head = current
        else:
            current.next = greater_head
            greater_head = current
        current = next_node

    sorted_smaller = quick_sort_linked_list(smaller_head)
    sorted_greater = quick_sort_linked_list(greater_head)

    result_head = None
    result_tail = None

    if sorted_smaller:
        result_head = sorted_smaller
        result_tail = get_tail(sorted_smaller)
    else:
        result_head = pivot

    if equal_head:
        if result_tail:
            result_tail.next = pivot
        else:
            result_head.next = pivot
        result_tail = get_tail(equal_head)
        result_tail.next = sorted_greater
    else:
        pivot.next = sorted_greater

    return result_head

def get_tail(head):
    current = head
    while current.next:
        current = current.next
    return current



# 4）Merge Sort for Linked List
def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_mid)

    sorted_list = merge(left, right)
    return sorted_list

def merge(left, right):
    dummy = Node(0)
    tail = dummy
    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left or right
    return dummy.next

def get_middle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

