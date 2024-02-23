# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, digits, l):
            if not root:
                return 
            if not root.left and not root.right:           
                digits+=str(root.val)
                l.append(digits)
                return l
            digits+=str(root.val)
            dfs(root.left, digits, l)
            dfs(root.right, digits, l)
            return l
            
        l = dfs(root, "", [])
        total = 0
        for i in l:
            total+=int(i)
        return total


                 

        