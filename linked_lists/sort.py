from linkednode import LinkedNode

def sortList(head):
    if not head or not head.next:
        return head
    prev, fast, slow = None, head, head
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    prev.next = None
    left = sortList(head)
    right = sortList(slow)
    return merge(left, right)

def merge(list1, list2):
    dummy = LinkedNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return dummy.next