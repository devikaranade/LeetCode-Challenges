# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
    
        child_parent = {root:None}
        qu = deque([root])
        while qu:
            node = qu.popleft()
            if node.left:
                qu.append(node.left)
                child_parent[node.left]=node
            if node.right:
                qu.append(node.right)
                child_parent[node.right]=node
        
        s = set()
        while p:
            s.add(p)
            p = child_parent[p]
        
        while q not in s:
            q=child_parent[q]
        
        return q