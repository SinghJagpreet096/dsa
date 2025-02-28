# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]

        def height(root):
            if not root: 
                return 0
            
            left_h = height(root.left)
            right_h = height(root.right)

            d = left_h + right_h

            max_d[0] = max(max_d[0], d)

            return 1 + max(left_h, right_h)   
        height(root) 
        return max_d[0]    

    # time: O(n)
    # space: O(n)
        
