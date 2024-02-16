#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Stack using Linked List 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        else:
            return None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # Linked list cannot be full as it can dynamically allocate memory
        return False

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None
