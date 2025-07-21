# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count+=1
            cur=cur.next
        nodes_to_traverse = count-n
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for i in range(nodes_to_traverse):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return dummy.next