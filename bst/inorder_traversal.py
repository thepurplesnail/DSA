"""
EX:
1
 \
  3
 /
2

Output: [1, 2, 3]
"""

from treenode import TreeNode
from bst import Bst

class Solution:
    def inorderTraversal(self, root):
        ans = []
        self.helper(ans, root)
        return ans

    def helper(self, arr, node):
        if node is None:
            return
        self.helper(arr, node.left)
        arr.append(node.val)
        self.helper(arr, node.right)


node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)

tree = Bst(node1)
tree.add(node2)
tree.add(node3)

sol = Solution()
ans = sol.inorderTraversal(tree.root)
print(ans)