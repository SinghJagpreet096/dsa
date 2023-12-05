# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root:[TreeNode]) -> int:
        def longestPath(root):
            if root is None:
                return 0
            return 1 + max(longestPath(root.left),longestPath(root.right))
        if root is None:
            return 0
        
        return sum(longestPath(root.left),longestPath(root.right))
