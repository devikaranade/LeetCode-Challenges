# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def rec(root):
            if not root:
                return
            rec(root.left)
            l.append(root.val)
            rec(root.right)
        rec(root)
        min_diff = float('inf')
        for i in range(1,len(l)):
            min_diff = min(min_diff, l[i]-l[i-1])
        return min_diff