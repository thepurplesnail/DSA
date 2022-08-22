"""
Remove the nth node from the end of the list and return its head.

EG:
    Input: head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 --> 5
"""
from linkednode import LinkedNode

def removeNthFromEnd(head: LinkedNode, n):
    if not (head and head.next):
        return None

    dummy = LinkedNode(0, head)
    prev, slow, fast = dummy, head, dummy

    for i in range(n):
        fast = fast.next

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next

    prev.next = slow.next
    return dummy.next