import collections

def levelOrder(root):
    ans = []
    q = collections.deque()
    q.append(root)

    while q:
        lvl = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                lvl.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if lvl:
            ans.append(lvl)

    return ans