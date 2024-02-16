#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# DoubleLinkedList
# ---------------------------------------------------------------------------
# .Head
# .Node
#   。Data
#   。Next
#   。Prev
# .Read (beginning, random position, end)
# .Insert (beginning, random position, end)
# .Delete (beginning, random position, end)
#
##############################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    #===================================================================
    # 1、Read Node
    #-------------------------------------------------------------------
    # 1）Method to read the double linked list from the beginning
    def read_beginning(self):
        if self.head:
            return self.head.data
        else:
            return None

    # 2）Method to read the double linked list from a random position
    def read_random_position(self, position):
        current = self.head
        index = 0
        while current and index < position:
            current = current.next
            index += 1
        if current:
            return current.data
        else:
            return None

    # 3）Method to read the double linked list from the end
    def read_end(self):
        current = self.head
        while current and current.next:
            current = current.next
        if current:
            return current.data
        else:
            return None

    #===================================================================
    # 2、Insert Node
    #-------------------------------------------------------------------
    # 1）Method to insert a node at the beginning of the double linked list
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node


    # 2）Method to insert a node at a random position in the double linked list
    def insert_random_position(self, position, data):
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        index = 0
        while current and index < position - 1:
            current = current.next
            index += 1
        if current:
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    # 3）Method to insert a node at the end of the double linked list
    def insert_end(self, data):
        new_node = Node(data)
        current = self.head
        while current and current.next:
            current = current.next
        if current:
            current.next = new_node
            new_node.prev = current
        else:
            self.head = new_node

    #===================================================================
    # 3、Delete Node
    #-------------------------------------------------------------------
    # 1）Method to delete a node from the beginning of the double linked list
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    # 2）Method to delete a node at a random position in the double linked list
    def delete_random_position(self, position):
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        index = 0
        while current and index < position:
            current = current.next
            index += 1
        if current:
            if current.next:
                current.prev.next = current.next
                current.next.prev = current.prev
            else:
                current.prev.next = None

    # 3）Method to delete a node at the end of the double linked list
    def delete_end(self):
        current = self.head
        while current and current.next:
            current = current.next
        if current and current.prev:
            current.prev.next = None
        elif current:
            self.head = None
