from treenode import TreeNode

class Bst:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def add(self, node):
        # if root is null -> set node as root
        if self.root is None:
            self.root = node

        # otherwise traverse the tree until pointer is null
        else:
            prev = now = self.root
            while now:
                prev = now
                # if node's value is smaller than the pointer node -> move pointer to left
                if node.val < now.val:
                    now = now.left
                # else move pointer to right
                else:
                    now = now.right

            # set node to the child of prev
            if node.val < prev.val:
                prev.left = node
            else:
                prev.right = node

    def setToHeight(self, node):
        if node is None:
            return

        # traverse left child
        self.setToHeight(node.left)

        # set height of the node to the max returned by helper
        node.val = self.helper(node)

        # traverse right child
        self.setToHeight(node.right)

    def helper(self, node):
        # if node is empty -> return -1
        if node is None:
            return -1
        # return max depth between left subtree and right subtree
        return max(1 + self.helper(node.left), 1 + self.helper(node.right))

node1 = TreeNode(9)
bst = Bst(node1)
bst.add(TreeNode(5))
bst.add(TreeNode(14))
bst.add(TreeNode(2))
bst.add(TreeNode(6))
bst.add(TreeNode(8))
bst.add(TreeNode(7))

bst = Bst(node1)

# bst.setToHeight(bst.root)
def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


#preorder(bst.root)
#inorder(bst.root)

inorder(bst.root)