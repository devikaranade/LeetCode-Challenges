# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node: TreeNode)->int:
            if not node:
                return -1
            return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        return (
                abs(self.height(root.left)-self.height(root.right))<2
                and self.isBalanced(root.left)
                and self.isBalanced(root.right)
            )
