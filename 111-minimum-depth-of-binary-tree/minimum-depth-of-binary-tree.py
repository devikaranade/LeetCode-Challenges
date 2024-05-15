# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root):
            if not root:
                return 0
            if not root.left:
                return 1 + rec(root.right)
            elif not root.right:
                return 1 + rec(root.left)
            return 1 + min(rec(root.left), rec(root.right))
        return rec(root)