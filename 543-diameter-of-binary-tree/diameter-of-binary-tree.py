# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def rec(root):
            if not root:
                return -1
            nonlocal diam
            left = rec(root.left)
            right = rec(root.right)
            diam = max(diam ,left+right+2)
            return max(left, right)+1
        rec(root)
        return diam