from linkednode import LinkedNode

def reorderList(head) -> None:
    if not (head and head.next):
        return

    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev, cur = slow, slow.next
    prev.next = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    while head.next and prev.next:
        nxtTail = prev.next
        nxtHead = head.next
        head.next = prev
        prev.next = nxtHead
        head = nxtHead
        prev = nxtTail

l1 = LinkedNode(1)
l1.add(LinkedNode(2))
l1.add(LinkedNode(3))
l1.add(LinkedNode(4))
reorderList(l1)