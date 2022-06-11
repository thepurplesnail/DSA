# Definition of linked node class
class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, node):
        cursor = self
        while cursor.next is not None:
            cursor = cursor.next
        cursor.next = node

    def toString(self):
        cursor = self
        while cursor is not None:
            print(cursor.val)
            cursor = cursor.next
