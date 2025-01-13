# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        curr = head
        l=1
        
        while curr.next:
            curr=curr.next
            l+=1
        k=k%l
        if k==0:
            return head
        
        curr.next = head
        steps = l-k
        prev = head
        for _ in range(steps-1):
            prev = prev.next
        nn=prev.next
        prev.next=None
        return nn

        