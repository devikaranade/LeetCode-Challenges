# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            return rec(left.left, right.left) and rec(left.right, right.right)
        return rec(p, q)
