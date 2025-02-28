# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_h = [0]
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)
        max_h[0] = max(height(root), max_h[0])

        return max_h[0]

    # time: O(n)
    # space: O(1)
        
