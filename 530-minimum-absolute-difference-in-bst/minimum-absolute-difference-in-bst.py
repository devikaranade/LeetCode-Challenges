# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        q = deque([root])
        min_diff = float('inf')
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                diff = abs(res[i]-res[j])
                if diff<min_diff:
                    min_diff = diff
        return min_diff


