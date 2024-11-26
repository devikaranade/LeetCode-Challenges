# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        result = []
        level = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if level%2==0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(tmp)
            level+=1
        return result
            
            