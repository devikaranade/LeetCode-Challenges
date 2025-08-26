# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = []

        def rec(root):
            if not root:
                return
            rec(root.left)
            l.append(root.val)
            rec(root.right)
            return l

        def build_balanced_BST(left, right):
            if left>right:
                return None
            mid = left+(right-left)//2
            root = TreeNode(l[mid])
            root.left = build_balanced_BST(left, mid-1)
            root.right = build_balanced_BST(mid+1, right)
            return root

        l = rec(root)
        ans = build_balanced_BST(0,len(l)-1)
        return ans
        



        
        
