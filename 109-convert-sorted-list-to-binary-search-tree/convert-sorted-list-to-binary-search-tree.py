# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr=curr.next
        def rec(left, right):
            if left>right:
                return None

            mid = left + (right-left)//2
            node = TreeNode(l[mid])

            if left==right:
                return node
            node.left=rec(left,mid-1)
            node.right=rec(mid+1,right)

            return node
        return rec(0, len(l)-1)

            


        