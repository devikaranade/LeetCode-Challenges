# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       
        l = []
        q = deque([root])
        while q:
            node = q.popleft()
            l.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        h = []
        for i in l:
            heapq.heappush(h, -i)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]*(-1)

