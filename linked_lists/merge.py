"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

EG:

    Input:
    1 -> 2 -> 4
    1 -> 3 -> 5

    Output:
    1 -> 1 -> 2 -> 3 -> 4 -> 5
"""
from linkednode import LinkedNode

def merge(list1: LinkedNode, list2: LinkedNode):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val < list2.val:
        nxt = list1.next
        list1.next = merge(nxt, list2)
        return list1
    else:
        nxt = list2.next
        list2.next = merge(nxt, list1)
        return list2