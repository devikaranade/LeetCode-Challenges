# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        total = 0
        q = deque()
        q.append((root,targetSum, []))
        while q:
            node, leftsum, path = q.popleft()
            
            leftsum-=node.val
            path.append(node.val)

            if node.left or node.right:
                if node.left:
                    q.append((node.left,leftsum, path.copy()))
                if node.right:
                    q.append((node.right, leftsum, path.copy()))
            elif leftsum==0:
                res.append(path)
            
        return res

















        # def dfs(root,target, res, final):
        #     if not root:
        #         return 
        #     if not root.left and not root.right and target+root.val==targetSum:
        #         res+=[root.val]
        #         return final.append(res[:])
        #     dfs(root.left, target+root.val, res+[root.val], final)
        #     dfs(root.right, target+root.val, res+[root.val], final)
            
        # final = []
        # dfs(root, 0, [], final)
        # return final
   

            
        