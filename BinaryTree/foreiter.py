# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []

        nodes = []
        stack = [root]
        while stack:
            c = stack.pop()
            if c is not None:
                nodes.append(c.val)
                if c.right is not None:
                    stack.append(c.right)
                if c.left is not None:
                    stack.append(c.left)
        return nodes
