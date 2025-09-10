# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        right_view_list = []
        q = deque([root])
        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(l)
        # print(res) # [[1], [2,3], [5,4]]
        for i in res:
            right_view_list.append(i[-1])
        return right_view_list

