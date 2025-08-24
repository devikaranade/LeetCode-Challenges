# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        nn = TreeNode(val)
        curr = root
        while curr:
            if curr.val>val:
                if not curr.left:
                    curr.left = nn 
                    return root
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = nn 
                    return root
                else:
                    curr = curr.right
        return nn

                