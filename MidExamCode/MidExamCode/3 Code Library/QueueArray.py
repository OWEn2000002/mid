#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Queue using Array
# ---------------------------------------------------------------------------
# method:
#    .Enqueue
#    .Dequeue
#    .IsEmpty.
#    .IsFull
#.   .Peek
#############################################################################

class QueueArray:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, data):
        if len(self.queue) < self.max_size:
            self.queue.insert(0, data)
        else:
            print("Queue is full")

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None
