# -----------------------------------------------
# file          : stack.py
# author        : Sang Shin | Chris Newman
# date          : 02-22-2014
# class         : CS 480 | Milestone #4
# description   : Contains the stack class
# -----------------------------------------------
#!/usr/bin/python

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    print("This is the stack.py file")
    print("This is a helper file to the main.py of Milestone #4 for CS 480")
    
