# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            nonlocal x
            x+=1
            dfs(root.left)
            dfs(root.right)
        x=0
        dfs(root)
        return x






    #     if not root:
    #         return 0
    #     if not root.right and not root.left:
    #         return 1
    #     elif root.right is None:
    #         return 2
    #     left = self.level(root.left)
    #     right = self.level(root.right)
    #     if left==right:
    #         return 2**left + self.countNodes(root.right)
    #     else:
    #         return 2**right + self.countNodes(root.left)

    # def level(self, root):
    #     i=0
    #     while root:
    #         i+=1
    #         root=root.left
    #     return i
        