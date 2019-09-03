# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        # 迭代
        if not root:
            return []
        stack = [root, ]
        res = []
        while stack:
            c = stack.pop()
            if c:
                res.append(c.val)
                if c.left:
                    stack.append(c.right)
                if c.right:
                    stack.append(c.left)
        return res
