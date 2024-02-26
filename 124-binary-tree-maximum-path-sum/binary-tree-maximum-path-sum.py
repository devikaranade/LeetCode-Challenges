# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float("-inf")
        def rec(root):
            nonlocal total 
            if not root:
                return 0
            # if not root.left and not root.right:
            #     total+=root.val
            left = max(rec(root.left), 0)
            right = max(rec(root.right), 0)

            curr_max = root.val + left + right
            total = max(total, curr_max)

            return root.val + max(left,right)
            
        rec(root)
        return total
