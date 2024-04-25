# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        q = collections.deque([(root, False)])
        res = []
        while q:
            node,parent=q.popleft()
            if not parent and node.val not in to_delete:
                res.append(node)
            parent=not node.val in to_delete
            if node.left:
                q.append((node.left, parent))
                if node.left.val in to_delete:
                    node.left=None
            if node.right:
                q.append((node.right,parent))
                if node.right.val in to_delete:
                    node.right=None
        return res

