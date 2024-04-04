# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []
        def rec(root, p, d):
            if not root:
                return 
            if len(res)==2:
                return
            if root.val==x or root.val==y:
                res.append([p,d])
            rec(root.left, root.val, d+1)
            rec(root.right, root.val, d+1)
        rec(root, -1, 0)
        return res[0][0]!=res[1][0] and res[0][1] == res[1][1]
