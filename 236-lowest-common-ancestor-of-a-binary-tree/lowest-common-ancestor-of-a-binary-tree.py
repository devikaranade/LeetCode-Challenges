# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def rec(node):
            nonlocal ans
            if not node:
                return False
            left = rec(node.left)
            right = rec(node.right)
            mid = node==p or node==q
            if mid+left+right>=2:
                ans = node
            return mid or left or right
        
        rec(root)
        return ans
        