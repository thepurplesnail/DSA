"""
Invert a binary tree
"""

def invert(self, root):
    if not root:
        return
    self.swap(root)
    self.invert(root.left)
    self.invert(root.right)
    return root


def swap(self, node):
    temp = node.left
    node.left = node.right
    node.right = temp