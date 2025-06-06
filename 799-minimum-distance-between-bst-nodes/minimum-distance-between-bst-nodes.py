# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        def inordr(root):
            if not root:
                return
            inordr(root.left)
            res.append(root.val)
            inordr(root.right)

        inordr(root)
        
        min_diff = float('inf')
        for i in range(1,len(res)):
            min_diff = min(min_diff, res[i]-res[i-1])
        return min_diff
