"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

E.G.
    Input:
         2 -> 3
                -> 4 -> 5
    1 -> 2 -> 3

    Ouput: 4

"""
def getIntersectionNode(headA, headB):
    ptrA, ptrB = headA, headB
    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA

    return ptrA