from linkednode import LinkedNode

def reverseBetween(head, left, right):
    # move pointer to just before left
    dummy = LinkedNode(0, head)
    ptr = dummy
    for i in range(left - 1):
        ptr = ptr.next

    # reverse the linked list from left to right
    prev = ptr
    cur = ptr.next

    for i in range(left, right + 1):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    ptr.next.next = cur
    ptr.next = prev

    return dummy.next