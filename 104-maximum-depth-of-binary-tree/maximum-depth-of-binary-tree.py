# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left = rec(root.left)
            right = rec(root.right)
            return 1+max(left,right)
        return rec(root)
