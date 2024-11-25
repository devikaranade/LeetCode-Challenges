# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        result = []

        while q:
            n = len(q)
            child = []
            for _ in range(n):
                value = q.popleft()
                if value:
                    child.append(value.val)
                    q.append(value.left)
                    q.append(value.right)
            if child:
                result.append(sum(child)/len(child))
        return result