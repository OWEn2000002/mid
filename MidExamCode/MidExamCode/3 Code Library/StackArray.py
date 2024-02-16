#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Stack using Array
# ---------------------------------------------------------------------------
# method:
# .Push
# .Pop
# .lsEmpty
# .IsFull
# .Peek
#############################################################################

class StackArray:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, data):
        if len(self.stack) < self.max_size:
            self.stack.append(data)
        else:
            print("Stack overflow")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
