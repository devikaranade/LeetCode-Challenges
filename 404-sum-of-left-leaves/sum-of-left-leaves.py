# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        total = 0
        while q:
            node = q.popleft()
            if node:
                if node.left and not node.left.left and not node.left.right:
                    total+=node.left.val
                q.append(node.left)
                q.append(node.right)
            
   
        return total

        
