# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_left(root):
            if root:
                if not root.left and not root.right:
                    return []
                else:
                    if root.left:
                        return [root.val] + dfs_left(root.left)
                    else:
                        return [root.val] + dfs_left(root.right)
            else:
                return []

        def find_leaves(root):
            if root:
                if not root.left and not root.right:
                    return [root.val]
                else:
                    return find_leaves(root.left) + find_leaves(root.right)
            else:
                return []

        def dfs_right(root):
            if root:
                if not root.left and not root.right:
                    return []
                else:
                    if root.right:
                        return dfs_right(root.right)+[root.val]
                    else:
                        return dfs_right(root.left)+[root.val]
            else:
                return []
            
        boundaries = [root.val] + dfs_left(root.left)+ find_leaves(root.left)+find_leaves(root.right)+dfs_right(root.right)
        
        return boundaries



