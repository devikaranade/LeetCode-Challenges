# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, total, targetSum):
            if not root:
                return False
            if not root.right and not root.left and total+root.val==targetSum:
                return True
            left = dfs(root.left, total+root.val, targetSum)
            right = dfs(root.right, total+root.val, targetSum)
            return left or right
        return dfs(root, 0, targetSum)
        