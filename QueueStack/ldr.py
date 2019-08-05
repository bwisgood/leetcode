# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        stack = [(1, root)]
        res = []
        while stack:
            command, node = stack.pop()
            if command == 0:
                res.append(node.val)
            else:
                # 模拟系统栈
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))
        return res
