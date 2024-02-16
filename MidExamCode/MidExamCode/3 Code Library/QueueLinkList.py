!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Queue using double linked list
# ---------------------------------------------------------------------------
# method:
#    .Enqueue
#    .Dequeue
#    .IsEmpty.
#    .IsFull
#.   .Peek
#############################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def dequeue(self):
        if self.tail:
            data = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return data
        else:
            return None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # Doubly linked list-based queue cannot be full as it can dynamically allocate memory
        return False

    def peek(self):
        if self.tail:
            return self.tail.data
        else:
            return None
