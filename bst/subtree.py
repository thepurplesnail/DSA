"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.

E.G.
    Input:
    Root          subRoot
        3           4
       / \         / \
      4   5       1   2
     / \
    1   2

    Output: True
"""
import collections
def isSameTree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

# BFS approach

def isSubtree(root, subRoot):
    q = collections.deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node:
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            q.append(node.left)
            q.append(node.right)

    return False

""" (recursive solution, not as fast and takes up more space)
def isSubtree(root, subRoot):
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    if root.val == subRoot.val:
        if isSameTree(root, subRoot):
            return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
"""