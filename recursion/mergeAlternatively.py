from linked_lists.linkednode import LinkedNode

"""
5. Given 2 linked_lists L1 and L2, return a linked list L which contains all the elements of L1 and L2 in alternating order. 
You must do this recursively. 

Example:
L1 = 1->2->3->4->5
L2 = 11->12->13->14->15
L = 1->11->2->12->3->13->4->14->5->15
"""

def merge(l1, l2):
    # if l2 is empty -> return l1
    if l2 is None:
        return l1
    # if l1 is empty -> return l2
    if l1 is None:
        return l2
    # pop l1 from the left and set its next to l2
    rest1 = l1.next
    rest2 = l2.next

    l1.next = l2
    l2.next = merge(rest1, rest2)

    return l1

l1 = LinkedNode(1)
l1.add(LinkedNode(2))
l1.add(LinkedNode(3))
l1.add(LinkedNode(4))
l1.add(LinkedNode(5))

l2 = LinkedNode(11)
l2.add(LinkedNode(12))
l2.add(LinkedNode(13))
l2.add(LinkedNode(14))
l2.add(LinkedNode(15))

ans = merge(l1, l2)
print(ans.toString())