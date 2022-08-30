"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

E.G.:
    Input:
        1               1
      /   \          /    \
     2     3        2      3
    Output: True

    Input:
        1               1
      /                  \
    2                     2
"""
def isSameTree(p, q) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)