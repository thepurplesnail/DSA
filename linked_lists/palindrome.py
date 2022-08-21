def isPalindrome(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse latter half
    prev = slow
    slow = slow.next
    prev.next = None

    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # compare halves
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True