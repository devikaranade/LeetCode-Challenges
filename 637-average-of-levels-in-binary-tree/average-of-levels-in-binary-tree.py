# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            total = []
            for _ in range(len(q)):
                node = q.popleft() 
                if node:
                    total.append(node.val)
                    q.append(node.left)
                    q.append(node.right)    
            if total:
                res.append(sum(total)/len(total))

        return res
                
                
                


