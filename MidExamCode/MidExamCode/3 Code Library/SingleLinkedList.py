#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# SingleLinkedList
# ---------------------------------------------------------------------------
# .Head
# .Node
#   。Data
#   。Next
# .Read (beginning, random position, end)
# .Insert (beginning, random position, end)
# .Delete (beginning, random position, end)
#
#############################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #===================================================================
    # 1、Read Node
    #-------------------------------------------------------------------
    # 1）Method to read the linked list from the beginning
    def read_from_beginning(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # 2）Method to read the linked list from a random position
    def read_from_position(self, position):
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        if current:
            print(current.data)
        else:
            print("Invalid position")

    # 3）Method to read the linked list from the end
    def read_from_end(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.read_from_beginning()

    #===================================================================
    # 2、Insert Node
    #-------------------------------------------------------------------
    # 1）Method to insert a node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2）Method to insert a node at a random position in the linked list
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current:
            new_node.next = current.next
            current.next = new_node
        else:
            print("Invalid position")

    # 3）Method to insert a node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    #===================================================================
    # 3、Delete Node
    #-------------------------------------------------------------------
    # 1）Method to delete a node from the beginning of the linked list
    def delete_from_beginning(self):
        if not self.head:
            print("Linked list is empty")
            return
        self.head = self.head.next


    # 2）Method to delete a node from a random position in the linked list
    def delete_from_position(self, position):
        if position == 0:
            self.delete_from_beginning()
            return
        current = self.head
        prev = None
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if current:
            prev.next = current.next
        else:
            print("Invalid position")

    # 3）Method to delete a node from the end of the linked list
    def delete_from_end(self):
        if not self.head:
            print("Linked list is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None