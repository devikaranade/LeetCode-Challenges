# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        p_val = p.val
        q_val = q.val
        
        while root:
            parent = root.val
            if p_val>parent and q_val>parent:
                root = root.right
            elif p_val<parent and q_val<parent:
                root=root.left
            else:
                return root
            